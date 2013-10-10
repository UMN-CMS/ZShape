#ifndef ZSHAPE_MAKEZEFFTREE_SRC_MAKEZEFFTREE_H_
#define ZSHAPE_MAKEZEFFTREE_SRC_MAKEZEFFTREE_H_

/*
 * -*- C++ -*-
 * 
 * Package:    MakeZEffTree
 * Class:      MakeZEffTree
 * 
 * MakeZEffTree MakeZEffTree.cc ZShape/MakeZEffTree/src/MakeZEffTree.cc
 * 
 * Description: [one line class summary]
 * 
 * Implementation:
 * [Notes on implementation]
 * 
 *  Original Author:  Alexander Gude
 *          Created:  Fri Sep 23 11:50:21 CDT 2011
 */

// CMSSW Basic Types
#include "FWCore/Framework/interface/EDAnalyzer.h"  // edm::EDAnalyzer
#include "FWCore/Framework/interface/Event.h"  // edm::Event

// Basic Candidate
#include "DataFormats/Candidate/interface/Candidate.h"  //  reco::CandidateBaseRef, reco::Candidate

// ZEffTree
#include "ZEffTree.h"  // ZEffTree, ZInfo

// HF Superclusters
#include "DataFormats/EgammaReco/interface/HFEMClusterShape.h"  // reco::HFEMClusterShape

// Trigger Objects
#include "DataFormats/HLTReco/interface/TriggerEvent.h"  // trigger namespace, TriggerEvent

/* 
 * Class Declaration
 */

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
        const reco::HFEMClusterShape* getHFEMClusterShape(const edm::Event& iEvent, const double eta, const double phi);
        const trigger::TriggerObject* getTriggerObject(const edm::Event& iEvent, const std::vector<std::string>& triggersToMatch, const double eta, const double phi);
        double getR9(const edm::Event& iEvent, const double eta, const double phi);

        // ----------member data ---------------------------
        ZEffTree *m_ze;
        edm::InputTag tnpProducer_;
        edm::InputTag photTag_;
        
        std::vector<edm::InputTag> passProbeCandTags_;
        double delRMatchingCut_, delPtRelMatchingCut_;
        std::vector<std::string> cutName_;
        std::vector<std::string> tagTriggersToMatch_, probeTriggersToMatch_;
        bool doTrigObjMatch_;

};
#endif  // ZSHAPE_MAKEZEFFTREE_SRC_MAKEZEFFTREE_H_
