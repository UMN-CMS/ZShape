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


process.HFXconstantX0X005Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X005Xsmear.HF.constantp = cms.double(0.005)
process.HFXconstantX0X005Xsmear.HF.constantm = cms.double(0.005)

process.HFXconstantX0X005 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X005.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X005.zsrc = cms.untracked.InputTag("HFXconstantX0X005Xsmear","ZEventParticles")
process.HFXconstantX0X005.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X005Xsmear","ZEventParticles")

process.HFXconstantX0X02Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X02Xsmear.HF.constantp = cms.double(0.02)
process.HFXconstantX0X02Xsmear.HF.constantm = cms.double(0.02)

process.HFXconstantX0X02 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X02.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X02.zsrc = cms.untracked.InputTag("HFXconstantX0X02Xsmear","ZEventParticles")
process.HFXconstantX0X02.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X02Xsmear","ZEventParticles")

process.HFXconstantX0X04Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X04Xsmear.HF.constantp = cms.double(0.04)
process.HFXconstantX0X04Xsmear.HF.constantm = cms.double(0.04)

process.HFXconstantX0X04 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X04.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X04.zsrc = cms.untracked.InputTag("HFXconstantX0X04Xsmear","ZEventParticles")
process.HFXconstantX0X04.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X04Xsmear","ZEventParticles")

process.HFXconstantX0X06Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X06Xsmear.HF.constantp = cms.double(0.06)
process.HFXconstantX0X06Xsmear.HF.constantm = cms.double(0.06)

process.HFXconstantX0X06 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X06.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X06.zsrc = cms.untracked.InputTag("HFXconstantX0X06Xsmear","ZEventParticles")
process.HFXconstantX0X06.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X06Xsmear","ZEventParticles")

process.HFXconstantX0X08Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X08Xsmear.HF.constantp = cms.double(0.08)
process.HFXconstantX0X08Xsmear.HF.constantm = cms.double(0.08)

process.HFXconstantX0X08 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X08.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X08.zsrc = cms.untracked.InputTag("HFXconstantX0X08Xsmear","ZEventParticles")
process.HFXconstantX0X08.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X08Xsmear","ZEventParticles")

process.HFXconstantX0X1Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X1Xsmear.HF.constantp = cms.double(0.1)
process.HFXconstantX0X1Xsmear.HF.constantm = cms.double(0.1)

process.HFXconstantX0X1 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X1.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X1.zsrc = cms.untracked.InputTag("HFXconstantX0X1Xsmear","ZEventParticles")
process.HFXconstantX0X1.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X1Xsmear","ZEventParticles")

process.HFXconstantX0X12Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X12Xsmear.HF.constantp = cms.double(0.12)
process.HFXconstantX0X12Xsmear.HF.constantm = cms.double(0.12)

process.HFXconstantX0X12 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X12.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X12.zsrc = cms.untracked.InputTag("HFXconstantX0X12Xsmear","ZEventParticles")
process.HFXconstantX0X12.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X12Xsmear","ZEventParticles")

process.HFXconstantX0X14Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X14Xsmear.HF.constantp = cms.double(0.14)
process.HFXconstantX0X14Xsmear.HF.constantm = cms.double(0.14)

process.HFXconstantX0X14 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X14.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X14.zsrc = cms.untracked.InputTag("HFXconstantX0X14Xsmear","ZEventParticles")
process.HFXconstantX0X14.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X14Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.HFXconstantX0X005Xsmear
+ process.HFXconstantX0X005
+ process.HFXconstantX0X02Xsmear
+ process.HFXconstantX0X02
+ process.HFXconstantX0X04Xsmear
+ process.HFXconstantX0X04
+ process.HFXconstantX0X06Xsmear
+ process.HFXconstantX0X06
+ process.HFXconstantX0X08Xsmear
+ process.HFXconstantX0X08
+ process.HFXconstantX0X1Xsmear
+ process.HFXconstantX0X1
+ process.HFXconstantX0X12Xsmear
+ process.HFXconstantX0X12
+ process.HFXconstantX0X14Xsmear
+ process.HFXconstantX0X14
)
