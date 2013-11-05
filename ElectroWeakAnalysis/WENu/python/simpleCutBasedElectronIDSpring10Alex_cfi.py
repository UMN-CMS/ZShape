import FWCore.ParameterSet.Config as cms

## Electron ID Based on Simple Cuts
#
# Designed to be imported by simpleCutBasedElectronIDSpring10_cfi
#
# These cuts are based on the ones found here:
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SimpleCutBasedEleID2011
#
# The have the following form:
# barrel =  cms.vdouble(
#     9999.,  # > H/E
#     0.010,  # > Sigma_iEta_iEta
#     0.020,  # > | Delta Phi_in |
#     0.004,  # > | Delta Eta_in |
#     -1,     # < e2x5/e5x5
#     -1,     # < e1x5/e5x5
#     9999.,  # > isoTK
#     9999.,  # > ecalIso
#     9999.,  # > hcalIso
#     9999.,  # > hcalIso 1 depth
#     9999.,  # > hcalIso 2 depth
#     9999.,  # > isoTK / electron pt
#     9999.,  # > ecalIso / electron pt
#     9999.,  # > hcalIso / electron pt
#     9999.,  # > isoTK + ecalIso + hcalIso - rhoCorrection
#     0.016,  # > (isoTK + ecalIso + hcalIso - rhoCorrection) / electron pt
#     9999.,  # > isoTK + ecalIsoPed + hcalIso - rhoCorrection
#     9999.,  # > (isoTK + ecalIsoPed + hcalIso - rhoCorrection) / electron pt
#     0.0,    # <= Sigma_iEta_iEta
#     -9999., # < E/P
#     9999.,  # > E/P
#     9999.,  # < IP ????
#     0,      # < missing_hits
#     -1,     # > 0 ???
#     0.02,   # > dist for conversion
#     0.02,   # > dcot for conversion
# )
#
# And the same for the endcap

# This cut is _NOT_ WP90 or anything like it. It is CaloIdL_CaloIsoVL as used
# by the 2011 HLT trigger

hijacked90 = cms.PSet(
        barrel =  cms.vdouble(
            0.15, 9999., 9999., 9999., -1, -1, 9999., 9999., 9999., 9999.,
            9999., 9999., 0.2, 0.2, 9999., 9999., 9999., 9999., 0.0, -9999.,
            9999., 9999., 0, -1, 0.0, 0.0
            ),
        endcap = cms.vdouble(
            0.1, 9999., 9999., 9999., -1, -1, 9999., 9999., 9999., 9999.,
            9999., 9999., 0.2, 0.2, 9999., 9999., 9999., 9999., 0.0, -9999.,
            9999., 9999., 0, -1, 0.0, 0.0
            ),
        )

# This cut is _NOT_ WP85 or anything like it. It is
# CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT as used by the 2011 HLT trigger, although
# that also requires a R9 < 0.98 (999999.9)

hijacked85 = cms.PSet(
        barrel =  cms.vdouble(
            0.05, 0.011, 0.07, 0.008, -1, -1, 9999., 9999., 9999., 9999.,
            9999., 0.05, 0.05, 0.05, 9999., 9999., 9999., 9999., 0.0, -9999.,
            9999., 9999., 0, -1, 0.0, 0.0
            ),
        endcap = cms.vdouble(
            0.05, 0.031, 0.05, 0.008, -1, -1, 9999., 9999., 9999., 9999.,
            9999., 0.05, 0.05, 0.05, 9999., 9999., 9999., 9999., 0.0, -9999.,
            9999., 9999., 0, -1, 0.0, 0.0
            ),
        )
# Remove relative

