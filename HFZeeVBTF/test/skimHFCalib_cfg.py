import FWCore.ParameterSet.Config as cms

process = cms.Process("CALSKIM")

process.load('FWCore/MessageService/MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound'),
    wantSummary = cms.untracked.bool(True)
)


# source
process.source = cms.Source("PoolSource",      
    fileNames=cms.untracked.vstring(     )
                  
)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )


## Load additional processes
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
## global tags:
process.GlobalTag.globaltag = cms.string('GR_R_50_V13::All')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.Services_cff')


################################################################################################
###    P r e p a r a t i o n      o f    t h e    P A T    O b j e c t s   f r o m    A O D  ###
################################################################################################

## pat sequences to be loaded:
#process.load("PhysicsTools.PFCandProducer.PF2PAT_cff")
process.load("PhysicsTools.PatAlgos.patSequences_cff")
#process.load("PhysicsTools.PatAlgos.triggerLayer1.triggerProducer_cff")
##
#
## %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## MET creation     <=== WARNING: YOU MAY WANT TO MODIFY THIS PART OF THE CODE       %%%%%%%%%%%%%
##                                specify the names of the MET collections that you need here %%%%
##                                                                                             #%%
## if you don't specify anything the default MET is the raw Calo MET                           #%%
## if you don't specify anything the default MET is the raw Calo MET                           #%%
process.caloMET = process.patMETs.clone(                                                       #%%
        metSource = cms.InputTag("met","","RECO"),
            addTrigMatch = cms.bool(False),
            addMuonCorrections = cms.bool(False),
            addGenMET = cms.bool(False),
        )
process.tcMET = process.patMETs.clone(                                                         #%%
        metSource = cms.InputTag("tcMet","","RECO"),
            addTrigMatch = cms.bool(False),
            addMuonCorrections = cms.bool(False),
            addGenMET = cms.bool(False),
        )
process.pfMET = process.patMETs.clone(                                                         #%%
        metSource = cms.InputTag("pfMet","","RECO"),
            addTrigMatch = cms.bool(False),
            addMuonCorrections = cms.bool(False),
            addGenMET = cms.bool(False),
        )
## specify here what you want to have on the plots! <===== MET THAT YOU WANT ON THE PLOTS  %%%%%%%
myMetCollection   = 'caloMET'
myPfMetCollection =   'pfMET'
myTcMetCollection =   'tcMET'

## specify here what you want to have on the plots! <===== MET THAT YOU WANT ON THE PLOTS  %%%%%%%
## myDesiredMetCollection = 'layer1RawCaloMETs'
## modify the sequence of the MET creation:                                                    #%%
process.makePatMETs = cms.Sequence(process.caloMET*process.tcMET*process.pfMET)

## GF changed here: more than one pat done here

## %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## modify the final pat sequence: keep only electrons + METS (muons are needed for met corrections)
process.load("RecoEgamma.EgammaIsolationAlgos.egammaIsolationSequence_cff")
#process.patElectronIsolation = cms.Sequence(process.egammaIsolationSequence)

process.patElectrons.isoDeposits = cms.PSet()
process.patElectrons.userIsolation = cms.PSet()
process.patElectrons.addElectronID = cms.bool(True)
process.patElectrons.electronIDSources = cms.PSet(
    simpleEleId95relIso= cms.InputTag("simpleEleId95relIso"),
    simpleEleId90relIso= cms.InputTag("simpleEleId90relIso"),
    simpleEleId85relIso= cms.InputTag("simpleEleId85relIso"),
    simpleEleId80relIso= cms.InputTag("simpleEleId80relIso"),
    simpleEleId70relIso= cms.InputTag("simpleEleId70relIso"),
    simpleEleId60relIso= cms.InputTag("simpleEleId60relIso"),
    simpleEleId95cIso= cms.InputTag("simpleEleId95cIso"),
    simpleEleId90cIso= cms.InputTag("simpleEleId90cIso"),
    simpleEleId85cIso= cms.InputTag("simpleEleId85cIso"),
    simpleEleId80cIso= cms.InputTag("simpleEleId80cIso"),
    simpleEleId70cIso= cms.InputTag("simpleEleId70cIso"),
    simpleEleId60cIso= cms.InputTag("simpleEleId60cIso"),    
    )
##
process.patElectrons.addGenMatch = cms.bool(False)
process.patElectrons.embedGenMatch = cms.bool(False)
process.patElectrons.usePV = cms.bool(False)
##
process.load("ElectroWeakAnalysis.WENu.simpleEleIdSequence_cff")
process.patElectronIDs = cms.Sequence(process.simpleEleIdSequence)
process.makePatElectrons = cms.Sequence(process.patElectronIDs*process.patElectrons)
# process.makePatMuons may be needed depending on how you calculate the MET
process.makePatCandidates = cms.Sequence(process.makePatElectrons+process.makePatMETs)
process.patDefaultSequence = cms.Sequence(process.makePatCandidates)


####################################################################################

# to access values of EldId cuts as defined by the EWK group
import ElectroWeakAnalysis.WENu.simpleCutBasedElectronIDSpring10_cfi

# EWK analyzer: different Z definitions with one ECAL electron and one HF electron
# ---> this is the instance to run AFTER the Wenu EWK filter


import ZShape.HFZeeVBTF.hfzeevbtf_cfi

process.hfzeeForCalib = ZShape.HFZeeVBTF.hfzeevbtf_cfi.hfzeevbtf.clone()
process.hfzeeForCalib.Zmass=cms.vdouble(70,120)
process.hfzeeForCalib.skipTrigger = cms.bool(True)
process.hfzeeForCalib.FILTERid = 'simpleEleId80cIso'

process.hfzeeBefCuts = ZShape.HFZeeVBTF.hfzeevbtf_cfi.hfzeevbtf.clone()
process.hfzeeBefCuts.Zmass=cms.vdouble(70,120)
process.hfzeeBefCuts.myName=cms.string('befCuts')
process.hfzeeBefCuts.skipTrigger = cms.bool(True)                             

# THIS IS PROD
process.TFileService = cms.Service("TFileService",
       fileName = cms.string(""),
)

process.load("RecoEgamma.EgammaHFProducers.hfRecoEcalCandidate_cfi")
process.hfRecoEcalCandidate.intercept2DCut=0.4
process.hfRecoEcalCandidate.e9e25Cut      =0.96
# 0.94 is the same as default in the HF cluster producer

process.zCOutputModule = cms.OutputModule( "PoolOutputModule",
                                           fileName = cms.untracked.string(""),
                                           maxSize = cms.untracked.int32(2000000),
                                           SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('zCalibPath'),
                                                                             )
                                           )


process.outpath = cms.EndPath(process.zCOutputModule)

process.zCalibPath = cms.Path(
    process.patDefaultSequence *
    process.hfRecoEcalCandidate *
    process.hfzeeBefCuts *
    process.hfzeeForCalib 
    )

