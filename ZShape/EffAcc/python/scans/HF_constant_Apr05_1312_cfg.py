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


process.HFXconstantX0X002Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X002Xsmear.HF.constantp = cms.double(0.002)
process.HFXconstantX0X002Xsmear.HF.constantm = cms.double(0.002)

process.HFXconstantX0X002 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X002.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X002.zsrc = cms.untracked.InputTag("HFXconstantX0X002Xsmear","ZEventParticles")
process.HFXconstantX0X002.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X002Xsmear","ZEventParticles")

process.HFXconstantX0X02Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X02Xsmear.HF.constantp = cms.double(0.02)
process.HFXconstantX0X02Xsmear.HF.constantm = cms.double(0.02)

process.HFXconstantX0X02 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X02.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X02.zsrc = cms.untracked.InputTag("HFXconstantX0X02Xsmear","ZEventParticles")
process.HFXconstantX0X02.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X02Xsmear","ZEventParticles")

process.HFXconstantX0X05Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X05Xsmear.HF.constantp = cms.double(0.05)
process.HFXconstantX0X05Xsmear.HF.constantm = cms.double(0.05)

process.HFXconstantX0X05 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X05.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X05.zsrc = cms.untracked.InputTag("HFXconstantX0X05Xsmear","ZEventParticles")
process.HFXconstantX0X05.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X05Xsmear","ZEventParticles")

process.HFXconstantX0X08Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X08Xsmear.HF.constantp = cms.double(0.08)
process.HFXconstantX0X08Xsmear.HF.constantm = cms.double(0.08)

process.HFXconstantX0X08 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X08.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X08.zsrc = cms.untracked.InputTag("HFXconstantX0X08Xsmear","ZEventParticles")
process.HFXconstantX0X08.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X08Xsmear","ZEventParticles")

process.HFXconstantX0X11Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X11Xsmear.HF.constantp = cms.double(0.11)
process.HFXconstantX0X11Xsmear.HF.constantm = cms.double(0.11)

process.HFXconstantX0X11 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X11.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X11.zsrc = cms.untracked.InputTag("HFXconstantX0X11Xsmear","ZEventParticles")
process.HFXconstantX0X11.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X11Xsmear","ZEventParticles")

process.HFXconstantX0X14Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X14Xsmear.HF.constantp = cms.double(0.14)
process.HFXconstantX0X14Xsmear.HF.constantm = cms.double(0.14)

process.HFXconstantX0X14 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X14.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X14.zsrc = cms.untracked.InputTag("HFXconstantX0X14Xsmear","ZEventParticles")
process.HFXconstantX0X14.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X14Xsmear","ZEventParticles")

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
+ process.HFXconstantX0X002Xsmear
+ process.HFXconstantX0X002
+ process.HFXconstantX0X02Xsmear
+ process.HFXconstantX0X02
+ process.HFXconstantX0X05Xsmear
+ process.HFXconstantX0X05
+ process.HFXconstantX0X08Xsmear
+ process.HFXconstantX0X08
+ process.HFXconstantX0X11Xsmear
+ process.HFXconstantX0X11
+ process.HFXconstantX0X14Xsmear
+ process.HFXconstantX0X14
+ process.HFXconstantX0X2Xsmear
+ process.HFXconstantX0X2
+ process.HFXconstantX0X25Xsmear
+ process.HFXconstantX0X25
+ process.HFXconstantX0X3Xsmear
+ process.HFXconstantX0X3
)
