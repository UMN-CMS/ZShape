import FWCore.ParameterSet.Config as cms

##                      _              _       
##   ___ ___  _ __  ___| |_ __ _ _ __ | |_ ___ 
##  / __/ _ \| '_ \/ __| __/ _` | '_ \| __/ __|
## | (_| (_) | | | \__ \ || (_| | | | | |_\__ \
##  \___\___/|_| |_|___/\__\__,_|_| |_|\__|___/
##                                              
########################
MC_flag = True
GLOBAL_TAG = 'START39_V8::All'
HLTPath = "HLT_Ele17_SW_TightEleId_L1R"
OUTPUT_FILE_NAME = "testNewWrite.root" 
#HLTPath = "HLT_Ele15_SW_CaloEleId_L1R"
#HLTPath = "HLT_Ele15_SW_L1R"
#HLTPath = "HLT_Ele15_LW_L1R"
#HLTPath = "HLT_Photon15_Cleaned_L1R"

#RECO_NAME = "reRECO"
RECO_NAME = "RECO"

#myHLT = "HLT"
myHLT = "REDIGI38X"


ELECTRON_ET_CUT_MIN = 20.0
ELECTRON_COLL = "gsfElectrons"
PATELECTRON_COLL = "patElectrons"
#ELECTRON_CUTS = "ecalDrivenSeed==1 && (abs(superCluster.eta)<2.5) && !(1.4442<abs(superCluster.eta)<1.566) && (ecalEnergy*sin(superClusterPosition.theta)>" + str(ELECTRON_ET_CUT_MIN) + ")"
ELECTRON_CUTS = "(abs(superCluster.eta)<2.5) && !(1.4442<abs(superCluster.eta)<1.566) && (ecalEnergy*sin(superClusterPosition.theta)>" + str(ELECTRON_ET_CUT_MIN) + ")"

####

PHOTON_COLL = "photons"
PHOTON_CUTS = "hadronicOverEm<0.15 && (abs(superCluster.eta)<2.5) && !(1.4442<abs(superCluster.eta)<1.566) && ((isEB && sigmaIetaIeta<0.01) || (isEE && sigmaIetaIeta<0.03)) && (superCluster.energy*sin(superCluster.position.theta)>" + str(ELECTRON_ET_CUT_MIN) + ")"
####

#SUPERCLUSTER_COLL_EB = "hybridSuperClusters"
#SUPERCLUSTER_COLL_EE = "multi5x5SuperClustersWithPreshower"
SUPERCLUSTER_COLL_EB = "correctedHybridSuperClusters"
SUPERCLUSTER_COLL_EE = "correctedMulti5x5SuperClustersWithPreshower"
SUPERCLUSTER_CUTS = "abs(eta)<2.9 && !(1.4442< abs(eta) <1.566) && et>" + str(ELECTRON_ET_CUT_MIN)
SIMPSUPERCLUSTER_CUTS = "abs(eta)<2.9 && !(1.4442< abs(eta) <1.566) && et> 5.0"


JET_COLL = "ak5PFJets"
JET_CUTS = "abs(eta)<2.6 && chargedHadronEnergyFraction>0 && electronEnergyFraction<0.1 && nConstituents>1 && neutralHadronEnergyFraction<0.99 && neutralEmEnergyFraction<0.99" 


#HLTPath = "HLT_Photon15_Cleaned_L1R" #GL1,2
#HLTPath = "HLT_Ele15_SW_L1R" #GL3
#HLTPath = "HLT_Ele15_SW_CaloEleId_L1R" #GL4
#HLTPath = "HLT_Ele17_SW_CaloEleId_L1R" #GL5

