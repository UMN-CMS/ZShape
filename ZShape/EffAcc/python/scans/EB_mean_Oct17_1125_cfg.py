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


process.EBXmeanX0X97Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX0X97Xsmear.EB.mean = cms.double(0.97)

process.EBXmeanX0X97 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX0X97.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX0X97.zsrc = cms.untracked.InputTag("EBXmeanX0X97Xsmear","ZEventParticles")
process.EBXmeanX0X97.zElectronsCollection = cms.untracked.InputTag("EBXmeanX0X97Xsmear","ZEventParticles")

process.EBXmeanX0X98Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX0X98Xsmear.EB.mean = cms.double(0.98)

process.EBXmeanX0X98 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX0X98.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX0X98.zsrc = cms.untracked.InputTag("EBXmeanX0X98Xsmear","ZEventParticles")
process.EBXmeanX0X98.zElectronsCollection = cms.untracked.InputTag("EBXmeanX0X98Xsmear","ZEventParticles")

process.EBXmeanX0X985Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX0X985Xsmear.EB.mean = cms.double(0.985)

process.EBXmeanX0X985 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX0X985.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX0X985.zsrc = cms.untracked.InputTag("EBXmeanX0X985Xsmear","ZEventParticles")
process.EBXmeanX0X985.zElectronsCollection = cms.untracked.InputTag("EBXmeanX0X985Xsmear","ZEventParticles")

process.EBXmeanX0X99Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX0X99Xsmear.EB.mean = cms.double(0.99)

process.EBXmeanX0X99 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX0X99.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX0X99.zsrc = cms.untracked.InputTag("EBXmeanX0X99Xsmear","ZEventParticles")
process.EBXmeanX0X99.zElectronsCollection = cms.untracked.InputTag("EBXmeanX0X99Xsmear","ZEventParticles")

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

process.EBXmeanX1X01Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX1X01Xsmear.EB.mean = cms.double(1.01)

process.EBXmeanX1X01 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX1X01.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX1X01.zsrc = cms.untracked.InputTag("EBXmeanX1X01Xsmear","ZEventParticles")
process.EBXmeanX1X01.zElectronsCollection = cms.untracked.InputTag("EBXmeanX1X01Xsmear","ZEventParticles")

process.EBXmeanX1X015Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX1X015Xsmear.EB.mean = cms.double(1.015)

process.EBXmeanX1X015 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX1X015.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX1X015.zsrc = cms.untracked.InputTag("EBXmeanX1X015Xsmear","ZEventParticles")
process.EBXmeanX1X015.zElectronsCollection = cms.untracked.InputTag("EBXmeanX1X015Xsmear","ZEventParticles")

process.EBXmeanX1X02Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX1X02Xsmear.EB.mean = cms.double(1.02)

process.EBXmeanX1X02 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX1X02.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX1X02.zsrc = cms.untracked.InputTag("EBXmeanX1X02Xsmear","ZEventParticles")
process.EBXmeanX1X02.zElectronsCollection = cms.untracked.InputTag("EBXmeanX1X02Xsmear","ZEventParticles")

process.EBXmeanX1X025Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX1X025Xsmear.EB.mean = cms.double(1.025)

process.EBXmeanX1X025 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX1X025.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX1X025.zsrc = cms.untracked.InputTag("EBXmeanX1X025Xsmear","ZEventParticles")
process.EBXmeanX1X025.zElectronsCollection = cms.untracked.InputTag("EBXmeanX1X025Xsmear","ZEventParticles")

process.EBXmeanX1X03Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX1X03Xsmear.EB.mean = cms.double(1.03)

process.EBXmeanX1X03 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX1X03.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX1X03.zsrc = cms.untracked.InputTag("EBXmeanX1X03Xsmear","ZEventParticles")
process.EBXmeanX1X03.zElectronsCollection = cms.untracked.InputTag("EBXmeanX1X03Xsmear","ZEventParticles")

process.EBXmeanX1X04Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX1X04Xsmear.EB.mean = cms.double(1.04)

process.EBXmeanX1X04 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX1X04.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX1X04.zsrc = cms.untracked.InputTag("EBXmeanX1X04Xsmear","ZEventParticles")
process.EBXmeanX1X04.zElectronsCollection = cms.untracked.InputTag("EBXmeanX1X04Xsmear","ZEventParticles")

process.EBXmeanX1X05Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX1X05Xsmear.EB.mean = cms.double(1.05)

process.EBXmeanX1X05 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX1X05.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX1X05.zsrc = cms.untracked.InputTag("EBXmeanX1X05Xsmear","ZEventParticles")
process.EBXmeanX1X05.zElectronsCollection = cms.untracked.InputTag("EBXmeanX1X05Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.EBXmeanX0X98Xsmear
+ process.EBXmeanX0X98
+ process.EBXmeanX0X985Xsmear
+ process.EBXmeanX0X985
+ process.EBXmeanX0X99Xsmear
+ process.EBXmeanX0X99
+ process.EBXmeanX0X995Xsmear
+ process.EBXmeanX0X995
+ process.EBXmeanX1X0Xsmear
+ process.EBXmeanX1X0
+ process.EBXmeanX1X005Xsmear
+ process.EBXmeanX1X005
+ process.EBXmeanX1X01Xsmear
+ process.EBXmeanX1X01

)
