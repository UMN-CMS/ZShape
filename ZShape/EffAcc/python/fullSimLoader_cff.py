import FWCore.ParameterSet.Config as cms

from ElectroWeakAnalysis.WENu.simpleEleIdSequence_cff import *
from RecoJets.JetProducers.PFJetParameters_cfi import *
from RecoJets.JetProducers.AnomalousCellParameters_cfi import *
 
kt6PFJets = cms.EDProducer(
     "FastjetJetProducer",
     PFJetParameters,
     AnomalousCellParameters,
     jetAlgorithm = cms.string("Kt"),
    rParam       = cms.double(0.6)
)

kt6PFJets.doRhoFastjet = True
kt6PFJets.Rho_EtaMax = 2.5

fullSimLoad = cms.EDProducer("ZFullSim2Event",
                             hfRecoTag = cms.untracked.InputTag("hfRecoEcalCandidateMC")
                             )

f2s_sequence = cms.Sequence(kt6PFJets * simpleEleIdSequence * fullSimLoad)
