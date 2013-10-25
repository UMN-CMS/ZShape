import FWCore.ParameterSet.Config as cms

process = cms.Process("ZFROMDATA")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("CondCore.DBCommon.CondDBSetup_cfi")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Geometry.CaloEventSetup.CaloGeometry_cfi")
process.load("Geometry.CaloEventSetup.CaloTopology_cfi")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load("RecoLocalCalo.EcalRecAlgos.EcalSeverityLevelESProducer_cfi")

process.GlobalTag.globaltag = 'GR_R_44_V11::All'

process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring('/store/mc/Summer11/DYToEE_M-20_CT10_TuneZ2_7TeV-powheg-pythia/GEN-SIM-RECO/PU_S4_START42_V11-v1/0000/3A5E80B6-14A8-E011-9E8C-0015178C49F8.root')
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

# Set the output root file to include the unix epoch as an int
from time import time
outfile  = "test_mc_" + str(int(time())) + ".root"

process.TFileService = cms.Service("TFileService",
        fileName = cms.string(outfile)
        )

process.options = cms.untracked.PSet(
        wantSummary = cms.untracked.bool(True),
        fileMode = cms.untracked.string('NOMERGE'),
        SkipEvent = cms.untracked.vstring('ProductNotFound')
        )

process.TimerService = cms.Service("TimerService",
        useCPUtime = cms.untracked.bool(True)
        )

process.load("ZShape.ZFromData.ZFromDataElectrons_cfi")

# Used to set which triggers cound for HFTID
process.theHLTGsf.hltTag = cms.untracked.VInputTag(
        cms.InputTag("HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1","","HLT"),
        cms.InputTag("HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v2","","HLT"),
        cms.InputTag("HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v3","","HLT"),
        cms.InputTag("HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v4","","HLT"),
        cms.InputTag("HLT_Ele17_CaloIdL_CaloIsoVL_v1","","HLT"),
        cms.InputTag("HLT_Ele17_CaloIdL_CaloIsoVL_v2","","HLT"),
        cms.InputTag("HLT_Ele17_CaloIdL_CaloIsoVL_v3","","HLT"),
        cms.InputTag("HLT_Ele17_CaloIdL_CaloIsoVL_v4","","HLT"),
        cms.InputTag("HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1","","HLT"),
        cms.InputTag("HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v2","","HLT"),
        cms.InputTag("HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v3","","HLT"),
        cms.InputTag("HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v4","","HLT")
        ) #remove the ones you don't want

# Alex's tuple makers
## GSF-GSF
process.tuplemakerGSFGSF = cms.EDAnalyzer('MakeZEffTree',
        quiet = cms.untracked.bool(True),
        MatchTriggerObjects = cms.untracked.bool(False),
        TagProbeProducer = cms.untracked.InputTag('tpMapGsfElectrons'), # No trigger matching
        CutNames = cms.untracked.vstring(
            "Supercluster-Eta", "GsfTrack-EtaDet", "Iso-Pt",
            "ElectronId-EtaDet", "HLT-EtaDet", "HFElectronId-EtaDet",
            "HFSuperCluster-Et", "HFTightElectronId-EtaDet", "EID95", "ISO95",
            "EID90", "ISO90", "EID85", "ISO85", "EID80", "ISO80", "EID70",
            "ISO70", "EID60", "ISO60", "HLT-GSF", "ISO80Only", "ISO80Conv",
            "EID80Only", "EID80Conv", "WP95", "WP90", "WP85", "WP80",
            "NTLooseElectronId-EtaDet", "HFTID"
            ),
        passProbeCandTags = cms.untracked.VInputTag(
            cms.InputTag("theSuperClusters"), cms.InputTag("theGsfElectrons"),
            cms.InputTag("theIsolation"), cms.InputTag("theId"),
            cms.InputTag("theHLT"), cms.InputTag("HFElectronID"),
            cms.InputTag("theHFSuperClusters"),
            cms.InputTag("HFElectronIDTight"), cms.InputTag("ElectronID95"),
            cms.InputTag("Iso95"), cms.InputTag("ElectronID90"),
            cms.InputTag("Iso90"), cms.InputTag("ElectronID85"),
            cms.InputTag("Iso85"), cms.InputTag("ElectronID80"),
            cms.InputTag("Iso80"), cms.InputTag("ElectronID70"),
            cms.InputTag("Iso70"), cms.InputTag("ElectronID60"),
            cms.InputTag("Iso60"), cms.InputTag("theHLTGsf"),
            cms.InputTag("Iso80Only"), cms.InputTag("Iso80WConv"),
            cms.InputTag("ElectronID80Only"),
            cms.InputTag("ElectronID80WConv"), cms.InputTag("WorkingPoint95"),
            cms.InputTag("WorkingPoint90"), cms.InputTag("WorkingPoint85"),
            cms.InputTag("WorkingPoint80"), cms.InputTag("NTElecLoose"),
            cms.InputTag("theHFHLT")
            ),
        )

## WP80-ECALSC
process.tuplemakerWP80ESC = process.tuplemakerGSFGSF.clone(
        TagProbeProducer = cms.untracked.InputTag('tpMapWP80AndECALSC'),
        )

## GSF-HF
process.tuplemakerGSFHF = process.tuplemakerGSFGSF.clone(
        TagProbeProducer = cms.untracked.InputTag('tpMapGsfAndHFSC'),
        )

## Jets for Isolation Cuts
process.load('RecoJets.JetProducers.kt4PFJets_cfi') # For isolation calculation
process.kt6PFJets = process.kt4PFJets.clone(
        rParam = 0.6,
        doRhoFastjet = True,
        Rho_EtaMax = cms.double(2.5),
        )

## Electron ID cuts
process.load("ElectroWeakAnalysis.WENu.simpleEleIdSequence_cff")
process.patElectronIDs = cms.Sequence(process.simpleEleIdSequence)

# Run
process.p1 = cms.Path(
        process.kt6PFJets
        * process.patElectronIDs
        * process.hfEMClusteringSequence  # Needed in MC
        * process.lepton_cands
        #* process.tuplemakerGSFGSF
        * process.tuplemakerWP80ESC
        #* process.tuplemakerGSFHF
        )
