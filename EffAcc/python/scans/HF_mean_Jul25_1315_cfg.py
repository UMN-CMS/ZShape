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


process.HFXmeanX0X01Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X01Xsmear.HF.mean = cms.double(0.01)

process.HFXmeanX0X01 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X01.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X01.zsrc = cms.untracked.InputTag("HFXmeanX0X01Xsmear","ZEventParticles")
process.HFXmeanX0X01.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X01Xsmear","ZEventParticles")

process.HFXmeanX0X02Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X02Xsmear.HF.mean = cms.double(0.02)

process.HFXmeanX0X02 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X02.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X02.zsrc = cms.untracked.InputTag("HFXmeanX0X02Xsmear","ZEventParticles")
process.HFXmeanX0X02.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X02Xsmear","ZEventParticles")

process.HFXmeanX0X03Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X03Xsmear.HF.mean = cms.double(0.03)

process.HFXmeanX0X03 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X03.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X03.zsrc = cms.untracked.InputTag("HFXmeanX0X03Xsmear","ZEventParticles")
process.HFXmeanX0X03.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X03Xsmear","ZEventParticles")

process.HFXmeanX0X04Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X04Xsmear.HF.mean = cms.double(0.04)

process.HFXmeanX0X04 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X04.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X04.zsrc = cms.untracked.InputTag("HFXmeanX0X04Xsmear","ZEventParticles")
process.HFXmeanX0X04.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X04Xsmear","ZEventParticles")

process.HFXmeanX0X05Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X05Xsmear.HF.mean = cms.double(0.05)

process.HFXmeanX0X05 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X05.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X05.zsrc = cms.untracked.InputTag("HFXmeanX0X05Xsmear","ZEventParticles")
process.HFXmeanX0X05.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X05Xsmear","ZEventParticles")

process.HFXmeanX0X06Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X06Xsmear.HF.mean = cms.double(0.06)

process.HFXmeanX0X06 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X06.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X06.zsrc = cms.untracked.InputTag("HFXmeanX0X06Xsmear","ZEventParticles")
process.HFXmeanX0X06.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X06Xsmear","ZEventParticles")

process.HFXmeanX0X07Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X07Xsmear.HF.mean = cms.double(0.07)

process.HFXmeanX0X07 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X07.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X07.zsrc = cms.untracked.InputTag("HFXmeanX0X07Xsmear","ZEventParticles")
process.HFXmeanX0X07.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X07Xsmear","ZEventParticles")

process.HFXmeanX0X08Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X08Xsmear.HF.mean = cms.double(0.08)

process.HFXmeanX0X08 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X08.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X08.zsrc = cms.untracked.InputTag("HFXmeanX0X08Xsmear","ZEventParticles")
process.HFXmeanX0X08.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X08Xsmear","ZEventParticles")

process.HFXmeanX0X09Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X09Xsmear.HF.mean = cms.double(0.09)

process.HFXmeanX0X09 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X09.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X09.zsrc = cms.untracked.InputTag("HFXmeanX0X09Xsmear","ZEventParticles")
process.HFXmeanX0X09.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X09Xsmear","ZEventParticles")

process.HFXmeanX0X1Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X1Xsmear.HF.mean = cms.double(0.1)

process.HFXmeanX0X1 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X1.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X1.zsrc = cms.untracked.InputTag("HFXmeanX0X1Xsmear","ZEventParticles")
process.HFXmeanX0X1.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X1Xsmear","ZEventParticles")

process.HFXmeanX0X11Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X11Xsmear.HF.mean = cms.double(0.11)

process.HFXmeanX0X11 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X11.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X11.zsrc = cms.untracked.InputTag("HFXmeanX0X11Xsmear","ZEventParticles")
process.HFXmeanX0X11.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X11Xsmear","ZEventParticles")

process.HFXmeanX0X12Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXmeanX0X12Xsmear.HF.mean = cms.double(0.12)

process.HFXmeanX0X12 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXmeanX0X12.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXmeanX0X12.zsrc = cms.untracked.InputTag("HFXmeanX0X12Xsmear","ZEventParticles")
process.HFXmeanX0X12.zElectronsCollection = cms.untracked.InputTag("HFXmeanX0X12Xsmear","ZEventParticles")

process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p = cms.Path(process.hfRecoEcalCandidate+process.f2s
+ process.HFXmeanX0X01Xsmear
+ process.HFXmeanX0X01
+ process.HFXmeanX0X02Xsmear
+ process.HFXmeanX0X02
+ process.HFXmeanX0X03Xsmear
+ process.HFXmeanX0X03
+ process.HFXmeanX0X04Xsmear
+ process.HFXmeanX0X04
+ process.HFXmeanX0X05Xsmear
+ process.HFXmeanX0X05
+ process.HFXmeanX0X06Xsmear
+ process.HFXmeanX0X06
+ process.HFXmeanX0X07Xsmear
+ process.HFXmeanX0X07
+ process.HFXmeanX0X08Xsmear
+ process.HFXmeanX0X08
+ process.HFXmeanX0X09Xsmear
+ process.HFXmeanX0X09
+ process.HFXmeanX0X1Xsmear
+ process.HFXmeanX0X1
+ process.HFXmeanX0X11Xsmear
+ process.HFXmeanX0X11
+ process.HFXmeanX0X12Xsmear
+ process.HFXmeanX0X12
)