###################LOOK FOR THE BELOW!!
#from ZShape.ZFromData.GoodLumis_cfi import *
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange(
#        GoodLumis1+GoodLumis2+
#        GoodLumis3+
#        GoodLumis4+
#        GoodLumis5
#)

process = cms.Process("TagProbe")

##    ___            _           _      
##   |_ _|_ __   ___| |_   _  __| | ___ 
##    | || '_ \ / __| | | | |/ _` |/ _ \
##    | || | | | (__| | |_| | (_| |  __/
##   |___|_| |_|\___|_|\__,_|\__,_|\___|

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Geometry.CaloEventSetup.CaloTopology_cfi")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
#process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.options   = cms.untracked.PSet( fileMode = cms.untracked.string('NOMERGE') )

process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("CondCore.DBCommon.CondDBSetup_cfi")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = GLOBAL_TAG


########################
process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")
process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cff")
process.load("Geometry.CaloEventSetup.CaloGeometry_cff")


process.hfRecoEcalCandidate.Correct = True
#process.hfRecoEcalCandidate.e9e25Cut = 0
process.hfRecoEcalCandidate.intercept2DCut = 0.32

process.hfSuperClusterCandidate = process.hfRecoEcalCandidate.clone()
process.hfSuperClusterCandidate.e9e25Cut = 0
process.hfSuperClusterCandidate.intercept2DCut = -99

process.hfRecoEcalCandidateTight = process.hfRecoEcalCandidate.clone()
process.hfRecoEcalCandidateTight.intercept2DCut = 0.45
#process.hfRecoEcalCandidateTight.e9e25Cut = 0


##   ____             _ ____                           
##  |  _ \ ___   ___ | / ___|  ___  _   _ _ __ ___ ___ 
##  | |_) / _ \ / _ \| \___ \ / _ \| | | | '__/ __/ _ \
##  |  __/ (_) | (_) | |___) | (_) | |_| | | | (_|  __/
##  |_|   \___/ \___/|_|____/ \___/ \__,_|_|  \___\___|
##  

process.source = cms.Source("PoolSource", 
    fileNames = cms.untracked.vstring(''  )
)

#from ZShape.ZFromData.GoodLumis_cfi import *
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange(
#            GoodLumis1+GoodLumis2+
#                    GoodLumis3+
#                    GoodLumis4+
#                    GoodLumis5
#            )


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(400000) )    

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')


#  Photons!!! ################ 
process.goodPhotons = cms.EDFilter("PhotonSelector",
                                   src = cms.InputTag("photons"),
                                   cut = cms.string("hadronicOverEm<0.15"
                                                    " && (superCluster.rawEnergy*sin(superCluster.position.theta)>20.0)"
                                                    " && (abs(superCluster.eta)<2.5) && !(1.4442<abs(superCluster.eta)<1.566)")
                                   )


process.FilteredPhotons = cms.EDFilter("PhotonRefSelector",
         src = cms.InputTag("goodPhotons"),
         cut = cms.string(process.goodPhotons.cut.value() +
                          " && ( (isEB"
                          " && ( (trkSumPtHollowConeDR03 + max(0.,ecalRecHitSumEtConeDR03  - 1.) + hcalTowerSumEtConeDR03)/(superCluster.rawEnergy*sin(superCluster.position.theta)) < 0.15)"
                          " && (sigmaIetaIeta<0.01)"
                          " && (hadronicOverEm<0.15))"
                          " || (isEE"
                          " && ( (trkSumPtHollowConeDR03 + ecalRecHitSumEtConeDR03 + hcalTowerSumEtConeDR03)/(superCluster.rawEnergy*sin(superCluster.position.theta)) <0.1)"
                          " && (sigmaIetaIeta<0.03)"
                          " && (hadronicOverEm<0.07)))"                
                          )
)      

process.NTElecLoose = cms.EDFilter("PhotonSelector",
                                   src = cms.InputTag("photons"),
                                   cut = cms.string("hadronicOverEm<0.07"
                                                    " && (superCluster.rawEnergy*sin(superCluster.position.theta)>20.0)"
                                                    " && (abs(superCluster.eta)>2.5) " # && abs(superCluster.eta)<2.8
                                                    " && (sigmaIetaIeta<0.03)"
                                                    " && (ecalRecHitSumEtConeDR03/(p4.Pt) < 0.06)"
                                                    " && (hcalTowerSumEtConeDR03/(p4.Pt) < 0.05)")
                                   )

process.NTElecTight = cms.EDFilter("PhotonSelector",
                                   src = cms.InputTag("photons"),
                                   cut = cms.string("hadronicOverEm<0.025"
                                                    " && (superCluster.rawEnergy*sin(superCluster.position.theta)>20.0)"
                                                    " && (abs(superCluster.eta)>2.5) " # && abs(superCluster.eta)<2.8
                                                    " && (sigmaIetaIeta<0.03)"
                                                    " && (ecalRecHitSumEtConeDR03/(p4.Pt) < 0.05)"
                                                    " && (hcalTowerSumEtConeDR03/(p4.Pt) < 0.025)")
                                   )


##   ____                         ____ _           _            
##  / ___| _   _ _ __   ___ _ __ / ___| |_   _ ___| |_ ___ _ __ 
##  \___ \| | | | '_ \ / _ \ '__| |   | | | | / __| __/ _ \ '__|
##   ___) | |_| | |_) |  __/ |  | |___| | |_| \__ \ ||  __/ |   
##  |____/ \__,_| .__/ \___|_|   \____|_|\__,_|___/\__\___|_|   
##  

#  SuperClusters  ################
process.superClusters = cms.EDProducer("SuperClusterMerger",
   src = cms.VInputTag(cms.InputTag(SUPERCLUSTER_COLL_EB,"", RECO_NAME ),
                       cms.InputTag(SUPERCLUSTER_COLL_EE,"", RECO_NAME))  
)

process.superClusterCands = cms.EDProducer("ConcreteEcalCandidateProducer",
   src = cms.InputTag("superClusters"),
   particleType = cms.int32(11),
)

#   Get the above SC's Candidates and place a cut on their Et and eta
process.goodSuperClusters = cms.EDFilter("CandViewSelector",
      src = cms.InputTag("superClusterCands"),
      cut = cms.string(SUPERCLUSTER_CUTS), #changed 2.5->2.9
      filter = cms.bool(True)
)

process.goodSimpSuperClusters = cms.EDFilter("CandViewSelector",
      src = cms.InputTag("superClusterCands"),
      cut = cms.string(SIMPSUPERCLUSTER_CUTS), #changed 2.5->2.9
      filter = cms.bool(True)
)
                                         
process.theHFSuperClusters = cms.EDFilter("CandViewSelector",
    src = cms.InputTag("hfSuperClusterCandidate"),
    cut = cms.string('et > 15.0')
)

                                         

#### remove real jets (with high hadronic energy fraction) from SC collection
##### this improves the purity of the probe sample without affecting efficiency

process.JetsToRemoveFromSuperCluster = cms.EDFilter("CaloJetSelector",   
    src = cms.InputTag("ak5CaloJets"),
    cut = cms.string('pt>5 && energyFractionHadronic > 0.15')
)


process.goodSuperClustersClean = cms.EDProducer("CandViewCleaner",
    srcObject = cms.InputTag("goodSuperClusters"),
    module_label = cms.string(''),
    srcObjectsToRemove = cms.VInputTag(cms.InputTag("JetsToRemoveFromSuperCluster")),
    deltaRMin = cms.double(0.1)
)



## process.superClusters = cms.EDFilter("EgammaHLTRecoEcalCandidateProducers",
##    scHybridBarrelProducer =  cms.InputTag("hybridSuperClusters","", RECO_NAME),
##    scIslandEndcapProducer =  cms.InputTag("multi5x5SuperClustersWithPreshower","", RECO_NAME),    
##    recoEcalCandidateCollection = cms.string("")
## )


process.sc_sequence = cms.Sequence( process.goodPhotons *
                                    process.FilteredPhotons *
                                    process.NTElecLoose * 
                                    process.NTElecTight *
                                    process.superClusters *
                                    process.superClusterCands *
                                    process.hfSuperClusterCandidate *                                   
                                    process.theHFSuperClusters *
                                    process.hfRecoEcalCandidateTight *
                                    process.goodSuperClusters *
                                    process.goodSimpSuperClusters *
                                    process.JetsToRemoveFromSuperCluster *
                                    process.goodSuperClustersClean 
                                    )


##    ____      __ _____ _           _                   
##   / ___|___ / _| ____| | ___  ___| |_ _ __ ___  _ __  
##  | |  _/ __| |_|  _| | |/ _ \/ __| __| '__/ _ \| '_ \ 
##  | |_| \__ \  _| |___| |  __/ (__| |_| | | (_) | | | |
##   \____|___/_| |_____|_|\___|\___|\__|_|  \___/|_| |_|
##  

from ElectroWeakAnalysis.ZEE.simpleEleIdSequence_cff import *
from RecoEgamma.EgammaIsolationAlgos.egammaIsolationSequence_cff import *
from PhysicsTools.PatAlgos.patSequences_cff import *
process.load("ElectroWeakAnalysis.ZEE.simpleEleIdSequence_cff")
process.load("RecoEgamma.EgammaIsolationAlgos.egammaIsolationSequence_cff")
process.load("PhysicsTools.PatAlgos.patSequences_cff")



process.patElectronIDs = cms.Sequence(process.simpleEleIdSequence)
process.patElectronIsolation = cms.Sequence(process.egammaIsolationSequence)
process.makePatElectrons = cms.Sequence(process.patElectronIDs*process.patElectronIsolation*process.patElectrons)
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
process.patElectrons.addGenMatch = cms.bool(False)
process.patElectrons.embedGenMatch = cms.bool(False)
process.patElectrons.isoDeposits = cms.PSet()
process.patElectrons.userIsolation = cms.PSet()


#  GsfElectron ################
process.PassingGsf = cms.EDFilter("PATElectronRefSelector",
    src = cms.InputTag("patElectrons"),
    cut = cms.string("(abs(superCluster.eta)<2.5) && !(1.4442<abs(superCluster.eta)<1.566)"
                     " && (ecalEnergy*sin(superClusterPosition.theta)>20.0) && (hadronicOverEm<0.15)")    
)


process.GsfMatchedSuperClusterCands = cms.EDProducer("CandidateMatchedCandidateProducer",
   src     = cms.InputTag("goodSuperClustersClean"),
   ReferenceCandidateCollection = cms.untracked.InputTag("PassingGsf"),
   deltaR =  cms.untracked.double(0.3)
)


process.GsfMatchedPhotonCands = cms.EDProducer("CandidateMatchedCandidateProducer",
   src     = cms.InputTag("FilteredPhotons"),
   ReferenceCandidateCollection = cms.untracked.InputTag("PassingGsf"),
   deltaR =  cms.untracked.double(0.3)
)

process.RawHFElectronID = cms.EDFilter("CandViewSelector",
    src = cms.InputTag("hfRecoEcalCandidate"),
    cut = cms.string('et > 15.0')
)

process.RawHFElectronIDTight = cms.EDFilter("CandViewSelector",
    src = cms.InputTag("hfRecoEcalCandidateTight"),
    cut = cms.string('et > 15.0')
)

process.HFElectronID = cms.EDProducer("CandidateMatchedCandidateProducer",
   src     = cms.InputTag("theHFSuperClusters"),
   ReferenceCandidateCollection = cms.untracked.InputTag("RawHFElectronID"),
   deltaR =  cms.untracked.double(0.3)
)

process.HFElectronIDTight = cms.EDProducer("CandidateMatchedCandidateProducer",
   src     = cms.InputTag("theHFSuperClusters"),
   ReferenceCandidateCollection = cms.untracked.InputTag("RawHFElectronIDTight"),
   deltaR =  cms.untracked.double(0.3)
)     
 
##     ___           _       _   _             
##    |_ _|___  ___ | | __ _| |_(_) ___  _ __  
##     | |/ __|/ _ \| |/ _` | __| |/ _ \| '_ \ 
##     | |\__ \ (_) | | (_| | |_| | (_) | | | |
##    |___|___/\___/|_|\__,_|\__|_|\___/|_| |_|

                                          
#  Isolation ################ 
#process.PassingIsolation = cms.EDFilter("PATElectronRefSelector",
#    src = cms.InputTag("gsfElectrons"),
#    cut = cms.string(process.PassingGsf.cut.value() +
#         " && (( isEB && ( (dr03TkSumPt + max(0., dr03EcalRecHitSumEt - 1.) + dr03HcalTowerSumEt)/(p4.Pt) < 0.15 ))"
#         " || (isEE && ((dr03TkSumPt + dr03EcalRecHitSumEt + dr03HcalTowerSumEt)/(p4.Pt) < 0.1 )))")
#)
#
#process.PassingIsolation80 = cms.EDFilter("PATElectronRefSelector",
#    src = cms.InputTag("gsfElectrons"),
#    cut = cms.string(process.PassingGsf.cut.value() +
#         " && (( isEB && ( (dr03TkSumPt + max(0., dr03EcalRecHitSumEt - 1.) + dr03HcalTowerSumEt)/(p4.Pt) < 0.07 ))"
#         " || (isEE && ((dr03TkSumPt + dr03EcalRecHitSumEt + dr03HcalTowerSumEt)/(p4.Pt) < 0.06 )))")
#)

##    _____ _           _                     ___    _ 
##   | ____| | ___  ___| |_ _ __ ___  _ __   |_ _|__| |
##   |  _| | |/ _ \/ __| __| '__/ _ \| '_ \   | |/ _` |
##   | |___| |  __/ (__| |_| | | (_) | | | |  | | (_| |
##   |_____|_|\___|\___|\__|_|  \___/|_| |_| |___\__,_|
##   

# Electron ID  ######
#process.PassingId = cms.EDFilter("PATElectronRefSelector",
#    src = cms.InputTag("gsfElectrons"),
#    cut = cms.string(process.PassingIsolation.cut.value() +
#                     " && (gsfTrack.trackerExpectedHitsInner.numberOfHits <= 1)"
#                     " && ((isEB"
#                                   " && (sigmaIetaIeta<0.01)"
#                                   " && ( -0.8<deltaPhiSuperClusterTrackAtVtx<0.8 )"
#                                   " && ( -0.007<deltaEtaSuperClusterTrackAtVtx<0.007 )"
#                                   " && (hadronicOverEm<0.15)"
#                                   ")"
#                     " || (isEE"
#                                   " && (sigmaIetaIeta<0.03)"
#                                  " && ( -0.7<deltaPhiSuperClusterTrackAtVtx<0.7 )"
#                                  #" && ( -0.01<deltaEtaSuperClusterTrackAtVtx<0.01 )"
#                                   " && (hadronicOverEm<0.07) "
#                                   "))"
#                     ) 
#)


#process.PassingId80 = cms.EDFilter("PATElectronRefSelector",
#    src = cms.InputTag("gsfElectrons"),
#    cut = cms.string(process.PassingIsolation80.cut.value() +
#                     " && (gsfTrack.trackerExpectedHitsInner.numberOfHits <= 0)"
#                     " && ((isEB"
#                                   " && (sigmaIetaIeta<0.01)"
#                                   " && ( -0.06<deltaPhiSuperClusterTrackAtVtx<0.06 )"
#                                   " && ( -0.004<deltaEtaSuperClusterTrackAtVtx<0.004 )"
#                                   " && (hadronicOverEm<0.04)"
#                                   ")"
#                     " || (isEE"
#                                   " && (sigmaIetaIeta<0.03)"
#                                   " && ( -0.03<deltaPhiSuperClusterTrackAtVtx<0.03 )"
#                                   #" && ( -0.007<deltaEtaSuperClusterTrackAtVtx<0.007 )"
#                                   " && (hadronicOverEm<0.025) "
#                                   "))"
#                     ) 
#)


##########################PATS
process.Iso95 =  cms.EDFilter("PATElectronRefSelector",
                          src = cms.InputTag("patElectrons"),
                          cut = cms.string(process.PassingGsf.cut.value() +' && pt > 15.0 &&  (electronID("simpleEleId95relIso") > 6-0.1 && electronID("simpleEleId95relIso") < 7+.1)')
                      )

process.ElectronID95 = cms.EDFilter("PATElectronRefSelector",
                                src = cms.InputTag("patElectrons"),
                                cut = cms.string(process.PassingGsf.cut.value() +' && pt > 15.0 && ( electronID("simpleEleId95relIso") > 7-0.1 && electronID("simpleEleId95relIso") < 7+.1)')
                            )

process.Iso90 =  cms.EDFilter("PATElectronRefSelector",
                          src = cms.InputTag("patElectrons"),
                          cut = cms.string(process.PassingGsf.cut.value() +' && pt > 15.0 && (electronID("simpleEleId90relIso") > 6-0.1 && electronID("simpleEleId90relIso") < 7+.1)')

                      )

process.ElectronID90 = cms.EDFilter("PATElectronRefSelector",
                                src = cms.InputTag("patElectrons"),
                                cut = cms.string(process.PassingGsf.cut.value() +' && pt > 15.0 && ( electronID("simpleEleId90relIso") == 7 )')
                            )

process.Iso85 =  cms.EDFilter("PATElectronRefSelector",
                      src = cms.InputTag("patElectrons"),
                      cut = cms.string(process.PassingGsf.cut.value() +' && pt > 15.0 && ( electronID("simpleEleId85relIso") == 6 || electronID("simpleEleId85relIso") == 7 )')
                      )

process.ElectronID85 = cms.EDFilter("PATElectronRefSelector",
                                src = cms.InputTag("patElectrons"),
                                cut = cms.string(process.PassingGsf.cut.value() +' && pt > 15.0 && ( electronID("simpleEleId85relIso") == 7 )')
                            )

process.Iso80 =  cms.EDFilter("PATElectronRefSelector",
                          src = cms.InputTag("patElectrons"),
                          cut = cms.string(process.PassingGsf.cut.value() +' && pt > 15.0 && ( electronID("simpleEleId80relIso") == 6 ||  electronID("simpleEleId80relIso") == 7 )')
                      )

process.ElectronID80 = cms.EDFilter("PATElectronRefSelector",
                                src = cms.InputTag("patElectrons"),
                                cut = cms.string(process.PassingGsf.cut.value() +' && pt > 15.0 && ( electronID("simpleEleId80relIso") == 7 )')
                            )

process.Iso70 =  cms.EDFilter("PATElectronRefSelector",
                          src = cms.InputTag("patElectrons"),
                          cut = cms.string(process.PassingGsf.cut.value() +' && pt > 15.0 && ( electronID("simpleEleId70relIso") == 6 || electronID("simpleEleId70relIso") == 7 )')
                      )

process.ElectronID70 = cms.EDFilter("PATElectronRefSelector",
                                src = cms.InputTag("patElectrons"),
                                cut = cms.string(process.PassingGsf.cut.value() +' && pt > 15.0 && ( electronID("simpleEleId70relIso") == 7 )')
                            )

process.Iso60 =  cms.EDFilter("PATElectronRefSelector",
                          src = cms.InputTag("patElectrons"),
                          cut = cms.string(process.PassingGsf.cut.value() +' && pt > 15.0 && ( electronID("simpleEleId60relIso") == 6 ||  electronID("simpleEleId60relIso") == 7 )')
                      )

process.ElectronID60 = cms.EDFilter("PATElectronRefSelector",
                                src = cms.InputTag("patElectrons"),
                                cut = cms.string(process.PassingGsf.cut.value() +' && pt > 15.0 && ( electronID("simpleEleId60relIso") == 7 )')
                            )

process.InvWP95 = cms.EDFilter("PATElectronRefSelector",
                                src = cms.InputTag("patElectrons"),
                                cut = cms.string(process.PassingGsf.cut.value() +' && pt > 15.0 && ( electronID("simpleEleId95relIso") == 0 )')
)
process.InvWP90 = cms.EDFilter("PATElectronRefSelector",
                                src = cms.InputTag("patElectrons"),
                                cut = cms.string(process.PassingGsf.cut.value() +' && pt > 15.0 && ( electronID("simpleEleId90relIso") == 0 )')
)

process.InvWP85 = cms.EDFilter("PATElectronRefSelector",
                                src = cms.InputTag("patElectrons"),
                                cut = cms.string(process.PassingGsf.cut.value() +' && pt > 15.0 && ( electronID("simpleEleId85relIso") == 0 )')
)
process.InvWP80 = cms.EDFilter("PATElectronRefSelector",
                                src = cms.InputTag("patElectrons"),
                                cut = cms.string(process.PassingGsf.cut.value() +' && pt > 15.0 && ( electronID("simpleEleId80relIso") == 0 )')
)

process.InvWP70 = cms.EDFilter("PATElectronRefSelector",
                                src = cms.InputTag("patElectrons"),
                                cut = cms.string(process.PassingGsf.cut.value() +' && pt > 15.0 && ( electronID("simpleEleId70relIso") == 0 )')
)
process.InvWP60 = cms.EDFilter("PATElectronRefSelector",
                                src = cms.InputTag("patElectrons"),
                                cut = cms.string(process.PassingGsf.cut.value() +' && pt > 15.0 && ( electronID("simpleEleId60relIso") == 0 )')
)


process.PassingId = process.ElectronID95.clone()
process.PassingId80 = process.ElectronID80.clone()
process.PassingIsolation = process.Iso95.clone()
process.PassingIsolation80 = process.Iso80.clone()




##    _____     _                         __  __       _       _     _             
##   |_   _| __(_) __ _  __ _  ___ _ __  |  \/  | __ _| |_ ___| |__ (_)_ __   __ _ 
##     | || '__| |/ _` |/ _` |/ _ \ '__| | |\/| |/ _` | __/ __| '_ \| | '_ \ / _` |
##     | || |  | | (_| | (_| |  __/ |    | |  | | (_| | || (__| | | | | | | | (_| |
##     |_||_|  |_|\__, |\__, |\___|_|    |_|  |_|\__,_|\__\___|_| |_|_|_| |_|\__, |
##                |___/ |___/                                                |___/ 
##   

# Trigger  ##################
process.PassingHLT = cms.EDProducer("trgMatchedGsfElectronProducer",                     
    InputProducer = cms.InputTag("PassingId"),                          
    hltTag = cms.untracked.VInputTag(
                cms.InputTag("HLT_Photon15_Cleaned_L1R","",myHLT),
                cms.InputTag("HLT_Ele15_SW_L1R","",myHLT),
                cms.InputTag("HLT_Ele15_SW_CaloEleId_L1R","",myHLT),
                cms.InputTag("HLT_Ele17_SW_CaloEleId_L1R","",myHLT),
                cms.InputTag("HLT_Ele17_SW_EleId_L1R","",myHLT),
                cms.InputTag("HLT_Ele17_SW_TightEleId_L1R","",myHLT),
                cms.InputTag("HLT_Ele17_SW_LooseEleId_L1R","",myHLT),
                cms.InputTag("HLT_Ele27_SW_TightCaloEleIdTrack_L1R ","",myHLT),
                #cms.InputTag("HLT_Ele17_SW_TightCaloEleId_SC8HE_L1R","",myHLT),
                #cms.InputTag("HLT_Ele17_SW_TightCaloEleId_SC8HE_L1R_v1","",myHLT),
                #cms.InputTag("HLT_DoubleEle15_SW_L1R","",myHLT),
                #cms.InputTag("HLT_DoubleEle15_SW_L1R_v1","",myHLT),
                cms.InputTag("HLT_Ele22_SW_CaloEleId_L1R","",myHLT),
                cms.InputTag("HLT_Ele17_SW_TighterEleIdIsol_L1R_v1","",myHLT),
                cms.InputTag("HLT_Ele17_SW_TighterEleIdIsol_L1R_v2","",myHLT),
                cms.InputTag("HLT_Ele17_SW_TighterEleIdIsol_L1R_v3","",myHLT),
                cms.InputTag("HLT_Ele22_SW_TighterEleId_L1R_v2","",myHLT),
                cms.InputTag("HLT_Ele22_SW_TighterCaloIdIsol_L1R_v1","",myHLT),
                #cms.InputTag("HLT_Ele17_SW_TightCaloEleId_Ele8HE_L1R","",myHLT),
                #cms.InputTag("HLT_Ele17_SW_TightCaloEleId_Ele8HE_L1R_v1","",myHLT),
                #cms.InputTag("HLT_DoubleEle17_SW_L1R","",myHLT),
                cms.InputTag("HLT_Ele32_SW_TighterEleId_L1R","",myHLT)),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",myHLT)
)

process.PassingHLT80 = cms.EDProducer("trgMatchedGsfElectronProducer",                     
    InputProducer = cms.InputTag("PassingId80"), #from PassinId80 for W-like studies.                          
    hltTag =  cms.untracked.VInputTag(
                cms.InputTag("HLT_Photon15_Cleaned_L1R","",myHLT),
                cms.InputTag("HLT_Ele15_SW_L1R","",myHLT),
                cms.InputTag("HLT_Ele15_SW_CaloEleId_L1R","",myHLT),
                cms.InputTag("HLT_Ele17_SW_CaloEleId_L1R","",myHLT),
                cms.InputTag("HLT_Ele17_SW_TightEleId_L1R","",myHLT),
                cms.InputTag("HLT_Ele17_SW_EleId_L1R","",myHLT),
                cms.InputTag("HLT_Ele17_SW_LooseEleId_L1R","",myHLT),
                cms.InputTag("HLT_Ele27_SW_TightCaloEleIdTrack_L1R","",myHLT),
                cms.InputTag("HLT_Ele17_SW_TighterEleIdIsol_L1R_v1","",myHLT),
                cms.InputTag("HLT_Ele17_SW_TighterEleIdIsol_L1R_v2","",myHLT),
                cms.InputTag("HLT_Ele17_SW_TighterEleIdIsol_L1R_v3","",myHLT),
                cms.InputTag("HLT_Ele22_SW_TighterEleId_L1R_v2","",myHLT),
                cms.InputTag("HLT_Ele22_SW_TighterCaloIdIsol_L1R_v1","",myHLT),
                cms.InputTag("HLT_Ele32_SW_TighterEleId_L1R","",myHLT),
                cms.InputTag("HLT_Ele22_SW_CaloEleId_L1R","",myHLT)),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",myHLT)
)


process.badSuperClustersClean = cms.EDProducer("CandViewCleaner",
    srcObject = cms.InputTag("goodSuperClustersClean"),
    module_label = cms.string(''),
    srcObjectsToRemove = cms.VInputTag(cms.InputTag("PassingHLT")),
    deltaRMin = cms.double(0.1)
)

##    _____      _                        _  __     __             
##   | ____|_  _| |_ ___ _ __ _ __   __ _| | \ \   / /_ _ _ __ ___ 
##   |  _| \ \/ / __/ _ \ '__| '_ \ / _` | |  \ \ / / _` | '__/ __|
##   | |___ >  <| ||  __/ |  | | | | (_| | |   \ V / (_| | |  \__ \
##   |_____/_/\_\\__\___|_|  |_| |_|\__,_|_|    \_/ \__,_|_|  |___/
##   

## Here we show how to use a module to compute an external variable
#process.load("JetMETCorrections.Configuration.DefaultJEC_cff")
#JET_COLL = "ak5CaloJets"
#JET_CUTS = "pt > 10.0 && abs(eta)<3.0 && (0.01 < emEnergyFraction < 0.9) && (n90>5)"

process.superClusterDRToNearestJet = cms.EDProducer("DeltaRNearestJetComputer",
    probes = cms.InputTag("goodSuperClusters"),
       # ^^--- NOTA BENE: if probes are defined by ref, as in this case, 
       #       this must be the full collection, not the subset by refs.
    objects = cms.InputTag(JET_COLL),
    objectSelection = cms.string(JET_CUTS+ " && pt > 15.0"),
)


process.JetMultiplicityInSCEvents = cms.EDProducer("CandMultiplicityCounter",
    probes = cms.InputTag("goodSuperClusters"),
    objects = cms.InputTag(JET_COLL),
    objectSelection = cms.string(JET_CUTS+ " && pt > 15.0"),
)


process.GsfDRToNearestJet = cms.EDProducer("DeltaRNearestJetComputer",
    probes = cms.InputTag("patElectrons"),
    objects = cms.InputTag(JET_COLL),
    objectSelection = cms.string(JET_CUTS+ " && pt > 15.0"),
)



process.JetMultiplicityInGsfEvents = cms.EDProducer("CandMultiplicityCounter",
    probes = cms.InputTag("patElectrons"),
    objects = cms.InputTag(JET_COLL),
    objectSelection = cms.string(JET_CUTS+ " && pt > 15.0"),
)

process.PhotonDRToNearestJet = process.superClusterDRToNearestJet.clone()
process.PhotonDRToNearestJet.probes =cms.InputTag("FilteredPhotons")
process.JetMultiplicityInPhotonEvents = process.JetMultiplicityInSCEvents.clone()
process.JetMultiplicityInPhotonEvents.probes = cms.InputTag("FilteredPhotons")

process.ext_ToNearestJet_sequence = cms.Sequence(
    #process.ak5CaloL2L3 + 
    process.superClusterDRToNearestJet +
    process.JetMultiplicityInSCEvents + 
    process.PhotonDRToNearestJet +
    process.JetMultiplicityInPhotonEvents +
    process.GsfDRToNearestJet +
    process.JetMultiplicityInGsfEvents
    )


##    _____             ____        __ _       _ _   _             
##   |_   _|_ _  __ _  |  _ \  ___ / _(_)_ __ (_) |_(_) ___  _ __  
##     | |/ _` |/ _` | | | | |/ _ \ |_| | '_ \| | __| |/ _ \| '_ \ 
##     | | (_| | (_| | | |_| |  __/  _| | | | | | |_| | (_) | | | |
##     |_|\__,_|\__, | |____/ \___|_| |_|_| |_|_|\__|_|\___/|_| |_|
##              |___/                                              

process.Tag95 = process.PassingHLT.clone()
process.Tag80 = process.PassingHLT80.clone()
process.Tag = process.PassingHLT80.clone()
process.InvWP95Tag = process.PassingHLT.clone()
process.InvWP95Tag.InputProducer = cms.InputTag("InvWP95")
process.InvWP80Tag = process.PassingHLT.clone()
process.InvWP80Tag.InputProducer = cms.InputTag("InvWP80")
process.InvWP95Tag80 = process.PassingHLT80.clone()
process.InvWP95Tag80.InputProducer = cms.InputTag("InvWP95")
process.InvWP80Tag80 = process.PassingHLT80.clone()
process.InvWP80Tag80.InputProducer = cms.InputTag("InvWP80")
 
process.TagMatchedSuperClusterCandsClean = cms.EDProducer("CandidateMatchedCandidateProducer",
   src     = cms.InputTag("goodSuperClustersClean"),
   ReferenceCandidateCollection = cms.untracked.InputTag("Tag"),
   deltaR =  cms.untracked.double(0.3)
)


process.TagMatchedPhotonCands = cms.EDProducer("CandidateMatchedCandidateProducer",
   src     = cms.InputTag("FilteredPhotons"),
   ReferenceCandidateCollection = cms.untracked.InputTag("Tag"),
   deltaR =  cms.untracked.double(0.3)
)

process.NTLooseMatchedSuperClusterCands = process.TagMatchedSuperClusterCandsClean.clone()
process.NTLooseMatchedSuperClusterCands.ReferenceCandidateCollection = cms.untracked.InputTag("NTElecLoose")
process.NTTightMatchedSuperClusterCands = process.TagMatchedSuperClusterCandsClean.clone()
process.NTTightMatchedSuperClusterCands.ReferenceCandidateCollection = cms.untracked.InputTag("NTElecTight")

process.IsoMatchedSuperClusterCandsClean = process.TagMatchedSuperClusterCandsClean.clone()
process.IsoMatchedSuperClusterCandsClean.ReferenceCandidateCollection = cms.untracked.InputTag("PassingIsolation")
process.IdMatchedSuperClusterCandsClean = process.TagMatchedSuperClusterCandsClean.clone()
process.IdMatchedSuperClusterCandsClean.ReferenceCandidateCollection = cms.untracked.InputTag("PassingId")

process.Iso80MatchedSuperClusterCandsClean = process.TagMatchedSuperClusterCandsClean.clone()
process.Iso80MatchedSuperClusterCandsClean.ReferenceCandidateCollection = cms.untracked.InputTag("PassingIsolation80")
process.Id80MatchedSuperClusterCandsClean = process.TagMatchedSuperClusterCandsClean.clone()
process.Id80MatchedSuperClusterCandsClean.ReferenceCandidateCollection = cms.untracked.InputTag("PassingId80")

process.InvWP95MatchedSuperClusterCands = process.TagMatchedSuperClusterCandsClean.clone()
process.InvWP95MatchedSuperClusterCands.ReferenceCandidateCollection = cms.untracked.InputTag("InvWP95")
process.InvWP90MatchedSuperClusterCands = process.TagMatchedSuperClusterCandsClean.clone()
process.InvWP90MatchedSuperClusterCands.ReferenceCandidateCollection = cms.untracked.InputTag("InvWP90")
process.InvWP85MatchedSuperClusterCands = process.TagMatchedSuperClusterCandsClean.clone()
process.InvWP85MatchedSuperClusterCands.ReferenceCandidateCollection = cms.untracked.InputTag("InvWP85")
process.InvWP80MatchedSuperClusterCands = process.TagMatchedSuperClusterCandsClean.clone()
process.InvWP80MatchedSuperClusterCands.ReferenceCandidateCollection = cms.untracked.InputTag("InvWP80")
process.InvWP70MatchedSuperClusterCands = process.TagMatchedSuperClusterCandsClean.clone()
process.InvWP70MatchedSuperClusterCands.ReferenceCandidateCollection = cms.untracked.InputTag("InvWP70")
process.InvWP60MatchedSuperClusterCands = process.TagMatchedSuperClusterCandsClean.clone()
process.InvWP60MatchedSuperClusterCands.ReferenceCandidateCollection = cms.untracked.InputTag("InvWP60")



process.ele_sequence = cms.Sequence(
    process.makePatElectrons *
    process.PassingGsf * process.GsfMatchedSuperClusterCands +
    process.RawHFElectronID * process.RawHFElectronIDTight *
    process.HFElectronID * process.HFElectronIDTight +
    process.GsfMatchedPhotonCands +
    process.PassingIsolation + process.PassingId +
    process.PassingIsolation80 +process.PassingId80 +
    process.Iso95 * process.ElectronID95 + process.Iso90 * process.ElectronID90 + process.Iso85 *
    process.ElectronID85 + process.Iso80 * process.ElectronID80+ process.Iso70 * process.ElectronID70 + process.Iso60 * process.ElectronID60 +   
    process.InvWP95 + process.InvWP90 + process.InvWP85 + process.InvWP80 +  process.InvWP70 + process.InvWP60 +
    process.PassingHLT + process.PassingHLT80 +  process.Tag* process.Tag80* process.Tag95*  process.InvWP95Tag * process.InvWP80Tag *
    process.InvWP95Tag80 * process.InvWP80Tag80 *
    process.TagMatchedSuperClusterCandsClean *
    process.badSuperClustersClean *
    process.TagMatchedPhotonCands *
    process.IsoMatchedSuperClusterCandsClean *
    process.IdMatchedSuperClusterCandsClean *
    process.Iso80MatchedSuperClusterCandsClean *
    process.Id80MatchedSuperClusterCandsClean *
    process.NTLooseMatchedSuperClusterCands *
    process.NTTightMatchedSuperClusterCands *
    process.InvWP95MatchedSuperClusterCands * process.InvWP90MatchedSuperClusterCands * process.InvWP85MatchedSuperClusterCands *
    process.InvWP80MatchedSuperClusterCands * process.InvWP70MatchedSuperClusterCands * process.InvWP60MatchedSuperClusterCands
    )

####################################################
####
####
####
###   CRAZY MC TRIAL!!! PLEASE WORK FIRST TIME
###
###
#################################################

process.trueEprobes =  cms.EDFilter("GenParticleRefSelector",
                          src = cms.InputTag("genParticles"),
                          cut = cms.string('pt > 15.0 && pdgId==11 && status == 1 ')
                      )

process.trueE = cms.EDFilter("CandViewSelector",
      src = cms.InputTag("trueEprobes"),
      cut = cms.string("pt > 0.0") #changed 2.5->2.9                            
)

process.SCMatchedTruth = cms.EDProducer("CandidateMatchedCandidateProducer",
   src     = cms.InputTag("trueEprobes"),
   ReferenceCandidateCollection = cms.untracked.InputTag("goodSimpSuperClusters"),
   deltaR =  cms.untracked.double(0.3)
)     
 

##    _____ ___   ____    ____       _          
##   |_   _( _ ) |  _ \  |  _ \ __ _(_)_ __ ___ 
##     | | / _ \/\ |_) | | |_) / _` | | '__/ __|
##     | || (_>  <  __/  |  __/ (_| | | |  \__ \
##     |_| \___/\/_|     |_|   \__,_|_|_|  |___/
##                                              
##   
#  Tag & probe selection ######

process.tagMC = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("Tag trueEprobes"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                           
    cut   = cms.string("40 < mass < 600"),
)

process.tagSC = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("Tag goodSuperClustersClean"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                           
    cut   = cms.string("40 < mass < 600"),
)

process.tag80SC = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("Tag80 goodSuperClustersClean"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                           
    cut   = cms.string("40 < mass < 600"),
)

process.tagPhoton = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("Tag FilteredPhotons"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                           
    cut   = cms.string("40 < mass < 600"),
)

process.SCSC = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("badSuperClustersClean badSuperClustersClean"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                           
    cut   = cms.string("40 < mass < 600"),
)

process.GsfGsf = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("PassingGsf PassingGsf"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                                   
    cut   = cms.string("40 < mass < 600"),
)

process.tagGsf = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("Tag PassingGsf"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                                   
    cut   = cms.string("40 < mass < 600"),
)

process.tag80Gsf = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("Tag80 PassingGsf"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                                   
    cut   = cms.string("40 < mass < 600"),
)


process.tagIso = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("Tag PassingIsolation"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                                   
    cut   = cms.string("40 < mass < 600"),
)


process.tagId = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("Tag PassingId"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                                  
    cut   = cms.string("40 < mass < 600"),
)


process.tagHLT = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("Tag PassingHLT"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                                   
    cut   = cms.string("40 < mass < 600"),
)

process.tagIso80 = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("Tag PassingIsolation80"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                                   
    cut   = cms.string("40 < mass < 600"),
)


process.tagId80 = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("Tag PassingId80"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                                  
    cut   = cms.string("40 < mass < 600"),
)


process.tagHLT80 = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("Tag PassingHLT80"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                                   
    cut   = cms.string("40 < mass < 600"),
)

process.tagHFSuperClusters = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("PassingHLT80 theHFSuperClusters"), # charge coniugate states are implied
    cut   = cms.string("40 < mass < 600"),
    checkCharge = cms.bool(False),
)


