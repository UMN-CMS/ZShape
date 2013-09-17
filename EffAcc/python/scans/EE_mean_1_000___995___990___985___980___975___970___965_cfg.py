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


process.EEXmeanX1X000Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX1X000Xsmear.EE.mean = cms.double(1.000)

process.EEXmeanX1X000 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX1X000.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX1X000.zsrc = cms.untracked.InputTag("EEXmeanX1X000Xsmear","ZEventParticles")
process.EEXmeanX1X000.zElectronsCollection = cms.untracked.InputTag("EEXmeanX1X000Xsmear","ZEventParticles")

process.EEXmeanXX995Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanXX995Xsmear.EE.mean = cms.double(.995)

process.EEXmeanXX995 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanXX995.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanXX995.zsrc = cms.untracked.InputTag("EEXmeanXX995Xsmear","ZEventParticles")
process.EEXmeanXX995.zElectronsCollection = cms.untracked.InputTag("EEXmeanXX995Xsmear","ZEventParticles")

process.EEXmeanXX990Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanXX990Xsmear.EE.mean = cms.double(.990)

process.EEXmeanXX990 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanXX990.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanXX990.zsrc = cms.untracked.InputTag("EEXmeanXX990Xsmear","ZEventParticles")
process.EEXmeanXX990.zElectronsCollection = cms.untracked.InputTag("EEXmeanXX990Xsmear","ZEventParticles")

process.EEXmeanXX985Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanXX985Xsmear.EE.mean = cms.double(.985)

process.EEXmeanXX985 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanXX985.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanXX985.zsrc = cms.untracked.InputTag("EEXmeanXX985Xsmear","ZEventParticles")
process.EEXmeanXX985.zElectronsCollection = cms.untracked.InputTag("EEXmeanXX985Xsmear","ZEventParticles")

process.EEXmeanXX980Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanXX980Xsmear.EE.mean = cms.double(.980)

process.EEXmeanXX980 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanXX980.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanXX980.zsrc = cms.untracked.InputTag("EEXmeanXX980Xsmear","ZEventParticles")
process.EEXmeanXX980.zElectronsCollection = cms.untracked.InputTag("EEXmeanXX980Xsmear","ZEventParticles")

process.EEXmeanXX975Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanXX975Xsmear.EE.mean = cms.double(.975)

process.EEXmeanXX975 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanXX975.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanXX975.zsrc = cms.untracked.InputTag("EEXmeanXX975Xsmear","ZEventParticles")
process.EEXmeanXX975.zElectronsCollection = cms.untracked.InputTag("EEXmeanXX975Xsmear","ZEventParticles")

process.EEXmeanXX970Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanXX970Xsmear.EE.mean = cms.double(.970)

process.EEXmeanXX970 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanXX970.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanXX970.zsrc = cms.untracked.InputTag("EEXmeanXX970Xsmear","ZEventParticles")
process.EEXmeanXX970.zElectronsCollection = cms.untracked.InputTag("EEXmeanXX970Xsmear","ZEventParticles")

process.EEXmeanXX965Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanXX965Xsmear.EE.mean = cms.double(.965)

process.EEXmeanXX965 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanXX965.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanXX965.zsrc = cms.untracked.InputTag("EEXmeanXX965Xsmear","ZEventParticles")
process.EEXmeanXX965.zElectronsCollection = cms.untracked.InputTag("EEXmeanXX965Xsmear","ZEventParticles")

process.p = cms.Path(process.f2s
+ process.EEXmeanX1X000Xsmear
+ process.EEXmeanX1X000
+ process.EEXmeanXX995Xsmear
+ process.EEXmeanXX995
+ process.EEXmeanXX990Xsmear
+ process.EEXmeanXX990
+ process.EEXmeanXX985Xsmear
+ process.EEXmeanXX985
+ process.EEXmeanXX980Xsmear
+ process.EEXmeanXX980
+ process.EEXmeanXX975Xsmear
+ process.EEXmeanXX975
+ process.EEXmeanXX970Xsmear
+ process.EEXmeanXX970
+ process.EEXmeanXX965Xsmear
+ process.EEXmeanXX965
)