# The cuts below are based on
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SimpleCutBasedEleID2011
ele95V20 = cms.PSet(
        barrel =  cms.vdouble(
            9999., 0.012, 0.8, 0.007, -1, -1, 9999., 9999., 9999., 9999.,
            9999., 9999., 9999., 9999., 9999., 0.150, 9999., 9999., 0.0,
            -9999., 9999., 9999., 0, -1, 0.0, 0.0
            ),
        endcap =  cms.vdouble(
            9999., 0.031, 0.7, 0.011, -1, -1, 9999., 9999., 9999., 9999.,
            9999., 9999., 9999., 9999., 9999., 0.100, 9999., 9999., 0.0,
            -9999., 9999., 9999., 0, -1, 0.0, 0.0
            ),
        )
ele90V20 = cms.PSet(
        barrel =  cms.vdouble(
            9999., 0.010, 0.071, 0.007, -1, -1, 9999., 9999., 9999., 9999.,
            9999., 9999., 9999., 9999., 9999., 0.085, 9999., 9999., 0.0,
            -9999., 9999., 9999., 0, -1, 0.0, 0.0
            ),
        endcap =  cms.vdouble(
            9999., 0.031, 0.047, 0.011, -1, -1, 9999., 9999., 9999., 9999.,
            9999., 9999., 9999., 9999., 9999., 0.051, 9999., 9999., 0.0,
            -9999., 9999., 9999., 0, -1, 0.0, 0.0
            ),
        )
ele85V20 = cms.PSet(
        barrel =  cms.vdouble(
            9999., 0.010, 0.039, 0.005, -1, -1, 9999., 9999., 9999., 9999.,
            9999., 9999., 9999., 9999., 9999., 0.053, 9999., 9999., 0.0,
            -9999., 9999., 9999., 0, -1, 0.02, 0.02
            ),
        endcap =  cms.vdouble(
            9999., 0.031, 0.028, 0.007, -1, -1, 9999., 9999., 9999., 9999.,
            9999., 9999., 9999., 9999., 9999., 0.042, 9999., 9999., 0.0,
            -9999., 9999., 9999., 0, -1, 0.02, 0.02
            ),
        )
ele80V20 = cms.PSet(
        barrel =  cms.vdouble(
            9999., 0.010, 0.027, 0.005, -1, -1, 9999., 9999., 9999., 9999.,
            9999., 9999., 9999., 9999., 9999., 0.040, 9999., 9999., 0.0,
            -9999., 9999., 9999., 0, -1, 0.02, 0.02
            ),
        endcap =  cms.vdouble(
            9999., 0.031, 0.021, 0.006, -1, -1, 9999., 9999., 9999., 9999.,
            9999., 9999., 9999., 9999., 9999., 0.033, 9999., 9999., 0.0,
            -9999., 9999., 9999., 0, -1, 0.02, 0.02
            ),
        )
ele70V20 = cms.PSet(
        barrel =  cms.vdouble(
            9999., 0.010, 0.020, 0.004, -1, -1, 9999., 9999., 9999., 9999.,
            9999., 9999., 9999., 9999., 9999., 0.030, 9999., 9999., 0.0,
            -9999., 9999., 9999., 0, -1, 0.02, 0.02
            ),
        endcap =  cms.vdouble(
            9999., 0.031, 0.021, 0.005, -1, -1, 9999., 9999., 9999., 9999.,
            9999., 9999., 9999., 9999., 9999., 0.016, 9999., 9999., 0.0,
            -9999., 9999., 9999., 0, -1, 0.02, 0.02
            ),
        )
ele60V20 = cms.PSet(
        barrel =  cms.vdouble(
            9999., 0.010, 0.020, 0.004, -1,   -1,   9999., 9999., 9999., 9999.,
            9999., 9999., 9999., 9999., 9999., 0.016, 9999., 9999., 0.0, -9999.,
            9999., 9999., 0, -1, 0.02, 0.02
            ),
        endcap =  cms.vdouble(
            9999., 0.031, 0.021, 0.004, -1, -1, 9999., 9999., 9999., 9999.,
            9999., 9999., 9999., 9999., 9999., 0.008, 9999., 9999., 0.0,
            -9999., 9999., 9999., 0, -1, 0.02,  0.02
            ),
        )
