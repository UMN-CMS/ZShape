// -*- C++ -*-
//
// Package:    HFSuperClusterFilterVL
// Class:      HFSuperClusterFilterVL
// 
/**\class HFSuperClusterFilterVL HFSuperClusterFilterVL.cc HFelectrons/HFSuperClusterFilterVL/src/HFSuperClusterFilterVL.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  Kevin  Klapoetke
//         Created:  Tue Jul 10 15:46:08 CDT 2012
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"
#include "DataFormats/EgammaReco/interface/SuperCluster.h"
#include "DataFormats/RecoCandidate/interface/RecoEcalCandidate.h"
#include "DataFormats/EgammaReco/interface/HFEMClusterShapeAssociation.h"
#include "DataFormats/EgammaReco/interface/HFEMClusterShape.h"
#include "DataFormats/EgammaReco/interface/SuperClusterFwd.h"

//
// class declaration
//

class HFSuperClusterFilterVL : public edm::EDFilter {
    public:
        explicit HFSuperClusterFilterVL(const edm::ParameterSet&);
        ~HFSuperClusterFilterVL();

        static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

    private:
        virtual void beginJob() ;
        virtual bool filter(edm::Event&, const edm::EventSetup&);
        virtual void endJob() ;

        virtual bool beginRun(edm::Run&, edm::EventSetup const&);
        virtual bool endRun(edm::Run&, edm::EventSetup const&);
        virtual bool beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
        virtual bool endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

        // ----------member data ---------------------------
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
HFSuperClusterFilterVL::HFSuperClusterFilterVL(const edm::ParameterSet& iConfig) {
    //now do what ever initialization is needed

}


HFSuperClusterFilterVL::~HFSuperClusterFilterVL() {

    // do anything here that needs to be done at desctruction time
    // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool HFSuperClusterFilterVL::filter(edm::Event& e, const edm::EventSetup& iSetup) {
    using namespace edm; using namespace reco;
    bool isHFSC = false;

    edm::InputTag hfRecoEcalCandidateProducer_("hfRecoEcalCandidate");
    edm::InputTag hfClusterShapes_("hfEMClusters");

    // edm::Handle<RecoEcalCandidateCollection> HFElectrons;
    edm::Handle<SuperClusterCollection> HFSC;
    edm::Handle<HFEMClusterShapeAssociationCollection> ClusterAssociation;

    //e.getByLabel(hfRecoEcalCandidateProducer_,HFElectrons);
    e.getByLabel(hfClusterShapes_, HFSC);
    e.getByLabel(hfClusterShapes_, ClusterAssociation);

    // std::vector<SuperClusterCollection>::const_iterator j;
    for (unsigned int j=0; j<HFSC->size(); j++){

        SuperClusterRef theClusRef = Ref<SuperClusterCollection>(HFSC, j);
        const HFEMClusterShapeRef clusShapeRef = ClusterAssociation->find(theClusRef)->val;
        const HFEMClusterShape& clusShape = *clusShapeRef;

        //  bool eCe9=clusShape.eCOREe9()>0.5;
        //     bool eSeL=clusShape.eSeL()<0.7;
        //     bool e9e25=(clusShape.eLong3x3()*1.0/clusShape.eLong5x5())>0.5;

        const bool eCe9 = clusShape.eCOREe9() > 0.5;
        const bool eSeL = clusShape.eSeL() < 1.0;
        const bool e9e25 = (clusShape.eLong3x3() * 1.0 / clusShape.eLong5x5()) > 0.7;
        isHFSC = (eCe9 && eSeL && e9e25);
        if (isHFSC){
            return isHFSC;
        }

    }//end of j for loop

    return isHFSC;
}

// ------------ method called once each job just before starting event loop  ------------
void HFSuperClusterFilterVL::beginJob() { }

// ------------ method called once each job just after ending the event loop  ------------
void HFSuperClusterFilterVL::endJob() { } 
// ------------ method called when starting to processes a run  ------------
bool HFSuperClusterFilterVL::beginRun(edm::Run&, edm::EventSetup const&) { 
    return true;
}

// ------------ method called when ending the processing of a run  ------------
bool HFSuperClusterFilterVL::endRun(edm::Run&, edm::EventSetup const&) {
    return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool HFSuperClusterFilterVL::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&) {
    return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool HFSuperClusterFilterVL::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&) {
    return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void HFSuperClusterFilterVL::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
    //The following says we do not know what parameters are allowed so do no validation
    // Please change this to state exactly what you do use, even if it is no parameters
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(HFSuperClusterFilterVL);
