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


process.HFXconstantX0X0001Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X0001Xsmear.HF.constant = cms.double(0.0001)

process.HFXconstantX0X0001 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X0001.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X0001.zsrc = cms.untracked.InputTag("HFXconstantX0X0001Xsmear","ZEventParticles")
process.HFXconstantX0X0001.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X0001Xsmear","ZEventParticles")

process.HFXconstantX0X001Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X001Xsmear.HF.constant = cms.double(0.001)

process.HFXconstantX0X001 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X001.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X001.zsrc = cms.untracked.InputTag("HFXconstantX0X001Xsmear","ZEventParticles")
process.HFXconstantX0X001.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X001Xsmear","ZEventParticles")

process.HFXconstantX0X005Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X005Xsmear.HF.constant = cms.double(0.005)

process.HFXconstantX0X005 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X005.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X005.zsrc = cms.untracked.InputTag("HFXconstantX0X005Xsmear","ZEventParticles")
process.HFXconstantX0X005.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X005Xsmear","ZEventParticles")

process.HFXconstantX0X01Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X01Xsmear.HF.constant = cms.double(0.01)

process.HFXconstantX0X01 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X01.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X01.zsrc = cms.untracked.InputTag("HFXconstantX0X01Xsmear","ZEventParticles")
process.HFXconstantX0X01.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X01Xsmear","ZEventParticles")

process.HFXconstantX0X03Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X03Xsmear.HF.constant = cms.double(0.03)

process.HFXconstantX0X03 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X03.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X03.zsrc = cms.untracked.InputTag("HFXconstantX0X03Xsmear","ZEventParticles")
process.HFXconstantX0X03.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X03Xsmear","ZEventParticles")

process.HFXconstantX0X06Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X06Xsmear.HF.constant = cms.double(0.06)

process.HFXconstantX0X06 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X06.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X06.zsrc = cms.untracked.InputTag("HFXconstantX0X06Xsmear","ZEventParticles")
process.HFXconstantX0X06.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X06Xsmear","ZEventParticles")

process.HFXconstantX0X08Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X08Xsmear.HF.constant = cms.double(0.08)

process.HFXconstantX0X08 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X08.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X08.zsrc = cms.untracked.InputTag("HFXconstantX0X08Xsmear","ZEventParticles")
process.HFXconstantX0X08.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X08Xsmear","ZEventParticles")

process.HFXconstantX0X085Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X085Xsmear.HF.constant = cms.double(0.085)

process.HFXconstantX0X085 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X085.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X085.zsrc = cms.untracked.InputTag("HFXconstantX0X085Xsmear","ZEventParticles")
process.HFXconstantX0X085.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X085Xsmear","ZEventParticles")

process.HFXconstantX0X09Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X09Xsmear.HF.constant = cms.double(0.09)

process.HFXconstantX0X09 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X09.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X09.zsrc = cms.untracked.InputTag("HFXconstantX0X09Xsmear","ZEventParticles")
process.HFXconstantX0X09.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X09Xsmear","ZEventParticles")

process.HFXconstantX0X092Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X092Xsmear.HF.constant = cms.double(0.092)

process.HFXconstantX0X092 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X092.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X092.zsrc = cms.untracked.InputTag("HFXconstantX0X092Xsmear","ZEventParticles")
process.HFXconstantX0X092.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X092Xsmear","ZEventParticles")

process.HFXconstantX0X094Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X094Xsmear.HF.constant = cms.double(0.094)

process.HFXconstantX0X094 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X094.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X094.zsrc = cms.untracked.InputTag("HFXconstantX0X094Xsmear","ZEventParticles")
process.HFXconstantX0X094.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X094Xsmear","ZEventParticles")

process.HFXconstantX0X096Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X096Xsmear.HF.constant = cms.double(0.096)

process.HFXconstantX0X096 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X096.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X096.zsrc = cms.untracked.InputTag("HFXconstantX0X096Xsmear","ZEventParticles")
process.HFXconstantX0X096.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X096Xsmear","ZEventParticles")

