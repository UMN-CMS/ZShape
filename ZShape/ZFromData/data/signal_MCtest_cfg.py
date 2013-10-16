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

#process.GlobalTag.globaltag = cms.string('IDEAL_V9::All')
#process.GlobalTag.globaltag = cms.string('MC_31X_V3::All')
#process.GlobalTag.globaltag = 'GR10_P_V10::All'
process.GlobalTag.globaltag = 'GR_R_44_V11::All'
#process.GlobalTag.globaltag = 'GR_R_42_V12::All'



process.source = cms.Source("PoolSource",
    #inputCommands=cms.untracked.vstring(
    #              'keep *',
    #              'drop *_*_*_reRECO',
    #               ),	
    fileNames = cms.untracked.vstring('file:/local/cms/user/gude/zshape/skimReReco/skimReReco_001.root ')                      
)

#process.load("ZShape.ZFromData.GoodDataLumis_160431_163869_cfi")

#from ZShape.ZFromData.GoodDataLumis_160431_163869_cfi import *
## #from ZShape.ZFromData.GoodLumis_July16ReReco_cfi import *
## #from ZShape.ZFromData.GoodLumis_June14thReReco_cfi import *

## process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange(
##     GoodLumis1
## ##    +GoodLumis2+
## ##    GoodLumis3+
## ##    GoodLumis4+
## ##    GoodLumis5+
## ##    GoodLumis6
## ##
##     )

#print(process.source.lumisTo-PT20Process)

process.maxEvents = cms.untracked.PSet(
   input = cms.untracked.int32(-1)
)

process.TFileService = cms.Service("TFileService",
     fileName = cms.string('KevTest.root')
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True),
    SkipEvent = cms.untracked.vstring('ProductNotFound'),
    fileMode = cms.untracked.string('NOMERGE')
)

process.TimerService = cms.Service("TimerService",
    useCPUtime = cms.untracked.bool(True)
)

process.load("ZShape.ZFromData.ZFromDataElectronsMC_cfi") 

#process.theHLT.hltTag = cms.untracked.InputTag("HLT_Photon15_L1R","","HLT")
#process.theHLTGsf.hltTag = cms.untracked.InputTag("HLT_Photon15_L1R","","HLT")
#process.theHLT.hltTag = cms.untracked.InputTag("HLT_Photon15_Cleaned_L1R","","HLT")
#process.theHLTGsf.hltTag = cms.untracked.InputTag("HLT_Photon15_Cleaned_L1R","","HLT")
#process.theHLT.hltTag = cms.untracked.InputTag("HLT_Ele15_SW_L1R","","HLT")
#process.theHLTGsf.hltTag = cms.untracked.InputTag("HLT_Ele15_SW_L1R","","HLT")
#process.theHLT.hltTag = cms.untracked.InputTag("HLT_Ele15_SW_CaloEleId_L1R","","HLT")
#process.theHLTGsf.hltTag = cms.untracked.InputTag("HLT_Ele15_SW_CaloEleId_L1R","","HLT")


