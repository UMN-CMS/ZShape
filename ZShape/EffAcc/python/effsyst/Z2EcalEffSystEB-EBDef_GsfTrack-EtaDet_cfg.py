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

process.dumpEv = cms.EDAnalyzer("EventContentAnalyzer")

process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                        
    fileNames = cms.untracked.vstring("" )
)


process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')
process.load("Configuration.StandardSequences.Geometry_cff")
process.TFileService = cms.Service("TFileService",
    fileName = cms.string('histo_10M_partBUILDINGTTEST.root')
)

process.load("ZShape.EffAcc.FullSimSmearedElectronProducer_cfi")



process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')


process.mcEff = cms.EDAnalyzer("ZEfficiencyCalculator",
    Effs = cms.untracked.VPSet(
        cms.PSet(
            effFile = cms.FileInPath('ZShape/EffAcc/data/HLT80-PtEta.txt'),
            name = cms.untracked.string('HLT-EtaDet')
        ), 
        cms.PSet(
            effFile = cms.FileInPath('ZShape/EffAcc/data/HLT80-PtEta_unity.txt'),
            name = cms.untracked.string('HLT-GSF')
        ),
        cms.PSet(
            effFile = cms.FileInPath('ZShape/EffAcc/data/ElectronId-Pt.txt'),
            name = cms.untracked.string('ElectronId-EtaDet')
        ), 
        cms.PSet(
            effFile = cms.FileInPath('ZShape/EffAcc/data/Iso-PtEta.txt'),
            name = cms.untracked.string('Iso-Pt')
        ),
        cms.PSet(
            effFile = cms.FileInPath('ZShape/EffAcc/data/ElectronId-Pt.txt'),
            name = cms.untracked.string('EID95')
        ), 
        cms.PSet(
            effFile = cms.FileInPath('ZShape/EffAcc/data/Iso-PtEta.txt'),
            name = cms.untracked.string('ISO95')
        ),
        cms.PSet(
            effFile = cms.FileInPath('ZShape/EffAcc/data/ElectronId80-Pt.txt'),
            name = cms.untracked.string('EID80')
        ), 
        cms.PSet(
            effFile = cms.FileInPath('ZShape/EffAcc/data/Iso80-PtEta.txt'),
            name = cms.untracked.string('ISO80')
        ),
        cms.PSet(
            effFile = cms.FileInPath('ZShape/EffAcc/data/GsfTrack-PtEta_unity.txt'),
   # effFile = cms.FileInPath('ZShape/EffAcc/data/GsfTrack-PtEta.txt'),         
            name = cms.untracked.string('GsfTrack-EtaDet')
        ), 
        cms.PSet(
            effFile = cms.FileInPath('ZShape/EffAcc/data/Supercluster-Eta_unity.txt'),
            # effFile = cms.FileInPath('ZShape/EffAcc/data/Supercluster-Eta.txt'),
            name = cms.untracked.string('Supercluster-Eta')
        ),
        cms.PSet(
            #effFile = cms.FileInPath('ZShape/EffAcc/data/HFEId-PtEta.txt'),
            effFile = cms.FileInPath('ZShape/EffAcc/data/HFEID-HFTID_phistar_etadet.txt'),
            name = cms.untracked.string('HFElectronId-EtaDet')
        ),
         cms.PSet(
            #effFile = cms.FileInPath('ZShape/EffAcc/data/HFEIdT-Pt.txt'),
            effFile = cms.FileInPath('ZShape/EffAcc/data/HFEID-HFTID_phistar_etadet.txt'),
            name = cms.untracked.string('HFTightElectronId-EtaDet')
        ),
        cms.PSet(
            effFile = cms.FileInPath('ZShape/EffAcc/data/SuperClusEff_HF_Et_unity.txt'),
            #effFile = cms.FileInPath('ZShape/EffAcc/data/HFSC-Et_910.txt'), 

            name = cms.untracked.string('HFSuperCluster-Et')
        ),
        cms.PSet(
            effFile = cms.FileInPath('ZShape/EffAcc/data/NTEId-EtaDet.txt'),
            name = cms.untracked.string('NTLooseElectronId-EtaDet')
        ),
        cms.PSet(
            effFile = cms.FileInPath('ZShape/EffAcc/data/NTEIdT-EtaDet.txt'),
            name = cms.untracked.string('NTTightElectronId-EtaDet')
        ),
        cms.PSet(
            effFile = cms.FileInPath('ZShape/EffAcc/data/WP95-PtEta.txt'),
            name = cms.untracked.string('WP95')
        ),
        cms.PSet(
            effFile = cms.FileInPath('ZShape/EffAcc/data/WP90-PtEta.txt'),
            name = cms.untracked.string('WP90')
        ),
        cms.PSet(
            effFile = cms.FileInPath('ZShape/EffAcc/data/WP85-PtEta.txt'),
            name = cms.untracked.string('WP85')
        ),

        cms.PSet(
            effFile = cms.FileInPath('ZShape/EffAcc/data/HFTID-PtEta_phistar.txt'),
            name = cms.untracked.string('HFTID')
        ),
        
        cms.PSet(
           #effFile = cms.FileInPath('ZShape/EffAcc/data/WP80-PtEta.txt'),
           #effFile = cms.FileInPath('ZShape/EffAcc/data/fitEffAcc_ee_eb_prelim_corrected_in_pt.txt'),
           effFile = cms.FileInPath('ZShape/EffAcc/data/WP80_data_eff_fits.txt'),
           # effFile = cms.FileInPath('ZShape/EffAcc/data/HFEID-HFTID_phistar_etadet.txt'),
            name = cms.untracked.string('WP80')
        )                                    
    ),
    writeHistoBeforeEndJob = cms.untracked.bool(False),
     zsrc = cms.untracked.InputTag("FullSimSmearedElectronsProducer","ZEventParticles"),
    zElectronsCollection = cms.untracked.InputTag("FullSimSmearedElectronsProducer","ZEventParticles"),
    zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3"),
    quiet = cms.untracked.bool(True),
    zElectronsCone = cms.double(0.00),
    doWeight = cms.untracked.bool(True),   
    acceptanceMassWindow = cms.vdouble(60.0,120.0),
    esys_zdef = cms.untracked.string('EB-EB'),
    esys_eff  = cms.untracked.string('GsfTrack-EtaDet'),
    ZDefs = cms.untracked.VPSet(

    cms.PSet(
            name = cms.untracked.string('AllInRange'),
            Z = cms.untracked.vstring('m(60,120)'),
            e1 = cms.untracked.vstring('PT0'),
            e2 = cms.untracked.vstring('PT0')
        ),
    cms.PSet(
            name = cms.untracked.string('AllIn'),
            Z = cms.untracked.vstring('m(35,10000)'),
            e1 = cms.untracked.vstring('PT0'),
            e2 = cms.untracked.vstring('PT0')
        ),
 
    cms.PSet( 
            name = cms.untracked.string('EB-EB'),
            e1 = cms.untracked.vstring("ACC(EB)","GPT20","Supercluster-Eta","PT20",
                                       "GsfTrack-EtaDet","PT20","WP80", "HLT-GSF"),
            e2 = cms.untracked.vstring("ACC(EB)","GPT20","Supercluster-Eta","PT20",
                                       "GsfTrack-EtaDet","PT20","WP80", "HLT-GSF"),		
            Z = cms.untracked.vstring('m(60,120)'),
            ptorder = cms.untracked.bool (False)
	),

    cms.PSet( 
            name = cms.untracked.string('EE-EB'),
            e1 = cms.untracked.vstring("ACC(EE+TRK)","GPT20","Supercluster-Eta","PT20",
                                       "GsfTrack-EtaDet","PT20","WP80", "HLT-GSF"),
            e2 = cms.untracked.vstring("ACC(EB)","GPT20","Supercluster-Eta","PT20",
                                           "GsfTrack-EtaDet","PT20","WP80", "HLT-GSF"),		
            Z = cms.untracked.vstring('m(60,120)'),
            ptorder = cms.untracked.bool (False)
	),


## cms.PSet( 
##             name = cms.untracked.string('EE-EE'),
##             e1 = cms.untracked.vstring("ACC(EE+TRK)","GPT20","Supercluster-Eta","PT20",
##                                        "GsfTrack-EtaDet","PT20","WP80", "HLT-GSF"),
##             e2 = cms.untracked.vstring("ACC(EE+TRK)","GPT20","Supercluster-Eta","PT20",
##                                            "GsfTrack-EtaDet","PT20","WP80", "HLT-GSF"),		
##             Z = cms.untracked.vstring('m(60,120)'),
##             ptorder = cms.untracked.bool (False)
## 	),
    cms.PSet( 
            name = cms.untracked.string('EE-HF'),
            e1 = cms.untracked.vstring("ACC(EE+TRK)","GPT20","Supercluster-Eta","PT20",
                                       "GsfTrack-EtaDet","PT20","WP80", "HLT-GSF"),
            e2 = cms.untracked.vstring("ACC(HF)","GPT20","HFSuperCluster-Et","PT20",
                                       "HFElectronId-EtaDet","PT20","PT20","PT20"),		
            Z = cms.untracked.vstring('m(60,120)'),
            ptorder = cms.untracked.bool (False)
	),


## cms.PSet( 
##             name = cms.untracked.string('EB-HF'),
##             e1 = cms.untracked.vstring("ACC(EB)","GPT20","Supercluster-Eta","PT20",
##                                        "GsfTrack-EtaDet","PT20","WP80", "HLT-GSF"),
##             e2 = cms.untracked.vstring("ACC(HF)","GPT20","HFSuperCluster-Et","PT20",
##                                        "HFElectronId-EtaDet","PT20","PT20","PT20"),		
##             Z = cms.untracked.vstring('m(60,120)'),
##             ptorder = cms.untracked.bool (False)
## 	),






    cms.PSet(
            name = cms.untracked.string('Maximal'),
            Z = cms.untracked.vstring('m(60,120)'),
            e1 = cms.untracked.vstring('ACC(ECAL+TRK)', 
                'GPT20', 
                'Supercluster-Eta', 
                'PT20', 
                'GsfTrack-Eta', 
                'Iso-Pt', 
                'ElectronId-Eta', 
                'HLT-Eta'),
            e2 = cms.untracked.vstring('ACC(ANY)', 
                'GPT20')
        ))
)

process.mcEff.zsrc = cms.untracked.InputTag("FullSimSmearedElectronsProducer","ZEventParticles")
process.mcEff.zElectronsCollection = cms.untracked.InputTag("FullSimSmearedElectronsProducer","ZEventParticles")
process.mcEff.zTreeLevelElectronsCollection = cms.untracked.InputTag("f2s","ZEventEle3")

process.f2s = cms.EDProducer("ZFullSim2Event",
                             hfRecoTag = cms.untracked.InputTag("hfRecoEcalCandidateMC")
                             )
process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")
process.hfRecoEcalCandidateMC.intercept2DCut = cms.double(-99)
process.hfRecoEcalCandidateMC.intercept2DSlope = cms.double(-99)
process.hfRecoEcalCandidateMC.e9e25Cut = cms.double(0)
process.p = cms.Path(process.hfEMClusters+process.hfRecoEcalCandidateMC+process.f2s+process.FullSimSmearedElectronsProducer+process.mcEff)

