# produces cones around electrons type 1
# reconstructing electrons and provides smearing

import FWCore.ParameterSet.Config as cms

FullSimSmearedElectronsProducer = cms.EDProducer("ZSmearingProducer",
    zsrc = cms.untracked.InputTag("fullSimLoad","ZEventParticles"),
    zElectronsCollection = cms.untracked.InputTag("fullSimLoad","ZEventParticles"),
    doSmearing = cms.untracked.bool(True),
    doEB= cms.untracked.bool(True),
    doEE= cms.untracked.bool(True),
    doHFenergy= cms.untracked.bool(True),
    doHFeta= cms.untracked.bool(False),
    doHFphi= cms.untracked.bool(False),
    quiet = cms.untracked.bool(True),
    zElectronsCone = cms.double(0.08),
    randomSeed = cms.int32(134),
    SmearTable = cms.FileInPath('ZShape/EffAcc/data/CBBinsFile.txt'),
    HF = cms.PSet(
       stocastic = cms.double(0.0),
       constantp = cms.double(0.070),#088),#uncert 0.02
       constantm = cms.double(0.070),#090),#uncert 0.0143
       constantp2 = cms.double(0.070),#uncert 0.02
       constantm2 = cms.double(0.070),#uncert 0.0143
       fraction2 = cms.double(0.00),
       meanp = cms.double(0.983),#985),  #uncert 0.007 
       meanm = cms.double(0.967),#986),  #uncert 0.009
       reseta = cms.double(0.001),
       resphi = cms.double(0.001)
       ),
    EB = cms.PSet(
       p0 = cms.double(0.0) , 
       p1 = cms.double(0.0),
       p2 = cms.double(0.0),
       c = cms.double(0.01),# uncertainty 0.002 
       alpha = cms.double(1.0), #doesn't matter with n=0
       mean = cms.double(0.993),  #uncertainty 0.00025
       n = cms.double(0.0)
   
    ),
     EE = cms.PSet(
   
       p0 = cms.double(0.0) , 
       p1 = cms.double(0.0),
       p2 = cms.double(0.0),
       c = cms.double(0.024), #uncertainty 0.016
       alpha = cms.double(1.0), #doesn't matter with n=0
       mean = cms.double(0.968),  #uncertainty 0.0007
       n = cms.double(0.0)
   
    )
)