process.tagInvWP80Gsf = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("InvWP80Tag PassingGsf"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                                   
    cut   = cms.string("40 < mass < 600"),
)

process.tagInvWP80SC = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("InvWP80Tag goodSuperClustersClean"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                                   
    cut   = cms.string("40 < mass < 600"),
)

process.tagHFEID = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("PassingHLT80 HFElectronID"), # charge coniugate states are implied
    cut   = cms.string("40 < mass < 600"),
    checkCharge = cms.bool(False),
)

process.tagNTTEID = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("PassingHLT80 NTElecTight"), # charge coniugate states are implied
    cut   = cms.string("40 < mass < 600"),
    checkCharge = cms.bool(False),
)

process.allTagsAndProbes = cms.Sequence(
    process.tagSC + process.SCSC + process.tagPhoton +
    process.tagGsf + process.GsfGsf +
    process.tagIso + process.tagId + process.tagHLT+
    process.tagIso80 + process.tagId80 + process.tagHLT80 +
    process.tagHFSuperClusters + process.tagHFEID + process.tagNTTEID +
    process.tag80SC + process.tag80Gsf + process.tagInvWP80Gsf + process.tagInvWP80SC
)


##    __  __  ____   __  __       _       _               
##   |  \/  |/ ___| |  \/  | __ _| |_ ___| |__   ___  ___ 
##   | |\/| | |     | |\/| |/ _` | __/ __| '_ \ / _ \/ __|
##   | |  | | |___  | |  | | (_| | || (__| | | |  __/\__ \
##   |_|  |_|\____| |_|  |_|\__,_|\__\___|_| |_|\___||___/
##                                                        

