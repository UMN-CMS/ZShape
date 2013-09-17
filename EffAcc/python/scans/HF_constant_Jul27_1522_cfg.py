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


process.HFXconstantX0X07Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X07Xsmear.HF.constantp = cms.double(0.07)
process.HFXconstantX0X07Xsmear.HF.constantm = cms.double(0.07)

process.HFXconstantX0X07 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X07.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X07.zsrc = cms.untracked.InputTag("HFXconstantX0X07Xsmear","ZEventParticles")
process.HFXconstantX0X07.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X07Xsmear","ZEventParticles")

process.HFXconstantX0X075Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X075Xsmear.HF.constantp = cms.double(0.075)
process.HFXconstantX0X075Xsmear.HF.constantm = cms.double(0.075)

process.HFXconstantX0X075 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X075.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X075.zsrc = cms.untracked.InputTag("HFXconstantX0X075Xsmear","ZEventParticles")
process.HFXconstantX0X075.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X075Xsmear","ZEventParticles")

process.HFXconstantX0X08Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X08Xsmear.HF.constantp = cms.double(0.08)
process.HFXconstantX0X08Xsmear.HF.constantm = cms.double(0.08)

process.HFXconstantX0X08 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X08.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X08.zsrc = cms.untracked.InputTag("HFXconstantX0X08Xsmear","ZEventParticles")
process.HFXconstantX0X08.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X08Xsmear","ZEventParticles")

process.HFXconstantX0X085Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X085Xsmear.HF.constantp = cms.double(0.085)
process.HFXconstantX0X085Xsmear.HF.constantm = cms.double(0.085)

process.HFXconstantX0X085 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X085.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X085.zsrc = cms.untracked.InputTag("HFXconstantX0X085Xsmear","ZEventParticles")
process.HFXconstantX0X085.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X085Xsmear","ZEventParticles")

process.HFXconstantX0X09Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X09Xsmear.HF.constantp = cms.double(0.09)
process.HFXconstantX0X09Xsmear.HF.constantm = cms.double(0.09)

process.HFXconstantX0X09 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X09.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X09.zsrc = cms.untracked.InputTag("HFXconstantX0X09Xsmear","ZEventParticles")
process.HFXconstantX0X09.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X09Xsmear","ZEventParticles")

process.HFXconstantX0X095Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X095Xsmear.HF.constantp = cms.double(0.095)
process.HFXconstantX0X095Xsmear.HF.constantm = cms.double(0.095)

process.HFXconstantX0X095 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X095.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X095.zsrc = cms.untracked.InputTag("HFXconstantX0X095Xsmear","ZEventParticles")
process.HFXconstantX0X095.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X095Xsmear","ZEventParticles")

process.HFXconstantX0X1Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X1Xsmear.HF.constantp = cms.double(0.1)
process.HFXconstantX0X1Xsmear.HF.constantm = cms.double(0.1)

process.HFXconstantX0X1 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X1.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X1.zsrc = cms.untracked.InputTag("HFXconstantX0X1Xsmear","ZEventParticles")
process.HFXconstantX0X1.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X1Xsmear","ZEventParticles")

process.HFXconstantX0X105Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X105Xsmear.HF.constantp = cms.double(0.105)
process.HFXconstantX0X105Xsmear.HF.constantm = cms.double(0.105)

process.HFXconstantX0X105 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X105.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X105.zsrc = cms.untracked.InputTag("HFXconstantX0X105Xsmear","ZEventParticles")
process.HFXconstantX0X105.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X105Xsmear","ZEventParticles")

process.HFXconstantX0X11Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X11Xsmear.HF.constantp = cms.double(0.11)
process.HFXconstantX0X11Xsmear.HF.constantm = cms.double(0.11)

process.HFXconstantX0X11 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X11.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X11.zsrc = cms.untracked.InputTag("HFXconstantX0X11Xsmear","ZEventParticles")
process.HFXconstantX0X11.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X11Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.HFXconstantX0X07Xsmear
+ process.HFXconstantX0X07
+ process.HFXconstantX0X075Xsmear
+ process.HFXconstantX0X075
+ process.HFXconstantX0X08Xsmear
+ process.HFXconstantX0X08
+ process.HFXconstantX0X085Xsmear
+ process.HFXconstantX0X085
+ process.HFXconstantX0X09Xsmear
+ process.HFXconstantX0X09
+ process.HFXconstantX0X095Xsmear
+ process.HFXconstantX0X095
+ process.HFXconstantX0X1Xsmear
+ process.HFXconstantX0X1
+ process.HFXconstantX0X105Xsmear
+ process.HFXconstantX0X105
+ process.HFXconstantX0X11Xsmear
+ process.HFXconstantX0X11
)
