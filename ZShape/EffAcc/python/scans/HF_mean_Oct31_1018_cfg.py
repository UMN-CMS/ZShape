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


process.HFXmeanX0X5Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X5Xsmear.HF.mean = cms.double(0.5)

process.HFXmeanX0X5 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X5.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X5.zsrc = cms.untracked.InputTag("HFXmeanX0X5Xsmear","ZEventParticles")
process.HFXmeanX0X5.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X5Xsmear","ZEventParticles")

process.HFXmeanX0X8Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X8Xsmear.HF.mean = cms.double(0.8)

process.HFXmeanX0X8 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X8.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X8.zsrc = cms.untracked.InputTag("HFXmeanX0X8Xsmear","ZEventParticles")
process.HFXmeanX0X8.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X8Xsmear","ZEventParticles")

process.HFXmeanX1X0Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X0Xsmear.HF.mean = cms.double(1.0)

process.HFXmeanX1X0 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X0.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X0.zsrc = cms.untracked.InputTag("HFXmeanX1X0Xsmear","ZEventParticles")
process.HFXmeanX1X0.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X0Xsmear","ZEventParticles")

process.HFXmeanX1X2Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X2Xsmear.HF.mean = cms.double(1.2)

process.HFXmeanX1X2 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X2.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X2.zsrc = cms.untracked.InputTag("HFXmeanX1X2Xsmear","ZEventParticles")
process.HFXmeanX1X2.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X2Xsmear","ZEventParticles")

process.HFXmeanX1X5Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X5Xsmear.HF.mean = cms.double(1.5)

process.HFXmeanX1X5 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X5.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X5.zsrc = cms.untracked.InputTag("HFXmeanX1X5Xsmear","ZEventParticles")
process.HFXmeanX1X5.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X5Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.HFXmeanX0X5Xsmear
+ process.HFXmeanX0X5
+ process.HFXmeanX0X8Xsmear
+ process.HFXmeanX0X8
+ process.HFXmeanX1X0Xsmear
+ process.HFXmeanX1X0
+ process.HFXmeanX1X2Xsmear
+ process.HFXmeanX1X2
+ process.HFXmeanX1X5Xsmear
+ process.HFXmeanX1X5
)
