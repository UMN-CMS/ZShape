#include "MakeZEffTree.h"

// CMSSW
#include "FWCore/Framework/interface/MakerMacros.h"  // LogWarning, edm::ParameterSetDescription, edm::ConfigurationDescriptions
#include "FWCore/ServiceRegistry/interface/Service.h"  // edm::Service
#include "CommonTools/UtilAlgos/interface/TFileService.h"  // TFileService

// Pile Up and Vertexes
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"  // PileupSummaryInfo
#include "DataFormats/VertexReco/interface/Vertex.h"  // reco::Vertex
#include "DataFormats/VertexReco/interface/VertexFwd.h"  // reco::VertexCollection

// MC Objects
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"  // edm::HepMCProduct

// HF Superclusters
#include "DataFormats/EgammaReco/interface/HFEMClusterShapeAssociation.h"  // HFEMClusterShapeAssociationCollection
#include "DataFormats/EgammaReco/interface/SuperCluster.h"  // SuperClusterCollection
#include "DataFormats/Common/interface/Ref.h"  // edm::Ref<>

// Photons (for R9)
#include "DataFormats/EgammaCandidates/interface/Photon.h"
#include "DataFormats/EgammaCandidates/interface/PhotonFwd.h"

// Delta R
#include "DataFormats/Math/interface/deltaR.h"  // deltaR

/*
 * Constructors and Destructor
 */
MakeZEffTree::MakeZEffTree(const edm::ParameterSet& iConfig) {
    //Now do what ever initialization is needed
    edm::Service<TFileService> ts;
    TFile &f = ts->file();
    const bool writable = true;
    m_ze = new ZEffTree(f, writable);

    tnpProducer_ = iConfig.getUntrackedParameter<edm::InputTag > ("TagProbeProducer");
    std::vector< edm::InputTag > defaultPassProbeCandTags;
    passProbeCandTags_ = iConfig.getUntrackedParameter< std::vector<edm::InputTag> >("passProbeCandTags", defaultPassProbeCandTags);

    delRMatchingCut_ = iConfig.getUntrackedParameter<double>("dRMatchCut", 0.2);
    delPtRelMatchingCut_ = iConfig.getUntrackedParameter<double>("dPtMatchCut", 15.0);
    cutName_ = iConfig.getUntrackedParameter< std::vector<std::string> >("CutNames");

    // Trigger Matching
    doTrigObjMatch_ = iConfig.getUntrackedParameter<bool>("MatchTriggerObjects", false);
    std::vector<std::string> defaultTagTriggersToMatch(1, "hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8TrackIsolFilter");
    tagTriggersToMatch_ = iConfig.getUntrackedParameter< std::vector<std::string> >("TagTriggers", defaultTagTriggersToMatch);
    std::vector<std::string> defaultProbeTriggersToMatch(1, "hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8PMMassFilter");
    probeTriggersToMatch_ = iConfig.getUntrackedParameter< std::vector<std::string> >("ProbeTriggers", defaultProbeTriggersToMatch);
}

MakeZEffTree::~MakeZEffTree() {
    // do anything here that needs to be done at desctruction time
    // (e.g. close files, deallocate resources etc.)
    //m_ze->Write();
}


/*
 * Member Functions
 */

