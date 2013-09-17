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


process.HFXconstantXX22Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantXX22Xsmear.HF.constant = cms.double(.22)

process.HFXconstantXX22 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantXX22.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantXX22.zsrc = cms.untracked.InputTag("HFXconstantXX22Xsmear","ZEventParticles")
process.HFXconstantXX22.zElectronsCollection = cms.untracked.InputTag("HFXconstantXX22Xsmear","ZEventParticles")

process.HFXconstantXX25Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantXX25Xsmear.HF.constant = cms.double(.25)

process.HFXconstantXX25 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantXX25.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantXX25.zsrc = cms.untracked.InputTag("HFXconstantXX25Xsmear","ZEventParticles")
process.HFXconstantXX25.zElectronsCollection = cms.untracked.InputTag("HFXconstantXX25Xsmear","ZEventParticles")

process.HFXconstantXX28Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantXX28Xsmear.HF.constant = cms.double(.28)

process.HFXconstantXX28 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantXX28.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantXX28.zsrc = cms.untracked.InputTag("HFXconstantXX28Xsmear","ZEventParticles")
process.HFXconstantXX28.zElectronsCollection = cms.untracked.InputTag("HFXconstantXX28Xsmear","ZEventParticles")

process.HFXconstantXX3Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantXX3Xsmear.HF.constant = cms.double(.3)

process.HFXconstantXX3 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantXX3.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantXX3.zsrc = cms.untracked.InputTag("HFXconstantXX3Xsmear","ZEventParticles")
process.HFXconstantXX3.zElectronsCollection = cms.untracked.InputTag("HFXconstantXX3Xsmear","ZEventParticles")

process.HFXconstantXX33Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantXX33Xsmear.HF.constant = cms.double(.33)

process.HFXconstantXX33 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantXX33.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantXX33.zsrc = cms.untracked.InputTag("HFXconstantXX33Xsmear","ZEventParticles")
process.HFXconstantXX33.zElectronsCollection = cms.untracked.InputTag("HFXconstantXX33Xsmear","ZEventParticles")

process.HFXconstantXX36Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantXX36Xsmear.HF.constant = cms.double(.36)

process.HFXconstantXX36 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantXX36.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantXX36.zsrc = cms.untracked.InputTag("HFXconstantXX36Xsmear","ZEventParticles")
process.HFXconstantXX36.zElectronsCollection = cms.untracked.InputTag("HFXconstantXX36Xsmear","ZEventParticles")

process.HFXconstantXX4Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantXX4Xsmear.HF.constant = cms.double(.4)

process.HFXconstantXX4 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantXX4.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantXX4.zsrc = cms.untracked.InputTag("HFXconstantXX4Xsmear","ZEventParticles")
process.HFXconstantXX4.zElectronsCollection = cms.untracked.InputTag("HFXconstantXX4Xsmear","ZEventParticles")

process.p = cms.Path(process.f2s
+ process.HFXconstantXX22Xsmear
+ process.HFXconstantXX22
+ process.HFXconstantXX25Xsmear
+ process.HFXconstantXX25
+ process.HFXconstantXX28Xsmear
+ process.HFXconstantXX28
+ process.HFXconstantXX3Xsmear
+ process.HFXconstantXX3
+ process.HFXconstantXX33Xsmear
+ process.HFXconstantXX33
+ process.HFXconstantXX36Xsmear
+ process.HFXconstantXX36
+ process.HFXconstantXX4Xsmear
+ process.HFXconstantXX4
)
