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


process.EEXmeanX0X989Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X989Xsmear.EE.mean = cms.double(0.989)

process.EEXmeanX0X989 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X989.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X989.zsrc = cms.untracked.InputTag("EEXmeanX0X989Xsmear","ZEventParticles")
process.EEXmeanX0X989.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X989Xsmear","ZEventParticles")

process.EEXmeanX0X990Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X990Xsmear.EE.mean = cms.double(0.990)

process.EEXmeanX0X990 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X990.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X990.zsrc = cms.untracked.InputTag("EEXmeanX0X990Xsmear","ZEventParticles")
process.EEXmeanX0X990.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X990Xsmear","ZEventParticles")

process.EEXmeanX0X991Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X991Xsmear.EE.mean = cms.double(0.991)

process.EEXmeanX0X991 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X991.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X991.zsrc = cms.untracked.InputTag("EEXmeanX0X991Xsmear","ZEventParticles")
process.EEXmeanX0X991.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X991Xsmear","ZEventParticles")

process.EEXmeanX0X992Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X992Xsmear.EE.mean = cms.double(0.992)

process.EEXmeanX0X992 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X992.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X992.zsrc = cms.untracked.InputTag("EEXmeanX0X992Xsmear","ZEventParticles")
process.EEXmeanX0X992.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X992Xsmear","ZEventParticles")

process.EEXmeanX0X993Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X993Xsmear.EE.mean = cms.double(0.993)

process.EEXmeanX0X993 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X993.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X993.zsrc = cms.untracked.InputTag("EEXmeanX0X993Xsmear","ZEventParticles")
process.EEXmeanX0X993.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X993Xsmear","ZEventParticles")

process.EEXmeanX0X994Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X994Xsmear.EE.mean = cms.double(0.994)

process.EEXmeanX0X994 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X994.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X994.zsrc = cms.untracked.InputTag("EEXmeanX0X994Xsmear","ZEventParticles")
process.EEXmeanX0X994.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X994Xsmear","ZEventParticles")

process.EEXmeanX0X995Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X995Xsmear.EE.mean = cms.double(0.995)

process.EEXmeanX0X995 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X995.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X995.zsrc = cms.untracked.InputTag("EEXmeanX0X995Xsmear","ZEventParticles")
process.EEXmeanX0X995.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X995Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.EEXmeanX0X989Xsmear
+ process.EEXmeanX0X989
+ process.EEXmeanX0X990Xsmear
+ process.EEXmeanX0X990
+ process.EEXmeanX0X991Xsmear
+ process.EEXmeanX0X991
+ process.EEXmeanX0X992Xsmear
+ process.EEXmeanX0X992
+ process.EEXmeanX0X993Xsmear
+ process.EEXmeanX0X993
+ process.EEXmeanX0X994Xsmear
+ process.EEXmeanX0X994
+ process.EEXmeanX0X995Xsmear
+ process.EEXmeanX0X995
)
