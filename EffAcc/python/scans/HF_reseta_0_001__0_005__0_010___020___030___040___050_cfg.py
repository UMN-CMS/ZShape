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


process.HFXresetaX0X001Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresetaX0X001Xsmear.HF.reseta = cms.double(0.001)

process.HFXresetaX0X001 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresetaX0X001.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresetaX0X001.zsrc = cms.untracked.InputTag("HFXresetaX0X001Xsmear","ZEventParticles")
process.HFXresetaX0X001.zElectronsCollection = cms.untracked.InputTag("HFXresetaX0X001Xsmear","ZEventParticles")

process.HFXresetaX0X005Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresetaX0X005Xsmear.HF.reseta = cms.double(0.005)

process.HFXresetaX0X005 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresetaX0X005.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresetaX0X005.zsrc = cms.untracked.InputTag("HFXresetaX0X005Xsmear","ZEventParticles")
process.HFXresetaX0X005.zElectronsCollection = cms.untracked.InputTag("HFXresetaX0X005Xsmear","ZEventParticles")

process.HFXresetaX0X010Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresetaX0X010Xsmear.HF.reseta = cms.double(0.010)

process.HFXresetaX0X010 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresetaX0X010.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresetaX0X010.zsrc = cms.untracked.InputTag("HFXresetaX0X010Xsmear","ZEventParticles")
process.HFXresetaX0X010.zElectronsCollection = cms.untracked.InputTag("HFXresetaX0X010Xsmear","ZEventParticles")

process.HFXresetaXX020Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresetaXX020Xsmear.HF.reseta = cms.double(.020)

process.HFXresetaXX020 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresetaXX020.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresetaXX020.zsrc = cms.untracked.InputTag("HFXresetaXX020Xsmear","ZEventParticles")
process.HFXresetaXX020.zElectronsCollection = cms.untracked.InputTag("HFXresetaXX020Xsmear","ZEventParticles")

process.HFXresetaXX030Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresetaXX030Xsmear.HF.reseta = cms.double(.030)

process.HFXresetaXX030 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresetaXX030.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresetaXX030.zsrc = cms.untracked.InputTag("HFXresetaXX030Xsmear","ZEventParticles")
process.HFXresetaXX030.zElectronsCollection = cms.untracked.InputTag("HFXresetaXX030Xsmear","ZEventParticles")

process.HFXresetaXX040Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresetaXX040Xsmear.HF.reseta = cms.double(.040)

process.HFXresetaXX040 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresetaXX040.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresetaXX040.zsrc = cms.untracked.InputTag("HFXresetaXX040Xsmear","ZEventParticles")
process.HFXresetaXX040.zElectronsCollection = cms.untracked.InputTag("HFXresetaXX040Xsmear","ZEventParticles")

process.HFXresetaXX050Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresetaXX050Xsmear.HF.reseta = cms.double(.050)

process.HFXresetaXX050 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresetaXX050.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresetaXX050.zsrc = cms.untracked.InputTag("HFXresetaXX050Xsmear","ZEventParticles")
process.HFXresetaXX050.zElectronsCollection = cms.untracked.InputTag("HFXresetaXX050Xsmear","ZEventParticles")

process.p = cms.Path(process.f2s
+ process.HFXresetaX0X001Xsmear
+ process.HFXresetaX0X001
+ process.HFXresetaX0X005Xsmear
+ process.HFXresetaX0X005
+ process.HFXresetaX0X010Xsmear
+ process.HFXresetaX0X010
+ process.HFXresetaXX020Xsmear
+ process.HFXresetaXX020
+ process.HFXresetaXX030Xsmear
+ process.HFXresetaXX030
+ process.HFXresetaXX040Xsmear
+ process.HFXresetaXX040
+ process.HFXresetaXX050Xsmear
+ process.HFXresetaXX050
)
