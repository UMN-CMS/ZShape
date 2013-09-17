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


process.HFXresphiX0X001Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X001Xsmear.HF.resphi = cms.double(0.001)

process.HFXresphiX0X001 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X001.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X001.zsrc = cms.untracked.InputTag("HFXresphiX0X001Xsmear","ZEventParticles")
process.HFXresphiX0X001.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X001Xsmear","ZEventParticles")

process.HFXresphiX0X005Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X005Xsmear.HF.resphi = cms.double(0.005)

process.HFXresphiX0X005 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X005.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X005.zsrc = cms.untracked.InputTag("HFXresphiX0X005Xsmear","ZEventParticles")
process.HFXresphiX0X005.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X005Xsmear","ZEventParticles")

process.HFXresphiX0X010Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X010Xsmear.HF.resphi = cms.double(0.010)

process.HFXresphiX0X010 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X010.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X010.zsrc = cms.untracked.InputTag("HFXresphiX0X010Xsmear","ZEventParticles")
process.HFXresphiX0X010.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X010Xsmear","ZEventParticles")

process.HFXresphiXX020Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiXX020Xsmear.HF.resphi = cms.double(.020)

process.HFXresphiXX020 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiXX020.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiXX020.zsrc = cms.untracked.InputTag("HFXresphiXX020Xsmear","ZEventParticles")
process.HFXresphiXX020.zElectronsCollection = cms.untracked.InputTag("HFXresphiXX020Xsmear","ZEventParticles")

process.HFXresphiXX030Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiXX030Xsmear.HF.resphi = cms.double(.030)

process.HFXresphiXX030 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiXX030.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiXX030.zsrc = cms.untracked.InputTag("HFXresphiXX030Xsmear","ZEventParticles")
process.HFXresphiXX030.zElectronsCollection = cms.untracked.InputTag("HFXresphiXX030Xsmear","ZEventParticles")

process.HFXresphiXX040Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiXX040Xsmear.HF.resphi = cms.double(.040)

process.HFXresphiXX040 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiXX040.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiXX040.zsrc = cms.untracked.InputTag("HFXresphiXX040Xsmear","ZEventParticles")
process.HFXresphiXX040.zElectronsCollection = cms.untracked.InputTag("HFXresphiXX040Xsmear","ZEventParticles")

process.HFXresphiXX050Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiXX050Xsmear.HF.resphi = cms.double(.050)

process.HFXresphiXX050 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiXX050.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiXX050.zsrc = cms.untracked.InputTag("HFXresphiXX050Xsmear","ZEventParticles")
process.HFXresphiXX050.zElectronsCollection = cms.untracked.InputTag("HFXresphiXX050Xsmear","ZEventParticles")

process.p = cms.Path(process.f2s
+ process.HFXresphiX0X001Xsmear
+ process.HFXresphiX0X001
+ process.HFXresphiX0X005Xsmear
+ process.HFXresphiX0X005
+ process.HFXresphiX0X010Xsmear
+ process.HFXresphiX0X010
+ process.HFXresphiXX020Xsmear
+ process.HFXresphiXX020
+ process.HFXresphiXX030Xsmear
+ process.HFXresphiXX030
+ process.HFXresphiXX040Xsmear
+ process.HFXresphiXX040
+ process.HFXresphiXX050Xsmear
+ process.HFXresphiXX050
)
