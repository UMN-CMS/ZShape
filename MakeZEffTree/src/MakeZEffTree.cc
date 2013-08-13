// -*- C++ -*-
//
// Package:    MakeZEffTree
// Class:      MakeZEffTree
// 
/**\class MakeZEffTree MakeZEffTree.cc ZShape/MakeZEffTree/src/MakeZEffTree.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  Alexander Gude
//         Created:  Fri Sep 23 11:50:21 CDT 2011


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/EcalDetId/interface/EEDetId.h"

#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "ZEffTree.h"

#include "DataFormats/Common/interface/AssociationMap.h"
#include "DataFormats/EgammaReco/interface/SuperCluster.h"
#include "DataFormats/RecoCandidate/interface/RecoEcalCandidate.h"

#include "DataFormats/Math/interface/deltaR.h"

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

// Trying to get Lozentz Vectors to work...
#include "Math/PtEtaPhiM4D.h"
#include "Math/VectorUtil.h"

// And 3d vectors
#include "Math/Vector3D.h"


//
// class declaration
//

class MakeZEffTree : public edm::EDAnalyzer {
    public:
        explicit MakeZEffTree(const edm::ParameterSet&);
        ~MakeZEffTree();

        static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


    private:
        virtual void beginJob() ;
        virtual void analyze(const edm::Event&, const edm::EventSetup&);
        virtual void endJob() ;

        virtual void beginRun(edm::Run const&, edm::EventSetup const&);
        virtual void endRun(edm::Run const&, edm::EventSetup const&);
        virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
        virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

        bool ProbePassProbeOverlap(const reco::CandidateBaseRef& probe, const edm::Handle<reco::CandidateView>& passprobes);
        bool MatchObjects(const reco::Candidate *hltObj, const reco::CandidateBaseRef& tagObj);
        double getPhiStar( const double eta0, const double phi0, const double eta1, const double phi1);
        // ----------member data ---------------------------
        ZEffTree *m_ze;
        edm::InputTag tnpProducer_;
        edm::InputTag photTag_;
        
        std::vector<edm::InputTag> passProbeCandTags_;
        double delRMatchingCut_, delPtRelMatchingCut_;
        std::vector<std::string> cutName_;

};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
MakeZEffTree::MakeZEffTree(const edm::ParameterSet& iConfig) {
    //now do what ever initialization is needed
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

}


MakeZEffTree::~MakeZEffTree() {
    // do anything here that needs to be done at desctruction time
    // (e.g. close files, deallocate resources etc.)
    //m_ze->Write();

}


//
// member functions
//

// ------------ method called for each event  ------------
void MakeZEffTree::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
    using namespace edm;

    m_ze->Clear();
    /* MC */
    if (!iEvent.isRealData()) {
        Handle<edm::HepMCProduct> HepMC;
        iEvent.getByLabel("generator", HepMC);
        const HepMC::GenEvent* genE=HepMC->GetEvent();

        // Read through the MC, looking for Z -> ee
        HepMC::GenEvent::vertex_const_iterator vtex;
        HepMC::GenVertex::particles_out_const_iterator Pout;
        HepMC::GenParticle* ge0=0;
        HepMC::GenParticle* ge1=0;
        HepMC::GenParticle* Z=0;
        for (vtex=genE->vertices_begin(); vtex!=genE->vertices_end(); vtex++){
            if (((*vtex)->particles_in_size())==1) {
                if ((*((*vtex)->particles_in_const_begin()))->pdg_id()==23){ // Test for Z
                    Z=(*((*vtex)->particles_in_const_begin()));
                    for (Pout=(*vtex)->particles_out_const_begin(); Pout!=(*vtex)->particles_out_const_end(); Pout++){
                        if (abs((*Pout)->pdg_id())==11){ // To Electrons
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

        int npv = 1; // Does not include primary vert
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
        m_ze->gen.yz = 0.5*log((Z->momentum().e()+Z->momentum().pz())/(Z->momentum().e()-Z->momentum().pz()));
        m_ze->gen.ptz = Z->momentum().perp();
        m_ze->gen.nverts = npv;
        m_ze->gen.phistar = MakeZEffTree::getPhiStar( m_ze->gen.eta[0], m_ze->gen.phi[0], m_ze->gen.eta[1], m_ze->gen.phi[1]);
    }

    /* Data */
    edm::Handle<reco::CandidateView> tagprobes;
    if (!iEvent.getByLabel(tnpProducer_, tagprobes)) {
        LogWarning("ZFromData") << "Could not extract tag-probe map with input tag " << tnpProducer_;
        std::cout << "Didn't get the input tag " << std::endl;
    } else {
        if (tagprobes.isValid()){
            /* Pick T&P pair */
            const int tpsize = tagprobes->size();
            if (tpsize == 0) {
                return; // No second electron
            }
            // We select "randomly" by using the event ID
            const int tpNum = iEvent.id().event() % tpsize;

            const reco::CandidateBaseRef &tag = tagprobes->at(tpNum).daughter(0)->masterClone();
            const reco::CandidateBaseRef &vprobes = tagprobes->at(tpNum).daughter(1)->masterClone(); // Maybe an arrow...

            math::XYZTLorentzVector tpP4 = tag->p4() + vprobes->p4(); //Create Z p4 vector

            m_ze->reco.eta[0] = tag->p4().eta();
            m_ze->reco.eta[1] = vprobes->p4().eta();
            m_ze->reco.phi[0] = tag->p4().phi();
            m_ze->reco.phi[1] = vprobes->p4().phi(); 
            m_ze->reco.pt[0] = tag->p4().pt();
            m_ze->reco.pt[1] = vprobes->p4().pt();
            m_ze->reco.charge[0] = tag->charge();
            m_ze->reco.charge[1] = vprobes->charge();
            m_ze->reco.mz = tpP4.M();
            m_ze->reco.yz = tpP4.Rapidity();
            m_ze->reco.ptz = tpP4.pt();

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

    /* Calculate dPhi, stolen from Kevin's code */
    const double pi = 3.14159265;
    double dPhi=phi0-phi1;

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

//define this as a plug-in
DEFINE_FWK_MODULE(MakeZEffTree);