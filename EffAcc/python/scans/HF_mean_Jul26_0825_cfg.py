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


process.HFXmeanXm0X5Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanXm0X5Xsmear.HF.mean = cms.double(-0.5)

process.HFXmeanXm0X5 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanXm0X5.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanXm0X5.zsrc = cms.untracked.InputTag("HFXmeanX-0X5Xsmear","ZEventParticles")
process.HFXmeanXm0X5.zElectronsCollection = cms.untracked.InputTag("HFXmeanX-0X5Xsmear","ZEventParticles")

process.HFXmeanXm0X2Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanXm0X2Xsmear.HF.mean = cms.double(-0.2)

process.HFXmeanXm0X2 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanXm0X2.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanXm0X2.zsrc = cms.untracked.InputTag("HFXmeanX-0X2Xsmear","ZEventParticles")
process.HFXmeanXm0X2.zElectronsCollection = cms.untracked.InputTag("HFXmeanX-0X2Xsmear","ZEventParticles")

process.HFXmeanXm0X15Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanXm0X15Xsmear.HF.mean = cms.double(-0.15)

process.HFXmeanXm0X15 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanXm0X15.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanXm0X15.zsrc = cms.untracked.InputTag("HFXmeanX-0X15Xsmear","ZEventParticles")
process.HFXmeanXm0X15.zElectronsCollection = cms.untracked.InputTag("HFXmeanX-0X15Xsmear","ZEventParticles")

process.HFXmeanXm0X1Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanXm0X1Xsmear.HF.mean = cms.double(-0.1)

process.HFXmeanXm0X1 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanXm0X1.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanXm0X1.zsrc = cms.untracked.InputTag("HFXmeanX-0X1Xsmear","ZEventParticles")
process.HFXmeanXm0X1.zElectronsCollection = cms.untracked.InputTag("HFXmeanX-0X1Xsmear","ZEventParticles")

process.HFXmeanXm0X05Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanXm0X05Xsmear.HF.mean = cms.double(-0.05)

process.HFXmeanXm0X05 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanXm0X05.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanXm0X05.zsrc = cms.untracked.InputTag("HFXmeanX-0X05Xsmear","ZEventParticles")
process.HFXmeanXm0X05.zElectronsCollection = cms.untracked.InputTag("HFXmeanX-0X05Xsmear","ZEventParticles")

process.HFXmeanX0X0Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X0Xsmear.HF.mean = cms.double(0.0)

process.HFXmeanX0X0 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X0.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X0.zsrc = cms.untracked.InputTag("HFXmeanX0X0Xsmear","ZEventParticles")
process.HFXmeanX0X0.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X0Xsmear","ZEventParticles")

process.HFXmeanX0X05Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X05Xsmear.HF.mean = cms.double(0.05)

process.HFXmeanX0X05 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X05.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X05.zsrc = cms.untracked.InputTag("HFXmeanX0X05Xsmear","ZEventParticles")
process.HFXmeanX0X05.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X05Xsmear","ZEventParticles")

process.HFXmeanX0X1Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X1Xsmear.HF.mean = cms.double(0.1)

process.HFXmeanX0X1 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X1.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X1.zsrc = cms.untracked.InputTag("HFXmeanX0X1Xsmear","ZEventParticles")
process.HFXmeanX0X1.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X1Xsmear","ZEventParticles")

process.HFXmeanX0X15Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X15Xsmear.HF.mean = cms.double(0.15)

process.HFXmeanX0X15 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X15.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X15.zsrc = cms.untracked.InputTag("HFXmeanX0X15Xsmear","ZEventParticles")
process.HFXmeanX0X15.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X15Xsmear","ZEventParticles")

process.HFXmeanX0X2Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X2Xsmear.HF.mean = cms.double(0.2)

process.HFXmeanX0X2 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X2.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X2.zsrc = cms.untracked.InputTag("HFXmeanX0X2Xsmear","ZEventParticles")
process.HFXmeanX0X2.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X2Xsmear","ZEventParticles")

process.HFXmeanX0X25Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X25Xsmear.HF.mean = cms.double(0.25)

process.HFXmeanX0X25 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X25.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X25.zsrc = cms.untracked.InputTag("HFXmeanX0X25Xsmear","ZEventParticles")
process.HFXmeanX0X25.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X25Xsmear","ZEventParticles")

process.HFXmeanX0X5Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X5Xsmear.HF.mean = cms.double(0.5)

process.HFXmeanX0X5 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X5.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X5.zsrc = cms.untracked.InputTag("HFXmeanX0X5Xsmear","ZEventParticles")
process.HFXmeanX0X5.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X5Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.HFXmeanXm0X5Xsmear
+ process.HFXmeanXm0X5
+ process.HFXmeanXm0X2Xsmear
+ process.HFXmeanXm0X2
+ process.HFXmeanXm0X15Xsmear
+ process.HFXmeanXm0X15
+ process.HFXmeanXm0X1Xsmear
+ process.HFXmeanXm0X1
+ process.HFXmeanXm0X05Xsmear
+ process.HFXmeanXm0X05
+ process.HFXmeanX0X0Xsmear
+ process.HFXmeanX0X0
+ process.HFXmeanX0X05Xsmear
+ process.HFXmeanX0X05
+ process.HFXmeanX0X1Xsmear
+ process.HFXmeanX0X1
+ process.HFXmeanX0X15Xsmear
+ process.HFXmeanX0X15
+ process.HFXmeanX0X2Xsmear
+ process.HFXmeanX0X2
+ process.HFXmeanX0X25Xsmear
+ process.HFXmeanX0X25
+ process.HFXmeanX0X5Xsmear
+ process.HFXmeanX0X5
)