process.McMatchTag = cms.EDProducer("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("Tag"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
)


process.McMatchSC = cms.EDProducer("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("goodSuperClustersClean"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles")
)


process.McMatchSCbad = cms.EDProducer("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("badSuperClustersClean"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles")
)


process.McMatchGsf = cms.EDProducer("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("PassingGsf"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
)

process.McMatchIso = cms.EDProducer("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("PassingIsolation"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
)

process.McMatchId = cms.EDProducer("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("PassingId"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
)

process.McMatchHLT = cms.EDProducer("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("PassingHLT"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
)

process.McMatchPhoton = cms.EDProducer("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("FilteredPhotons"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
)

process.McMatchHF = cms.EDProducer("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("HFElectronID"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
)

process.McMatchHFSC = cms.EDProducer("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("theHFSuperClusters"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
)


process.McMatchNT = cms.EDProducer("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("NTElecTight"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
)

process.McMatchMC = cms.EDProducer("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("trueEprobes"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
)

process.mc_sequence = cms.Sequence(
   process.McMatchTag + process.McMatchSC + process.McMatchSCbad +
   process.McMatchGsf + process.McMatchIso + process.McMatchPhoton + process.McMatchNT + 
   process.McMatchId  + process.McMatchHLT + process.McMatchHF + process.McMatchHFSC
)