process.ZFromData = cms.EDAnalyzer("ZFromData",
    quiet = cms.untracked.bool(False),
    src = cms.untracked.InputTag('generator'),
    outHistogramsFile = cms.untracked.string('base_Jan23rd_1.root'),
    ExtraFromDataHistos = cms.untracked.bool(True),
    doMC = cms.untracked.bool(False),                               
    WeightsFile = cms.untracked.string('none'),                               

	dRMatchCut = cms.untracked.double(0.3),
	dPtMatchCut = cms.untracked.double(0.6),

	Effs = cms.untracked.VPSet(
	  cms.PSet(
	         name = cms.untracked.FileInPath('ZShape/EffAcc/data/Supercluster-Eta.txt'),
	         effFile = cms.untracked.string('Supercluster-Eta.txt')
	#  ),
	#  cms.PSet(
	#         name = cms.untracked.string('GsfTrack-EtaDet'),
	#         effFile = cms.untracked.string('GsfTrack-EtaDet.txt')
	#  ),
	#  cms.PSet(
	#         name = cms.untracked.string('Iso-Pt'),
	#         effFile = cms.untracked.string('Iso-Pt.txt')
	#  ),
	#  cms.PSet(
	#         name = cms.untracked.string('ElectronId-EtaDet'),
	#         effFile = cms.untracked.string('ElectronId-EtaDet.txt')
	#  ),
	#  cms.PSet(
	#         name = cms.untracked.string('HLT-EtaDet'),
	#         effFile = cms.untracked.string('HLT-EtaDet.txt')
	  )),
	  
	#TagProbeProducer = cms.untracked.InputTag('tpMapGsfElectrons'),
	#TagProbeProducer = cms.untracked.InputTag('tpMapSuperClusters'),
	#TagProbeProducer = cms.untracked.InputTag('tpMapGsfAndHF'),
        TagProbeProducer = cms.untracked.InputTag('tpMapGsfAndHF'),
	GsfProducer = cms.untracked.InputTag('theGsfElectrons'),
                                   
        CutNames          = cms.untracked.vstring("Supercluster-Eta", "GsfTrack-EtaDet",#1
                                                  "Iso-Pt",        "ElectronId-EtaDet",#2
                                                  "HLT-EtaDet", "HFElectronId-EtaDet",#3
                                                  "HFSuperCluster-Et","HFTightElectronId-EtaDet",#4
                                                  "EID95","ISO95",#5
                                                  "EID90","ISO90",#6
                                                  "EID85","ISO85",#7
                                                  "EID80","ISO80",#8
                                                  "EID70","ISO70",#9
                                                  "EID60","ISO60",#10
                                                  "HLT-GSF","ISO80Only",#11
                                                  "ISO80Conv","EID80Only",#12
                                                  "EID80Conv","WP95",#13
                                                  "WP90","WP85",#14
                                                  "WP80","NTLooseElectronId-EtaDet",#15
                                                  "NTTightElectronId-EtaDet" ),#16
	allProbeCandTags  = cms.untracked.VInputTag(cms.InputTag("theSuperClusters"),cms.InputTag("theSuperClusters"),#1
                                                    cms.InputTag("theGsfElectrons"),cms.InputTag("theIsolation"),#2
                                                    cms.InputTag("theId"),cms.InputTag("theHFSuperClusters"),#3
                                                    cms.InputTag("theHFSuperClusters"),cms.InputTag("theHFSuperClusters"),#4
                                                    cms.InputTag("theGsfElectrons"),cms.InputTag("theGsfElectrons"),#5
                                                    cms.InputTag("theGsfElectrons"),cms.InputTag("theGsfElectrons"),#6
                                                    cms.InputTag("theGsfElectrons"),cms.InputTag("theGsfElectrons"),#7
                                                    cms.InputTag("theGsfElectrons"),cms.InputTag("theGsfElectrons"),#8
                                                    cms.InputTag("theGsfElectrons"),cms.InputTag("theGsfElectrons"),#9
                                                    cms.InputTag("theGsfElectrons"),cms.InputTag("theGsfElectrons"),#10
                                                    cms.InputTag("theGsfElectrons"),cms.InputTag("theGsfElectrons"),#11
                                                    cms.InputTag("theGsfElectrons"),cms.InputTag("theGsfElectrons"),#12
                                                    cms.InputTag("theGsfElectrons"),cms.InputTag("theGsfElectrons"),#13
                                                    cms.InputTag("theGsfElectrons"),cms.InputTag("theGsfElectrons"),#14
                                                    cms.InputTag("ElectronID80Only"),cms.InputTag("NTElecLoose"),#15
                                                    cms.InputTag("NTElecLoose")),#6
	passProbeCandTags = cms.untracked.VInputTag(cms.InputTag("theSuperClusters"),cms.InputTag("theGsfElectrons"),#1
                                                    cms.InputTag("theIsolation"),cms.InputTag("theId"),#2
                                                    cms.InputTag("theHLT"), cms.InputTag("HFElectronID"),#3
                                                    cms.InputTag("theHFSuperClusters"), cms.InputTag("HFElectronIDTight"),#4
                                                    cms.InputTag("ElectronID95"), cms.InputTag("Iso95"),#5
                                                    cms.InputTag("ElectronID90"), cms.InputTag("Iso90"),#6
                                                    cms.InputTag("ElectronID85"), cms.InputTag("Iso85"),#7
                                                    cms.InputTag("ElectronID80"), cms.InputTag("Iso80"),#8
                                                    cms.InputTag("ElectronID70"), cms.InputTag("Iso70"),#9
                                                    cms.InputTag("ElectronID60"), cms.InputTag("Iso60"),#10
                                                    cms.InputTag("theHLTGsf"), cms.InputTag("Iso80Only"),#11
                                                    cms.InputTag("Iso80WConv"), cms.InputTag("ElectronID80Only"),#12
                                                    cms.InputTag("ElectronID80WConv"), cms.InputTag("ElectronID95"),#13
                                                    cms.InputTag("ElectronID90"),cms.InputTag("ElectronID85"),#14
                                                    cms.InputTag("WorkingPoint80"),cms.InputTag("NTElecLoose"),#15
                                                    cms.InputTag("NTElecTight")),#16
        ExactMatch        = cms.untracked.vint32(1,1,#1
                                                 1,1,#2
                                                 1,0,#3
                                                 0,0,#4
                                                 1,1,#5
                                                 1,1,#6
                                                 1,1,#7
                                                 1,1,#8
                                                 1,1,#9
                                                 1,1,#10
                                                 1,1,#11
                                                 1,1,#12
                                                 1,1,#13
                                                 1,1,#14
                                                 1,1,#15
                                                 1),#16
	writeHistoBeforeEndJob = cms.untracked.bool(False),

	#Here is where the bulk of everything goes, into the Z definitions
	ZDefs = cms.untracked.VPSet( 
      	 
	  cms.PSet(
            name = cms.untracked.string('AllInRange'),
            Z = cms.untracked.vstring('m(60,120)'),
            e1 = cms.untracked.vstring('PT0'),
            e2 = cms.untracked.vstring('PT0')
          ),


    cms.PSet( 
            name = cms.untracked.string('EB-EB'),
            e1 = cms.untracked.vstring("ACC(EB)","PT20","Supercluster-Eta","PT20",
                                       "GsfTrack-EtaDet","EID80Only","WP80"),
            e2 = cms.untracked.vstring("ACC(EB)","PT20","Supercluster-Eta","PT20",
                                       "GsfTrack-EtaDet","EID80Only","WP80"),		
            Z = cms.untracked.vstring('m(60,120)'),
            ptorder = cms.untracked.bool (False)
	),


    cms.PSet( 
            name = cms.untracked.string('EE-EB'),
            e1 = cms.untracked.vstring("ACC(EE+TRK)","PT20","Supercluster-Eta","PT20",
                                       "GsfTrack-EtaDet","EID80Only","WP80"),
            e2 = cms.untracked.vstring("ACC(EB)","PT20","Supercluster-Eta","PT20",
                                           "GsfTrack-EtaDet","EID80Only","WP80"),		
            Z = cms.untracked.vstring('m(60,120)'),
            ptorder = cms.untracked.bool (False)
	),


cms.PSet( 
            name = cms.untracked.string('EE-EB0'),
            e1 = cms.untracked.vstring("ACC(EE+TRK)","PT20","Supercluster-Eta","PT20",
                                       "GsfTrack-EtaDet","EID80Only","WP80"),
           
            e2 = cms.untracked.vstring("ACC(EB)","PT20","Supercluster-Eta","PT20",
                                           "GsfTrack-EtaDet","PT20","PT20"),		
            Z = cms.untracked.vstring('m(60,120)'),
            ptorder = cms.untracked.bool (True)
	),


cms.PSet( 
            name = cms.untracked.string('EE0-EB'),
            e1 = cms.untracked.vstring("ACC(EE+TRK)","PT20","Supercluster-Eta","PT20",
                                       "GsfTrack-EtaDet","PT20","PT20"),
           
            e2 = cms.untracked.vstring("ACC(EB)","PT20","Supercluster-Eta","PT20",
                                           "GsfTrack-EtaDet","EID80Only","WP80"),		
            Z = cms.untracked.vstring('m(60,120)'),
            ptorder = cms.untracked.bool (True)
	),


    cms.PSet( 
            name = cms.untracked.string('EE-HF'),
            e1 = cms.untracked.vstring("ACC(EE)","PT20","Supercluster-Eta","PT20",
                                       "GsfTrack-EtaDet","EID80Only","WP80","PT20",),
            e2 = cms.untracked.vstring("ACC(HF)","PT20","HFSuperCluster-Et","PT20",
                                       "PT20","PT20","PT20","HFElectronId-EtaDet"),		
            Z = cms.untracked.vstring('m(60,120)'),
            ptorder = cms.untracked.bool (False)
            ))
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

##process.p1 = cms.Path(process.patElectronIDs+process.hfRecoEcalCandidateMC+process.lepton_cands+process.ZFromData)
process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")

process.p1 = cms.Path(process.kt6PFJets+process.patElectronIDs+process.hfEMClusters+process.hfRecoEcalCandidateMC+process.lepton_cands+process.ZFromData)	 
