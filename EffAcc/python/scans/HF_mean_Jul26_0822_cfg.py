import FWCore.ParameterSet.Config as cms

process = cms.Process("Zefficiency")
process.TimerService = cms.Service("TimerService")
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True),
    SkipEvent = cms.untracked.vstring('ProductNotFound') 
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(40000)
    )

process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
    fileNames = cms.untracked.vstring("file:/home/jmmans/data/zshape/Summer11_DYToEE_M-20_CT10_TuneZ2_7TeV-powheg-pythia/F61A0CD6-9AA8-E011-A92B-0024E8769B05.root" )
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('histo_10M_partBUILDINGTTEST.root')
)

process.f2s = cms.EDProducer("ZFullSim2Event"
                             )
import ZShape.EffAcc.FullSimSmearedElectronProducer_cfi
import ZShape.EffAcc.ZEfficiencyKevin_cfi


process.HFXmeanXm1Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanXm1Xsmear.HF.mean = cms.double(-1)

process.HFXmeanX-1 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX-1.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX-1.zsrc = cms.untracked.InputTag("HFXmeanX-1Xsmear","ZEventParticles")
process.HFXmeanX-1.zElectronsCollection = cms.untracked.InputTag("HFXmeanX-1Xsmear","ZEventParticles")

process.HFXmeanX0Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0Xsmear.HF.mean = cms.double(0)

process.HFXmeanX0 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0.zsrc = cms.untracked.InputTag("HFXmeanX0Xsmear","ZEventParticles")
process.HFXmeanX0.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0Xsmear","ZEventParticles")

process.HFXmeanX1Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1Xsmear.HF.mean = cms.double(1)

process.HFXmeanX1 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1.zsrc = cms.untracked.InputTag("HFXmeanX1Xsmear","ZEventParticles")
process.HFXmeanX1.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.HFXmeanXm1Xsmear
+ process.HFXmeanX-1
+ process.HFXmeanX0Xsmear
+ process.HFXmeanX0
+ process.HFXmeanX1Xsmear
+ process.HFXmeanX1
)
