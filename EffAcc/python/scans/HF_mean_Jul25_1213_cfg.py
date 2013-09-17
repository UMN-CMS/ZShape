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


process.HFXmeanX0X075Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X075Xsmear.HF.mean = cms.double(0.075)

process.HFXmeanX0X075 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X075.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X075.zsrc = cms.untracked.InputTag("HFXmeanX0X075Xsmear","ZEventParticles")
process.HFXmeanX0X075.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X075Xsmear","ZEventParticles")

process.HFXmeanX0X08Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X08Xsmear.HF.mean = cms.double(0.08)

process.HFXmeanX0X08 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X08.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X08.zsrc = cms.untracked.InputTag("HFXmeanX0X08Xsmear","ZEventParticles")
process.HFXmeanX0X08.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X08Xsmear","ZEventParticles")

process.HFXmeanX0X085Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X085Xsmear.HF.mean = cms.double(0.085)

process.HFXmeanX0X085 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X085.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X085.zsrc = cms.untracked.InputTag("HFXmeanX0X085Xsmear","ZEventParticles")
process.HFXmeanX0X085.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X085Xsmear","ZEventParticles")

process.HFXmeanX0X09Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X09Xsmear.HF.mean = cms.double(0.09)

process.HFXmeanX0X09 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X09.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X09.zsrc = cms.untracked.InputTag("HFXmeanX0X09Xsmear","ZEventParticles")
process.HFXmeanX0X09.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X09Xsmear","ZEventParticles")

process.HFXmeanX0X095Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X095Xsmear.HF.mean = cms.double(0.095)

process.HFXmeanX0X095 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X095.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X095.zsrc = cms.untracked.InputTag("HFXmeanX0X095Xsmear","ZEventParticles")
process.HFXmeanX0X095.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X095Xsmear","ZEventParticles")

process.HFXmeanX0X1Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X1Xsmear.HF.mean = cms.double(0.1)

process.HFXmeanX0X1 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X1.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X1.zsrc = cms.untracked.InputTag("HFXmeanX0X1Xsmear","ZEventParticles")
process.HFXmeanX0X1.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X1Xsmear","ZEventParticles")

process.HFXmeanX0X11Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X11Xsmear.HF.mean = cms.double(0.11)

process.HFXmeanX0X11 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X11.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X11.zsrc = cms.untracked.InputTag("HFXmeanX0X11Xsmear","ZEventParticles")
process.HFXmeanX0X11.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X11Xsmear","ZEventParticles")

process.HFXmeanX0X12Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X12Xsmear.HF.mean = cms.double(0.12)

process.HFXmeanX0X12 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X12.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X12.zsrc = cms.untracked.InputTag("HFXmeanX0X12Xsmear","ZEventParticles")
process.HFXmeanX0X12.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X12Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.HFXmeanX0X075Xsmear
+ process.HFXmeanX0X075
+ process.HFXmeanX0X08Xsmear
+ process.HFXmeanX0X08
+ process.HFXmeanX0X085Xsmear
+ process.HFXmeanX0X085
+ process.HFXmeanX0X09Xsmear
+ process.HFXmeanX0X09
+ process.HFXmeanX0X095Xsmear
+ process.HFXmeanX0X095
+ process.HFXmeanX0X1Xsmear
+ process.HFXmeanX0X1
+ process.HFXmeanX0X11Xsmear
+ process.HFXmeanX0X11
+ process.HFXmeanX0X12Xsmear
+ process.HFXmeanX0X12
)
