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


process.EEXcX0X001Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X001Xsmear.EE.c = cms.double(0.001)

process.EEXcX0X001 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X001.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X001.zsrc = cms.untracked.InputTag("EEXcX0X001Xsmear","ZEventParticles")
process.EEXcX0X001.zElectronsCollection = cms.untracked.InputTag("EEXcX0X001Xsmear","ZEventParticles")

process.EEXcX0X004Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X004Xsmear.EE.c = cms.double(0.004)

process.EEXcX0X004 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X004.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X004.zsrc = cms.untracked.InputTag("EEXcX0X004Xsmear","ZEventParticles")
process.EEXcX0X004.zElectronsCollection = cms.untracked.InputTag("EEXcX0X004Xsmear","ZEventParticles")

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

process.EEXcX0X016Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X016Xsmear.EE.c = cms.double(0.016)

process.EEXcX0X016 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X016.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X016.zsrc = cms.untracked.InputTag("EEXcX0X016Xsmear","ZEventParticles")
process.EEXcX0X016.zElectronsCollection = cms.untracked.InputTag("EEXcX0X016Xsmear","ZEventParticles")

process.EEXcX0X019Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXcX0X019Xsmear.EE.c = cms.double(0.019)

process.EEXcX0X019 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXcX0X019.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXcX0X019.zsrc = cms.untracked.InputTag("EEXcX0X019Xsmear","ZEventParticles")
process.EEXcX0X019.zElectronsCollection = cms.untracked.InputTag("EEXcX0X019Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.EEXcX0X001Xsmear
+ process.EEXcX0X001
+ process.EEXcX0X004Xsmear
+ process.EEXcX0X004
+ process.EEXcX0X007Xsmear
+ process.EEXcX0X007
+ process.EEXcX0X010Xsmear
+ process.EEXcX0X010
+ process.EEXcX0X013Xsmear
+ process.EEXcX0X013
+ process.EEXcX0X016Xsmear
+ process.EEXcX0X016
+ process.EEXcX0X019Xsmear
+ process.EEXcX0X019
)
