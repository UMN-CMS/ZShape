#ifndef PhysicsTools_TagAndProbe_CandidateMatchedCandidateProducer_h
#define PhysicsTools_TagAndProbe_CandidateMatchedCandidateProducer_h

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"


// forward declarations

class CandidateMatchedCandidateProducer : public edm::EDProducer 
{
 public:
  explicit CandidateMatchedCandidateProducer(const edm::ParameterSet&);
  ~CandidateMatchedCandidateProducer();

 private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
      
  // ----------member data ---------------------------

  edm::InputTag ccCollection_;
  edm::InputTag scCollection_;
  double delRMatchingCut_;
};

#endif
