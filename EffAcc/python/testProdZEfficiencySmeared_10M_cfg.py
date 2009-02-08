import FWCore.ParameterSet.Config as cms

process = cms.Process("Zefficiency")
process.TimerService = cms.Service("TimerService")

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000000)
    )

process.dumpEv = cms.EDAnalyzer("EventContentAnalyzer")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    'file:/data/whybee0c/user/jmmans/Zee_shape_10TeV_GEN/Zee_shape_10TeV_GEN_1.root',
    'file:/data/whybee0c/user/jmmans/Zee_shape_10TeV_GEN/Zee_shape_10TeV_GEN_2.root',
    'file:/data/whybee0c/user/jmmans/Zee_shape_10TeV_GEN/Zee_shape_10TeV_GEN_3.root',
    'file:/data/whybee0c/user/jmmans/Zee_shape_10TeV_GEN/Zee_shape_10TeV_GEN_4.root',
    'file:/data/whybee0c/user/jmmans/Zee_shape_10TeV_GEN/Zee_shape_10TeV_GEN_5.root',
    'file:/data/whybee0c/user/jmmans/Zee_shape_10TeV_GEN/Zee_shape_10TeV_GEN_6.root',
    'file:/data/whybee0c/user/jmmans/Zee_shape_10TeV_GEN/Zee_shape_10TeV_GEN_7.root',
    'file:/data/whybee0c/user/jmmans/Zee_shape_10TeV_GEN/Zee_shape_10TeV_GEN_8.root',
    'file:/data/whybee0c/user/jmmans/Zee_shape_10TeV_GEN/Zee_shape_10TeV_GEN_9.root',
    'file:/data/whybee0c/user/jmmans/Zee_shape_10TeV_GEN/Zee_shape_10TeV_GEN_10.root'

#     'file:/data/franzoni/cmssw/ph/januaryBinMigration_CMSSW_2_2_3/src/ZShape/EffAcc/python/myfile_pythia_1M.root'
    )
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('histo_10M_partBUILDINGTTEST.root')
)

process.load("ZShape.EffAcc.SmearedElectronsProducer_cfi")

process.mcEff = cms.EDFilter("ZEfficiencyCalculator",
    Effs = cms.untracked.VPSet(cms.PSet(
        effFile = cms.FileInPath('ZShape/EffAcc/data/HLT-EtaDet.txt'),
        name = cms.untracked.string('HLT-EtaDet')
    ), 
        cms.PSet(
            effFile = cms.FileInPath('ZShape/EffAcc/data/ElectronId-EtaDet.txt'),
            name = cms.untracked.string('ElectronId-EtaDet')
        ), 
        cms.PSet(
            effFile = cms.FileInPath('ZShape/EffAcc/data/Iso-Pt.txt'),
            name = cms.untracked.string('Iso-Pt')
        ), 
        cms.PSet(
            effFile = cms.FileInPath('ZShape/EffAcc/data/GsfTrack-EtaDet.txt'),
            name = cms.untracked.string('GsfTrack-EtaDet')
        ), 
        cms.PSet(
            effFile = cms.FileInPath('ZShape/EffAcc/data/Supercluster-Eta.txt'),
            name = cms.untracked.string('Supercluster-Eta')
        ),
        cms.PSet(
            effFile = cms.FileInPath('ZShape/EffAcc/data/HFEId-EtaDet.txt'), 
            name = cms.untracked.string('HFElectronId-EtaDet')
        )

                               ),
    writeHistoBeforeEndJob = cms.untracked.bool(False),
    zsrc = cms.untracked.InputTag("SmearedElectronsProducer","ZEventParticles"),
    zElectronsCollection = cms.untracked.InputTag("SmearedElectronsProducer","ZEventParticles"),
    zTreeLevelElectronsCollection = cms.untracked.InputTag("ZIntoElectronsEventProducer","ZEventEle3"), quiet = cms.untracked.bool(True),
    zElectronsCone = cms.double(0.00),
    ZDefs = cms.untracked.VPSet(cms.PSet(
        name = cms.untracked.string('Golden-EB-EB'),
        Z = cms.untracked.vstring(),
        e1 = cms.untracked.vstring(
            'ACC(EB)', 
            'PT10', 
            'Supercluster-Eta', 
            'PT20', 
            'GsfTrack-EtaDet', 
            'Iso-Pt', 
            'ElectronId-EtaDet', 
            'HLT-EtaDet'),
        e2 = cms.untracked.vstring('ACC(EB)', 
            'PT10', 
            'Supercluster-Eta', 
            'PT20', 
            'GsfTrack-EtaDet', 
            'Iso-Pt', 
            'ElectronId-EtaDet') #, 
            #'HLT-EtaDet')
    ), 
        cms.PSet(
            name = cms.untracked.string('Tight-EB-Loose-ECAL'),
            Z = cms.untracked.vstring(),
            e1 = cms.untracked.vstring('ACC(EB)', 
                'PT10', 
                'Supercluster-Eta', 
                'PT20', 
                'GsfTrack-EtaDet', 
                'Iso-Pt', 
                'ElectronId-EtaDet', 
                'HLT-EtaDet'),
            e2 = cms.untracked.vstring('ACC(ECAL)', 
                'PT10', 
                'Supercluster-Eta', 
                'PT20', 
                'GsfTrack-EtaDet', 
                'Iso-Pt', 
                'ElectronId-EtaDet')
        ), 
        cms.PSet(
            name = cms.untracked.string('Tight-ECAL-Loose-ECAL'),
            Z = cms.untracked.vstring(),
            e1 = cms.untracked.vstring('ACC(ECAL)', 
                'PT10', 
                'Supercluster-Eta', 
                'PT20', 
                'GsfTrack-EtaDet', 
                'Iso-Pt', 
                'ElectronId-EtaDet', 
                'HLT-EtaDet'),
            e2 = cms.untracked.vstring('ACC(ECAL)', 
                'PT10', 
                'Supercluster-Eta', 
                'PT20', 
                'GsfTrack-EtaDet', 
                'Iso-Pt', 
                'ElectronId-EtaDet')
        ), 
        cms.PSet(
            name = cms.untracked.string('Tight-ECAL-HF'),
            Z = cms.untracked.vstring(),
            e1 = cms.untracked.vstring('ACC(ECAL)', 
                'PT10', 
                'Supercluster-Eta', 
                'PT20', 
                'GsfTrack-EtaDet', 
                'Iso-Pt', 
                'ElectronId-EtaDet', 
                'HLT-EtaDet'),
            e2 = cms.untracked.vstring('ACC(HF)', 
                'PT10', 
                'PT20',
                'HFElectronId-EtaDet')
        ), 
        cms.PSet(
            name = cms.untracked.string('Maximal'),
            Z = cms.untracked.vstring(),
            e1 = cms.untracked.vstring('ACC(ECAL)', 
                'PT10', 
                'Supercluster-Eta', 
                'PT20', 
                'GsfTrack-Eta', 
                'Iso-Pt', 
                'ElectronId-Eta', 
                'HLT-Eta'),
            e2 = cms.untracked.vstring('ACC(ANY)', 
                'PT10')
        ))
)

process.p = cms.Path(process.SmearedElectronsProducer
                     + process.mcEff
                     + process.dumpEv
                     )
 
