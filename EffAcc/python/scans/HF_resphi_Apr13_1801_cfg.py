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
    input = cms.untracked.int32(30000)
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


process.HFXresphiX0X001Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X001Xsmear.HF.resphi = cms.double(0.001)

process.HFXresphiX0X001 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X001.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X001.zsrc = cms.untracked.InputTag("HFXresphiX0X001Xsmear","ZEventParticles")
process.HFXresphiX0X001.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X001Xsmear","ZEventParticles")

process.HFXresphiX0X002Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X002Xsmear.HF.resphi = cms.double(0.002)

process.HFXresphiX0X002 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X002.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X002.zsrc = cms.untracked.InputTag("HFXresphiX0X002Xsmear","ZEventParticles")
process.HFXresphiX0X002.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X002Xsmear","ZEventParticles")

process.HFXresphiX0X003Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X003Xsmear.HF.resphi = cms.double(0.003)

process.HFXresphiX0X003 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X003.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X003.zsrc = cms.untracked.InputTag("HFXresphiX0X003Xsmear","ZEventParticles")
process.HFXresphiX0X003.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X003Xsmear","ZEventParticles")

process.HFXresphiX0X01Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X01Xsmear.HF.resphi = cms.double(0.01)

process.HFXresphiX0X01 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X01.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X01.zsrc = cms.untracked.InputTag("HFXresphiX0X01Xsmear","ZEventParticles")
process.HFXresphiX0X01.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X01Xsmear","ZEventParticles")

process.HFXresphiX0X02Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X02Xsmear.HF.resphi = cms.double(0.02)

process.HFXresphiX0X02 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X02.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X02.zsrc = cms.untracked.InputTag("HFXresphiX0X02Xsmear","ZEventParticles")
process.HFXresphiX0X02.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X02Xsmear","ZEventParticles")

process.HFXresphiX0X03Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X03Xsmear.HF.resphi = cms.double(0.03)

process.HFXresphiX0X03 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X03.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X03.zsrc = cms.untracked.InputTag("HFXresphiX0X03Xsmear","ZEventParticles")
process.HFXresphiX0X03.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X03Xsmear","ZEventParticles")

process.HFXresphiX0X05Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X05Xsmear.HF.resphi = cms.double(0.05)

process.HFXresphiX0X05 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X05.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X05.zsrc = cms.untracked.InputTag("HFXresphiX0X05Xsmear","ZEventParticles")
process.HFXresphiX0X05.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X05Xsmear","ZEventParticles")

process.HFXresphiX0X1Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X1Xsmear.HF.resphi = cms.double(0.1)

process.HFXresphiX0X1 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X1.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X1.zsrc = cms.untracked.InputTag("HFXresphiX0X1Xsmear","ZEventParticles")
process.HFXresphiX0X1.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X1Xsmear","ZEventParticles")

process.HFXresphiX0X15Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X15Xsmear.HF.resphi = cms.double(0.15)

process.HFXresphiX0X15 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X15.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X15.zsrc = cms.untracked.InputTag("HFXresphiX0X15Xsmear","ZEventParticles")
process.HFXresphiX0X15.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X15Xsmear","ZEventParticles")

process.HFXresphiX0X25Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X25Xsmear.HF.resphi = cms.double(0.25)

process.HFXresphiX0X25 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X25.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X25.zsrc = cms.untracked.InputTag("HFXresphiX0X25Xsmear","ZEventParticles")
process.HFXresphiX0X25.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X25Xsmear","ZEventParticles")

process.HFXresphiX0X3Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X3Xsmear.HF.resphi = cms.double(0.3)

process.HFXresphiX0X3 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X3.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X3.zsrc = cms.untracked.InputTag("HFXresphiX0X3Xsmear","ZEventParticles")
process.HFXresphiX0X3.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X3Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.HFXresphiX0X001Xsmear
+ process.HFXresphiX0X001
+ process.HFXresphiX0X002Xsmear
+ process.HFXresphiX0X002
+ process.HFXresphiX0X003Xsmear
+ process.HFXresphiX0X003
+ process.HFXresphiX0X01Xsmear
+ process.HFXresphiX0X01
+ process.HFXresphiX0X02Xsmear
+ process.HFXresphiX0X02
+ process.HFXresphiX0X03Xsmear
+ process.HFXresphiX0X03
+ process.HFXresphiX0X05Xsmear
+ process.HFXresphiX0X05
+ process.HFXresphiX0X1Xsmear
+ process.HFXresphiX0X1
+ process.HFXresphiX0X15Xsmear
+ process.HFXresphiX0X15
+ process.HFXresphiX0X25Xsmear
+ process.HFXresphiX0X25
+ process.HFXresphiX0X3Xsmear
+ process.HFXresphiX0X3
)
