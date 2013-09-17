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


process.EBXcX0X002Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXcX0X002Xsmear.EB.c = cms.double(0.002)

process.EBXcX0X002 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXcX0X002.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXcX0X002.zsrc = cms.untracked.InputTag("EBXcX0X002Xsmear","ZEventParticles")
process.EBXcX0X002.zElectronsCollection = cms.untracked.InputTag("EBXcX0X002Xsmear","ZEventParticles")

process.EBXcX0X004Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXcX0X004Xsmear.EB.c = cms.double(0.004)

process.EBXcX0X004 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXcX0X004.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXcX0X004.zsrc = cms.untracked.InputTag("EBXcX0X004Xsmear","ZEventParticles")
process.EBXcX0X004.zElectronsCollection = cms.untracked.InputTag("EBXcX0X004Xsmear","ZEventParticles")

process.EBXcX0X006Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXcX0X006Xsmear.EB.c = cms.double(0.006)

process.EBXcX0X006 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXcX0X006.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXcX0X006.zsrc = cms.untracked.InputTag("EBXcX0X006Xsmear","ZEventParticles")
process.EBXcX0X006.zElectronsCollection = cms.untracked.InputTag("EBXcX0X006Xsmear","ZEventParticles")

process.EBXcX0X008Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXcX0X008Xsmear.EB.c = cms.double(0.008)

process.EBXcX0X008 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXcX0X008.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXcX0X008.zsrc = cms.untracked.InputTag("EBXcX0X008Xsmear","ZEventParticles")
process.EBXcX0X008.zElectronsCollection = cms.untracked.InputTag("EBXcX0X008Xsmear","ZEventParticles")

process.EBXcX0X01Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXcX0X01Xsmear.EB.c = cms.double(0.01)

process.EBXcX0X01 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXcX0X01.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXcX0X01.zsrc = cms.untracked.InputTag("EBXcX0X01Xsmear","ZEventParticles")
process.EBXcX0X01.zElectronsCollection = cms.untracked.InputTag("EBXcX0X01Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.EBXcX0X002Xsmear
+ process.EBXcX0X002
+ process.EBXcX0X004Xsmear
+ process.EBXcX0X004
+ process.EBXcX0X006Xsmear
+ process.EBXcX0X006
+ process.EBXcX0X008Xsmear
+ process.EBXcX0X008
+ process.EBXcX0X01Xsmear
+ process.EBXcX0X01
)
