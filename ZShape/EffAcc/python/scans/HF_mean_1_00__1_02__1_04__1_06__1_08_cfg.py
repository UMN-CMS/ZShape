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


process.HFXmeanX1X00Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X00Xsmear.HF.meanp = cms.double(1.00)
process.HFXmeanX1X00Xsmear.HF.meanm = cms.double(1.00)

process.HFXmeanX1X00 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X00.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X00.zsrc = cms.untracked.InputTag("HFXmeanX1X00Xsmear","ZEventParticles")
process.HFXmeanX1X00.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X00Xsmear","ZEventParticles")

process.HFXmeanX1X02Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X02Xsmear.HF.meanp = cms.double(1.02)
process.HFXmeanX1X02Xsmear.HF.meanm = cms.double(1.02)

process.HFXmeanX1X02 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X02.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X02.zsrc = cms.untracked.InputTag("HFXmeanX1X02Xsmear","ZEventParticles")
process.HFXmeanX1X02.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X02Xsmear","ZEventParticles")

process.HFXmeanX1X04Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X04Xsmear.HF.meanp = cms.double(1.04)
process.HFXmeanX1X04Xsmear.HF.meanm = cms.double(1.04)

process.HFXmeanX1X04 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X04.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X04.zsrc = cms.untracked.InputTag("HFXmeanX1X04Xsmear","ZEventParticles")
process.HFXmeanX1X04.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X04Xsmear","ZEventParticles")

process.HFXmeanX1X06Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X06Xsmear.HF.meanp = cms.double(1.06)
process.HFXmeanX1X06Xsmear.HF.meanm = cms.double(1.06)

process.HFXmeanX1X06 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X06.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X06.zsrc = cms.untracked.InputTag("HFXmeanX1X06Xsmear","ZEventParticles")
process.HFXmeanX1X06.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X06Xsmear","ZEventParticles")

process.HFXmeanX1X08Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X08Xsmear.HF.meanp = cms.double(1.08)
process.HFXmeanX1X08Xsmear.HF.meanm = cms.double(1.08)

process.HFXmeanX1X08 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X08.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X08.zsrc = cms.untracked.InputTag("HFXmeanX1X08Xsmear","ZEventParticles")
process.HFXmeanX1X08.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X08Xsmear","ZEventParticles")

process.p = cms.Path(process.f2s
+ process.HFXmeanX1X00Xsmear
+ process.HFXmeanX1X00
+ process.HFXmeanX1X02Xsmear
+ process.HFXmeanX1X02
+ process.HFXmeanX1X04Xsmear
+ process.HFXmeanX1X04
+ process.HFXmeanX1X06Xsmear
+ process.HFXmeanX1X06
+ process.HFXmeanX1X08Xsmear
+ process.HFXmeanX1X08
)
