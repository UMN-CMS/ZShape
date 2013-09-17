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


process.EBXcX0X001Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXcX0X001Xsmear.EB.c = cms.double(0.001)

process.EBXcX0X001 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXcX0X001.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXcX0X001.zsrc = cms.untracked.InputTag("EBXcX0X001Xsmear","ZEventParticles")
process.EBXcX0X001.zElectronsCollection = cms.untracked.InputTag("EBXcX0X001Xsmear","ZEventParticles")

process.EBXcX0X003Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXcX0X003Xsmear.EB.c = cms.double(0.003)

process.EBXcX0X003 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXcX0X003.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXcX0X003.zsrc = cms.untracked.InputTag("EBXcX0X003Xsmear","ZEventParticles")
process.EBXcX0X003.zElectronsCollection = cms.untracked.InputTag("EBXcX0X003Xsmear","ZEventParticles")

process.EBXcX0X005Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXcX0X005Xsmear.EB.c = cms.double(0.005)

process.EBXcX0X005 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXcX0X005.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXcX0X005.zsrc = cms.untracked.InputTag("EBXcX0X005Xsmear","ZEventParticles")
process.EBXcX0X005.zElectronsCollection = cms.untracked.InputTag("EBXcX0X005Xsmear","ZEventParticles")

process.EBXcX0X0075Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXcX0X0075Xsmear.EB.c = cms.double(0.0075)

process.EBXcX0X0075 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXcX0X0075.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXcX0X0075.zsrc = cms.untracked.InputTag("EBXcX0X0075Xsmear","ZEventParticles")
process.EBXcX0X0075.zElectronsCollection = cms.untracked.InputTag("EBXcX0X0075Xsmear","ZEventParticles")

process.EBXcX0X009Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXcX0X009Xsmear.EB.c = cms.double(0.009)

process.EBXcX0X009 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXcX0X009.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXcX0X009.zsrc = cms.untracked.InputTag("EBXcX0X009Xsmear","ZEventParticles")
process.EBXcX0X009.zElectronsCollection = cms.untracked.InputTag("EBXcX0X009Xsmear","ZEventParticles")

process.EBXcX0X01Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXcX0X01Xsmear.EB.c = cms.double(0.01)

process.EBXcX0X01 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXcX0X01.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXcX0X01.zsrc = cms.untracked.InputTag("EBXcX0X01Xsmear","ZEventParticles")
process.EBXcX0X01.zElectronsCollection = cms.untracked.InputTag("EBXcX0X01Xsmear","ZEventParticles")

process.EBXcX0X015Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXcX0X015Xsmear.EB.c = cms.double(0.015)

process.EBXcX0X015 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXcX0X015.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXcX0X015.zsrc = cms.untracked.InputTag("EBXcX0X015Xsmear","ZEventParticles")
process.EBXcX0X015.zElectronsCollection = cms.untracked.InputTag("EBXcX0X015Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.EBXcX0X001Xsmear
+ process.EBXcX0X001
+ process.EBXcX0X003Xsmear
+ process.EBXcX0X003
+ process.EBXcX0X005Xsmear
+ process.EBXcX0X005
+ process.EBXcX0X0075Xsmear
+ process.EBXcX0X0075
+ process.EBXcX0X009Xsmear
+ process.EBXcX0X009
+ process.EBXcX0X01Xsmear
+ process.EBXcX0X01
+ process.EBXcX0X015Xsmear
+ process.EBXcX0X015
)