############################################################################
##    _____           _       _ ____            _            _   _  ____  ##
##   |_   _|_ _  __ _( )_ __ ( )  _ \ _ __ ___ | |__   ___  | \ | |/ ___| ##
##     | |/ _` |/ _` |/| '_ \|/| |_) | '__/ _ \| '_ \ / _ \ |  \| | |  _  ##
##     | | (_| | (_| | | | | | |  __/| | | (_) | |_) |  __/ | |\  | |_| | ##
##     |_|\__,_|\__, | |_| |_| |_|   |_|  \___/|_.__/ \___| |_| \_|\____| ##
##              |___/                                                     ##
##                                                                        ##
############################################################################
##    ____                      _     _           
##   |  _ \ ___ _   _ ___  __ _| |__ | | ___  ___ 
##   | |_) / _ \ | | / __|/ _` | '_ \| |/ _ \/ __|
##   |  _ <  __/ |_| \__ \ (_| | |_) | |  __/\__ \
##   |_| \_\___|\__,_|___/\__,_|_.__/|_|\___||___/


## I define some common variables for re-use later.
## This will save us repeating the same code for each efficiency category

ZVariablesToStore = cms.PSet(
    eta = cms.string("eta"),
    pt  = cms.string("pt"),
    phi  = cms.string("phi"),
    et  = cms.string("et"),
    e  = cms.string("energy"),
    p  = cms.string("p"),
    px  = cms.string("px"),
    py  = cms.string("py"),
    pz  = cms.string("pz"),
    theta  = cms.string("theta"),    
    vx     = cms.string("vx"),
    vy     = cms.string("vy"),
    vz     = cms.string("vz"),
    rapidity  = cms.string("rapidity"),
    mass  = cms.string("mass"),
    mt  = cms.string("mt"),    
)   



ProbeVariablesToStore = cms.PSet(
    probe_gsfEle_eta = cms.string("eta"),
    probe_gsfEle_pt  = cms.string("pt"),
    probe_gsfEle_phi  = cms.string("phi"),
    probe_gsfEle_et  = cms.string("et"),
    probe_gsfEle_e  = cms.string("energy"),
    probe_gsfEle_p  = cms.string("p"),
    probe_gsfEle_px  = cms.string("px"),
    probe_gsfEle_py  = cms.string("py"),
    probe_gsfEle_pz  = cms.string("pz"),
    probe_gsfEle_theta  = cms.string("theta"),    
    probe_gsfEle_charge = cms.string("charge"),
    probe_gsfEle_vx     = cms.string("vx"),
    probe_gsfEle_vy     = cms.string("vy"),
    probe_gsfEle_vz     = cms.string("vz"),
    probe_gsfEle_rapidity  = cms.string("rapidity"),
    probe_gsfEle_missingHits = cms.string("gsfTrack.trackerExpectedHitsInner.numberOfHits"),
    probe_gsfEle_hasValidHitInFirstPixelBarrel = cms.string("gsfTrack.hitPattern.hasValidHitInFirstPixelBarrel"),
    ## super cluster quantities
    probe_sc_energy = cms.string("superCluster.energy"),
    probe_sc_et    = cms.string("superCluster.energy*sin(superClusterPosition.theta)"),    
    probe_sc_x      = cms.string("superCluster.x"),
    probe_sc_y      = cms.string("superCluster.y"),
    probe_sc_z      = cms.string("superCluster.z"),
    probe_sc_eta    = cms.string("superCluster.eta"),
    probe_sc_theta  = cms.string("superClusterPosition.theta"),   
    probe_sc_phi    = cms.string("superCluster.phi"),
    probe_sc_size   = cms.string("superCluster.size"), # number of hits
    probe_sc_rawEnergy = cms.string("superCluster.rawEnergy"), 
    probe_sc_preshowerEnergy   = cms.string("superCluster.preshowerEnergy"), 
    probe_sc_phiWidth   = cms.string("superCluster.phiWidth"), 
    probe_sc_etaWidth   = cms.string("superCluster.etaWidth"),         
    ## isolation 
    probe_gsfEle_trackiso_dr04 = cms.string("dr04TkSumPt"),
    probe_gsfEle_ecaliso_dr04  = cms.string("dr04EcalRecHitSumEt"),
    probe_gsfEle_hcaliso_dr04  = cms.string("dr04HcalTowerSumEt"),
    probe_gsfEle_trackiso_dr03 = cms.string("dr03TkSumPt"),
    probe_gsfEle_ecaliso_dr03  = cms.string("dr03EcalRecHitSumEt"),
    probe_gsfEle_hcaliso_dr03  = cms.string("dr03HcalTowerSumEt"),
    ## classification, location, etc.    
    probe_gsfEle_classification = cms.string("classification"),
    probe_gsfEle_numberOfBrems  = cms.string("numberOfBrems"),     
    probe_gsfEle_bremFraction   = cms.string("fbrem"),
    probe_gsfEle_mva            = cms.string("mva"),        
    probe_gsfEle_deltaEta       = cms.string("deltaEtaSuperClusterTrackAtVtx"),
    probe_gsfEle_deltaPhi       = cms.string("deltaPhiSuperClusterTrackAtVtx"),
    probe_gsfEle_deltaPhiOut    = cms.string("deltaPhiSeedClusterTrackAtCalo"),
    probe_gsfEle_deltaEtaOut    = cms.string("deltaEtaSeedClusterTrackAtCalo"),
    probe_gsfEle_isEB           = cms.string("isEB"),
    probe_gsfEle_isEE           = cms.string("isEE"),
    probe_gsfEle_isGap          = cms.string("isGap"),
    probe_gsfEle_isEBEEGap      = cms.string("isEBEEGap"),
    probe_gsfEle_isEBGap        = cms.string("isEBGap"),
    probe_gsfEle_isEBEtaGap     = cms.string("isEBEtaGap"),
    probe_gsfEle_isEBPhiGap     = cms.string("isEBPhiGap"),
    probe_gsfEle_isEEGap        = cms.string("isEEGap"),
    probe_gsfEle_isEEDeeGap     = cms.string("isEEDeeGap"),
    probe_gsfEle_isEERingGap    = cms.string("isEERingGap"),
    ## Hcal energy over Ecal Energy
    probe_gsfEle_HoverE         = cms.string("hcalOverEcal"),
    probe_gsfEle_EoverP         = cms.string("eSuperClusterOverP"),        
    probe_gsfEle_EoverPout      = cms.string("eSeedClusterOverPout"),
    probe_gsfEle_HoverE_Depth1  = cms.string("hcalDepth1OverEcal"),
    probe_gsfEle_HoverE_Depth2  = cms.string("hcalDepth2OverEcal"),
    ## Cluster shape information
    probe_gsfEle_sigmaEtaEta  = cms.string("sigmaEtaEta"),
    probe_gsfEle_sigmaIetaIeta = cms.string("sigmaIetaIeta"),
    probe_gsfEle_e1x5               = cms.string("e1x5"),
    probe_gsfEle_e2x5Max            = cms.string("e2x5Max"),
    probe_gsfEle_e5x5               = cms.string("e5x5"),
    ## is ECAL driven ? is Track driven ?
    probe_gsfEle_ecalDrivenSeed     = cms.string("ecalDrivenSeed"),
    probe_gsfEle_trackerDrivenSeed  = cms.string("trackerDrivenSeed"),
    ## fraction of common hits between the GSF and CTF tracks
    probe_gsfEle_shFracInnerHits    = cms.string("shFracInnerHits"),  
)


