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
    fileNames = cms.untracked.vstring("file:/hdfs/cms/phedex/store/mc/Summer11/DYToEE_M-20_CT10_TuneZ2_7TeV-powheg-pythia/GEN-SIM-RECO/PU_S4_START42_V11-v1/0000/00F71C3D-88A8-E011-AC48-001D0967D0DA.root" )
)
process.load("Configuration.StandardSequences.Geometry_cff")
process.TFileService = cms.Service("TFileService",
    fileName = cms.string('histo_10M_partBUILDINGTTEST.root')
)

process.load("ZShape.EffAcc.FullSimSmearedElectronProducer_cfi")
process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")
process.load("ZShape.EffAcc.fullSimLoader_cff")
process.hfRecoEcalCandidateMC.intercept2DCut = cms.double(-99)
process.hfRecoEcalCandidateMC.intercept2DSlope = cms.double(-99)
process.hfRecoEcalCandidateMC.e9e25Cut = cms.double(0)







#multiple runs
import ZShape.EffAcc.ZEfficiencyUnity_cfi
process.mcEff = ZShape.EffAcc.ZEfficiencyUnity_cfi.mcEff.clone()
process.mcEff.zsrc = cms.untracked.InputTag("fullSimLoad","ZEventParticles")
process.mcEff.zElectronsCollection = cms.untracked.InputTag("fullSimLoad","ZEventParticles")
process.mcEff.zTreeLevelElectronsCollection = cms.untracked.InputTag("fullSimLoad","ZEventEle3")
#ECALScale- ECALScale+ (0.005) HFScale+ HFScale-  (0.003)
process.esEcalP = ZShape.EffAcc.ZEfficiencyUnity_cfi.mcEff.clone()

process.esEcalP.systematic = "ECALScale+"
process.esEcalP.systematicScale = cms.untracked.double(0.005)
process.esEcalP.zsrc = cms.untracked.InputTag("fullSimLoad","ZEventParticles")
process.esEcalP.zElectronsCollection = cms.untracked.InputTag("fullSimLoad","ZEventParticles")
process.esEcalP.zTreeLevelElectronsCollection = cms.untracked.InputTag("fullSimLoad","ZEventEle3")

process.esEcalM = ZShape.EffAcc.ZEfficiencyUnity_cfi.mcEff.clone()

process.esEcalM.systematic = "ECALScale-"
process.esEcalM.systematicScale = cms.untracked.double(0.005)
process.esEcalM.zsrc = cms.untracked.InputTag("fullSimLoad","ZEventParticles")
process.esEcalM.zElectronsCollection = cms.untracked.InputTag("fullSimLoad","ZEventParticles")
process.esEcalM.zTreeLevelElectronsCollection = cms.untracked.InputTag("fullSimLoad","ZEventEle3")


process.esHFP = ZShape.EffAcc.ZEfficiencyUnity_cfi.mcEff.clone()

process.esHFP.systematic = "HFScale+"
process.esHFP.systematicScale = cms.untracked.double(0.03)
process.esHFP.zsrc = cms.untracked.InputTag("fullSimLoad","ZEventParticles")
process.esHFP.zElectronsCollection = cms.untracked.InputTag("fullSimLoad","ZEventParticles")
process.esHFP.zTreeLevelElectronsCollection = cms.untracked.InputTag("fullSimLoad","ZEventEle3")



process.esHFM = ZShape.EffAcc.ZEfficiencyUnity_cfi.mcEff.clone()

process.esHFM.systematic = "HFScale-"
process.esHFM.systematicScale = cms.untracked.double(0.03)
process.esHFM.zsrc = cms.untracked.InputTag("fullSimLoad","ZEventParticles")
process.esHFM.zElectronsCollection = cms.untracked.InputTag("fullSimLoad","ZEventParticles")
process.esHFM.zTreeLevelElectronsCollection = cms.untracked.InputTag("fullSimLoad","ZEventEle3")




#process.p = cms.Path(process.makePatElectrons+process.f2s)
process.p = cms.Path(process.hfEMClusters+process.hfRecoEcalCandidateMC+process.f2s_sequence+process.mcEff
                     +process.esEcalP
                     +process.esEcalM
                     +process.esHFP
                     +process.esHFM)

