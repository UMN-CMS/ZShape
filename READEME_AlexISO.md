# Electron Efficiency at High Pileup

The Higgs to WW group has modified definitions of the Working Points for electrons. These can be found here: https://twiki.cern.ch/twiki/bin/viewauth/CMS/SimpleCutBasedEleID2011

## Set Up

In simpleCutBasedElectronIDSpring10_cfi.py you'll need to make sure that you're using V20:

  simpleCutBasedElectronID = cms.EDProducer("EleIdCutBasedExtProducer",
  ...
  electronVersion = cms.string('V20'),
  ...
  )

To include the cuts in your analysis you'll have to add the following to your cfg.py:
```python
## Electron ID cuts
process.load("RecoLocalCalo.EcalRecAlgos.EcalSeverityLevelESProducer_cfi")
process.load("ElectroWeakAnalysis.WENu.simpleEleIdSequence_cff")
process.patElectronIDs = cms.Sequence(process.simpleEleIdSequence)
```
### Example Cuts

The cuts are defined in simpleCutBasedElectronIDSpring10_cfi.py as follows:
```python
    robust60cIsoEleIDCutsV20 = cms.PSet(
            barrel =  cms.vdouble(
                9999.,  # > H/E
                0.010,  # > Sigma_iEta_iEta
                0.020,    # > | Delta Phi_in |
                0.004,  # > | Delta Eta_in |
                -1,     # < e2x5/e5x5
                -1,     # < e1x5/e5x5
                9999.,  # > isoTK
                9999.,  # > ecalIso
                9999.,  # > hcalIso
                9999.,  # > hcalIso 1 depth
                9999.,  # > hcalIso 2 depth
                9999.,  # > isoTK / electron pt
                9999.,  # > ecalIso / electron pt
                9999.,  # > hcalIso / electron pt
                9999.,  # > isoTK + ecalIso + hcalIso - rhoCorrection
                0.016,  # > (isoTK + ecalIso + hcalIso - rhoCorrection) / electron pt
                9999.,  # > isoTK + ecalIsoPed + hcalIso - rhoCorrection
                9999.,  # > (isoTK + ecalIsoPed + hcalIso - rhoCorrection) / electron pt
                0.0,    # <= Sigma_iEta_iEta
                -9999., # < E/P
                9999.,  # > E/P
                9999.,  # < IP ????
                0,      # < missing_hits
                -1,     # > 0 ???
                0.02,    # > dist for conversion
                0.02,    # > dcot for conversion
                ),
            endcap =  cms.vdouble(
                9999.,  # > H/E
                0.031,  # > Sigma_iEta_iEta
                0.021,    # > | Delta Phi_in |
                0.004,  # > | Delta Eta_in |
                -1,     # < e2x5/e5x5
                -1,     # < e1x5/e5x5
                9999.,  # > isoTK
                9999.,  # > ecalIso
                9999.,  # > hcalIso
                9999.,  # > hcalIso 1 depth
                9999.,  # > hcalIso 2 depth
                9999.,  # > isoTK / electron pt
                9999.,  # > ecalIso / electron pt
                9999.,  # > hcalIso / electron pt
                9999.,  # > isoTK + ecalIso + hcalIso - rhoCorrection
                0.008,  # > (isoTK + ecalIso + hcalIso - rhoCorrection) / electron pt
                9999.,  # > isoTK + ecalIsoPed + hcalIso - rhoCorrection
                9999.,  # > (isoTK + ecalIsoPed + hcalIso - rhoCorrection) / electron pt
                0.0,    # <= Sigma_iEta_iEta
                -9999., # < E/P
                9999.,  # > E/P
                9999.,  # < IP ????
                0,      # < missing_hits
                -1,     # > 0 ???
                0.02,    # > dist for conversion
                0.02,    # > dcot for conversion
                ),
            ),
```
### Jets

The isolation calculation requires kt6PFJets. If these are missing, you can produce by adding the process below:

```python
## Jets for Isolation Cuts
process.load('RecoJets.JetProducers.kt4PFJets_cfi') # For isolation calculation
process.kt6PFJets = process.kt4PFJets.clone(
        rParam = 0.6,
        doRhoFastjet = True,
        Rho_EtaMax = cms.double(2.5),
        )
```