TagVariablesToStore = cms.PSet(
    gsfEle_eta = cms.string("eta"),
    gsfEle_pt  = cms.string("pt"),
    gsfEle_phi  = cms.string("phi"),
    gsfEle_et  = cms.string("et"),
    gsfEle_e  = cms.string("energy"),
    gsfEle_p  = cms.string("p"),
    gsfEle_px  = cms.string("px"),
    gsfEle_py  = cms.string("py"),
    gsfEle_pz  = cms.string("pz"),
    gsfEle_theta  = cms.string("theta"),    
    gsfEle_charge = cms.string("charge"),
    gsfEle_vx     = cms.string("vx"),
    gsfEle_vy     = cms.string("vy"),
    gsfEle_vz     = cms.string("vz"),
    gsfEle_rapidity  = cms.string("rapidity"),
    gsfEle_missingHits = cms.string("gsfTrack.trackerExpectedHitsInner.numberOfHits"),
    gsfEle_hasValidHitInFirstPixelBarrel = cms.string("gsfTrack.hitPattern.hasValidHitInFirstPixelBarrel"),
    ## super cluster quantities
    sc_energy = cms.string("superCluster.energy"),
    sc_et     = cms.string("superCluster.energy*sin(superClusterPosition.theta)"),    
    sc_x      = cms.string("superCluster.x"),
    sc_y      = cms.string("superCluster.y"),
    sc_z      = cms.string("superCluster.z"),
    sc_eta    = cms.string("superCluster.eta"),
    sc_theta  = cms.string("superClusterPosition.theta"),      
    sc_phi    = cms.string("superCluster.phi"),
    sc_size   = cms.string("superCluster.size"), # number of hits
    sc_rawEnergy = cms.string("superCluster.rawEnergy"), 
    sc_preshowerEnergy   = cms.string("superCluster.preshowerEnergy"), 
    sc_phiWidth   = cms.string("superCluster.phiWidth"), 
    sc_etaWidth   = cms.string("superCluster.etaWidth"),         
    ## isolation 
    gsfEle_trackiso_dr04 = cms.string("dr04TkSumPt"),
    gsfEle_ecaliso_dr04  = cms.string("dr04EcalRecHitSumEt"),
    gsfEle_hcaliso_dr04  = cms.string("dr04HcalTowerSumEt"),
    gsfEle_trackiso_dr03 = cms.string("dr03TkSumPt"),
    gsfEle_ecaliso_dr03  = cms.string("dr03EcalRecHitSumEt"),
    gsfEle_hcaliso_dr03  = cms.string("dr03HcalTowerSumEt"),
    ## classification, location, etc.    
    gsfEle_classification = cms.string("classification"),
    gsfEle_numberOfBrems  = cms.string("numberOfBrems"),     
    gsfEle_bremFraction   = cms.string("fbrem"),
    gsfEle_mva            = cms.string("mva"),        
    gsfEle_deltaEta       = cms.string("deltaEtaSuperClusterTrackAtVtx"),
    gsfEle_deltaPhi       = cms.string("deltaPhiSuperClusterTrackAtVtx"),
    gsfEle_deltaPhiOut    = cms.string("deltaPhiSeedClusterTrackAtCalo"),
    gsfEle_deltaEtaOut    = cms.string("deltaEtaSeedClusterTrackAtCalo"),
    gsfEle_isEB           = cms.string("isEB"),
    gsfEle_isEE           = cms.string("isEE"),
    gsfEle_isGap          = cms.string("isGap"),
    gsfEle_isEBEEGap      = cms.string("isEBEEGap"),
    gsfEle_isEBGap        = cms.string("isEBGap"),
    gsfEle_isEBEtaGap     = cms.string("isEBEtaGap"),
    gsfEle_isEBPhiGap     = cms.string("isEBPhiGap"),
    gsfEle_isEEGap        = cms.string("isEEGap"),
    gsfEle_isEEDeeGap     = cms.string("isEEDeeGap"),
    gsfEle_isEERingGap    = cms.string("isEERingGap"),
    ## Hcal energy over Ecal Energy
    gsfEle_HoverE         = cms.string("hcalOverEcal"),
    gsfEle_EoverP         = cms.string("eSuperClusterOverP"),        
    gsfEle_EoverPout      = cms.string("eSeedClusterOverPout"),
    gsfEle_HoverE_Depth1  = cms.string("hcalDepth1OverEcal"),
    gsfEle_HoverE_Depth2  = cms.string("hcalDepth2OverEcal"),
    ## Cluster shape information
    gsfEle_sigmaEtaEta  = cms.string("sigmaEtaEta"),
    gsfEle_sigmaIetaIeta = cms.string("sigmaIetaIeta"),
    gsfEle_e1x5               = cms.string("e1x5"),
    gsfEle_e2x5Max            = cms.string("e2x5Max"),
    gsfEle_e5x5               = cms.string("e5x5"),
    ## is ECAL driven ? is Track driven ?
    gsfEle_ecalDrivenSeed     = cms.string("ecalDrivenSeed"),
    gsfEle_trackerDrivenSeed  = cms.string("trackerDrivenSeed"),
    ## fraction of common hits between the GSF and CTF tracks
    gsfEle_shFracInnerHits    = cms.string("shFracInnerHits"),  
)


ProbePhotonVariablesToStore = cms.PSet(
        probe_eta = cms.string("eta"),
        probe_phi  = cms.string("phi"),
        probe_et  = cms.string("et"),
        probe_e  = cms.string("energy"),
        probe_p  = cms.string("p"),
        probe_px  = cms.string("px"),
        probe_py  = cms.string("py"),
        probe_pz  = cms.string("pz"),
        probe_theta  = cms.string("theta"),    
        ## isolation 
        probe_trkSumPtHollowConeDR03 = cms.string("trkSumPtHollowConeDR03"),
        probe_ecalRecHitSumEtConeDR03  = cms.string("ecalRecHitSumEtConeDR03"),
        probe_hcalTowerSumEtConeDR03  = cms.string("hcalTowerSumEtConeDR03"),
        ## booleans
        probe_isPhoton  = cms.string("isPhoton"),     
        probe_hasConversionTracks = cms.string("hasConversionTracks"),

        ## Hcal energy over Ecal Energy
        probe_hadronicOverEm = cms.string("hadronicOverEm"),
        ## Cluster shape information
        probe_sigmaIetaIeta = cms.string("sigmaIetaIeta"),

        probe_sc_energy = cms.string("superCluster.energy"),
        probe_sc_et    = cms.string("superCluster.energy*sin(superCluster.position.theta)"),    
        probe_sc_x      = cms.string("superCluster.x"),
        probe_sc_y      = cms.string("superCluster.y"),
        probe_sc_z      = cms.string("superCluster.z"),
        probe_sc_eta    = cms.string("superCluster.eta"),
        probe_sc_theta  = cms.string("superCluster.position.theta"),   
        probe_sc_phi    = cms.string("superCluster.phi"),
        probe_sc_size   = cms.string("superCluster.size"), # number of hits
        probe_sc_rawEnergy = cms.string("superCluster.rawEnergy"), 
        probe_sc_preshowerEnergy   = cms.string("superCluster.preshowerEnergy"), 
        probe_sc_phiWidth   = cms.string("superCluster.phiWidth"), 
        probe_sc_etaWidth   = cms.string("superCluster.etaWidth"),
)


ProbeSuperClusterVariablesToStore = cms.PSet(
    probe_sc_eta = cms.string("eta"),
    probe_sc_pt  = cms.string("pt"),
    probe_sc_phi  = cms.string("phi"),
    probe_sc_et  = cms.string("et"),
    probe_sc_e  = cms.string("energy"),
    probe_sc_p  = cms.string("p"),
    probe_sc_px  = cms.string("px"),
    probe_sc_py  = cms.string("py"),
    probe_sc_pz  = cms.string("pz"),
    probe_sc_theta  = cms.string("theta"),
)




TagSuperClusterVariablesToStore = cms.PSet(
    sc_eta = cms.string("eta"),
    sc_pt  = cms.string("pt"),
    sc_phi  = cms.string("phi"),
    sc_et  = cms.string("et"),
    sc_e  = cms.string("energy"),
    sc_p  = cms.string("p"),
    sc_px  = cms.string("px"),
    sc_py  = cms.string("py"),
        sc_pz  = cms.string("pz"),
    sc_theta  = cms.string("theta"),
)





CommonStuffForSuperClusterProbe = cms.PSet(
   variables = cms.PSet(ProbeSuperClusterVariablesToStore),
   ignoreExceptions =  cms.bool (False),
   #fillTagTree      =  cms.bool (True),
   addRunLumiInfo   =  cms.bool (True),
   addEventVariablesInfo   =  cms.bool (True),
   pairVariables =  cms.PSet(ZVariablesToStore),
   pairFlags     =  cms.PSet(
          mass60to120 = cms.string("60 < mass < 120")
    ),
    tagVariables   =  cms.PSet(TagVariablesToStore),
    tagFlags     =  cms.PSet(
          flag = cms.string("pt>0")
    ),    
)






CommonStuffForGsfElectronProbe = cms.PSet(
    variables = cms.PSet(ProbeVariablesToStore),
    ignoreExceptions =  cms.bool (False),
    #fillTagTree      =  cms.bool (True),
    addRunLumiInfo   =  cms.bool (True),
    addEventVariablesInfo   =  cms.bool (True),
    pairVariables =  cms.PSet(ZVariablesToStore),
    pairFlags     =  cms.PSet(
          mass60to120 = cms.string("60 < mass < 120")
    ),
    tagVariables   =  cms.PSet(TagVariablesToStore),
    tagFlags     =  cms.PSet(
          flag = cms.string("pt>0")
    ),    
)


if MC_flag:
    mcTruthCommonStuff = cms.PSet(
       isMC = cms.bool(MC_flag),
       tagMatches = cms.InputTag("McMatchTag"),
       motherPdgId = cms.vint32(22,23),
       makeMCUnbiasTree = cms.bool(True),
       checkMotherInUnbiasEff = cms.bool(True),
       mcVariables = cms.PSet(
        probe_eta = cms.string("eta"),
        probe_pt  = cms.string("pt"),
        probe_phi  = cms.string("phi"),
        probe_et  = cms.string("et"),
        probe_e  = cms.string("energy"),
        probe_p  = cms.string("p"),
        probe_px  = cms.string("px"),
        probe_py  = cms.string("py"),
        probe_pz  = cms.string("pz"),
        probe_theta  = cms.string("theta"),    
        probe_vx     = cms.string("vx"),
        probe_vy     = cms.string("vy"),
        probe_vz     = cms.string("vz"),   
        probe_charge = cms.string("charge"),
        probe_rapidity  = cms.string("rapidity"),    
        probe_mass  = cms.string("mass"),
        probe_mt  = cms.string("mt"),    
        ),
        mcFlags     =  cms.PSet(
              probe_flag = cms.string("pt>0")
         ),      
       )
else:
     mcTruthCommonStuff = cms.PSet(
         isMC = cms.bool(False)
         )


## truth to --> sc electron
process.MCToSC = cms.EDAnalyzer("TagProbeFitTreeProducer",
    ## pick the defaults
    CommonStuffForSuperClusterProbe, mcTruthCommonStuff,
    #isMC = cms.bool(False), 
                     
    # choice of tag and probe pairs, and arbitration                 
    tagProbePairs = cms.InputTag("tagMC"),
    arbitration   = cms.string("Random2"),                      
    flags = cms.PSet(
        probe_passing = cms.InputTag("SCMatchedTruth")       
    ),
    probeMatches  = cms.InputTag("McMatchMC"),
    allProbes     = cms.InputTag("trueEprobes")
)
##    ____   ____       __     ____      __ 
##   / ___| / ___|      \ \   / ___|___ / _|
##   \___ \| |      _____\ \ | |  _/ __| |_ 
##    ___) | |___  |_____/ / | |_| \__ \  _|
##   |____/ \____|      /_/   \____|___/_|  

