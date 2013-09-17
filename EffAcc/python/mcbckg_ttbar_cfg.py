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
    fileNames = cms.untracked.vstring("file:/local/cms/phedex/store/mc/Summer11/DYToEE_M-20_CT10_TuneZ2_7TeV-powheg-pythia/GEN-SIM-RECO/PU_S4_START42_V11-v1/0000/047818FC-A8A7-E011-BCFF-00151796C088.root")
)
process.load("Configuration.StandardSequences.Geometry_cff")
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
## global tags:
#process.GlobalTag.globaltag = cms.string('GR_P_V16::All')
#process.load("Configuration.StandardSequences.MagneticField_cff")
#process.load('Configuration.StandardSequences.Services_cff')
#process.load("PhysicsTools.PatAlgos.patSequences_cff")

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('histo_10M_partBUILDINGTTEST.root')
)
process.load("ZShape.EffAcc.FullSimSmearedElectronProducer_cfi")
process.load("ZShape.EffAcc.ZEfficiencyKevin_cfi")

#process.load("ZShape.EffAcc.ZEfficiencyStd_cfi")

process.mcEff.zsrc = cms.untracked.InputTag("FullSimSmearedElectronsProducer","ZEventParticles")
process.mcEff.zElectronsCollection = cms.untracked.InputTag("FullSimSmearedElectronsProducer","ZEventParticles")
process.mcEff.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")

process.f2s = cms.EDProducer("ZFullSim2Event"
                             )
process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")
#process.p = cms.Path(process.makePatElectrons+process.f2s)
process.p = cms.Path(process.makePatElectrons+process.hfRecoEcalCandidateMC+process.f2s+process.FullSimSmearedElectronsProducer+process.mcEff)
