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


process.HFXresetaX0X001Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresetaX0X001Xsmear.HF.reseta = cms.double(0.001)

process.HFXresetaX0X001 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresetaX0X001.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresetaX0X001.zsrc = cms.untracked.InputTag("HFXresetaX0X001Xsmear","ZEventParticles")
process.HFXresetaX0X001.zElectronsCollection = cms.untracked.InputTag("HFXresetaX0X001Xsmear","ZEventParticles")

process.HFXresetaX0X025Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresetaX0X025Xsmear.HF.reseta = cms.double(0.025)

process.HFXresetaX0X025 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresetaX0X025.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresetaX0X025.zsrc = cms.untracked.InputTag("HFXresetaX0X025Xsmear","ZEventParticles")
process.HFXresetaX0X025.zElectronsCollection = cms.untracked.InputTag("HFXresetaX0X025Xsmear","ZEventParticles")

process.HFXresetaX0X05Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresetaX0X05Xsmear.HF.reseta = cms.double(0.05)

process.HFXresetaX0X05 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresetaX0X05.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresetaX0X05.zsrc = cms.untracked.InputTag("HFXresetaX0X05Xsmear","ZEventParticles")
process.HFXresetaX0X05.zElectronsCollection = cms.untracked.InputTag("HFXresetaX0X05Xsmear","ZEventParticles")

process.HFXresetaX0X075Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresetaX0X075Xsmear.HF.reseta = cms.double(0.075)

process.HFXresetaX0X075 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresetaX0X075.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresetaX0X075.zsrc = cms.untracked.InputTag("HFXresetaX0X075Xsmear","ZEventParticles")
process.HFXresetaX0X075.zElectronsCollection = cms.untracked.InputTag("HFXresetaX0X075Xsmear","ZEventParticles")

process.HFXresetaX0X10Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresetaX0X10Xsmear.HF.reseta = cms.double(0.10)

process.HFXresetaX0X10 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresetaX0X10.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresetaX0X10.zsrc = cms.untracked.InputTag("HFXresetaX0X10Xsmear","ZEventParticles")
process.HFXresetaX0X10.zElectronsCollection = cms.untracked.InputTag("HFXresetaX0X10Xsmear","ZEventParticles")

process.HFXresetaX0X125Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresetaX0X125Xsmear.HF.reseta = cms.double(0.125)

process.HFXresetaX0X125 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresetaX0X125.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresetaX0X125.zsrc = cms.untracked.InputTag("HFXresetaX0X125Xsmear","ZEventParticles")
process.HFXresetaX0X125.zElectronsCollection = cms.untracked.InputTag("HFXresetaX0X125Xsmear","ZEventParticles")

process.HFXresetaX0X15Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresetaX0X15Xsmear.HF.reseta = cms.double(0.15)

process.HFXresetaX0X15 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresetaX0X15.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresetaX0X15.zsrc = cms.untracked.InputTag("HFXresetaX0X15Xsmear","ZEventParticles")
process.HFXresetaX0X15.zElectronsCollection = cms.untracked.InputTag("HFXresetaX0X15Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.HFXresetaX0X001Xsmear
+ process.HFXresetaX0X001
+ process.HFXresetaX0X025Xsmear
+ process.HFXresetaX0X025
+ process.HFXresetaX0X05Xsmear
+ process.HFXresetaX0X05
+ process.HFXresetaX0X075Xsmear
+ process.HFXresetaX0X075
+ process.HFXresetaX0X10Xsmear
+ process.HFXresetaX0X10
+ process.HFXresetaX0X125Xsmear
+ process.HFXresetaX0X125
+ process.HFXresetaX0X15Xsmear
+ process.HFXresetaX0X15
)