## super cluster --> gsf electron
process.SCToGsf = cms.EDAnalyzer("TagProbeFitTreeProducer",
    ## pick the defaults
    CommonStuffForSuperClusterProbe, mcTruthCommonStuff,
    # choice of tag and probe pairs, and arbitration                 
    tagProbePairs = cms.InputTag("tagSC"),
    arbitration   = cms.string("Random2"),                      
    flags = cms.PSet(
        probe_passing = cms.InputTag("GsfMatchedSuperClusterCands"),
        probe_passingGsf = cms.InputTag("GsfMatchedSuperClusterCands"),        
        probe_passingIso = cms.InputTag("IsoMatchedSuperClusterCandsClean"),
        probe_passingId = cms.InputTag("IdMatchedSuperClusterCandsClean"),        
        probe_passingALL = cms.InputTag("TagMatchedSuperClusterCandsClean"),
        probe_passing_nt_loose = cms.InputTag("NTLooseMatchedSuperClusterCands"),
        probe_passing_nt_tight = cms.InputTag("NTTightMatchedSuperClusterCands"),
        probe_passing_InvWp95  = cms.InputTag("InvWP95MatchedSuperClusterCands"),
        probe_passing_InvWp90  = cms.InputTag("InvWP90MatchedSuperClusterCands"),
        probe_passing_InvWp85  = cms.InputTag("InvWP85MatchedSuperClusterCands"),
        probe_passing_InvWp80  = cms.InputTag("InvWP80MatchedSuperClusterCands"),
        probe_passing_InvWp70  = cms.InputTag("InvWP70MatchedSuperClusterCands"),
        probe_passing_InvWp60  = cms.InputTag("InvWP60MatchedSuperClusterCands")
    ),
    probeMatches  = cms.InputTag("McMatchSC"),
    allProbes     = cms.InputTag("goodSuperClustersClean")
)
process.SCToGsf.variables.probe_dRjet = cms.InputTag("superClusterDRToNearestJet")
process.SCToGsf.variables.probe_nJets = cms.InputTag("JetMultiplicityInSCEvents")

process.T80SCToGsf = process.SCToGsf.clone()
process.T80SCToGsf.tagProbePairs = cms.InputTag("tag80SC")

process.InvWP80SCToGsf = process.SCToGsf.clone()
process.InvWP80SCToGsf.tagProbePairs = cms.InputTag("tagInvWP80SC")
process.InvWP80SCToGsf.isMC = cms.bool(False) 

process.HFSCToEID = cms.EDAnalyzer("TagProbeFitTreeProducer",
    ## pick the defaults
    CommonStuffForSuperClusterProbe, mcTruthCommonStuff,
    # choice of tag and probe pairs, and arbitration                 
    tagProbePairs = cms.InputTag("tagHFSuperClusters"),
    arbitration   = cms.string("Random2"),                      
    flags = cms.PSet(
        probe_passing = cms.InputTag("HFElectronID"),
        probe_passing_tight = cms.InputTag("HFElectronIDTight")
    ),
    probeMatches  = cms.InputTag("McMatchHFSC"),
    allProbes     = cms.InputTag("theHFSuperClusters")
)
#process.HFSCToEID.variables.probe_dRjet = cms.InputTag("superClusterDRToNearestJet")
#process.HFSCToEID.variables.probe_nJets = cms.InputTag("JetMultiplicityInSCEvents")

process.HFEID = cms.EDAnalyzer("TagProbeFitTreeProducer",
    ## pick the defaults
    CommonStuffForSuperClusterProbe, mcTruthCommonStuff,
    # choice of tag and probe pairs, and arbitration                 
    tagProbePairs = cms.InputTag("tagHFEID"),
    arbitration   = cms.string("Random2"),                      
    flags = cms.PSet(
        probe_passing = cms.InputTag("HFElectronID"),
        probe_passing_tight = cms.InputTag("HFElectronIDTight")
    ),
    probeMatches  = cms.InputTag("McMatchHF"),
    allProbes     = cms.InputTag("HFElectronID")
)
#process.HFEID.variables.probe_dRjet = cms.InputTag("superClusterDRToNearestJet")
#process.HFEID.variables.probe_nJets = cms.InputTag("JetMultiplicityInSCEvents")



process.SCSCtoTagSC = cms.EDAnalyzer("TagProbeFitTreeProducer",
    ## pick the defaults
   variables = cms.PSet(ProbeSuperClusterVariablesToStore),
   ignoreExceptions =  cms.bool (False),
   addRunLumiInfo   =  cms.bool (True),
   addEventVariablesInfo   =  cms.bool (True),
   pairVariables =  cms.PSet(ZVariablesToStore),
   pairFlags     =  cms.PSet(
          mass60to120 = cms.string("60 < mass < 120")
    ),
    tagVariables   =  cms.PSet(TagSuperClusterVariablesToStore),
    tagFlags     =  cms.PSet(
          flag = cms.string("pt>0")
    ),                                         
    isMC = cms.bool(False),
    #mcTruthCommonStuff,
    # choice of tag and probe pairs, and arbitration                      
    tagProbePairs = cms.InputTag("SCSC"),
    arbitration   = cms.string("Random2"),
    massForArbitration = cms.double(91.1876),
    flags = cms.PSet(
          probe_passing = cms.InputTag("TagMatchedSuperClusterCandsClean")
    ),
    probeMatches  = cms.InputTag("McMatchSCbad"),         
    allProbes     = cms.InputTag("badSuperClustersClean")
)

## filtered photon --> gsf electron
process.PhotonToGsf = cms.EDAnalyzer("TagProbeFitTreeProducer",
    ## pick the defaults
    mcTruthCommonStuff,
    CommonStuffForSuperClusterProbe,
    # choice of tag and probe pairs, and arbitration                 
    tagProbePairs = cms.InputTag("tagPhoton"),
    arbitration   = cms.string("Random2"),                      
    flags = cms.PSet(
        probe_passing = cms.InputTag("GsfMatchedPhotonCands"),
        probe_passingALL = cms.InputTag("TagMatchedPhotonCands")
    ),
    probeMatches  = cms.InputTag("McMatchPhoton"),
    allProbes     = cms.InputTag("FilteredPhotons")
)
process.PhotonToGsf.variables=ProbePhotonVariablesToStore

# filtered photon --> gsf electron
process.PhotonToNT = cms.EDAnalyzer("TagProbeFitTreeProducer",
    ## pick the defaults
    mcTruthCommonStuff,
    CommonStuffForSuperClusterProbe,
    # choice of tag and probe pairs, and arbitration                 
    tagProbePairs = cms.InputTag("tagNTTEID"),
    arbitration   = cms.string("Random2"),                      
    flags = cms.PSet(
        probe_passing = cms.InputTag("NTElecTight")
    ),
    probeMatches  = cms.InputTag("McMatchNT"),
    allProbes     = cms.InputTag("NTElecTight")
)
process.PhotonToNT.variables=ProbePhotonVariablesToStore

process.SCSCbad = cms.EDAnalyzer("TagProbeFitTreeProducer",
    ## pick the defaults
   #######mcTruthCommonStuff,
   variables = cms.PSet(ProbeSuperClusterVariablesToStore),
   ignoreExceptions =  cms.bool (False),
   addRunLumiInfo   =  cms.bool (True),
   addEventVariablesInfo   =  cms.bool (True),
   pairVariables =  cms.PSet(ZVariablesToStore),
   pairFlags     =  cms.PSet(
          mass60to120 = cms.string("60 < mass < 120")
          ),
   tagVariables   =  cms.PSet(TagSuperClusterVariablesToStore),
   tagFlags     =  cms.PSet(
          flag = cms.string("pt>0")
   ),                                         
   isMC = cms.bool(False),
   # choice of tag and probe pairs, and arbitration                      
   tagProbePairs = cms.InputTag("SCSC"),
   arbitration   = cms.string("Random2"),
   massForArbitration = cms.double(91.1876),
   flags = cms.PSet(
          probe_passing = cms.InputTag("TagMatchedSuperClusterCandsClean")
   ),
   #probeMatches  = cms.InputTag("McMatchSCbad"),         
   allProbes     = cms.InputTag("badSuperClustersClean")
)

process.GsfGsfToIso = cms.EDAnalyzer("TagProbeFitTreeProducer",
    ########mcTruthCommonStuff,
    CommonStuffForGsfElectronProbe,
    isMC = cms.bool(False), 
    tagProbePairs = cms.InputTag("GsfGsf"),
    arbitration   = cms.string("Random2"),
    flags = cms.PSet(
        probe_passing = cms.InputTag("PassingIsolation"),
        probe_passingGsf = cms.InputTag("PassingGsf"),
        probe_passingId = cms.InputTag("PassingId"),
        probe_passingId80 = cms.InputTag("PassingId80"),        
        probe_passingIso80 = cms.InputTag("PassingIsolation80"),
        probe_passingALL = cms.InputTag("PassingHLT"),
        probe_passingALL80 = cms.InputTag("PassingHLT80"),
        probe_passingWP95 = cms.InputTag("ElectronID95"),
        probe_passingWP90 = cms.InputTag("ElectronID90"),
        probe_passingWP85 = cms.InputTag("ElectronID85"),
        probe_passingWP80 = cms.InputTag("ElectronID80"),
        probe_passingWP70 = cms.InputTag("ElectronID70"),
        probe_passingWP60 = cms.InputTag("ElectronID60"),
        probe_passing_InvWp95  = cms.InputTag("InvWP95"),
        probe_passing_InvWp90  = cms.InputTag("InvWP90"),
        probe_passing_InvWp85  = cms.InputTag("InvWP85"),
        probe_passing_InvWp80  = cms.InputTag("InvWP80"),
        probe_passing_InvWp70  = cms.InputTag("InvWP70"),
        probe_passing_InvWp60  = cms.InputTag("InvWP60")
    ),
    probeMatches  = cms.InputTag("McMatchGsf"),
    allProbes     = cms.InputTag("PassingGsf")
)
process.GsfGsfToIso.variables.probe_dRjet = cms.InputTag("GsfDRToNearestJet")
process.GsfGsfToIso.variables.probe_nJets = cms.InputTag("JetMultiplicityInGsfEvents")



##     ____      __       __    ___           
##    / ___|___ / _|      \ \  |_ _|___  ___  
##   | |  _/ __| |_   _____\ \  | |/ __|/ _ \ 
##   | |_| \__ \  _| |_____/ /  | |\__ \ (_) |
##    \____|___/_|        /_/  |___|___/\___/ 
##   
##  gsf electron --> isolation