// ------------ method called for each event  ------------
void MakeZEffTree::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
    using namespace edm;

    m_ze->Clear();
    /* MC */
    if (!iEvent.isRealData()) {
        Handle<edm::HepMCProduct> HepMC;
        iEvent.getByLabel("generator", HepMC);
        const HepMC::GenEvent* genE = HepMC->GetEvent();

        // Read through the MC, looking for Z -> ee
        HepMC::GenEvent::vertex_const_iterator vtex;
        HepMC::GenVertex::particles_out_const_iterator Pout;
        HepMC::GenParticle* ge0 = 0;
        HepMC::GenParticle* ge1 = 0;
        HepMC::GenParticle* Z = 0;
        for (vtex = genE->vertices_begin(); vtex != genE->vertices_end(); vtex++) {  // Loop over all vertexes
            if (((*vtex)->particles_in_size()) == 1) {  // Find vertexes with only one incoming particle
                if ((*((*vtex)->particles_in_const_begin()))->pdg_id() == 23) {  // Incoming particle is a Z
                    Z=(*((*vtex)->particles_in_const_begin()));
                    for (Pout=(*vtex)->particles_out_const_begin(); Pout!=(*vtex)->particles_out_const_end(); Pout++){  // Loop over decay products of the Z
                        if (abs((*Pout)->pdg_id()) == 11){  // Insure the decay products are electrons
                            if(ge0==0){
                                ge0=*Pout;
                            } else {
                                ge1=*Pout;
                            }
                        }
                    }
                }
            }
        }

        if (ge0==0 || ge1==0 || Z->momentum().m() < 40) {
            // Low mass or failed to get electrons
            return;
        }

        // ge0 is always the highest pt electron
        if (ge1->momentum().perp() > ge0->momentum().perp()) {
            std::swap(ge0, ge1);
        }

        // Get PileUp info
        edm::Handle<std::vector<PileupSummaryInfo> > pPU;
        iEvent.getByLabel("addPileupInfo", pPU);
        std::vector<PileupSummaryInfo>::const_iterator pPUI;

        int npv = 1; // pPU does not include primary vertex by default
        for(pPUI = pPU->begin(); pPUI != pPU->end(); ++pPUI) {
            if (pPUI->getBunchCrossing() == 0) {
                npv = pPUI->getPU_NumInteractions() + 1;
                break;
            }
        }

        m_ze->gen.eta[0] = ge0->momentum().eta();
        m_ze->gen.eta[1] = ge1->momentum().eta();
        m_ze->gen.phi[0] = ge0->momentum().phi();
        m_ze->gen.phi[1] = ge1->momentum().phi();
        m_ze->gen.pt[0] = ge0->momentum().perp();
        m_ze->gen.pt[1] = ge1->momentum().perp();
        if (ge0->pdg_id() == 11) {
            m_ze->gen.charge[0] = -1;
            m_ze->gen.charge[1] = 1;
        } else {
            m_ze->gen.charge[1] = -1;
            m_ze->gen.charge[0] = 1;
        }
        m_ze->gen.mz = Z->momentum().m();
        m_ze->gen.yz = 0.5 * log((Z->momentum().e()+Z->momentum().pz())/(Z->momentum().e()-Z->momentum().pz()));
        m_ze->gen.ptz = Z->momentum().perp();
        m_ze->gen.nverts = npv;
        m_ze->gen.phistar = MakeZEffTree::getPhiStar( m_ze->gen.eta[0], m_ze->gen.phi[0], m_ze->gen.eta[1], m_ze->gen.phi[1]);
    }

    /* Data */
    edm::Handle<reco::CandidateView> tagprobes;
    if (!iEvent.getByLabel(tnpProducer_, tagprobes)) {
        LogWarning("ZFromData") << "Could not extract tag-probe map with input tag " << tnpProducer_;
        std::cout << "Didn't get the input tag." << std::endl;
    } else {
        if (tagprobes.isValid()){
            /* Pick T&P pair */
            const int tpsize = tagprobes->size();
            if (tpsize == 0) {
                return; // No second electron
            }
            // We select "randomly" by using the event ID
            const int tpNum = iEvent.id().event() % tpsize;
            m_ze->reco.ntp = tpNum;  // Set the number of electrons

            const reco::CandidateBaseRef &tag = tagprobes->at(tpNum).daughter(0)->masterClone();
            const reco::CandidateBaseRef &vprobes = tagprobes->at(tpNum).daughter(1)->masterClone();
            // Require both electrons to match to trigger objects
            if ( doTrigObjMatch_ ){
                const trigger::TriggerObject* tagTO = getTriggerObject(iEvent, tagTriggersToMatch_, tag->p4().eta(), tag->p4().phi());
                const trigger::TriggerObject* probeTO = getTriggerObject(iEvent, probeTriggersToMatch_, vprobes->p4().eta(), vprobes->p4().phi());

                // Requre the Tag to pass the tag trigger, and the probe to
                // pass the probe trigger
                if ( tagTO == NULL || probeTO == NULL ) {
                    std::cout << "Failed to match both objects";
                    return;
                } else {  // These are set to false by default when the ZEffTree is created
                    m_ze->reco.trigtag[0] = true;  // True by virture of being in the else statement
                    m_ze->reco.trigprobe[1] = true;
                    // Check if the objects pass the other trigger
                    const trigger::TriggerObject* tagTOAsProbe = getTriggerObject(iEvent, probeTriggersToMatch_, tag->p4().eta(), tag->p4().phi());
                    const trigger::TriggerObject* probeTOAsTag = getTriggerObject(iEvent, tagTriggersToMatch_, vprobes->p4().eta(), vprobes->p4().phi());
                    if (tagTOAsProbe != NULL) {
                        m_ze->reco.trigprobe[0] = true;
                    } 
                    if (probeTOAsTag != NULL) {
                        m_ze->reco.trigtag[1] = true;
                    }
                    // Set kinematics
                    m_ze->reco.trigeta[0] = tagTO->eta();
                    m_ze->reco.trigphi[0] = tagTO->phi();
                    m_ze->reco.trigpt[0]  = tagTO->pt();
                    m_ze->reco.trigeta[1] = probeTO->eta();
                    m_ze->reco.trigphi[1] = probeTO->phi();
                    m_ze->reco.trigpt[1]  = probeTO->pt();
                    // Recalculate the ZMass
                    math::PtEtaPhiMLorentzVector e0lv(tagTO->pt(), tagTO->eta(), tagTO->phi(), 5.109989e-4);
                    math::PtEtaPhiMLorentzVector e1lv(probeTO->pt(), probeTO->eta(), probeTO->phi(), 5.109989e-4);
                    math::PtEtaPhiMLorentzVector Zlv;
                    Zlv = e0lv + e1lv;
                    m_ze->reco.trigmz = Zlv.mass();
                    m_ze->reco.trigyz = Zlv.Rapidity();
                    m_ze->reco.trigptz = Zlv.pt();
                    //std::cout << "eta: " << m_ze->reco.trigeta[0] << " ";
                    //std::cout << "phi: " << m_ze->reco.trigphi[0] << " ";
                    //std::cout << "pt: " << m_ze->reco.trigpt[0] << std::endl;
                    //std::cout << "eta: " << m_ze->reco.trigeta[1] << " ";
                    //std::cout << "phi: " << m_ze->reco.trigphi[1] << " ";
                    //std::cout << "pt: " << m_ze->reco.trigpt[1] << std::endl;
                    std::cout << "MZ: " << m_ze->reco.trigmz << " ";
                    std::cout << "YZ: " << m_ze->reco.trigyz << " ";
                    std::cout << "Zpt: " << m_ze->reco.trigptz <<std::endl;
                }
            } 

            // Kinematics
            m_ze->reco.eta[0] = tag->p4().eta();
            m_ze->reco.eta[1] = vprobes->p4().eta();
            m_ze->reco.phi[0] = tag->p4().phi();
            m_ze->reco.phi[1] = vprobes->p4().phi();
            m_ze->reco.pt[0] = tag->p4().pt();
            m_ze->reco.pt[1] = vprobes->p4().pt();

            // Charge
            m_ze->reco.charge[0] = tag->charge();
            m_ze->reco.charge[1] = vprobes->charge();

            // Z Kinematics and Mass
            math::XYZTLorentzVector tpP4 = tag->p4() + vprobes->p4(); //Create Z p4 vector
            m_ze->reco.mz = tpP4.M();
            m_ze->reco.yz = tpP4.Rapidity();
            m_ze->reco.ptz = tpP4.pt();

            // Supercluster Variables
            m_ze->reco.r9[0] = getR9(iEvent, tag->p4().eta(), tag->p4().phi());
            m_ze->reco.r9[1] = getR9(iEvent, vprobes->p4().eta(), vprobes->p4().phi());

            // Assign HF Variables
            const reco::HFEMClusterShape* hfemcs0 = getHFEMClusterShape(iEvent, tag->p4().eta(), tag->p4().phi());
            if (hfemcs0 != NULL){
                m_ze->reco.esel[0] = hfemcs0->eSeL();
                m_ze->reco.ece9[0] = hfemcs0->eCOREe9();
                m_ze->reco.e9e25[0] = hfemcs0->e9e25();
            }  // If it is NULL, the default values have already been set by
               // the ZEffTree class so we don't have to set them by hand
            const reco::HFEMClusterShape* hfemcs1 = getHFEMClusterShape(iEvent, vprobes->p4().eta(), vprobes->p4().phi());
            if (hfemcs1 != NULL){
                m_ze->reco.esel[1] = hfemcs1->eSeL();
                m_ze->reco.ece9[1] = hfemcs1->eCOREe9();
                m_ze->reco.e9e25[1] = hfemcs1->e9e25();
            }

            /* Use the electron that we have a charge for to set the PhiStar */
            m_ze->reco.phistar = MakeZEffTree::getPhiStar( m_ze->reco.eta[1], m_ze->reco.phi[1], m_ze->reco.eta[0], m_ze->reco.phi[0]);

            /* Fill cuts */
            // We iterate over the list of cuts as supplied by ZEffTree, where
            // each number is assigned a cut. We then make a list of these
            // objects that pass the cut, called passprobes. We then delta R
            // match our objects to these, and if there is a match we say that
            // our object passed.
            for (int itype = 0; itype < (int) passProbeCandTags_.size(); ++itype){
                edm::Handle<reco::CandidateView> passprobes;
                if (!iEvent.getByLabel(passProbeCandTags_[itype], passprobes)){
                    LogWarning("ZFromData") << "Could not extract tag candidates with input tag." << passProbeCandTags_[itype];
                    std::cout << "Didn't get the tag. " << std::endl;
                } else {
                    m_ze->reco.setBit(0, cutName_[itype], ProbePassProbeOverlap(tag, passprobes));
                    m_ze->reco.setBit(1, cutName_[itype], ProbePassProbeOverlap(vprobes, passprobes));
                }
            }

            /* Find the number of vertices */
            edm::Handle<reco::VertexCollection> recVtxs;
            iEvent.getByLabel("offlinePrimaryVertices", recVtxs);
            int nvert = 0;
            for(unsigned int ind=0; ind < recVtxs->size(); ind++) {
                if (
                        !((*recVtxs)[ind].isFake())
                        && ((*recVtxs)[ind].ndof()>4)
                        && (fabs((*recVtxs)[ind].z())<=24.0)
                        && ((*recVtxs)[ind].position().Rho()<=2.0)
                   ) {
                    nvert++;
                }
            }

            m_ze->reco.nverts = nvert;

        } else {
            std::cout << "Tagprobes not valid!" << std::endl;
        }
    }

    if (m_ze->reco.mz > 0){
        // A last filter on events
        m_ze->Fill();
    }
}


