process.load("RecoEgamma.EgammaHFProducers.hfEMClusteringSequence_cff")
process.load("ZShape.EffAcc.fullSimLoader_cff")
process.hfRecoEcalCandidateMC.intercept2DCut = cms.double(-99)
process.hfRecoEcalCandidateMC.intercept2DSlope = cms.double(-99)
process.hfRecoEcalCandidateMC.e9e25Cut = cms.double(0)


process.p = cms.Path(process.hfRecoEcalCandidateMC+process.f2s_sequence
