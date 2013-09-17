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


process.EBXmeanX0X980Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX0X980Xsmear.EB.mean = cms.double(0.980)

process.EBXmeanX0X980 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX0X980.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX0X980.zsrc = cms.untracked.InputTag("EBXmeanX0X980Xsmear","ZEventParticles")
process.EBXmeanX0X980.zElectronsCollection = cms.untracked.InputTag("EBXmeanX0X980Xsmear","ZEventParticles")

process.EBXmeanX0X985Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX0X985Xsmear.EB.mean = cms.double(0.985)

process.EBXmeanX0X985 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX0X985.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX0X985.zsrc = cms.untracked.InputTag("EBXmeanX0X985Xsmear","ZEventParticles")
process.EBXmeanX0X985.zElectronsCollection = cms.untracked.InputTag("EBXmeanX0X985Xsmear","ZEventParticles")

process.EBXmeanX0X991Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX0X991Xsmear.EB.mean = cms.double(0.991)

process.EBXmeanX0X991 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX0X991.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX0X991.zsrc = cms.untracked.InputTag("EBXmeanX0X991Xsmear","ZEventParticles")
process.EBXmeanX0X991.zElectronsCollection = cms.untracked.InputTag("EBXmeanX0X991Xsmear","ZEventParticles")

process.EBXmeanX0X993Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX0X993Xsmear.EB.mean = cms.double(0.993)

process.EBXmeanX0X993 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX0X993.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX0X993.zsrc = cms.untracked.InputTag("EBXmeanX0X993Xsmear","ZEventParticles")
process.EBXmeanX0X993.zElectronsCollection = cms.untracked.InputTag("EBXmeanX0X993Xsmear","ZEventParticles")

process.EBXmeanX0X995Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX0X995Xsmear.EB.mean = cms.double(0.995)

process.EBXmeanX0X995 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX0X995.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX0X995.zsrc = cms.untracked.InputTag("EBXmeanX0X995Xsmear","ZEventParticles")
process.EBXmeanX0X995.zElectronsCollection = cms.untracked.InputTag("EBXmeanX0X995Xsmear","ZEventParticles")

process.EBXmeanX1X0Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX1X0Xsmear.EB.mean = cms.double(1.0)

process.EBXmeanX1X0 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX1X0.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX1X0.zsrc = cms.untracked.InputTag("EBXmeanX1X0Xsmear","ZEventParticles")
process.EBXmeanX1X0.zElectronsCollection = cms.untracked.InputTag("EBXmeanX1X0Xsmear","ZEventParticles")

process.EBXmeanX1X005Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX1X005Xsmear.EB.mean = cms.double(1.005)

process.EBXmeanX1X005 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX1X005.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX1X005.zsrc = cms.untracked.InputTag("EBXmeanX1X005Xsmear","ZEventParticles")
process.EBXmeanX1X005.zElectronsCollection = cms.untracked.InputTag("EBXmeanX1X005Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.EBXmeanX0X980Xsmear
+ process.EBXmeanX0X980
+ process.EBXmeanX0X985Xsmear
+ process.EBXmeanX0X985
+ process.EBXmeanX0X991Xsmear
+ process.EBXmeanX0X991
+ process.EBXmeanX0X993Xsmear
+ process.EBXmeanX0X993
+ process.EBXmeanX0X995Xsmear
+ process.EBXmeanX0X995
+ process.EBXmeanX1X0Xsmear
+ process.EBXmeanX1X0
+ process.EBXmeanX1X005Xsmear
+ process.EBXmeanX1X005
)
