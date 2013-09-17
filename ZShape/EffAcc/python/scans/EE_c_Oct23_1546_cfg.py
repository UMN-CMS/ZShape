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


process.EEXcX0X00001Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X00001Xsmear.EE.c = cms.double(0.00001)

process.EEXcX0X00001 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X00001.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X00001.zsrc = cms.untracked.InputTag("EEXcX0X00001Xsmear","ZEventParticles")
process.EEXcX0X00001.zElectronsCollection = cms.untracked.InputTag("EEXcX0X00001Xsmear","ZEventParticles")

process.EEXcX0X0005Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X0005Xsmear.EE.c = cms.double(0.0005)

process.EEXcX0X0005 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X0005.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X0005.zsrc = cms.untracked.InputTag("EEXcX0X0005Xsmear","ZEventParticles")
process.EEXcX0X0005.zElectronsCollection = cms.untracked.InputTag("EEXcX0X0005Xsmear","ZEventParticles")

process.EEXcX0X001Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X001Xsmear.EE.c = cms.double(0.001)

process.EEXcX0X001 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X001.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X001.zsrc = cms.untracked.InputTag("EEXcX0X001Xsmear","ZEventParticles")
process.EEXcX0X001.zElectronsCollection = cms.untracked.InputTag("EEXcX0X001Xsmear","ZEventParticles")

process.EEXcX0X005Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X005Xsmear.EE.c = cms.double(0.005)

process.EEXcX0X005 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X005.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X005.zsrc = cms.untracked.InputTag("EEXcX0X005Xsmear","ZEventParticles")
process.EEXcX0X005.zElectronsCollection = cms.untracked.InputTag("EEXcX0X005Xsmear","ZEventParticles")

process.EEXcX0X01Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X01Xsmear.EE.c = cms.double(0.01)

process.EEXcX0X01 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X01.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X01.zsrc = cms.untracked.InputTag("EEXcX0X01Xsmear","ZEventParticles")
process.EEXcX0X01.zElectronsCollection = cms.untracked.InputTag("EEXcX0X01Xsmear","ZEventParticles")

process.EEXcX0X02Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X02Xsmear.EE.c = cms.double(0.02)

process.EEXcX0X02 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X02.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X02.zsrc = cms.untracked.InputTag("EEXcX0X02Xsmear","ZEventParticles")
process.EEXcX0X02.zElectronsCollection = cms.untracked.InputTag("EEXcX0X02Xsmear","ZEventParticles")

process.EEXcX0X03Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X03Xsmear.EE.c = cms.double(0.03)

process.EEXcX0X03 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X03.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X03.zsrc = cms.untracked.InputTag("EEXcX0X03Xsmear","ZEventParticles")
process.EEXcX0X03.zElectronsCollection = cms.untracked.InputTag("EEXcX0X03Xsmear","ZEventParticles")

process.EEXcX0X04Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X04Xsmear.EE.c = cms.double(0.04)

process.EEXcX0X04 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X04.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X04.zsrc = cms.untracked.InputTag("EEXcX0X04Xsmear","ZEventParticles")
process.EEXcX0X04.zElectronsCollection = cms.untracked.InputTag("EEXcX0X04Xsmear","ZEventParticles")

process.EEXcX0X05Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X05Xsmear.EE.c = cms.double(0.05)

process.EEXcX0X05 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X05.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X05.zsrc = cms.untracked.InputTag("EEXcX0X05Xsmear","ZEventParticles")
process.EEXcX0X05.zElectronsCollection = cms.untracked.InputTag("EEXcX0X05Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.EEXcX0X00001Xsmear
+ process.EEXcX0X00001
+ process.EEXcX0X0005Xsmear
+ process.EEXcX0X0005
+ process.EEXcX0X001Xsmear
+ process.EEXcX0X001
+ process.EEXcX0X005Xsmear
+ process.EEXcX0X005
+ process.EEXcX0X01Xsmear
+ process.EEXcX0X01
+ process.EEXcX0X02Xsmear
+ process.EEXcX0X02
+ process.EEXcX0X03Xsmear
+ process.EEXcX0X03
+ process.EEXcX0X04Xsmear
+ process.EEXcX0X04
+ process.EEXcX0X05Xsmear
+ process.EEXcX0X05
)
