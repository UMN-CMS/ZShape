#include "PhysicsTools/TagAndProbe/interface/CandidateMatchedCandidateProducer.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "DataFormats/RecoCandidate/interface/RecoCandidate.h"
#include "DataFormats/Math/interface/deltaR.h" // reco::deltaR


CandidateMatchedCandidateProducer::CandidateMatchedCandidateProducer(const edm::ParameterSet &params)
{

  const edm::InputTag allcands("");
  ccCollection_ = 
    params.getUntrackedParameter<edm::InputTag>("ReferenceCandidateCollection", 
						allcands);
  scCollection_ = 
    params.getParameter<edm::InputTag>("src");

  delRMatchingCut_ = params.getUntrackedParameter<double>("deltaR",
							   0.30);
  
  produces< edm::PtrVector<reco::Candidate> >();
  produces< edm::RefToBaseVector<reco::Candidate> >();
}




CandidateMatchedCandidateProducer::~CandidateMatchedCandidateProducer()
{

}


//
// member functions
//


// ------------ method called to produce the data  ------------

void CandidateMatchedCandidateProducer::produce(edm::Event &event, 
			      const edm::EventSetup &eventSetup)
{
   // Create the output collection
  std::auto_ptr< edm::RefToBaseVector<reco::Candidate> > 
    outColRef( new edm::RefToBaseVector<reco::Candidate> );
  std::auto_ptr< edm::PtrVector<reco::Candidate> > 
    outColPtr( new edm::PtrVector<reco::Candidate> );


  // Read recocandidates
  edm::Handle<edm::View<reco::Candidate> > recocands;
  event.getByLabel(ccCollection_, recocands);
   


  //Read candidates
  edm::Handle<edm::View<reco::Candidate> > recoCandColl; 
  event.getByLabel( scCollection_ , recoCandColl); 


  const edm::PtrVector<reco::Candidate>& ptrVect = recoCandColl->ptrVector();
  const edm::RefToBaseVector<reco::Candidate>& refs = recoCandColl->refVector();
  unsigned int counter=0;

  // Loop over candidates
  for(edm::View<reco::Candidate>::const_iterator scIt = recoCandColl->begin();
      scIt != recoCandColl->end(); ++scIt, ++counter){
    // Now loop over electrons
    for(edm::View<reco::Candidate>::const_iterator  cand = recocands->begin(); 
	cand != recocands->end();  ++cand) {

 
      double dRval = reco::deltaR(cand->eta(), cand->phi(), 
				  scIt->eta(), scIt->phi());	
       
      if( dRval < delRMatchingCut_ ) {
	//outCol->push_back( *scIt );
	outColRef->push_back( refs[counter] );
	outColPtr->push_back( ptrVect[counter]  );
      } // end if loop
    } // end electron loop

  } // end candidate loop

  event.put(outColRef);
  event.put(outColPtr);
}




// ------ method called once each job just before starting event loop  ---



void CandidateMatchedCandidateProducer::beginJob() {}



void CandidateMatchedCandidateProducer::endJob() {}



//define this as a plug-in
DEFINE_FWK_MODULE( CandidateMatchedCandidateProducer );