process.HFXconstantX0X098Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X098Xsmear.HF.constant = cms.double(0.098)

process.HFXconstantX0X098 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X098.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X098.zsrc = cms.untracked.InputTag("HFXconstantX0X098Xsmear","ZEventParticles")
process.HFXconstantX0X098.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X098Xsmear","ZEventParticles")

process.HFXconstantX0X099Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X099Xsmear.HF.constant = cms.double(0.099)

process.HFXconstantX0X099 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X099.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X099.zsrc = cms.untracked.InputTag("HFXconstantX0X099Xsmear","ZEventParticles")
process.HFXconstantX0X099.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X099Xsmear","ZEventParticles")

process.HFXconstantX0X100Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X100Xsmear.HF.constant = cms.double(0.100)

process.HFXconstantX0X100 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X100.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X100.zsrc = cms.untracked.InputTag("HFXconstantX0X100Xsmear","ZEventParticles")
process.HFXconstantX0X100.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X100Xsmear","ZEventParticles")

process.HFXconstantX0X102Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X102Xsmear.HF.constant = cms.double(0.102)

process.HFXconstantX0X102 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X102.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X102.zsrc = cms.untracked.InputTag("HFXconstantX0X102Xsmear","ZEventParticles")
process.HFXconstantX0X102.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X102Xsmear","ZEventParticles")

process.HFXconstantX0X104Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X104Xsmear.HF.constant = cms.double(0.104)

process.HFXconstantX0X104 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X104.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X104.zsrc = cms.untracked.InputTag("HFXconstantX0X104Xsmear","ZEventParticles")
process.HFXconstantX0X104.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X104Xsmear","ZEventParticles")

process.HFXconstantX0X106Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X106Xsmear.HF.constant = cms.double(0.106)

process.HFXconstantX0X106 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X106.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X106.zsrc = cms.untracked.InputTag("HFXconstantX0X106Xsmear","ZEventParticles")
process.HFXconstantX0X106.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X106Xsmear","ZEventParticles")

process.HFXconstantX0X108Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X108Xsmear.HF.constant = cms.double(0.108)

process.HFXconstantX0X108 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X108.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X108.zsrc = cms.untracked.InputTag("HFXconstantX0X108Xsmear","ZEventParticles")
process.HFXconstantX0X108.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X108Xsmear","ZEventParticles")

process.HFXconstantX0X11Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X11Xsmear.HF.constant = cms.double(0.11)

process.HFXconstantX0X11 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X11.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X11.zsrc = cms.untracked.InputTag("HFXconstantX0X11Xsmear","ZEventParticles")
process.HFXconstantX0X11.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X11Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.HFXconstantX0X0001Xsmear
+ process.HFXconstantX0X0001
+ process.HFXconstantX0X001Xsmear
+ process.HFXconstantX0X001
+ process.HFXconstantX0X005Xsmear
+ process.HFXconstantX0X005
+ process.HFXconstantX0X01Xsmear
+ process.HFXconstantX0X01
+ process.HFXconstantX0X03Xsmear
+ process.HFXconstantX0X03
+ process.HFXconstantX0X06Xsmear
+ process.HFXconstantX0X06
+ process.HFXconstantX0X08Xsmear
+ process.HFXconstantX0X08
+ process.HFXconstantX0X085Xsmear
+ process.HFXconstantX0X085
+ process.HFXconstantX0X09Xsmear
+ process.HFXconstantX0X09
+ process.HFXconstantX0X092Xsmear
+ process.HFXconstantX0X092
+ process.HFXconstantX0X094Xsmear
+ process.HFXconstantX0X094
+ process.HFXconstantX0X096Xsmear
+ process.HFXconstantX0X096
+ process.HFXconstantX0X098Xsmear
+ process.HFXconstantX0X098
+ process.HFXconstantX0X099Xsmear
+ process.HFXconstantX0X099
)
