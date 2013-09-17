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


process.HFXmeanX0X88Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X88Xsmear.HF.meanp = cms.double(0.88)
process.HFXmeanX0X88Xsmear.HF.meanm = cms.double(0.88)

process.HFXmeanX0X88 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X88.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X88.zsrc = cms.untracked.InputTag("HFXmeanX0X88Xsmear","ZEventParticles")
process.HFXmeanX0X88.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X88Xsmear","ZEventParticles")

process.HFXmeanX0X90Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X90Xsmear.HF.meanp = cms.double(0.90)
process.HFXmeanX0X90Xsmear.HF.meanm = cms.double(0.90)

process.HFXmeanX0X90 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X90.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X90.zsrc = cms.untracked.InputTag("HFXmeanX0X90Xsmear","ZEventParticles")
process.HFXmeanX0X90.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X90Xsmear","ZEventParticles")

process.HFXmeanX0X92Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X92Xsmear.HF.meanp = cms.double(0.92)
process.HFXmeanX0X92Xsmear.HF.meanm = cms.double(0.92)

process.HFXmeanX0X92 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X92.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X92.zsrc = cms.untracked.InputTag("HFXmeanX0X92Xsmear","ZEventParticles")
process.HFXmeanX0X92.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X92Xsmear","ZEventParticles")

process.HFXmeanX0X94Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X94Xsmear.HF.meanp = cms.double(0.94)
process.HFXmeanX0X94Xsmear.HF.meanm = cms.double(0.94)

process.HFXmeanX0X94 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X94.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X94.zsrc = cms.untracked.InputTag("HFXmeanX0X94Xsmear","ZEventParticles")
process.HFXmeanX0X94.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X94Xsmear","ZEventParticles")

process.HFXmeanX0X96Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X96Xsmear.HF.meanp = cms.double(0.96)
process.HFXmeanX0X96Xsmear.HF.meanm = cms.double(0.96)

process.HFXmeanX0X96 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X96.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X96.zsrc = cms.untracked.InputTag("HFXmeanX0X96Xsmear","ZEventParticles")
process.HFXmeanX0X96.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X96Xsmear","ZEventParticles")

process.HFXmeanX0X98Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X98Xsmear.HF.meanp = cms.double(0.98)
process.HFXmeanX0X98Xsmear.HF.meanm = cms.double(0.98)

process.HFXmeanX0X98 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X98.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X98.zsrc = cms.untracked.InputTag("HFXmeanX0X98Xsmear","ZEventParticles")
process.HFXmeanX0X98.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X98Xsmear","ZEventParticles")

process.HFXmeanX1X0Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X0Xsmear.HF.meanp = cms.double(1.0)
process.HFXmeanX1X0Xsmear.HF.meanm = cms.double(1.0)

process.HFXmeanX1X0 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X0.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X0.zsrc = cms.untracked.InputTag("HFXmeanX1X0Xsmear","ZEventParticles")
process.HFXmeanX1X0.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X0Xsmear","ZEventParticles")

process.p = cms.Path(process.f2s
+ process.HFXmeanX0X88Xsmear
+ process.HFXmeanX0X88
+ process.HFXmeanX0X90Xsmear
+ process.HFXmeanX0X90
+ process.HFXmeanX0X92Xsmear
+ process.HFXmeanX0X92
+ process.HFXmeanX0X94Xsmear
+ process.HFXmeanX0X94
+ process.HFXmeanX0X96Xsmear
+ process.HFXmeanX0X96
+ process.HFXmeanX0X98Xsmear
+ process.HFXmeanX0X98
+ process.HFXmeanX1X0Xsmear
+ process.HFXmeanX1X0
)
