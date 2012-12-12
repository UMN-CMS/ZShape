// -*- C++ -*-
//
// Package:    MakeSmearedZEffTree
// Class:      MakeSmearedZEffTree
// 
/**\class MakeSmearedZEffTree MakeSmearedZEffTree.cc ZShape/MakeSmearedZEffTree/src/MakeSmearedZEffTree.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  Alexander Gude
//         Created:  Fri Sep 23 11:50:21 CDT 2011
// $Id: MakeSmearedZEffTree.cc,v 1.2 2012/12/12 21:00:31 gude Exp $
//
//


// system include files
#include <memory>
#include <iostream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"

#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "ZEffTree.h"

#include "DataFormats/Common/interface/AssociationMap.h"
#include "DataFormats/EgammaReco/interface/SuperCluster.h"
#include "DataFormats/RecoCandidate/interface/RecoEcalCandidate.h"
#include "DataFormats/RecoCandidate/interface/RecoEcalCandidateFwd.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

#include "DataFormats/EgammaReco/interface/HFEMClusterShapeAssociation.h"
#include "DataFormats/EgammaReco/interface/HFEMClusterShape.h"
// Trying to get Lozentz Vectors to work...
#include "Math/PtEtaPhiM4D.h"
#include "Math/VectorUtil.h"

// And 3d vectors
#include "Math/Vector3D.h"

//
// class declaration
//

class MakeSmearedZEffTree : public edm::EDAnalyzer {
    public:
        explicit MakeSmearedZEffTree(const edm::ParameterSet&);
        ~MakeSmearedZEffTree();

        static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


    private:
        virtual void beginJob() ;
        virtual void analyze(const edm::Event&, const edm::EventSetup&);
        virtual void endJob() ;

        virtual void beginRun(edm::Run const&, edm::EventSetup const&);
        virtual void endRun(edm::Run const&, edm::EventSetup const&);
        virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
        virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

        float getPhiStar( float eta0, float phi0, int charge0, float eta1, float phi1);
        bool inHF( double eta );
        int getHFTower( double eta );
        double getHFSlope( double eta );

        // ----------member data ---------------------------
        ZEffTree *m_ze;
        edm::InputTag source_;
        bool doHFCor_;

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
MakeSmearedZEffTree::MakeSmearedZEffTree(const edm::ParameterSet& iConfig) {
    //now do what ever initialization is needed
    edm::Service<TFileService> ts;
    TFile &f = ts->file();
    bool writable=true;
    m_ze = new ZEffTree(f,writable);

    source_ = iConfig.getUntrackedParameter<edm::InputTag>("zsrc");
    doHFCor_ = iConfig.getUntrackedParameter<bool>("doHFCorrection",false);
}


MakeSmearedZEffTree::~MakeSmearedZEffTree() {
    // do anything here that needs to be done at desctruction time
    // (e.g. close files, deallocate resources etc.)
    //m_ze->Write();

}


//
// member functions
//

// ------------ method called for each event  ------------
void MakeSmearedZEffTree::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
    using namespace edm;
    //using namespace reco;

    m_ze->Clear();

    Handle<edm::HepMCProduct> HepMC;

    if (!iEvent.isRealData()) {
        Handle <reco::GenParticleCollection> pZeeParticles;
        iEvent.getByLabel(source_,pZeeParticles);

        reco::GenParticleCollection::const_iterator me[2];
        int ne=0;

        for(reco::GenParticleCollection::const_iterator ZeeElectron_itr = pZeeParticles->begin(); ZeeElectron_itr != pZeeParticles->end(); ZeeElectron_itr++){
            if (ne < 2){
                me[ne] = ZeeElectron_itr;
                ne++;
            } else {
                break;
            }
        }

        // ge0 is always the highest pt electron
        if (me[0]->momentum().Rho() > me[1]->momentum().Rho()) {
            std::swap(me[0],me[1]);
        }

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

        math::XYZTLorentzVector Zp4 = me[0]->p4() + me[1]->p4(); //Create Z p4 vector

        m_ze->reco.eta[0] = me[0]->momentum().Eta();
        m_ze->reco.eta[1] = me[1]->momentum().Eta();
        m_ze->reco.phi[0] = me[0]->momentum().Phi();
        m_ze->reco.phi[1] = me[1]->momentum().Phi();
        m_ze->reco.charge[0] = me[0]->charge();
        m_ze->reco.charge[1] = me[1]->charge();
        m_ze->reco.mz = Zp4.M();
        m_ze->reco.yz = Zp4.Rapidity();
        m_ze->reco.qtz = Zp4.pt();
        m_ze->reco.nverts = npv;
        m_ze->reco.phistar = getPhiStar(m_ze->reco.eta[0], m_ze->reco.phi[0], m_ze->reco.charge[0], m_ze->reco.eta[1], m_ze->reco.phi[1]);
        /* Apply HF correction if required */
        if ( doHFCor_ && inHF(me[0]->momentum().Eta()) ){
            double hfcorrection = (npv - 1) * getHFSlope(me[0]->momentum().Eta());
            m_ze->reco.pt[0] = me[0]->momentum().Rho()*(1-hfcorrection);
        } else {
            m_ze->reco.pt[0] = me[0]->momentum().Rho();
        }
        if ( doHFCor_ && inHF(me[1]->momentum().Eta()) ){
            double hfcorrection = (npv - 1) * getHFSlope(me[1]->momentum().Eta());
            m_ze->reco.pt[1] = me[1]->momentum().Rho()*(1-hfcorrection);
        } else {
            m_ze->reco.pt[1] = me[1]->momentum().Rho();
        }
    }

    m_ze->Fill();
}

