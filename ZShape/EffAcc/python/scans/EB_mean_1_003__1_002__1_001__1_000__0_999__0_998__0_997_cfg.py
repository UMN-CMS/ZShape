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
    input = cms.untracked.int32(50000)
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


process.EBXmeanX1X003Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX1X003Xsmear.EB.mean = cms.double(1.003)

process.EBXmeanX1X003 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX1X003.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX1X003.zsrc = cms.untracked.InputTag("EBXmeanX1X003Xsmear","ZEventParticles")
process.EBXmeanX1X003.zElectronsCollection = cms.untracked.InputTag("EBXmeanX1X003Xsmear","ZEventParticles")

process.EBXmeanX1X002Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX1X002Xsmear.EB.mean = cms.double(1.002)

process.EBXmeanX1X002 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX1X002.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX1X002.zsrc = cms.untracked.InputTag("EBXmeanX1X002Xsmear","ZEventParticles")
process.EBXmeanX1X002.zElectronsCollection = cms.untracked.InputTag("EBXmeanX1X002Xsmear","ZEventParticles")

process.EBXmeanX1X001Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX1X001Xsmear.EB.mean = cms.double(1.001)

process.EBXmeanX1X001 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX1X001.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX1X001.zsrc = cms.untracked.InputTag("EBXmeanX1X001Xsmear","ZEventParticles")
process.EBXmeanX1X001.zElectronsCollection = cms.untracked.InputTag("EBXmeanX1X001Xsmear","ZEventParticles")

process.EBXmeanX1X000Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX1X000Xsmear.EB.mean = cms.double(1.000)

process.EBXmeanX1X000 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX1X000.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX1X000.zsrc = cms.untracked.InputTag("EBXmeanX1X000Xsmear","ZEventParticles")
process.EBXmeanX1X000.zElectronsCollection = cms.untracked.InputTag("EBXmeanX1X000Xsmear","ZEventParticles")

process.EBXmeanX0X999Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX0X999Xsmear.EB.mean = cms.double(0.999)

process.EBXmeanX0X999 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX0X999.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX0X999.zsrc = cms.untracked.InputTag("EBXmeanX0X999Xsmear","ZEventParticles")
process.EBXmeanX0X999.zElectronsCollection = cms.untracked.InputTag("EBXmeanX0X999Xsmear","ZEventParticles")

process.EBXmeanX0X998Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX0X998Xsmear.EB.mean = cms.double(0.998)

process.EBXmeanX0X998 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX0X998.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX0X998.zsrc = cms.untracked.InputTag("EBXmeanX0X998Xsmear","ZEventParticles")
process.EBXmeanX0X998.zElectronsCollection = cms.untracked.InputTag("EBXmeanX0X998Xsmear","ZEventParticles")

process.EBXmeanX0X997Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX0X997Xsmear.EB.mean = cms.double(0.997)

process.EBXmeanX0X997 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX0X997.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX0X997.zsrc = cms.untracked.InputTag("EBXmeanX0X997Xsmear","ZEventParticles")
process.EBXmeanX0X997.zElectronsCollection = cms.untracked.InputTag("EBXmeanX0X997Xsmear","ZEventParticles")

process.p = cms.Path(process.f2s
+ process.EBXmeanX1X003Xsmear
+ process.EBXmeanX1X003
+ process.EBXmeanX1X002Xsmear
+ process.EBXmeanX1X002
+ process.EBXmeanX1X001Xsmear
+ process.EBXmeanX1X001
+ process.EBXmeanX1X000Xsmear
+ process.EBXmeanX1X000
+ process.EBXmeanX0X999Xsmear
+ process.EBXmeanX0X999
+ process.EBXmeanX0X998Xsmear
+ process.EBXmeanX0X998
+ process.EBXmeanX0X997Xsmear
+ process.EBXmeanX0X997
)