// ------------ method called once each job just before starting event loop  ------------
void MakeZEffTree::beginJob(){ }

// ------------ method called once each job just after ending the event loop  ------------
void MakeZEffTree::endJob(){ }

// ------------ method called when starting to processes a run  ------------
void MakeZEffTree::beginRun(edm::Run const&, edm::EventSetup const&){ }

// ------------ method called when ending the processing of a run  ------------
void MakeZEffTree::endRun(edm::Run const&, edm::EventSetup const&){ }

// ------------ method called when starting to processes a luminosity block  ------------
void MakeZEffTree::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&){ }

// ------------ method called when ending the processing of a luminosity block  ------------
void MakeZEffTree::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&){ }

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void MakeZEffTree::fillDescriptions(edm::ConfigurationDescriptions& descriptions){
    //The following says we do not know what parameters are allowed so do no validation
    // Please change this to state exactly what you do use, even if it is no parameters
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}

bool MakeZEffTree::ProbePassProbeOverlap(const reco::CandidateBaseRef& probe, const edm::Handle<reco::CandidateView>& passprobes) {
    if (passprobes.isValid()) {
        for (int i = 0; i < (int)passprobes->size(); ++i) {
            if (MatchObjects(&((*passprobes)[i]), probe)){
                return true;
            }
        }
    }
    return false;
}