// ------------ method called once each job just before starting event loop  ------------
    void 
MakeSmearedZEffTree::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
    void 
MakeSmearedZEffTree::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
    void 
MakeSmearedZEffTree::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
    void 
MakeSmearedZEffTree::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
    void 
MakeSmearedZEffTree::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
    void 
MakeSmearedZEffTree::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
MakeSmearedZEffTree::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
    //The following says we do not know what parameters are allowed so do no validation
    // Please change this to state exactly what you do use, even if it is no parameters
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}

float MakeSmearedZEffTree::getPhiStar(float eta0, float phi0, int charge0, float eta1, float phi1){
    /* Calculate dPhi, stolen from Kevin's code */
    const double pi = 3.14159265;
    float dPhi=phi0-phi1;

    if (dPhi < 0){
        if (dPhi > -pi){
            dPhi = fabs(dPhi);
        }
        if (dPhi < -pi) {
            dPhi += 2*pi;
        }
    }

    /* Theta* */
    float thetaStar = acos( tanh( -0.5 * ( (charge0 * eta0) - (charge0 * eta1) ) ) );

    /* PhiStar */
    float phiStar = tan( (pi - dPhi)/2. ) * sin( thetaStar );

    return phiStar;
}

bool MakeSmearedZEffTree::inHF( double eta ){
    double feta = fabs(eta);
    if ( fabs(2.853) < feta && feta < fabs(5.191) ){
        return true;
    } else {
        return false;
    }
}

int MakeSmearedZEffTree::getHFTower( double eta ){
    static const int arraySize = 13;
    static const double starts[arraySize] = {2.853, 2.964, 3.139, 3.314, 3.489, 3.664, 3.839, 4.013, 4.191, 4.363, 4.538, 4.716, 4.889};
    static const double ends[arraySize] = {2.964, 3.139, 3.314, 3.489, 3.664, 3.839, 4.013, 4.191, 4.363, 4.538, 4.716, 4.889, 5.191};
    static const int towers[arraySize] = {29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41};
    static const double feta = fabs(eta);
    /* Check for outside range */
    if (feta < starts[0] || feta > ends[arraySize-1]){
        return 0;
    }
    /* Determine Sign of the tower */
    int sign = 1;
    if (eta < 0){
        sign = -1;
    }

    /* Binary search for location */
    int lower = 0;
    int upper = arraySize-1;
    int location = (arraySize-1)/2;
    while ( ( upper > lower ) ){
        if ( eta < starts[location] ){
            upper = location;
        } else {
            lower = location;
        }
        if ( eta < ends[location] ){
            upper = location;
        } else {
            lower = location;
        }

        int step = ( upper - lower )/2;
        location = upper - step;
    }

    /* Return location */
    return sign*towers[location];
}

double MakeSmearedZEffTree::getHFSlope( double eta ){
    static const int arraySize = 13;
    static const double starts[arraySize] = {2.853, 2.964, 3.139, 3.314, 3.489, 3.664, 3.839, 4.013, 4.191, 4.363, 4.538, 4.716, 4.889};
    static const double ends[arraySize] = {2.964, 3.139, 3.314, 3.489, 3.664, 3.839, 4.013, 4.191, 4.363, 4.538, 4.716, 4.889, 5.191};
    /* Corrections: 29, 30, ..., 41 for positive and negative ieta  */
    static const double pos_correction[arraySize] = {0.0862, 0.0862, 0.1402, 0.0862, 0.0862, 0.0862, 0.0862, 0.0862, 0.0862, 0.0862, 0.0862, 0.0862, 0.0862};  
    static const double neg_correction[arraySize] = {0.0862, 0.0862, 0.1402, 0.0862, 0.0862, 0.0862, 0.0862, 0.0862, 0.0862, 0.0862, 0.0862, 0.0862, 0.0862};  
    static const double feta = fabs(eta);
    /* Check for outside range */
    if (feta < starts[0] || feta > ends[arraySize-1]){
        return 0;
    }

    /* Binary search for location */
    int lower = 0;
    int upper = arraySize-1;
    int location = (arraySize-1)/2;
    while ( ( upper > lower ) ){
        if ( eta < starts[location] ){
            upper = location;
        } else {
            lower = location;
        }
        if ( eta < ends[location] ){
            upper = location;
        } else {
            lower = location;
        }

        int step = ( upper - lower )/2;
        location = upper - step;
    }

    /* Determine Sign of the tower */
    if (eta < 0){
        return neg_correction[location];
    } else {
        return pos_correction[location];
    }
}


//define this as a plug-in
DEFINE_FWK_MODULE(MakeSmearedZEffTree);
