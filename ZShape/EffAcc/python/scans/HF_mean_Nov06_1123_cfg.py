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
    input = cms.untracked.int32(10)
    )

process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
    fileNames = cms.untracked.vstring("file:/local/cms/phedex/store/mc/Summer11/DYToEE_M-20_CT10_TuneZ2_7TeV-powheg-pythia/GEN-SIM-RECO/PU_S4_START42_V11-v1/0000/04EB52AF-5BA8-E011-A4C2-00266CFABAF0.root" )
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('histo_10Mblkjkljkj.root')
)

process.f2s = cms.EDProducer("ZFullSim2Event"
                             )
import ZShape.EffAcc.FullSimSmearedElectronProducer_cfi
import ZShape.EffAcc.ZEfficiencyKevin_cfi


process.HFXmeanX0X96Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X96Xsmear.HF.meanp = cms.double(0.96)
process.HFXmeanX0X96Xsmear.HF.meanm = cms.double(0.96)

process.HFXmeanX0X96 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X96.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X96.zsrc = cms.untracked.InputTag("HFXmeanX0X96Xsmear","ZEventParticles")
process.HFXmeanX0X96.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X96Xsmear","ZEventParticles")

process.HFXmeanX0X97Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X97Xsmear.HF.meanp = cms.double(0.97)
process.HFXmeanX0X97Xsmear.HF.meanm = cms.double(0.97)

process.HFXmeanX0X97 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X97.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X97.zsrc = cms.untracked.InputTag("HFXmeanX0X97Xsmear","ZEventParticles")
process.HFXmeanX0X97.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X97Xsmear","ZEventParticles")

process.HFXmeanX0X985Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X985Xsmear.HF.meanp = cms.double(0.985)
process.HFXmeanX0X985Xsmear.HF.meanm = cms.double(0.985)

process.HFXmeanX0X985 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X985.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X985.zsrc = cms.untracked.InputTag("HFXmeanX0X985Xsmear","ZEventParticles")
process.HFXmeanX0X985.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X985Xsmear","ZEventParticles")

process.HFXmeanX0X99Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X99Xsmear.HF.meanp = cms.double(0.99)
process.HFXmeanX0X99Xsmear.HF.meanm = cms.double(0.99)

process.HFXmeanX0X99 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X99.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X99.zsrc = cms.untracked.InputTag("HFXmeanX0X99Xsmear","ZEventParticles")
process.HFXmeanX0X99.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X99Xsmear","ZEventParticles")

process.HFXmeanX0X995Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X995Xsmear.HF.meanp = cms.double(0.995)
process.HFXmeanX0X995Xsmear.HF.meanm = cms.double(0.995)

process.HFXmeanX0X995 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X995.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X995.zsrc = cms.untracked.InputTag("HFXmeanX0X995Xsmear","ZEventParticles")
process.HFXmeanX0X995.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X995Xsmear","ZEventParticles")

process.HFXmeanX1X0Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X0Xsmear.HF.meanp = cms.double(1.0)
process.HFXmeanX1X0Xsmear.HF.meanm = cms.double(1.0)

process.HFXmeanX1X0 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X0.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X0.zsrc = cms.untracked.InputTag("HFXmeanX1X0Xsmear","ZEventParticles")
process.HFXmeanX1X0.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X0Xsmear","ZEventParticles")

process.HFXmeanX1X005Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X005Xsmear.HF.meanp = cms.double(1.005)
process.HFXmeanX1X005Xsmear.HF.meanm = cms.double(1.005)

process.HFXmeanX1X005 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X005.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X005.zsrc = cms.untracked.InputTag("HFXmeanX1X005Xsmear","ZEventParticles")
process.HFXmeanX1X005.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X005Xsmear","ZEventParticles")

process.HFXmeanX1X01Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X01Xsmear.HF.meanp = cms.double(1.01)
process.HFXmeanX1X01Xsmear.HF.meanm = cms.double(1.01)

process.HFXmeanX1X01 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X01.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X01.zsrc = cms.untracked.InputTag("HFXmeanX1X01Xsmear","ZEventParticles")
process.HFXmeanX1X01.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X01Xsmear","ZEventParticles")

process.HFXmeanX1X015Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X015Xsmear.HF.meanp = cms.double(1.015)
process.HFXmeanX1X015Xsmear.HF.meanm = cms.double(1.015)

process.HFXmeanX1X015 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X015.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X015.zsrc = cms.untracked.InputTag("HFXmeanX1X015Xsmear","ZEventParticles")
process.HFXmeanX1X015.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X015Xsmear","ZEventParticles")

process.HFXmeanX1X02Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X02Xsmear.HF.meanp = cms.double(1.02)
process.HFXmeanX1X02Xsmear.HF.meanm = cms.double(1.02)

process.HFXmeanX1X02 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X02.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X02.zsrc = cms.untracked.InputTag("HFXmeanX1X02Xsmear","ZEventParticles")
process.HFXmeanX1X02.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X02Xsmear","ZEventParticles")

process.HFXmeanX1X03Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X03Xsmear.HF.meanp = cms.double(1.03)
process.HFXmeanX1X03Xsmear.HF.meanm = cms.double(1.03)

process.HFXmeanX1X03 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X03.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X03.zsrc = cms.untracked.InputTag("HFXmeanX1X03Xsmear","ZEventParticles")
process.HFXmeanX1X03.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X03Xsmear","ZEventParticles")

process.HFXmeanX1X04Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX1X04Xsmear.HF.meanp = cms.double(1.04)
process.HFXmeanX1X04Xsmear.HF.meanm = cms.double(1.04)

process.HFXmeanX1X04 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX1X04.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX1X04.zsrc = cms.untracked.InputTag("HFXmeanX1X04Xsmear","ZEventParticles")
process.HFXmeanX1X04.zElectronsCollection = cms.untracked.InputTag("HFXmeanX1X04Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.HFXmeanX0X96Xsmear
+ process.HFXmeanX0X96
+ process.HFXmeanX0X97Xsmear
+ process.HFXmeanX0X97
+ process.HFXmeanX0X985Xsmear
+ process.HFXmeanX0X985
+ process.HFXmeanX0X99Xsmear
+ process.HFXmeanX0X99
+ process.HFXmeanX0X995Xsmear
+ process.HFXmeanX0X995
+ process.HFXmeanX1X0Xsmear
+ process.HFXmeanX1X0
+ process.HFXmeanX1X005Xsmear
+ process.HFXmeanX1X005
+ process.HFXmeanX1X01Xsmear
+ process.HFXmeanX1X01
+ process.HFXmeanX1X015Xsmear
+ process.HFXmeanX1X015
+ process.HFXmeanX1X02Xsmear
+ process.HFXmeanX1X02
+ process.HFXmeanX1X03Xsmear
+ process.HFXmeanX1X03
+ process.HFXmeanX1X04Xsmear
+ process.HFXmeanX1X04
)