process.GsfToIso = cms.EDAnalyzer("TagProbeFitTreeProducer",
    mcTruthCommonStuff, CommonStuffForGsfElectronProbe,                        
    tagProbePairs = cms.InputTag("tagGsf"),
    arbitration   = cms.string("Random2"),
    flags = cms.PSet(
        probe_passing = cms.InputTag("PassingIsolation"),
        probe_passingIso = cms.InputTag("PassingIsolation"),
        probe_passingGsf = cms.InputTag("PassingGsf"),
        probe_passingId = cms.InputTag("PassingId"),
        probe_passingId80 = cms.InputTag("PassingId80"),        
        probe_passingIso80 = cms.InputTag("PassingIsolation80"),
        probe_passingALL = cms.InputTag("PassingHLT"),
        probe_passingALL80 = cms.InputTag("PassingHLT80"),
        probe_passingWP90 = cms.InputTag("ElectronID90"),
        probe_passingWP85 = cms.InputTag("ElectronID85"),
        probe_passingWP70 = cms.InputTag("ElectronID70"),
        probe_passingWP60 = cms.InputTag("ElectronID60"),
        probe_passing_InvWp95  = cms.InputTag("InvWP95"),
        probe_passing_InvWp90  = cms.InputTag("InvWP90"),
        probe_passing_InvWp85  = cms.InputTag("InvWP85"),
        probe_passing_InvWp80  = cms.InputTag("InvWP80"),
        probe_passing_InvWp70  = cms.InputTag("InvWP70"),
        probe_passing_InvWp60  = cms.InputTag("InvWP60")
    ),
    probeMatches  = cms.InputTag("McMatchGsf"),
    allProbes     = cms.InputTag("PassingGsf")
)
process.GsfToIso.variables.probe_dRjet = cms.InputTag("GsfDRToNearestJet")
process.GsfToIso.variables.probe_nJets = cms.InputTag("JetMultiplicityInGsfEvents")

process.T80GsfToIso = process.GsfToIso.clone()
process.T80GsfToIso.tagProbePairs = cms.InputTag("tag80Gsf")

process.InvWP80GsfToIso = process.GsfToIso.clone()
process.InvWP80GsfToIso.tagProbePairs = cms.InputTag("tagInvWP80Gsf")
process.InvWP80GsfToIso.isMC = cms.bool(False) 
##    ___                 __    ___    _ 
##   |_ _|___  ___        \ \  |_ _|__| |
##    | |/ __|/ _ \   _____\ \  | |/ _` |
##    | |\__ \ (_) | |_____/ /  | | (_| |
##   |___|___/\___/       /_/  |___\__,_|
##   
##  isolation --> Id

process.IsoToId = cms.EDAnalyzer("TagProbeFitTreeProducer",
    mcTruthCommonStuff, CommonStuffForGsfElectronProbe,                              
    tagProbePairs = cms.InputTag("tagIso"),
    arbitration   = cms.string("Random2"),
    flags = cms.PSet(
        probe_passing = cms.InputTag("PassingId"),
        probe_passingId = cms.InputTag("PassingId"),
        probe_passingId80 = cms.InputTag("PassingId80"),        
        probe_passingIso80 = cms.InputTag("PassingIsolation80"),
        probe_passingALL = cms.InputTag("PassingHLT"),
        probe_passingALL80 = cms.InputTag("PassingHLT80")
    ),
    probeMatches  = cms.InputTag("McMatchIso"),
    allProbes     = cms.InputTag("PassingIsolation")
)
process.IsoToId.variables.probe_dRjet = cms.InputTag("GsfDRToNearestJet")
process.IsoToId.variables.probe_nJets = cms.InputTag("JetMultiplicityInGsfEvents")

process.IsoToId80 = cms.EDAnalyzer("TagProbeFitTreeProducer",
    mcTruthCommonStuff, CommonStuffForGsfElectronProbe,                              
    tagProbePairs = cms.InputTag("tagIso80"),
    arbitration   = cms.string("Random2"),
    flags = cms.PSet(
        probe_passing = cms.InputTag("PassingId80"),
        probe_passingId = cms.InputTag("PassingId80"),
        probe_passingId95 = cms.InputTag("PassingId"),        
        probe_passingALL = cms.InputTag("PassingHLT"),
        probe_passingALL80 = cms.InputTag("PassingHLT80")
    ),
    probeMatches  = cms.InputTag("McMatchIso"),
    allProbes     = cms.InputTag("PassingIsolation80")
)
process.IsoToId80.variables.probe_dRjet = cms.InputTag("GsfDRToNearestJet")
process.IsoToId80.variables.probe_nJets = cms.InputTag("JetMultiplicityInGsfEvents")

##    ___    _       __    _   _ _   _____ 
##   |_ _|__| |      \ \  | | | | | |_   _|
##    | |/ _` |  _____\ \ | |_| | |   | |  
##    | | (_| | |_____/ / |  _  | |___| |  
##   |___\__,_|      /_/  |_| |_|_____|_|  

##  Id --> HLT
process.IdToHLT = cms.EDAnalyzer("TagProbeFitTreeProducer",
    mcTruthCommonStuff, CommonStuffForGsfElectronProbe,                             
    tagProbePairs = cms.InputTag("tagId"),
    arbitration   = cms.string("Random2"),
    flags = cms.PSet(
        probe_passing = cms.InputTag("PassingHLT"),
        probe_passing80 = cms.InputTag("PassingHLT80"),
        probe_passingId = cms.InputTag("PassingId"),
        probe_passingId80 = cms.InputTag("PassingId80"),
    ),
    probeMatches  = cms.InputTag("McMatchId"),
    allProbes     = cms.InputTag("PassingId")
)
process.IdToHLT.variables.probe_dRjet = cms.InputTag("GsfDRToNearestJet")
process.IdToHLT.variables.probe_nJets = cms.InputTag("JetMultiplicityInGsfEvents")

process.IdToHLT80 = cms.EDAnalyzer("TagProbeFitTreeProducer",
    mcTruthCommonStuff, CommonStuffForGsfElectronProbe,                             
    tagProbePairs = cms.InputTag("tagId80"),
    arbitration   = cms.string("Random2"),
    flags = cms.PSet(
        probe_passing = cms.InputTag("PassingHLT80"),
        probe_passing95 = cms.InputTag("PassingHLT"),
    ),
    probeMatches  = cms.InputTag("McMatchId"),
    allProbes     = cms.InputTag("PassingId80")
)
process.IdToHLT80.variables.probe_dRjet = cms.InputTag("GsfDRToNearestJet")
process.IdToHLT80.variables.probe_nJets = cms.InputTag("JetMultiplicityInGsfEvents")
process.tree_sequence = cms.Sequence(
    process.SCToGsf + process.SCSCtoTagSC +
    process.SCSCbad + process.GsfGsfToIso + process.InvWP80GsfToIso + process.InvWP80SCToGsf +
    process.PhotonToGsf + process.HFEID + process.PhotonToNT +
    process.GsfToIso +
    process.IsoToId + process.IdToHLT +
    process.IsoToId80 + process.IdToHLT80 +
    process.HFSCToEID + 
    process.T80SCToGsf +
    process.T80GsfToIso 
)    
 
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("testNewWrite.root")
                                   )


##    ____       _   _     
##   |  _ \ __ _| |_| |__  
##   | |_) / _` | __| '_ \ 
##   |  __/ (_| | |_| | | |
##   |_|   \__,_|\__|_| |_|
##


#process.MyHLTHLTEle15SWL1R =  process.PassingHLT.clone()
#process.MyHLTHLTEle15SWL1R.hltTag =  cms.untracked.InputTag("HLT_Ele15_SW_L1R", "", myHLT)

#process.TreeHLTHLTEle15SWL1R =  process.IdToHLT.clone()
#process.TreeHLTHLTEle15SWL1R.flags = cms.PSet( probe_passing = cms.InputTag("MyHLTHLTEle15SWL1R"))
#process.TreeHLTHLTEle15SWL1R.tagProbePairs =  cms.InputTag("tagGsf")

#process.MyHLTHLTEle15LWL1R =  process.PassingHLT.clone()
#process.MyHLTHLTEle15LWL1R.hltTag =  cms.untracked.InputTag("HLT_Ele15_LW_L1R", "", myHLT)

#process.TreeHLTHLTEle15LWL1R =  process.IdToHLT.clone()
#process.TreeHLTHLTEle15LWL1R.flags = cms.PSet( probe_passing = cms.InputTag("MyHLTHLTEle15LWL1R"))
#process.TreeHLTHLTEle15LWL1R.tagProbePairs =  cms.InputTag("tagGsf")

#process.MyHLTHLTEle20SWL1R =  process.PassingHLT.clone()
#process.MyHLTHLTEle20SWL1R.hltTag =  cms.untracked.InputTag("HLT_Ele20_SW_L1R", "", myHLT)

#process.TreeHLTHLTEle20SWL1R =  process.IdToHLT.clone()
#process.TreeHLTHLTEle20SWL1R.flags = cms.PSet( probe_passing = cms.InputTag("MyHLTHLTEle20SWL1R"))
#process.TreeHLTHLTEle20SWL1R.tagProbePairs =  cms.InputTag("tagGsf")

#process.MyHLTHLTEle20LWL1R =  process.PassingHLT.clone()
#process.MyHLTHLTEle20LWL1R.hltTag =  cms.untracked.InputTag("HLT_Ele20_LW_L1R", "", myHLT)

#process.TreeHLTHLTEle20LWL1R =  process.IdToHLT.clone()
#process.TreeHLTHLTEle20LWL1R.flags = cms.PSet( probe_passing = cms.InputTag("MyHLTHLTEle20LWL1R"))
#process.TreeHLTHLTEle20LWL1R.tagProbePairs =  cms.InputTag("tagGsf")

#process.HLTSeq = cms.Sequence(process.MyHLTHLTEle15SWL1R + process.MyHLTHLTEle15LWL1R + process.MyHLTHLTEle20SWL1R + process.MyHLTHLTEle20LWL1R )
#process.HLTTSeq = cms.Sequence(process.TreeHLTHLTEle15SWL1R + process.TreeHLTHLTEle15LWL1R + process.TreeHLTHLTEle20SWL1R + process.TreeHLTHLTEle20LWL1R )

process.sceff = cms.Sequence(
    process.trueEprobes + 
    process.tagMC +
    process.SCMatchedTruth +
    process.McMatchMC + 
    process.MCToSC
)

process.tagAndProbe = cms.Path(
            process.hfEMClusteringSequence +
            #process.gsfElectrons +
            process.sc_sequence + process.ele_sequence + 
            process.mc_sequence + 
            process.ext_ToNearestJet_sequence + 
            process.allTagsAndProbes + 
            process.sceff +
            process.tree_sequence #+ 
            #process.HLTSeq + process.HLTTSeq
)


