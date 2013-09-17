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


process.EEXcX0X004Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X004Xsmear.EE.c = cms.double(0.004)

process.EEXcX0X004 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X004.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X004.zsrc = cms.untracked.InputTag("EEXcX0X004Xsmear","ZEventParticles")
process.EEXcX0X004.zElectronsCollection = cms.untracked.InputTag("EEXcX0X004Xsmear","ZEventParticles")

process.EEXcX0X008Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X008Xsmear.EE.c = cms.double(0.008)

process.EEXcX0X008 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X008.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X008.zsrc = cms.untracked.InputTag("EEXcX0X008Xsmear","ZEventParticles")
process.EEXcX0X008.zElectronsCollection = cms.untracked.InputTag("EEXcX0X008Xsmear","ZEventParticles")

process.EEXcX0X012Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X012Xsmear.EE.c = cms.double(0.012)

process.EEXcX0X012 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X012.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X012.zsrc = cms.untracked.InputTag("EEXcX0X012Xsmear","ZEventParticles")
process.EEXcX0X012.zElectronsCollection = cms.untracked.InputTag("EEXcX0X012Xsmear","ZEventParticles")

process.EEXcX0X016Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X016Xsmear.EE.c = cms.double(0.016)

process.EEXcX0X016 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X016.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X016.zsrc = cms.untracked.InputTag("EEXcX0X016Xsmear","ZEventParticles")
process.EEXcX0X016.zElectronsCollection = cms.untracked.InputTag("EEXcX0X016Xsmear","ZEventParticles")

process.EEXcX0X020Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X020Xsmear.EE.c = cms.double(0.020)

process.EEXcX0X020 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X020.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X020.zsrc = cms.untracked.InputTag("EEXcX0X020Xsmear","ZEventParticles")
process.EEXcX0X020.zElectronsCollection = cms.untracked.InputTag("EEXcX0X020Xsmear","ZEventParticles")

process.EEXcX0X024Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X024Xsmear.EE.c = cms.double(0.024)

process.EEXcX0X024 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X024.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X024.zsrc = cms.untracked.InputTag("EEXcX0X024Xsmear","ZEventParticles")
process.EEXcX0X024.zElectronsCollection = cms.untracked.InputTag("EEXcX0X024Xsmear","ZEventParticles")

process.p = cms.Path(process.f2s
+ process.EEXcX0X004Xsmear
+ process.EEXcX0X004
+ process.EEXcX0X008Xsmear
+ process.EEXcX0X008
+ process.EEXcX0X012Xsmear
+ process.EEXcX0X012
+ process.EEXcX0X016Xsmear
+ process.EEXcX0X016
+ process.EEXcX0X020Xsmear
+ process.EEXcX0X020
+ process.EEXcX0X024Xsmear
+ process.EEXcX0X024
)
