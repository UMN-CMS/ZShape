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
process.HFXconstantX0X001Xsmear.HF.constantp = cms.double(0.001)
process.HFXconstantX0X001Xsmear.HF.constantm = cms.double(0.001)

process.HFXconstantX0X001 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X001.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X001.zsrc = cms.untracked.InputTag("HFXconstantX0X001Xsmear","ZEventParticles")
process.HFXconstantX0X001.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X001Xsmear","ZEventParticles")

process.HFXconstantX0X010Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X010Xsmear.HF.constantp = cms.double(0.010)
process.HFXconstantX0X010Xsmear.HF.constantm = cms.double(0.010)

process.HFXconstantX0X010 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X010.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X010.zsrc = cms.untracked.InputTag("HFXconstantX0X010Xsmear","ZEventParticles")
process.HFXconstantX0X010.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X010Xsmear","ZEventParticles")

process.HFXconstantX0X030Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X030Xsmear.HF.constantp = cms.double(0.030)
process.HFXconstantX0X030Xsmear.HF.constantm = cms.double(0.030)

process.HFXconstantX0X030 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X030.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X030.zsrc = cms.untracked.InputTag("HFXconstantX0X030Xsmear","ZEventParticles")
process.HFXconstantX0X030.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X030Xsmear","ZEventParticles")

process.HFXconstantX0X050Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X050Xsmear.HF.constantp = cms.double(0.050)
process.HFXconstantX0X050Xsmear.HF.constantm = cms.double(0.050)

process.HFXconstantX0X050 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X050.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X050.zsrc = cms.untracked.InputTag("HFXconstantX0X050Xsmear","ZEventParticles")
process.HFXconstantX0X050.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X050Xsmear","ZEventParticles")

process.HFXconstantX0X070Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X070Xsmear.HF.constantp = cms.double(0.070)
process.HFXconstantX0X070Xsmear.HF.constantm = cms.double(0.070)

process.HFXconstantX0X070 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X070.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X070.zsrc = cms.untracked.InputTag("HFXconstantX0X070Xsmear","ZEventParticles")
process.HFXconstantX0X070.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X070Xsmear","ZEventParticles")

process.HFXconstantX0X100Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X100Xsmear.HF.constantp = cms.double(0.100)
process.HFXconstantX0X100Xsmear.HF.constantm = cms.double(0.100)

process.HFXconstantX0X100 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X100.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X100.zsrc = cms.untracked.InputTag("HFXconstantX0X100Xsmear","ZEventParticles")
process.HFXconstantX0X100.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X100Xsmear","ZEventParticles")

process.HFXconstantX0X130Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X130Xsmear.HF.constantp = cms.double(0.130)
process.HFXconstantX0X130Xsmear.HF.constantm = cms.double(0.130)

process.HFXconstantX0X130 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X130.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X130.zsrc = cms.untracked.InputTag("HFXconstantX0X130Xsmear","ZEventParticles")
process.HFXconstantX0X130.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X130Xsmear","ZEventParticles")

process.p = cms.Path(process.f2s
+ process.HFXconstantX0X001Xsmear
+ process.HFXconstantX0X001
+ process.HFXconstantX0X010Xsmear
+ process.HFXconstantX0X010
+ process.HFXconstantX0X030Xsmear
+ process.HFXconstantX0X030
+ process.HFXconstantX0X050Xsmear
+ process.HFXconstantX0X050
+ process.HFXconstantX0X070Xsmear
+ process.HFXconstantX0X070
+ process.HFXconstantX0X100Xsmear
+ process.HFXconstantX0X100
+ process.HFXconstantX0X130Xsmear
+ process.HFXconstantX0X130
)
