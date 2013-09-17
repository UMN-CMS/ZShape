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


process.constantX0.04X0X06Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.constantX0.04X0X06Xsmear.constant.0.04p = cms.double(0.06)
process.constantX0.04X0X06Xsmear.constant.0.04m = cms.double(0.06)

process.constantX0.04X0X06 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.constantX0.04X0X06.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.constantX0.04X0X06.zsrc = cms.untracked.InputTag("constantX0.04X0X06Xsmear","ZEventParticles")
process.constantX0.04X0X06.zElectronsCollection = cms.untracked.InputTag("constantX0.04X0X06Xsmear","ZEventParticles")

process.constantX0.04X0X08Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.constantX0.04X0X08Xsmear.constant.0.04p = cms.double(0.08)
process.constantX0.04X0X08Xsmear.constant.0.04m = cms.double(0.08)

process.constantX0.04X0X08 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.constantX0.04X0X08.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.constantX0.04X0X08.zsrc = cms.untracked.InputTag("constantX0.04X0X08Xsmear","ZEventParticles")
process.constantX0.04X0X08.zElectronsCollection = cms.untracked.InputTag("constantX0.04X0X08Xsmear","ZEventParticles")

process.constantX0.04X0X1Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.constantX0.04X0X1Xsmear.constant.0.04p = cms.double(0.1)
process.constantX0.04X0X1Xsmear.constant.0.04m = cms.double(0.1)

process.constantX0.04X0X1 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.constantX0.04X0X1.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.constantX0.04X0X1.zsrc = cms.untracked.InputTag("constantX0.04X0X1Xsmear","ZEventParticles")
process.constantX0.04X0X1.zElectronsCollection = cms.untracked.InputTag("constantX0.04X0X1Xsmear","ZEventParticles")

process.constantX0.04X0X125Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.constantX0.04X0X125Xsmear.constant.0.04p = cms.double(0.125)
process.constantX0.04X0X125Xsmear.constant.0.04m = cms.double(0.125)

process.constantX0.04X0X125 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.constantX0.04X0X125.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.constantX0.04X0X125.zsrc = cms.untracked.InputTag("constantX0.04X0X125Xsmear","ZEventParticles")
process.constantX0.04X0X125.zElectronsCollection = cms.untracked.InputTag("constantX0.04X0X125Xsmear","ZEventParticles")

process.constantX0.04X0X15Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.constantX0.04X0X15Xsmear.constant.0.04p = cms.double(0.15)
process.constantX0.04X0X15Xsmear.constant.0.04m = cms.double(0.15)

process.constantX0.04X0X15 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.constantX0.04X0X15.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.constantX0.04X0X15.zsrc = cms.untracked.InputTag("constantX0.04X0X15Xsmear","ZEventParticles")
process.constantX0.04X0X15.zElectronsCollection = cms.untracked.InputTag("constantX0.04X0X15Xsmear","ZEventParticles")

process.constantX0.04X0X175Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.constantX0.04X0X175Xsmear.constant.0.04p = cms.double(0.175)
process.constantX0.04X0X175Xsmear.constant.0.04m = cms.double(0.175)

process.constantX0.04X0X175 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.constantX0.04X0X175.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.constantX0.04X0X175.zsrc = cms.untracked.InputTag("constantX0.04X0X175Xsmear","ZEventParticles")
process.constantX0.04X0X175.zElectronsCollection = cms.untracked.InputTag("constantX0.04X0X175Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.constantX0.04X0X06Xsmear
+ process.constantX0.04X0X06
+ process.constantX0.04X0X08Xsmear
+ process.constantX0.04X0X08
+ process.constantX0.04X0X1Xsmear
+ process.constantX0.04X0X1
+ process.constantX0.04X0X125Xsmear
+ process.constantX0.04X0X125
+ process.constantX0.04X0X15Xsmear
+ process.constantX0.04X0X15
+ process.constantX0.04X0X175Xsmear
+ process.constantX0.04X0X175
)
