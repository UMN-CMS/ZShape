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
    input = cms.untracked.int32(-1)
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


process.HF_constantp_1_0_smear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HF_constantp_1_0_smear.HF.constantp = cms.double(1.0)

process.HF_constantp_1_0 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HF_constantp_1_0.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HF_constantp_1_0.zsrc = cms.untracked.InputTag("HF_constantp_1_0_smear","ZEventParticles")
process.HF_constantp_1_0.zElectronsCollection = cms.untracked.InputTag("HF_constantp_1_0_smear","ZEventParticles")

process.HF_constantp_0_002_smear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HF_constantp_0_002_smear.HF.constantp = cms.double(0.002)

process.HF_constantp_0_002 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HF_constantp_0_002.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HF_constantp_0_002.zsrc = cms.untracked.InputTag("HF_constantp_0_002_smear","ZEventParticles")
process.HF_constantp_0_002.zElectronsCollection = cms.untracked.InputTag("HF_constantp_0_002_smear","ZEventParticles")

process.HF_constantp_2_0_smear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HF_constantp_2_0_smear.HF.constantp = cms.double(2.0)

process.HF_constantp_2_0 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HF_constantp_2_0.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HF_constantp_2_0.zsrc = cms.untracked.InputTag("HF_constantp_2_0_smear","ZEventParticles")
process.HF_constantp_2_0.zElectronsCollection = cms.untracked.InputTag("HF_constantp_2_0_smear","ZEventParticles")

process.HF_constantp_0_1_smear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HF_constantp_0_1_smear.HF.constantp = cms.double(0.1)

process.HF_constantp_0_1 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HF_constantp_0_1.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HF_constantp_0_1.zsrc = cms.untracked.InputTag("HF_constantp_0_1_smear","ZEventParticles")
process.HF_constantp_0_1.zElectronsCollection = cms.untracked.InputTag("HF_constantp_0_1_smear","ZEventParticles")

process.p = cms.Path(process.f2s
+ process.HF_constantp_1_0_smear
+ process.HF_constantp_1_0
+ process.HF_constantp_0_002_smear
+ process.HF_constantp_0_002
+ process.HF_constantp_2_0_smear
+ process.HF_constantp_2_0
+ process.HF_constantp_0_1_smear
+ process.HF_constantp_0_1
)
