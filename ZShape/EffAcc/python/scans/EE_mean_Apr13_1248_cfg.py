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


process.EEXmeanX0X975Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X975Xsmear.EE.mean = cms.double(0.975)

process.EEXmeanX0X975 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X975.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X975.zsrc = cms.untracked.InputTag("EEXmeanX0X975Xsmear","ZEventParticles")
process.EEXmeanX0X975.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X975Xsmear","ZEventParticles")

process.EEXmeanX0X980Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X980Xsmear.EE.mean = cms.double(0.980)

process.EEXmeanX0X980 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X980.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X980.zsrc = cms.untracked.InputTag("EEXmeanX0X980Xsmear","ZEventParticles")
process.EEXmeanX0X980.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X980Xsmear","ZEventParticles")

process.EEXmeanX0X985Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X985Xsmear.EE.mean = cms.double(0.985)

process.EEXmeanX0X985 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X985.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X985.zsrc = cms.untracked.InputTag("EEXmeanX0X985Xsmear","ZEventParticles")
process.EEXmeanX0X985.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X985Xsmear","ZEventParticles")

process.EEXmeanX0X990Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EEXmeanX0X990Xsmear.EE.mean = cms.double(0.990)

process.EEXmeanX0X990 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EEXmeanX0X990.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EEXmeanX0X990.zsrc = cms.untracked.InputTag("EEXmeanX0X990Xsmear","ZEventParticles")
process.EEXmeanX0X990.zElectronsCollection = cms.untracked.InputTag("EEXmeanX0X990Xsmear","ZEventParticles")

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

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.EEXmeanX0X975Xsmear
+ process.EEXmeanX0X975
+ process.EEXmeanX0X980Xsmear
+ process.EEXmeanX0X980
+ process.EEXmeanX0X985Xsmear
+ process.EEXmeanX0X985
+ process.EEXmeanX0X990Xsmear
+ process.EEXmeanX0X990
+ process.EEXmeanX0X995Xsmear
+ process.EEXmeanX0X995
+ process.EEXmeanX1X0Xsmear
+ process.EEXmeanX1X0
)
