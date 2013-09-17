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


process.EEXcX0X0001Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X0001Xsmear.EE.c = cms.double(0.0001)

process.EEXcX0X0001 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X0001.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X0001.zsrc = cms.untracked.InputTag("EEXcX0X0001Xsmear","ZEventParticles")
process.EEXcX0X0001.zElectronsCollection = cms.untracked.InputTag("EEXcX0X0001Xsmear","ZEventParticles")

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

process.EEXcX0X012Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X012Xsmear.EE.c = cms.double(0.012)

process.EEXcX0X012 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X012.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X012.zsrc = cms.untracked.InputTag("EEXcX0X012Xsmear","ZEventParticles")
process.EEXcX0X012.zElectronsCollection = cms.untracked.InputTag("EEXcX0X012Xsmear","ZEventParticles")

process.EEXcX0X013Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X013Xsmear.EE.c = cms.double(0.013)

process.EEXcX0X013 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X013.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X013.zsrc = cms.untracked.InputTag("EEXcX0X013Xsmear","ZEventParticles")
process.EEXcX0X013.zElectronsCollection = cms.untracked.InputTag("EEXcX0X013Xsmear","ZEventParticles")

process.EEXcX0X014Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X014Xsmear.EE.c = cms.double(0.014)

process.EEXcX0X014 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X014.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X014.zsrc = cms.untracked.InputTag("EEXcX0X014Xsmear","ZEventParticles")
process.EEXcX0X014.zElectronsCollection = cms.untracked.InputTag("EEXcX0X014Xsmear","ZEventParticles")

process.EEXcX0X015Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X015Xsmear.EE.c = cms.double(0.015)

process.EEXcX0X015 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X015.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X015.zsrc = cms.untracked.InputTag("EEXcX0X015Xsmear","ZEventParticles")
process.EEXcX0X015.zElectronsCollection = cms.untracked.InputTag("EEXcX0X015Xsmear","ZEventParticles")

process.EEXcX0X016Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X016Xsmear.EE.c = cms.double(0.016)

process.EEXcX0X016 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X016.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X016.zsrc = cms.untracked.InputTag("EEXcX0X016Xsmear","ZEventParticles")
process.EEXcX0X016.zElectronsCollection = cms.untracked.InputTag("EEXcX0X016Xsmear","ZEventParticles")

process.EEXcX0X017Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X017Xsmear.EE.c = cms.double(0.017)

process.EEXcX0X017 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X017.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X017.zsrc = cms.untracked.InputTag("EEXcX0X017Xsmear","ZEventParticles")
process.EEXcX0X017.zElectronsCollection = cms.untracked.InputTag("EEXcX0X017Xsmear","ZEventParticles")

process.EEXcX0X018Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X018Xsmear.EE.c = cms.double(0.018)

process.EEXcX0X018 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X018.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X018.zsrc = cms.untracked.InputTag("EEXcX0X018Xsmear","ZEventParticles")
process.EEXcX0X018.zElectronsCollection = cms.untracked.InputTag("EEXcX0X018Xsmear","ZEventParticles")

process.EEXcX0X019Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X019Xsmear.EE.c = cms.double(0.019)

process.EEXcX0X019 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X019.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X019.zsrc = cms.untracked.InputTag("EEXcX0X019Xsmear","ZEventParticles")
process.EEXcX0X019.zElectronsCollection = cms.untracked.InputTag("EEXcX0X019Xsmear","ZEventParticles")

process.EEXcX0X02Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X02Xsmear.EE.c = cms.double(0.02)

process.EEXcX0X02 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X02.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X02.zsrc = cms.untracked.InputTag("EEXcX0X02Xsmear","ZEventParticles")
process.EEXcX0X02.zElectronsCollection = cms.untracked.InputTag("EEXcX0X02Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.EEXcX0X0001Xsmear
+ process.EEXcX0X0001
+ process.EEXcX0X001Xsmear
+ process.EEXcX0X001
+ process.EEXcX0X005Xsmear
+ process.EEXcX0X005
+ process.EEXcX0X01Xsmear
+ process.EEXcX0X01
+ process.EEXcX0X012Xsmear
+ process.EEXcX0X012
+ process.EEXcX0X013Xsmear
+ process.EEXcX0X013
+ process.EEXcX0X014Xsmear
+ process.EEXcX0X014
+ process.EEXcX0X015Xsmear
+ process.EEXcX0X015
+ process.EEXcX0X016Xsmear
+ process.EEXcX0X016
+ process.EEXcX0X017Xsmear
+ process.EEXcX0X017
+ process.EEXcX0X018Xsmear
+ process.EEXcX0X018
+ process.EEXcX0X019Xsmear
+ process.EEXcX0X019
+ process.EEXcX0X02Xsmear
+ process.EEXcX0X02
)
