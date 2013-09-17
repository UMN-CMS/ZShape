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


process.HFXresphiX0X001Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X001Xsmear.HF.resphi = cms.double(0.001)

process.HFXresphiX0X001 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X001.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X001.zsrc = cms.untracked.InputTag("HFXresphiX0X001Xsmear","ZEventParticles")
process.HFXresphiX0X001.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X001Xsmear","ZEventParticles")

process.HFXresphiX0X05Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X05Xsmear.HF.resphi = cms.double(0.05)

process.HFXresphiX0X05 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X05.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X05.zsrc = cms.untracked.InputTag("HFXresphiX0X05Xsmear","ZEventParticles")
process.HFXresphiX0X05.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X05Xsmear","ZEventParticles")

process.HFXresphiX0X10Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X10Xsmear.HF.resphi = cms.double(0.10)

process.HFXresphiX0X10 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X10.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X10.zsrc = cms.untracked.InputTag("HFXresphiX0X10Xsmear","ZEventParticles")
process.HFXresphiX0X10.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X10Xsmear","ZEventParticles")

process.HFXresphiX0X15Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X15Xsmear.HF.resphi = cms.double(0.15)

process.HFXresphiX0X15 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X15.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X15.zsrc = cms.untracked.InputTag("HFXresphiX0X15Xsmear","ZEventParticles")
process.HFXresphiX0X15.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X15Xsmear","ZEventParticles")

process.HFXresphiX0X175Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X175Xsmear.HF.resphi = cms.double(0.175)

process.HFXresphiX0X175 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X175.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X175.zsrc = cms.untracked.InputTag("HFXresphiX0X175Xsmear","ZEventParticles")
process.HFXresphiX0X175.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X175Xsmear","ZEventParticles")

process.HFXresphiX0X2Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X2Xsmear.HF.resphi = cms.double(0.2)

process.HFXresphiX0X2 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X2.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X2.zsrc = cms.untracked.InputTag("HFXresphiX0X2Xsmear","ZEventParticles")
process.HFXresphiX0X2.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X2Xsmear","ZEventParticles")

process.HFXresphiX0X225Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X225Xsmear.HF.resphi = cms.double(0.225)

process.HFXresphiX0X225 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X225.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X225.zsrc = cms.untracked.InputTag("HFXresphiX0X225Xsmear","ZEventParticles")
process.HFXresphiX0X225.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X225Xsmear","ZEventParticles")

process.HFXresphiX0X25Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X25Xsmear.HF.resphi = cms.double(0.25)

process.HFXresphiX0X25 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X25.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X25.zsrc = cms.untracked.InputTag("HFXresphiX0X25Xsmear","ZEventParticles")
process.HFXresphiX0X25.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X25Xsmear","ZEventParticles")

process.HFXresphiX0X275Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXresphiX0X275Xsmear.HF.resphi = cms.double(0.275)

process.HFXresphiX0X275 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXresphiX0X275.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXresphiX0X275.zsrc = cms.untracked.InputTag("HFXresphiX0X275Xsmear","ZEventParticles")
process.HFXresphiX0X275.zElectronsCollection = cms.untracked.InputTag("HFXresphiX0X275Xsmear","ZEventParticles")

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
+ process.HFXresphiX0X05Xsmear
+ process.HFXresphiX0X05
+ process.HFXresphiX0X10Xsmear
+ process.HFXresphiX0X10
+ process.HFXresphiX0X15Xsmear
+ process.HFXresphiX0X15
+ process.HFXresphiX0X175Xsmear
+ process.HFXresphiX0X175
+ process.HFXresphiX0X2Xsmear
+ process.HFXresphiX0X2
+ process.HFXresphiX0X225Xsmear
+ process.HFXresphiX0X225
+ process.HFXresphiX0X25Xsmear
+ process.HFXresphiX0X25
+ process.HFXresphiX0X275Xsmear
+ process.HFXresphiX0X275
+ process.HFXresphiX0X3Xsmear
+ process.HFXresphiX0X3
)
