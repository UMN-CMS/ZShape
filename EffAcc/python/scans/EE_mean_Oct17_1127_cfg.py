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


process.EEXmeanX0X97Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X97Xsmear.EE.mean = cms.double(0.97)

process.EEXmeanX0X97 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X97.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X97.zsrc = cms.untracked.InputTag("EEXmeanX0X97Xsmear","ZEventParticles")
process.EEXmeanX0X97.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X97Xsmear","ZEventParticles")

process.EEXmeanX0X98Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X98Xsmear.EE.mean = cms.double(0.98)

process.EEXmeanX0X98 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X98.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X98.zsrc = cms.untracked.InputTag("EEXmeanX0X98Xsmear","ZEventParticles")
process.EEXmeanX0X98.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X98Xsmear","ZEventParticles")

process.EEXmeanX0X985Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X985Xsmear.EE.mean = cms.double(0.985)

process.EEXmeanX0X985 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X985.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X985.zsrc = cms.untracked.InputTag("EEXmeanX0X985Xsmear","ZEventParticles")
process.EEXmeanX0X985.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X985Xsmear","ZEventParticles")

process.EEXmeanX0X99Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X99Xsmear.EE.mean = cms.double(0.99)

process.EEXmeanX0X99 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X99.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X99.zsrc = cms.untracked.InputTag("EEXmeanX0X99Xsmear","ZEventParticles")
process.EEXmeanX0X99.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X99Xsmear","ZEventParticles")

process.EEXmeanX0X995Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X995Xsmear.EE.mean = cms.double(0.995)

process.EEXmeanX0X995 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X995.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X995.zsrc = cms.untracked.InputTag("EEXmeanX0X995Xsmear","ZEventParticles")
process.EEXmeanX0X995.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X995Xsmear","ZEventParticles")

process.EEXmeanX1X0Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX1X0Xsmear.EE.mean = cms.double(1.0)

process.EEXmeanX1X0 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX1X0.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX1X0.zsrc = cms.untracked.InputTag("EEXmeanX1X0Xsmear","ZEventParticles")
process.EEXmeanX1X0.zElectronsCollection = cms.untracked.InputTag("EEXmeanX1X0Xsmear","ZEventParticles")

process.EEXmeanX1X005Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX1X005Xsmear.EE.mean = cms.double(1.005)

process.EEXmeanX1X005 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX1X005.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX1X005.zsrc = cms.untracked.InputTag("EEXmeanX1X005Xsmear","ZEventParticles")
process.EEXmeanX1X005.zElectronsCollection = cms.untracked.InputTag("EEXmeanX1X005Xsmear","ZEventParticles")

process.EEXmeanX1X01Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX1X01Xsmear.EE.mean = cms.double(1.01)

process.EEXmeanX1X01 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX1X01.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX1X01.zsrc = cms.untracked.InputTag("EEXmeanX1X01Xsmear","ZEventParticles")
process.EEXmeanX1X01.zElectronsCollection = cms.untracked.InputTag("EEXmeanX1X01Xsmear","ZEventParticles")

process.EEXmeanX1X015Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX1X015Xsmear.EE.mean = cms.double(1.015)

process.EEXmeanX1X015 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX1X015.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX1X015.zsrc = cms.untracked.InputTag("EEXmeanX1X015Xsmear","ZEventParticles")
process.EEXmeanX1X015.zElectronsCollection = cms.untracked.InputTag("EEXmeanX1X015Xsmear","ZEventParticles")

process.EEXmeanX1X02Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX1X02Xsmear.EE.mean = cms.double(1.02)

process.EEXmeanX1X02 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX1X02.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX1X02.zsrc = cms.untracked.InputTag("EEXmeanX1X02Xsmear","ZEventParticles")
process.EEXmeanX1X02.zElectronsCollection = cms.untracked.InputTag("EEXmeanX1X02Xsmear","ZEventParticles")

process.EEXmeanX1X025Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX1X025Xsmear.EE.mean = cms.double(1.025)

process.EEXmeanX1X025 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX1X025.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX1X025.zsrc = cms.untracked.InputTag("EEXmeanX1X025Xsmear","ZEventParticles")
process.EEXmeanX1X025.zElectronsCollection = cms.untracked.InputTag("EEXmeanX1X025Xsmear","ZEventParticles")

process.EEXmeanX1X03Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX1X03Xsmear.EE.mean = cms.double(1.03)

process.EEXmeanX1X03 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX1X03.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX1X03.zsrc = cms.untracked.InputTag("EEXmeanX1X03Xsmear","ZEventParticles")
process.EEXmeanX1X03.zElectronsCollection = cms.untracked.InputTag("EEXmeanX1X03Xsmear","ZEventParticles")

process.EEXmeanX1X04Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX1X04Xsmear.EE.mean = cms.double(1.04)

process.EEXmeanX1X04 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX1X04.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX1X04.zsrc = cms.untracked.InputTag("EEXmeanX1X04Xsmear","ZEventParticles")
process.EEXmeanX1X04.zElectronsCollection = cms.untracked.InputTag("EEXmeanX1X04Xsmear","ZEventParticles")

process.EEXmeanX1X05Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX1X05Xsmear.EE.mean = cms.double(1.05)

process.EEXmeanX1X05 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX1X05.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX1X05.zsrc = cms.untracked.InputTag("EEXmeanX1X05Xsmear","ZEventParticles")
process.EEXmeanX1X05.zElectronsCollection = cms.untracked.InputTag("EEXmeanX1X05Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.EEXmeanX0X97Xsmear
+ process.EEXmeanX0X97
+ process.EEXmeanX0X98Xsmear
+ process.EEXmeanX0X98
+ process.EEXmeanX0X985Xsmear
+ process.EEXmeanX0X985
+ process.EEXmeanX0X99Xsmear
+ process.EEXmeanX0X99
+ process.EEXmeanX0X995Xsmear
+ process.EEXmeanX0X995
+ process.EEXmeanX1X0Xsmear
+ process.EEXmeanX1X0
)
