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


process.EEXmeanX1X003Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX1X003Xsmear.EE.mean = cms.double(1.003)

process.EEXmeanX1X003 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX1X003.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX1X003.zsrc = cms.untracked.InputTag("EEXmeanX1X003Xsmear","ZEventParticles")
process.EEXmeanX1X003.zElectronsCollection = cms.untracked.InputTag("EEXmeanX1X003Xsmear","ZEventParticles")

process.EEXmeanX1X002Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX1X002Xsmear.EE.mean = cms.double(1.002)

process.EEXmeanX1X002 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX1X002.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX1X002.zsrc = cms.untracked.InputTag("EEXmeanX1X002Xsmear","ZEventParticles")
process.EEXmeanX1X002.zElectronsCollection = cms.untracked.InputTag("EEXmeanX1X002Xsmear","ZEventParticles")

process.EEXmeanX1X001Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX1X001Xsmear.EE.mean = cms.double(1.001)

process.EEXmeanX1X001 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX1X001.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX1X001.zsrc = cms.untracked.InputTag("EEXmeanX1X001Xsmear","ZEventParticles")
process.EEXmeanX1X001.zElectronsCollection = cms.untracked.InputTag("EEXmeanX1X001Xsmear","ZEventParticles")

process.EEXmeanX1X000Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX1X000Xsmear.EE.mean = cms.double(1.000)

process.EEXmeanX1X000 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX1X000.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX1X000.zsrc = cms.untracked.InputTag("EEXmeanX1X000Xsmear","ZEventParticles")
process.EEXmeanX1X000.zElectronsCollection = cms.untracked.InputTag("EEXmeanX1X000Xsmear","ZEventParticles")

process.EEXmeanX0X999Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X999Xsmear.EE.mean = cms.double(0.999)

process.EEXmeanX0X999 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X999.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X999.zsrc = cms.untracked.InputTag("EEXmeanX0X999Xsmear","ZEventParticles")
process.EEXmeanX0X999.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X999Xsmear","ZEventParticles")

process.EEXmeanX0X998Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X998Xsmear.EE.mean = cms.double(0.998)

process.EEXmeanX0X998 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X998.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X998.zsrc = cms.untracked.InputTag("EEXmeanX0X998Xsmear","ZEventParticles")
process.EEXmeanX0X998.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X998Xsmear","ZEventParticles")

process.EEXmeanX0X997Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X997Xsmear.EE.mean = cms.double(0.997)

process.EEXmeanX0X997 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X997.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X997.zsrc = cms.untracked.InputTag("EEXmeanX0X997Xsmear","ZEventParticles")
process.EEXmeanX0X997.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X997Xsmear","ZEventParticles")

process.p = cms.Path(process.f2s
+ process.EEXmeanX1X003Xsmear
+ process.EEXmeanX1X003
+ process.EEXmeanX1X002Xsmear
+ process.EEXmeanX1X002
+ process.EEXmeanX1X001Xsmear
+ process.EEXmeanX1X001
+ process.EEXmeanX1X000Xsmear
+ process.EEXmeanX1X000
+ process.EEXmeanX0X999Xsmear
+ process.EEXmeanX0X999
+ process.EEXmeanX0X998Xsmear
+ process.EEXmeanX0X998
+ process.EEXmeanX0X997Xsmear
+ process.EEXmeanX0X997
)
