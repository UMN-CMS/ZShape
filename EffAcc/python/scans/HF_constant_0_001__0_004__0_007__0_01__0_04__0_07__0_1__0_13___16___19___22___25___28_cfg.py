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
    input = cms.untracked.int32(50000)
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


process.HFXconstantX0X001Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X001Xsmear.HF.constant = cms.double(0.001)

process.HFXconstantX0X001 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X001.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X001.zsrc = cms.untracked.InputTag("HFXconstantX0X001Xsmear","ZEventParticles")
process.HFXconstantX0X001.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X001Xsmear","ZEventParticles")

process.HFXconstantX0X004Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X004Xsmear.HF.constant = cms.double(0.004)

process.HFXconstantX0X004 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X004.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X004.zsrc = cms.untracked.InputTag("HFXconstantX0X004Xsmear","ZEventParticles")
process.HFXconstantX0X004.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X004Xsmear","ZEventParticles")

process.HFXconstantX0X007Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X007Xsmear.HF.constant = cms.double(0.007)

process.HFXconstantX0X007 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X007.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X007.zsrc = cms.untracked.InputTag("HFXconstantX0X007Xsmear","ZEventParticles")
process.HFXconstantX0X007.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X007Xsmear","ZEventParticles")

process.HFXconstantX0X01Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X01Xsmear.HF.constant = cms.double(0.01)

process.HFXconstantX0X01 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X01.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X01.zsrc = cms.untracked.InputTag("HFXconstantX0X01Xsmear","ZEventParticles")
process.HFXconstantX0X01.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X01Xsmear","ZEventParticles")

process.HFXconstantX0X04Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X04Xsmear.HF.constant = cms.double(0.04)

process.HFXconstantX0X04 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X04.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X04.zsrc = cms.untracked.InputTag("HFXconstantX0X04Xsmear","ZEventParticles")
process.HFXconstantX0X04.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X04Xsmear","ZEventParticles")

process.HFXconstantX0X07Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X07Xsmear.HF.constant = cms.double(0.07)

process.HFXconstantX0X07 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X07.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X07.zsrc = cms.untracked.InputTag("HFXconstantX0X07Xsmear","ZEventParticles")
process.HFXconstantX0X07.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X07Xsmear","ZEventParticles")

process.HFXconstantX0X1Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X1Xsmear.HF.constant = cms.double(0.1)

process.HFXconstantX0X1 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X1.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X1.zsrc = cms.untracked.InputTag("HFXconstantX0X1Xsmear","ZEventParticles")
process.HFXconstantX0X1.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X1Xsmear","ZEventParticles")

process.HFXconstantX0X13Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantX0X13Xsmear.HF.constant = cms.double(0.13)

process.HFXconstantX0X13 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantX0X13.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantX0X13.zsrc = cms.untracked.InputTag("HFXconstantX0X13Xsmear","ZEventParticles")
process.HFXconstantX0X13.zElectronsCollection = cms.untracked.InputTag("HFXconstantX0X13Xsmear","ZEventParticles")

process.HFXconstantXX16Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantXX16Xsmear.HF.constant = cms.double(.16)

process.HFXconstantXX16 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantXX16.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantXX16.zsrc = cms.untracked.InputTag("HFXconstantXX16Xsmear","ZEventParticles")
process.HFXconstantXX16.zElectronsCollection = cms.untracked.InputTag("HFXconstantXX16Xsmear","ZEventParticles")

process.HFXconstantXX19Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantXX19Xsmear.HF.constant = cms.double(.19)

process.HFXconstantXX19 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantXX19.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantXX19.zsrc = cms.untracked.InputTag("HFXconstantXX19Xsmear","ZEventParticles")
process.HFXconstantXX19.zElectronsCollection = cms.untracked.InputTag("HFXconstantXX19Xsmear","ZEventParticles")

process.HFXconstantXX22Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantXX22Xsmear.HF.constant = cms.double(.22)

process.HFXconstantXX22 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantXX22.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantXX22.zsrc = cms.untracked.InputTag("HFXconstantXX22Xsmear","ZEventParticles")
process.HFXconstantXX22.zElectronsCollection = cms.untracked.InputTag("HFXconstantXX22Xsmear","ZEventParticles")

process.HFXconstantXX25Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantXX25Xsmear.HF.constant = cms.double(.25)

process.HFXconstantXX25 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantXX25.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantXX25.zsrc = cms.untracked.InputTag("HFXconstantXX25Xsmear","ZEventParticles")
process.HFXconstantXX25.zElectronsCollection = cms.untracked.InputTag("HFXconstantXX25Xsmear","ZEventParticles")

process.HFXconstantXX28Xsmear = ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone()
process.HFXconstantXX28Xsmear.HF.constant = cms.double(.28)

process.HFXconstantXX28 = ZShape.EffAcc.ZEfficiencyKevin_cfi.mcEff.clone()
process.HFXconstantXX28.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")
process.HFXconstantXX28.zsrc = cms.untracked.InputTag("HFXconstantXX28Xsmear","ZEventParticles")
process.HFXconstantXX28.zElectronsCollection = cms.untracked.InputTag("HFXconstantXX28Xsmear","ZEventParticles")

process.p = cms.Path(process.f2s
+ process.HFXconstantX0X001Xsmear
+ process.HFXconstantX0X001
+ process.HFXconstantX0X004Xsmear
+ process.HFXconstantX0X004
+ process.HFXconstantX0X007Xsmear
+ process.HFXconstantX0X007
+ process.HFXconstantX0X01Xsmear
+ process.HFXconstantX0X01
+ process.HFXconstantX0X04Xsmear
+ process.HFXconstantX0X04
+ process.HFXconstantX0X07Xsmear
+ process.HFXconstantX0X07
+ process.HFXconstantX0X1Xsmear
+ process.HFXconstantX0X1
+ process.HFXconstantX0X13Xsmear
+ process.HFXconstantX0X13
+ process.HFXconstantXX16Xsmear
+ process.HFXconstantXX16
+ process.HFXconstantXX19Xsmear
+ process.HFXconstantXX19
+ process.HFXconstantXX22Xsmear
+ process.HFXconstantXX22
+ process.HFXconstantXX25Xsmear
+ process.HFXconstantXX25
+ process.HFXconstantXX28Xsmear
+ process.HFXconstantXX28
)
