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


process.HFXmeanX0X05Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X05Xsmear.HF.mean = cms.double(0.05)

process.HFXmeanX0X05 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X05.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X05.zsrc = cms.untracked.InputTag("HFXmeanX0X05Xsmear","ZEventParticles")
process.HFXmeanX0X05.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X05Xsmear","ZEventParticles")

process.HFXmeanX0X1Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X1Xsmear.HF.mean = cms.double(0.1)

process.HFXmeanX0X1 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X1.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X1.zsrc = cms.untracked.InputTag("HFXmeanX0X1Xsmear","ZEventParticles")
process.HFXmeanX0X1.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X1Xsmear","ZEventParticles")

process.HFXmeanX0X12Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X12Xsmear.HF.mean = cms.double(0.12)

process.HFXmeanX0X12 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X12.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X12.zsrc = cms.untracked.InputTag("HFXmeanX0X12Xsmear","ZEventParticles")
process.HFXmeanX0X12.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X12Xsmear","ZEventParticles")

process.HFXmeanX0X14Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X14Xsmear.HF.mean = cms.double(0.14)

process.HFXmeanX0X14 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X14.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X14.zsrc = cms.untracked.InputTag("HFXmeanX0X14Xsmear","ZEventParticles")
process.HFXmeanX0X14.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X14Xsmear","ZEventParticles")

process.HFXmeanX0X16Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X16Xsmear.HF.mean = cms.double(0.16)

process.HFXmeanX0X16 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X16.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X16.zsrc = cms.untracked.InputTag("HFXmeanX0X16Xsmear","ZEventParticles")
process.HFXmeanX0X16.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X16Xsmear","ZEventParticles")

process.HFXmeanX0X18Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X18Xsmear.HF.mean = cms.double(0.18)

process.HFXmeanX0X18 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X18.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X18.zsrc = cms.untracked.InputTag("HFXmeanX0X18Xsmear","ZEventParticles")
process.HFXmeanX0X18.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X18Xsmear","ZEventParticles")

process.HFXmeanX0X2Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X2Xsmear.HF.mean = cms.double(0.2)

process.HFXmeanX0X2 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X2.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X2.zsrc = cms.untracked.InputTag("HFXmeanX0X2Xsmear","ZEventParticles")
process.HFXmeanX0X2.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X2Xsmear","ZEventParticles")

process.HFXmeanX0X22Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X22Xsmear.HF.mean = cms.double(0.22)

process.HFXmeanX0X22 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X22.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X22.zsrc = cms.untracked.InputTag("HFXmeanX0X22Xsmear","ZEventParticles")
process.HFXmeanX0X22.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X22Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.HFXmeanX0X05Xsmear
+ process.HFXmeanX0X05
+ process.HFXmeanX0X1Xsmear
+ process.HFXmeanX0X1
+ process.HFXmeanX0X12Xsmear
+ process.HFXmeanX0X12
+ process.HFXmeanX0X14Xsmear
+ process.HFXmeanX0X14
+ process.HFXmeanX0X16Xsmear
+ process.HFXmeanX0X16
+ process.HFXmeanX0X18Xsmear
+ process.HFXmeanX0X18
+ process.HFXmeanX0X2Xsmear
+ process.HFXmeanX0X2
+ process.HFXmeanX0X22Xsmear
+ process.HFXmeanX0X22
)
