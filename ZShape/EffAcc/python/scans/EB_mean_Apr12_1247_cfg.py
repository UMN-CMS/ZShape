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
    input = cms.untracked.int32(20000)
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


process.EBXmeanX1X000Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX1X000Xsmear.EB.mean = cms.double(1.000)

process.EBXmeanX1X000 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX1X000.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX1X000.zsrc = cms.untracked.InputTag("EBXmeanX1X000Xsmear","ZEventParticles")
process.EBXmeanX1X000.zElectronsCollection = cms.untracked.InputTag("EBXmeanX1X000Xsmear","ZEventParticles")

process.EBXmeanX1X001Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX1X001Xsmear.EB.mean = cms.double(1.001)

process.EBXmeanX1X001 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX1X001.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX1X001.zsrc = cms.untracked.InputTag("EBXmeanX1X001Xsmear","ZEventParticles")
process.EBXmeanX1X001.zElectronsCollection = cms.untracked.InputTag("EBXmeanX1X001Xsmear","ZEventParticles")

process.EBXmeanX1X002Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX1X002Xsmear.EB.mean = cms.double(1.002)

process.EBXmeanX1X002 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX1X002.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX1X002.zsrc = cms.untracked.InputTag("EBXmeanX1X002Xsmear","ZEventParticles")
process.EBXmeanX1X002.zElectronsCollection = cms.untracked.InputTag("EBXmeanX1X002Xsmear","ZEventParticles")

process.EBXmeanX1X003Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX1X003Xsmear.EB.mean = cms.double(1.003)

process.EBXmeanX1X003 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX1X003.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX1X003.zsrc = cms.untracked.InputTag("EBXmeanX1X003Xsmear","ZEventParticles")
process.EBXmeanX1X003.zElectronsCollection = cms.untracked.InputTag("EBXmeanX1X003Xsmear","ZEventParticles")

process.EBXmeanX1X004Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX1X004Xsmear.EB.mean = cms.double(1.004)

process.EBXmeanX1X004 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX1X004.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX1X004.zsrc = cms.untracked.InputTag("EBXmeanX1X004Xsmear","ZEventParticles")
process.EBXmeanX1X004.zElectronsCollection = cms.untracked.InputTag("EBXmeanX1X004Xsmear","ZEventParticles")

process.EBXmeanX1X005Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.EBXmeanX1X005Xsmear.EB.mean = cms.double(1.005)

process.EBXmeanX1X005 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.EBXmeanX1X005.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.EBXmeanX1X005.zsrc = cms.untracked.InputTag("EBXmeanX1X005Xsmear","ZEventParticles")
process.EBXmeanX1X005.zElectronsCollection = cms.untracked.InputTag("EBXmeanX1X005Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.EBXmeanX1X000Xsmear
+ process.EBXmeanX1X000
+ process.EBXmeanX1X001Xsmear
+ process.EBXmeanX1X001
+ process.EBXmeanX1X002Xsmear
+ process.EBXmeanX1X002
+ process.EBXmeanX1X003Xsmear
+ process.EBXmeanX1X003
+ process.EBXmeanX1X004Xsmear
+ process.EBXmeanX1X004
+ process.EBXmeanX1X005Xsmear
+ process.EBXmeanX1X005
)
