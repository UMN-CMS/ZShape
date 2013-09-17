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

process.HFXconstantX0X03Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X03Xsmear.HF.constantp = cms.double(0.03)
process.HFXconstantX0X03Xsmear.HF.constantm = cms.double(0.03)

process.HFXconstantX0X03 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X03.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X03.zsrc = cms.untracked.InputTag("HFXconstantX0X03Xsmear","ZEventParticles")
process.HFXconstantX0X03.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X03Xsmear","ZEventParticles")

process.HFXconstantX0X05Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X05Xsmear.HF.constantp = cms.double(0.05)
process.HFXconstantX0X05Xsmear.HF.constantm = cms.double(0.05)

process.HFXconstantX0X05 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X05.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X05.zsrc = cms.untracked.InputTag("HFXconstantX0X05Xsmear","ZEventParticles")
process.HFXconstantX0X05.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X05Xsmear","ZEventParticles")

process.HFXconstantX0X07Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X07Xsmear.HF.constantp = cms.double(0.07)
process.HFXconstantX0X07Xsmear.HF.constantm = cms.double(0.07)

process.HFXconstantX0X07 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X07.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X07.zsrc = cms.untracked.InputTag("HFXconstantX0X07Xsmear","ZEventParticles")
process.HFXconstantX0X07.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X07Xsmear","ZEventParticles")

process.HFXconstantX0X08Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X08Xsmear.HF.constantp = cms.double(0.08)
process.HFXconstantX0X08Xsmear.HF.constantm = cms.double(0.08)

process.HFXconstantX0X08 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X08.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X08.zsrc = cms.untracked.InputTag("HFXconstantX0X08Xsmear","ZEventParticles")
process.HFXconstantX0X08.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X08Xsmear","ZEventParticles")

process.HFXconstantX0X09Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X09Xsmear.HF.constantp = cms.double(0.09)
process.HFXconstantX0X09Xsmear.HF.constantm = cms.double(0.09)

process.HFXconstantX0X09 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X09.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X09.zsrc = cms.untracked.InputTag("HFXconstantX0X09Xsmear","ZEventParticles")
process.HFXconstantX0X09.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X09Xsmear","ZEventParticles")

process.HFXconstantX0X10Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X10Xsmear.HF.constantp = cms.double(0.10)
process.HFXconstantX0X10Xsmear.HF.constantm = cms.double(0.10)

process.HFXconstantX0X10 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X10.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X10.zsrc = cms.untracked.InputTag("HFXconstantX0X10Xsmear","ZEventParticles")
process.HFXconstantX0X10.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X10Xsmear","ZEventParticles")

process.HFXconstantX0X11Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X11Xsmear.HF.constantp = cms.double(0.11)
process.HFXconstantX0X11Xsmear.HF.constantm = cms.double(0.11)

process.HFXconstantX0X11 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X11.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X11.zsrc = cms.untracked.InputTag("HFXconstantX0X11Xsmear","ZEventParticles")
process.HFXconstantX0X11.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X11Xsmear","ZEventParticles")

process.HFXconstantX0X12Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X12Xsmear.HF.constantp = cms.double(0.12)
process.HFXconstantX0X12Xsmear.HF.constantm = cms.double(0.12)

process.HFXconstantX0X12 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X12.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X12.zsrc = cms.untracked.InputTag("HFXconstantX0X12Xsmear","ZEventParticles")
process.HFXconstantX0X12.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X12Xsmear","ZEventParticles")

process.HFXconstantX0X13Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X13Xsmear.HF.constantp = cms.double(0.13)
process.HFXconstantX0X13Xsmear.HF.constantm = cms.double(0.13)

process.HFXconstantX0X13 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X13.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X13.zsrc = cms.untracked.InputTag("HFXconstantX0X13Xsmear","ZEventParticles")
process.HFXconstantX0X13.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X13Xsmear","ZEventParticles")

process.HFXconstantX0X14Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X14Xsmear.HF.constantp = cms.double(0.14)
process.HFXconstantX0X14Xsmear.HF.constantm = cms.double(0.14)

process.HFXconstantX0X14 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X14.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X14.zsrc = cms.untracked.InputTag("HFXconstantX0X14Xsmear","ZEventParticles")
process.HFXconstantX0X14.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X14Xsmear","ZEventParticles")

process.HFXconstantX0X15Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X15Xsmear.HF.constantp = cms.double(0.15)
process.HFXconstantX0X15Xsmear.HF.constantm = cms.double(0.15)

process.HFXconstantX0X15 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X15.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X15.zsrc = cms.untracked.InputTag("HFXconstantX0X15Xsmear","ZEventParticles")
process.HFXconstantX0X15.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X15Xsmear","ZEventParticles")

process.HFXconstantX0X16Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X16Xsmear.HF.constantp = cms.double(0.16)
process.HFXconstantX0X16Xsmear.HF.constantm = cms.double(0.16)

process.HFXconstantX0X16 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X16.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X16.zsrc = cms.untracked.InputTag("HFXconstantX0X16Xsmear","ZEventParticles")
process.HFXconstantX0X16.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X16Xsmear","ZEventParticles")

process.HFXconstantX0X17Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X17Xsmear.HF.constantp = cms.double(0.17)
process.HFXconstantX0X17Xsmear.HF.constantm = cms.double(0.17)

process.HFXconstantX0X17 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X17.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X17.zsrc = cms.untracked.InputTag("HFXconstantX0X17Xsmear","ZEventParticles")
process.HFXconstantX0X17.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X17Xsmear","ZEventParticles")

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

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.HFXconstantX0X002Xsmear
+ process.HFXconstantX0X002
+ process.HFXconstantX0X03Xsmear
+ process.HFXconstantX0X03
+ process.HFXconstantX0X05Xsmear
+ process.HFXconstantX0X05
+ process.HFXconstantX0X07Xsmear
+ process.HFXconstantX0X07
+ process.HFXconstantX0X08Xsmear
+ process.HFXconstantX0X08
+ process.HFXconstantX0X09Xsmear
+ process.HFXconstantX0X09
+ process.HFXconstantX0X10Xsmear
+ process.HFXconstantX0X10
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
+ process.HFXconstantX0X2Xsmear
+ process.HFXconstantX0X2
+ process.HFXconstantX0X25Xsmear
+ process.HFXconstantX0X25
)
