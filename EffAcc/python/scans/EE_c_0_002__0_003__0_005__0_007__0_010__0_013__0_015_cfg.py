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


process.EEXcX0X002Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X002Xsmear.EE.c = cms.double(0.002)

process.EEXcX0X002 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X002.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X002.zsrc = cms.untracked.InputTag("EEXcX0X002Xsmear","ZEventParticles")
process.EEXcX0X002.zElectronsCollection = cms.untracked.InputTag("EEXcX0X002Xsmear","ZEventParticles")

process.EEXcX0X003Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X003Xsmear.EE.c = cms.double(0.003)

process.EEXcX0X003 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X003.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X003.zsrc = cms.untracked.InputTag("EEXcX0X003Xsmear","ZEventParticles")
process.EEXcX0X003.zElectronsCollection = cms.untracked.InputTag("EEXcX0X003Xsmear","ZEventParticles")

process.EEXcX0X005Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X005Xsmear.EE.c = cms.double(0.005)

process.EEXcX0X005 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X005.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X005.zsrc = cms.untracked.InputTag("EEXcX0X005Xsmear","ZEventParticles")
process.EEXcX0X005.zElectronsCollection = cms.untracked.InputTag("EEXcX0X005Xsmear","ZEventParticles")

process.EEXcX0X007Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X007Xsmear.EE.c = cms.double(0.007)

process.EEXcX0X007 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X007.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X007.zsrc = cms.untracked.InputTag("EEXcX0X007Xsmear","ZEventParticles")
process.EEXcX0X007.zElectronsCollection = cms.untracked.InputTag("EEXcX0X007Xsmear","ZEventParticles")

process.EEXcX0X010Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X010Xsmear.EE.c = cms.double(0.010)

process.EEXcX0X010 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X010.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X010.zsrc = cms.untracked.InputTag("EEXcX0X010Xsmear","ZEventParticles")
process.EEXcX0X010.zElectronsCollection = cms.untracked.InputTag("EEXcX0X010Xsmear","ZEventParticles")

process.EEXcX0X013Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X013Xsmear.EE.c = cms.double(0.013)

process.EEXcX0X013 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X013.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X013.zsrc = cms.untracked.InputTag("EEXcX0X013Xsmear","ZEventParticles")
process.EEXcX0X013.zElectronsCollection = cms.untracked.InputTag("EEXcX0X013Xsmear","ZEventParticles")

process.EEXcX0X015Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X015Xsmear.EE.c = cms.double(0.015)

process.EEXcX0X015 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X015.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X015.zsrc = cms.untracked.InputTag("EEXcX0X015Xsmear","ZEventParticles")
process.EEXcX0X015.zElectronsCollection = cms.untracked.InputTag("EEXcX0X015Xsmear","ZEventParticles")

process.p = cms.Path(process.f2s
+ process.EEXcX0X002Xsmear
+ process.EEXcX0X002
+ process.EEXcX0X003Xsmear
+ process.EEXcX0X003
+ process.EEXcX0X005Xsmear
+ process.EEXcX0X005
+ process.EEXcX0X007Xsmear
+ process.EEXcX0X007
+ process.EEXcX0X010Xsmear
+ process.EEXcX0X010
+ process.EEXcX0X013Xsmear
+ process.EEXcX0X013
+ process.EEXcX0X015Xsmear
+ process.EEXcX0X015
)
