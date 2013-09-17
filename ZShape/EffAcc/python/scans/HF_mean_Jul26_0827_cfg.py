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


process.HFXmeanX0X8Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X8Xsmear.HF.mean = cms.double(0.8)

process.HFXmeanX0X8 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X8.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X8.zsrc = cms.untracked.InputTag("HFXmeanX0X8Xsmear","ZEventParticles")
process.HFXmeanX0X8.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X8Xsmear","ZEventParticles")

process.HFXmeanX0X9Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X9Xsmear.HF.mean = cms.double(0.9)

process.HFXmeanX0X9 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X9.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X9.zsrc = cms.untracked.InputTag("HFXmeanX0X9Xsmear","ZEventParticles")
process.HFXmeanX0X9.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X9Xsmear","ZEventParticles")

process.HFXmeanX0X95Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X95Xsmear.HF.mean = cms.double(0.95)

process.HFXmeanX0X95 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X95.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X95.zsrc = cms.untracked.InputTag("HFXmeanX0X95Xsmear","ZEventParticles")
process.HFXmeanX0X95.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X95Xsmear","ZEventParticles")

process.HFXmeanX1X0Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X0Xsmear.HF.mean = cms.double(1.0)

process.HFXmeanX1X0 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X0.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X0.zsrc = cms.untracked.InputTag("HFXmeanX1X0Xsmear","ZEventParticles")
process.HFXmeanX1X0.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X0Xsmear","ZEventParticles")

process.HFXmeanX1X05Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X05Xsmear.HF.mean = cms.double(1.05)

process.HFXmeanX1X05 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X05.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X05.zsrc = cms.untracked.InputTag("HFXmeanX1X05Xsmear","ZEventParticles")
process.HFXmeanX1X05.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X05Xsmear","ZEventParticles")

process.HFXmeanX1X1Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X1Xsmear.HF.mean = cms.double(1.1)

process.HFXmeanX1X1 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X1.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X1.zsrc = cms.untracked.InputTag("HFXmeanX1X1Xsmear","ZEventParticles")
process.HFXmeanX1X1.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X1Xsmear","ZEventParticles")

process.HFXmeanX1X15Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X15Xsmear.HF.mean = cms.double(1.15)

process.HFXmeanX1X15 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X15.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X15.zsrc = cms.untracked.InputTag("HFXmeanX1X15Xsmear","ZEventParticles")
process.HFXmeanX1X15.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X15Xsmear","ZEventParticles")

process.HFXmeanX1X2Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X2Xsmear.HF.mean = cms.double(1.2)

process.HFXmeanX1X2 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X2.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X2.zsrc = cms.untracked.InputTag("HFXmeanX1X2Xsmear","ZEventParticles")
process.HFXmeanX1X2.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X2Xsmear","ZEventParticles")

process.HFXmeanX1X25Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X25Xsmear.HF.mean = cms.double(1.25)

process.HFXmeanX1X25 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X25.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X25.zsrc = cms.untracked.InputTag("HFXmeanX1X25Xsmear","ZEventParticles")
process.HFXmeanX1X25.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X25Xsmear","ZEventParticles")

process.HFXmeanX1X3Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X3Xsmear.HF.mean = cms.double(1.3)

process.HFXmeanX1X3 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X3.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X3.zsrc = cms.untracked.InputTag("HFXmeanX1X3Xsmear","ZEventParticles")
process.HFXmeanX1X3.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X3Xsmear","ZEventParticles")

process.HFXmeanX1X35Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X35Xsmear.HF.mean = cms.double(1.35)

process.HFXmeanX1X35 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X35.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X35.zsrc = cms.untracked.InputTag("HFXmeanX1X35Xsmear","ZEventParticles")
process.HFXmeanX1X35.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X35Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.HFXmeanX0X8Xsmear
+ process.HFXmeanX0X8
+ process.HFXmeanX0X9Xsmear
+ process.HFXmeanX0X9
+ process.HFXmeanX0X95Xsmear
+ process.HFXmeanX0X95
+ process.HFXmeanX1X0Xsmear
+ process.HFXmeanX1X0
+ process.HFXmeanX1X05Xsmear
+ process.HFXmeanX1X05
+ process.HFXmeanX1X1Xsmear
+ process.HFXmeanX1X1
+ process.HFXmeanX1X15Xsmear
+ process.HFXmeanX1X15
+ process.HFXmeanX1X2Xsmear
+ process.HFXmeanX1X2
+ process.HFXmeanX1X25Xsmear
+ process.HFXmeanX1X25
+ process.HFXmeanX1X3Xsmear
+ process.HFXmeanX1X3
+ process.HFXmeanX1X35Xsmear
+ process.HFXmeanX1X35
)
