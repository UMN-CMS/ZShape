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


process.HFXconstantX0X1Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X1Xsmear.HF.constant = cms.double(0.1)

process.HFXconstantX0X1 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X1.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X1.zsrc = cms.untracked.InputTag("HFXconstantX0X1Xsmear","ZEventParticles")
process.HFXconstantX0X1.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X1Xsmear","ZEventParticles")

process.HFXconstantX0X11Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X11Xsmear.HF.constant = cms.double(0.11)

process.HFXconstantX0X11 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X11.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X11.zsrc = cms.untracked.InputTag("HFXconstantX0X11Xsmear","ZEventParticles")
process.HFXconstantX0X11.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X11Xsmear","ZEventParticles")

process.HFXconstantX0X12Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X12Xsmear.HF.constant = cms.double(0.12)

process.HFXconstantX0X12 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X12.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X12.zsrc = cms.untracked.InputTag("HFXconstantX0X12Xsmear","ZEventParticles")
process.HFXconstantX0X12.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X12Xsmear","ZEventParticles")

process.HFXconstantX0X13Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X13Xsmear.HF.constant = cms.double(0.13)

process.HFXconstantX0X13 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X13.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X13.zsrc = cms.untracked.InputTag("HFXconstantX0X13Xsmear","ZEventParticles")
process.HFXconstantX0X13.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X13Xsmear","ZEventParticles")

process.HFXconstantX0X14Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X14Xsmear.HF.constant = cms.double(0.14)

process.HFXconstantX0X14 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X14.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X14.zsrc = cms.untracked.InputTag("HFXconstantX0X14Xsmear","ZEventParticles")
process.HFXconstantX0X14.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X14Xsmear","ZEventParticles")

process.HFXconstantX0X15Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X15Xsmear.HF.constant = cms.double(0.15)

process.HFXconstantX0X15 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X15.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X15.zsrc = cms.untracked.InputTag("HFXconstantX0X15Xsmear","ZEventParticles")
process.HFXconstantX0X15.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X15Xsmear","ZEventParticles")

process.HFXconstantX0X16Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X16Xsmear.HF.constant = cms.double(0.16)

process.HFXconstantX0X16 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X16.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X16.zsrc = cms.untracked.InputTag("HFXconstantX0X16Xsmear","ZEventParticles")
process.HFXconstantX0X16.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X16Xsmear","ZEventParticles")

process.HFXconstantX0X17Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X17Xsmear.HF.constant = cms.double(0.17)

process.HFXconstantX0X17 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X17.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X17.zsrc = cms.untracked.InputTag("HFXconstantX0X17Xsmear","ZEventParticles")
process.HFXconstantX0X17.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X17Xsmear","ZEventParticles")

process.HFXconstantX0X18Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X18Xsmear.HF.constant = cms.double(0.18)

process.HFXconstantX0X18 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X18.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X18.zsrc = cms.untracked.InputTag("HFXconstantX0X18Xsmear","ZEventParticles")
process.HFXconstantX0X18.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X18Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.HFXconstantX0X1Xsmear
+ process.HFXconstantX0X1
+ process.HFXconstantX0X11Xsmear
+ process.HFXconstantX0X11
+ process.HFXconstantX0X12Xsmear
+ process.HFXconstantX0X12
+ process.HFXconstantX0X13Xsmear
+ process.HFXconstantX0X13
+ process.HFXconstantX0X14Xsmear
+ process.HFXconstantX0X14
+ process.HFXconstantX0X15Xsmear
+ process.HFXconstantX0X15
+ process.HFXconstantX0X16Xsmear
+ process.HFXconstantX0X16
+ process.HFXconstantX0X17Xsmear
+ process.HFXconstantX0X17
+ process.HFXconstantX0X18Xsmear
+ process.HFXconstantX0X18
)
