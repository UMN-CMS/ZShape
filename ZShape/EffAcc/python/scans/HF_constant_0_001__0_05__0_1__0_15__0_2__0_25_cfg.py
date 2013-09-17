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


process.HFXconstantX0X001Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X001Xsmear.HF.constant = cms.double(0.001)

process.HFXconstantX0X001 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X001.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X001.zsrc = cms.untracked.InputTag("HFXconstantX0X001Xsmear","ZEventParticles")
process.HFXconstantX0X001.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X001Xsmear","ZEventParticles")

process.HFXconstantX0X05Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X05Xsmear.HF.constant = cms.double(0.05)

process.HFXconstantX0X05 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X05.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X05.zsrc = cms.untracked.InputTag("HFXconstantX0X05Xsmear","ZEventParticles")
process.HFXconstantX0X05.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X05Xsmear","ZEventParticles")

process.HFXconstantX0X1Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X1Xsmear.HF.constant = cms.double(0.1)

process.HFXconstantX0X1 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X1.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X1.zsrc = cms.untracked.InputTag("HFXconstantX0X1Xsmear","ZEventParticles")
process.HFXconstantX0X1.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X1Xsmear","ZEventParticles")

process.HFXconstantX0X15Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X15Xsmear.HF.constant = cms.double(0.15)

process.HFXconstantX0X15 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X15.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X15.zsrc = cms.untracked.InputTag("HFXconstantX0X15Xsmear","ZEventParticles")
process.HFXconstantX0X15.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X15Xsmear","ZEventParticles")

process.HFXconstantX0X2Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X2Xsmear.HF.constant = cms.double(0.2)

process.HFXconstantX0X2 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X2.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X2.zsrc = cms.untracked.InputTag("HFXconstantX0X2Xsmear","ZEventParticles")
process.HFXconstantX0X2.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X2Xsmear","ZEventParticles")

process.HFXconstantX0X25Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X25Xsmear.HF.constant = cms.double(0.25)

process.HFXconstantX0X25 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X25.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X25.zsrc = cms.untracked.InputTag("HFXconstantX0X25Xsmear","ZEventParticles")
process.HFXconstantX0X25.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X25Xsmear","ZEventParticles")

process.p = cms.Path(process.f2s
+ process.HFXconstantX0X001Xsmear
+ process.HFXconstantX0X001
+ process.HFXconstantX0X05Xsmear
+ process.HFXconstantX0X05
+ process.HFXconstantX0X1Xsmear
+ process.HFXconstantX0X1
+ process.HFXconstantX0X15Xsmear
+ process.HFXconstantX0X15
+ process.HFXconstantX0X2Xsmear
+ process.HFXconstantX0X2
+ process.HFXconstantX0X25Xsmear
+ process.HFXconstantX0X25
)
