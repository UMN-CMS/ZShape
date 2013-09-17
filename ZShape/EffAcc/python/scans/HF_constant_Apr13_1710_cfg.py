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
    input = cms.untracked.int32(30000)
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

process.HFXconstantX0X005Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X005Xsmear.HF.constantp = cms.double(0.005)
process.HFXconstantX0X005Xsmear.HF.constantm = cms.double(0.005)

process.HFXconstantX0X005 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X005.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X005.zsrc = cms.untracked.InputTag("HFXconstantX0X005Xsmear","ZEventParticles")
process.HFXconstantX0X005.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X005Xsmear","ZEventParticles")

process.HFXconstantX0X01Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X01Xsmear.HF.constantp = cms.double(0.01)
process.HFXconstantX0X01Xsmear.HF.constantm = cms.double(0.01)

process.HFXconstantX0X01 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X01.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X01.zsrc = cms.untracked.InputTag("HFXconstantX0X01Xsmear","ZEventParticles")
process.HFXconstantX0X01.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X01Xsmear","ZEventParticles")

process.HFXconstantX0X05Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X05Xsmear.HF.constantp = cms.double(0.05)
process.HFXconstantX0X05Xsmear.HF.constantm = cms.double(0.05)

process.HFXconstantX0X05 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X05.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X05.zsrc = cms.untracked.InputTag("HFXconstantX0X05Xsmear","ZEventParticles")
process.HFXconstantX0X05.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X05Xsmear","ZEventParticles")

process.HFXconstantX0X1Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X1Xsmear.HF.constantp = cms.double(0.1)
process.HFXconstantX0X1Xsmear.HF.constantm = cms.double(0.1)

process.HFXconstantX0X1 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X1.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X1.zsrc = cms.untracked.InputTag("HFXconstantX0X1Xsmear","ZEventParticles")
process.HFXconstantX0X1.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X1Xsmear","ZEventParticles")

process.HFXconstantX0X15Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X15Xsmear.HF.constantp = cms.double(0.15)
process.HFXconstantX0X15Xsmear.HF.constantm = cms.double(0.15)

process.HFXconstantX0X15 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X15.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X15.zsrc = cms.untracked.InputTag("HFXconstantX0X15Xsmear","ZEventParticles")
process.HFXconstantX0X15.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X15Xsmear","ZEventParticles")

process.HFXconstantX0X2Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X2Xsmear.HF.constantp = cms.double(0.2)
process.HFXconstantX0X2Xsmear.HF.constantm = cms.double(0.2)

process.HFXconstantX0X2 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X2.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X2.zsrc = cms.untracked.InputTag("HFXconstantX0X2Xsmear","ZEventParticles")
process.HFXconstantX0X2.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X2Xsmear","ZEventParticles")

process.HFXconstantX0X25Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X25Xsmear.HF.constantp = cms.double(0.25)
process.HFXconstantX0X25Xsmear.HF.constantm = cms.double(0.25)

process.HFXconstantX0X25 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X25.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X25.zsrc = cms.untracked.InputTag("HFXconstantX0X25Xsmear","ZEventParticles")
process.HFXconstantX0X25.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X25Xsmear","ZEventParticles")

process.HFXconstantX0X3Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X3Xsmear.HF.constantp = cms.double(0.3)
process.HFXconstantX0X3Xsmear.HF.constantm = cms.double(0.3)

process.HFXconstantX0X3 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X3.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X3.zsrc = cms.untracked.InputTag("HFXconstantX0X3Xsmear","ZEventParticles")
process.HFXconstantX0X3.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X3Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.HFXconstantX0X001Xsmear
+ process.HFXconstantX0X001
+ process.HFXconstantX0X005Xsmear
+ process.HFXconstantX0X005
+ process.HFXconstantX0X01Xsmear
+ process.HFXconstantX0X01
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
+ process.HFXconstantX0X3Xsmear
+ process.HFXconstantX0X3
)
