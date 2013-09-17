 #include "FWCore/Framework/interface/MakerMacros.h"
 #include "CommonTools/UtilAlgos/interface/SingleObjectSelector.h"
 #include "CommonTools/UtilAlgos/interface/StringCutObjectSelector.h"
 #include "DataFormats/RecoCandidate/interface/RecoEcalCandidate.h"
 #include "DataFormats/RecoCandidate/interface/RecoEcalCandidateFwd.h"
  typedef SingleObjectSelector<
            reco::RecoEcalCandidateCollection, 
            StringCutObjectSelector<reco::RecoEcalCandidate>,
            reco::RecoEcalCandidateRefVector
          > RecoEcalCandidateRefSelector;
 
 DEFINE_FWK_MODULE( RecoEcalCandidateRefSelector );
