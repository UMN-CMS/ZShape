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


process.constantX0.05X0X06Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.constantX0.05X0X06Xsmear.constant.0.05p = cms.double(0.06)
process.constantX0.05X0X06Xsmear.constant.0.05m = cms.double(0.06)

process.constantX0.05X0X06 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.constantX0.05X0X06.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.constantX0.05X0X06.zsrc = cms.untracked.InputTag("constantX0.05X0X06Xsmear","ZEventParticles")
process.constantX0.05X0X06.zElectronsCollection = cms.untracked.InputTag("constantX0.05X0X06Xsmear","ZEventParticles")

process.constantX0.05X0X07Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.constantX0.05X0X07Xsmear.constant.0.05p = cms.double(0.07)
process.constantX0.05X0X07Xsmear.constant.0.05m = cms.double(0.07)

process.constantX0.05X0X07 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.constantX0.05X0X07.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.constantX0.05X0X07.zsrc = cms.untracked.InputTag("constantX0.05X0X07Xsmear","ZEventParticles")
process.constantX0.05X0X07.zElectronsCollection = cms.untracked.InputTag("constantX0.05X0X07Xsmear","ZEventParticles")

process.constantX0.05X0XXsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.constantX0.05X0XXsmear.constant.0.05p = cms.double(0.)
process.constantX0.05X0XXsmear.constant.0.05m = cms.double(0.)

process.constantX0.05X0X = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.constantX0.05X0X.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.constantX0.05X0X.zsrc = cms.untracked.InputTag("constantX0.05X0XXsmear","ZEventParticles")
process.constantX0.05X0X.zElectronsCollection = cms.untracked.InputTag("constantX0.05X0XXsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.constantX0.05X0X06Xsmear
+ process.constantX0.05X0X06
+ process.constantX0.05X0X07Xsmear
+ process.constantX0.05X0X07
+ process.constantX0.05X0XXsmear
+ process.constantX0.05X0X
)
