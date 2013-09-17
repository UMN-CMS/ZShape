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
    input = cms.untracked.int32(80000)
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


process.EEXmeanX0X94Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X94Xsmear.EE.mean = cms.double(0.94)

process.EEXmeanX0X94 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X94.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X94.zsrc = cms.untracked.InputTag("EEXmeanX0X94Xsmear","ZEventParticles")
process.EEXmeanX0X94.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X94Xsmear","ZEventParticles")

process.EEXmeanX0X95Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X95Xsmear.EE.mean = cms.double(0.95)

process.EEXmeanX0X95 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X95.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X95.zsrc = cms.untracked.InputTag("EEXmeanX0X95Xsmear","ZEventParticles")
process.EEXmeanX0X95.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X95Xsmear","ZEventParticles")

process.EEXmeanX0X96Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X96Xsmear.EE.mean = cms.double(0.96)

process.EEXmeanX0X96 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X96.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X96.zsrc = cms.untracked.InputTag("EEXmeanX0X96Xsmear","ZEventParticles")
process.EEXmeanX0X96.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X96Xsmear","ZEventParticles")

process.EEXmeanX0X97Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X97Xsmear.EE.mean = cms.double(0.97)

process.EEXmeanX0X97 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X97.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X97.zsrc = cms.untracked.InputTag("EEXmeanX0X97Xsmear","ZEventParticles")
process.EEXmeanX0X97.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X97Xsmear","ZEventParticles")

process.EEXmeanX0X98Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X98Xsmear.EE.mean = cms.double(0.98)

process.EEXmeanX0X98 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X98.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X98.zsrc = cms.untracked.InputTag("EEXmeanX0X98Xsmear","ZEventParticles")
process.EEXmeanX0X98.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X98Xsmear","ZEventParticles")

process.EEXmeanX0X985Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X985Xsmear.EE.mean = cms.double(0.985)

process.EEXmeanX0X985 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X985.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X985.zsrc = cms.untracked.InputTag("EEXmeanX0X985Xsmear","ZEventParticles")
process.EEXmeanX0X985.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X985Xsmear","ZEventParticles")

process.EEXmeanX0X99Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X99Xsmear.EE.mean = cms.double(0.99)

process.EEXmeanX0X99 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X99.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X99.zsrc = cms.untracked.InputTag("EEXmeanX0X99Xsmear","ZEventParticles")
process.EEXmeanX0X99.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X99Xsmear","ZEventParticles")

process.EEXmeanX0X995Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X995Xsmear.EE.mean = cms.double(0.995)

process.EEXmeanX0X995 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X995.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X995.zsrc = cms.untracked.InputTag("EEXmeanX0X995Xsmear","ZEventParticles")
process.EEXmeanX0X995.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X995Xsmear","ZEventParticles")

process.EEXmeanX1X0Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX1X0Xsmear.EE.mean = cms.double(1.0)

process.EEXmeanX1X0 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX1X0.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX1X0.zsrc = cms.untracked.InputTag("EEXmeanX1X0Xsmear","ZEventParticles")
process.EEXmeanX1X0.zElectronsCollection = cms.untracked.InputTag("EEXmeanX1X0Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.EEXmeanX0X94Xsmear
+ process.EEXmeanX0X94
+ process.EEXmeanX0X95Xsmear
+ process.EEXmeanX0X95
+ process.EEXmeanX0X96Xsmear
+ process.EEXmeanX0X96
+ process.EEXmeanX0X97Xsmear
+ process.EEXmeanX0X97
+ process.EEXmeanX0X98Xsmear
+ process.EEXmeanX0X98
+ process.EEXmeanX0X985Xsmear
+ process.EEXmeanX0X985
+ process.EEXmeanX0X99Xsmear
+ process.EEXmeanX0X99
+ process.EEXmeanX0X995Xsmear
+ process.EEXmeanX0X995
+ process.EEXmeanX1X0Xsmear
+ process.EEXmeanX1X0
)