bool MakeZEffTree::MatchObjects(const reco::Candidate *hltObj, const reco::CandidateBaseRef& tagObj) {
    /* Check dR */
    const double tEta = tagObj->eta();
    const double tPhi = tagObj->phi();
    const double hEta = hltObj->eta();
    const double hPhi = hltObj->phi();

    const double dRval = deltaR(tEta, tPhi, hEta, hPhi);
    if (dRval > delRMatchingCut_){
        return false;
    }

    /* Check dPt */
    const double tPt = tagObj->pt();
    const double hPt = hltObj->pt();
    double dPtRel;
    if (tPt > 0.0){
        dPtRel = fabs(hPt - tPt) / tPt;
    } else {
        return false;
    }

    return (dRval < delRMatchingCut_ && dPtRel < delPtRelMatchingCut_);
}

double MakeZEffTree::getPhiStar(const double eta0, const double phi0, const double eta1, const double phi1){
    /* Calculate phi star */
    const double pi = 3.14159265;
    double dPhi=phi0-phi1;

    // Properly account for the fact that 2pi == 0.
    if (dPhi < 0){
        if (dPhi > -pi){
            dPhi = fabs(dPhi);
        }
        if (dPhi < -pi) {
            dPhi += 2*pi;
        }
    }
    if (dPhi > pi){
        dPhi = 2*pi - dPhi;
    }

    const double dEta = fabs(eta0 - eta1);

    /* PhiStar */
    const double phiStar = ( 1 / cosh( dEta / 2 ) ) * (1 / tan( dPhi / 2 ) );
    return phiStar;
}

