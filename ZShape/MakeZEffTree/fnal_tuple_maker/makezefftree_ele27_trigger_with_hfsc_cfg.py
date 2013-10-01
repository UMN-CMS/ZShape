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

process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring('file:/uscms_data/d3/gude/DoubleElectron_HFpositionFix_313.root')
        )

# Select only events in the same data range as our analysis
from ZShape.ZFromData.GoodDataLumis_160431_163869_cfi import *

process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange(
        GoodLumis1
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

process.TFileService = cms.Service("TFileService",
        fileName = cms.string('KevTest.root')
        )

process.options = cms.untracked.PSet(
        wantSummary = cms.untracked.bool(True),
        fileMode = cms.untracked.string('NOMERGE'),
        SkipEvent = cms.untracked.vstring('ProductNotFound')
        )

process.TimerService = cms.Service("TimerService",
        useCPUtime = cms.untracked.bool(True)
        )

#Ele27 Trigger Filter
process.hltPickTriggered = cms.EDFilter('TriggerResultsFilter',
        hltResults              = cms.InputTag('TriggerResults','','HLT'),   # HLT results   - set to empty to ignore HLT
        l1tResults              = cms.InputTag(''),                 # L1 GT results - set to empty to ignore L1
        l1tIgnoreMask           = cms.bool(False),                  # use L1 mask
        l1techIgnorePrescales   = cms.bool(False),                  # read L1 technical bits from PSB#9, bypassing the prescales
        daqPartitions           = cms.uint32(0x01),                 # used by the definition of the L1 mask
        throw                   = cms.bool(False),                  # throw exception on unknown trigger names
        triggerConditions       = cms.vstring('HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v*')
        )

process.load("ZShape.ZFromData.ZFromDataElectrons_cfi")

# Used to set which triggers cound for HLT-GSF
process.theHLTGsf.hltTag = cms.untracked.VInputTag(
        cms.InputTag("HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1","","HLT"),
        cms.InputTag("HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v2","","HLT"),
        cms.InputTag("HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v3","","HLT"),
        cms.InputTag("HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v4","","HLT")
        ) #remove the ones you don't want

# Alex's tuple maker
process.tuplemaker = cms.EDAnalyzer('MakeZEffTree',
        quiet = cms.untracked.bool(True),
        TagProbeProducer = cms.untracked.InputTag('tpMapWP80AndHFSC'),
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

# Bryna's simple HFSC Filter to prevent PAT from running if the event is
# uninteresting
process.HFSCfilter = cms.EDFilter('HFSuperClusterFilterVL')

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
        process.hltPickTriggered
        * process.HFSCfilter
        * process.kt6PFJets
        * process.patElectronIDs
        * process.hfRecoEcalCandidate
        * process.lepton_cands
        * process.tuplemaker
        )
