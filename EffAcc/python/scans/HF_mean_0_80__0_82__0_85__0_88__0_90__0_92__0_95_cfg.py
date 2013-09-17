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


process.HFXmeanX0X80Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X80Xsmear.HF.meanp = cms.double(0.80)
process.HFXmeanX0X80Xsmear.HF.meanm = cms.double(0.80)

process.HFXmeanX0X80 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X80.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X80.zsrc = cms.untracked.InputTag("HFXmeanX0X80Xsmear","ZEventParticles")
process.HFXmeanX0X80.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X80Xsmear","ZEventParticles")

process.HFXmeanX0X82Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X82Xsmear.HF.meanp = cms.double(0.82)
process.HFXmeanX0X82Xsmear.HF.meanm = cms.double(0.82)

process.HFXmeanX0X82 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X82.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X82.zsrc = cms.untracked.InputTag("HFXmeanX0X82Xsmear","ZEventParticles")
process.HFXmeanX0X82.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X82Xsmear","ZEventParticles")

process.HFXmeanX0X85Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X85Xsmear.HF.meanp = cms.double(0.85)
process.HFXmeanX0X85Xsmear.HF.meanm = cms.double(0.85)

process.HFXmeanX0X85 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X85.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X85.zsrc = cms.untracked.InputTag("HFXmeanX0X85Xsmear","ZEventParticles")
process.HFXmeanX0X85.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X85Xsmear","ZEventParticles")

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

process.HFXmeanX0X95Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X95Xsmear.HF.meanp = cms.double(0.95)
process.HFXmeanX0X95Xsmear.HF.meanm = cms.double(0.95)

process.HFXmeanX0X95 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X95.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X95.zsrc = cms.untracked.InputTag("HFXmeanX0X95Xsmear","ZEventParticles")
process.HFXmeanX0X95.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X95Xsmear","ZEventParticles")

process.p = cms.Path(process.f2s
+ process.HFXmeanX0X80Xsmear
+ process.HFXmeanX0X80
+ process.HFXmeanX0X82Xsmear
+ process.HFXmeanX0X82
+ process.HFXmeanX0X85Xsmear
+ process.HFXmeanX0X85
+ process.HFXmeanX0X88Xsmear
+ process.HFXmeanX0X88
+ process.HFXmeanX0X90Xsmear
+ process.HFXmeanX0X90
+ process.HFXmeanX0X92Xsmear
+ process.HFXmeanX0X92
+ process.HFXmeanX0X95Xsmear
+ process.HFXmeanX0X95
)