const reco::HFEMClusterShape* MakeZEffTree::getHFEMClusterShape(const edm::Event& iEvent, const double eta, const double phi){
    double dr = 1000;
    const reco::HFEMClusterShape* cluster = NULL;
    const double feta = fabs(eta);
    if (3.1 < feta && feta < 4.6){  // Check that we're in HF
        // Load HF Clusters
        edm::InputTag hfClusterShapes_("hfEMClusters");

        edm::Handle<reco::HFEMClusterShapeAssociationCollection> ClusterAssociation;
        iEvent.getByLabel(hfClusterShapes_, ClusterAssociation);

        edm::Handle<reco::SuperClusterCollection> HFSC;
        iEvent.getByLabel(hfClusterShapes_, HFSC);
        // Loop until to find the closet match
        for (unsigned int j=0; j < HFSC->size(); ++j){

            const reco::SuperCluster sc = (*HFSC)[j];  // Get Super Cluster
            const double newdr = deltaR(eta, phi, sc.eta(), sc.phi());
            if (newdr < dr && newdr < delRMatchingCut_){  // New dr is smaller, and under our maximum
                const reco::SuperClusterRef theClusRef = edm::Ref<reco::SuperClusterCollection>(HFSC, j);  // Get reference to SC
                const reco::HFEMClusterShape* newcluster = &(*ClusterAssociation->find(theClusRef)->val);  // Find the Shape Reference and dereference and then get the pointer
                dr = newdr;
                cluster = newcluster;
            }
        }
    }
    return cluster;
}

const trigger::TriggerObject* MakeZEffTree::getTriggerObject(const edm::Event& iEvent, const std::vector<std::string>& triggersToMatch, const double eta, const double phi){
    // If our vector is empty or the first item is blank
    if (triggersToMatch.size() == 0 || triggersToMatch[0].size() == 0) {
        return NULL;
    }
    // Initial values
    double dr = 1000;
    const trigger::TriggerObject* trigObj = NULL;

    // Load Trigger Objects
    edm::InputTag hltTrigInfoTag("hltTriggerSummaryAOD","","HLT");
    edm::Handle<trigger::TriggerEvent> trigEvent;

    iEvent.getByLabel(hltTrigInfoTag, trigEvent);
    if (!trigEvent.isValid() ){
        std::cout << "No valid hltTriggerSummaryAOD." << std::endl;
        return false;
    }
    // Loop over triggers, filter the objects from these triggers, and then try to match
    for(std::vector<std::string>::const_iterator trigs = triggersToMatch.begin(); trigs != triggersToMatch.end(); ++trigs) {
        // Grab objects that pass our filter
        edm::InputTag filterTag(*trigs, "", "HLT");
        trigger::size_type filterIndex = trigEvent->filterIndex(filterTag);
        if(filterIndex < trigEvent->sizeFilters()) { // Check that the filter is in triggerEvent
            // Get our trigger keys that pass the filter
            const trigger::Keys& trigKeys = trigEvent->filterKeys(filterIndex);
            const trigger::TriggerObjectCollection& trigObjColl(trigEvent->getObjects());
            // Get the objects that from the trigger keys
            for(trigger::Keys::const_iterator keyIt = trigKeys.begin(); keyIt!=trigKeys.end(); ++keyIt){
                const trigger::TriggerObject* newTrigObj = &trigObjColl[*keyIt];
                const double newdr = deltaR(eta, phi, newTrigObj->eta(), newTrigObj->phi());
                // Do Delta R matching, and assign a new object if we have a
                // better match
                if (newdr < delRMatchingCut_ && newdr < dr){
                    dr = newdr;
                    trigObj = newTrigObj;
                }
            }
        }
    }
    return trigObj;
}

double MakeZEffTree::getR9(const edm::Event& iEvent, const double eta, const double phi){
    // Initial Values
    double r9 = -100;
    double dr = 1000;

    // Get the photons
    edm::Handle< reco::PhotonCollection > NTprobes;
    iEvent.getByLabel("photons", NTprobes);
    // Find the closest match in Delta R
    for(reco::PhotonCollection::const_iterator pit = NTprobes->begin(); pit != NTprobes->end(); pit++) {    
        const double newdr = deltaR(eta, phi, pit->p4().eta(), pit->p4().phi());
        if (newdr < delRMatchingCut_ && newdr < dr){
            dr = newdr;
            r9 = pit->maxEnergyXtal() / pit->e3x3(); // HLT uses Seed/3x3, the R9 in Photons is 3x3/Whole SC
        }
    }

    return r9;
}

//define this as a plug-in
DEFINE_FWK_MODULE(MakeZEffTree);
