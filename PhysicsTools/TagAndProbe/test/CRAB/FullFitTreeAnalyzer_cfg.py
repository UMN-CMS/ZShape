import FWCore.ParameterSet.Config as cms

process = cms.Process("TagProbe")
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1000


process.TagProbeFitTreeAnalyzer = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
    # IO parameters:
    #InputFileNames = cms.vstring("/data/whybee0c/user/haupt/Electrons/TNPTREE10/TagProbeTreeTRIAL/FullZHLT.root"),
    #InputFileNames = cms.vstring("/data/cms004/oradata/myTNPOct10th.root"),
    #InputFileNames = cms.vstring("/data/whybee1a/user/haupt/Electrons/TNPTREE10/TnPSept17thReReco.root"),
    #InputFileNames = cms.vstring("/data/whybee1a/user/haupt/Electrons/TNPTREE10/TnP.5.3invpb.root"),
    #InputFileNames = cms.vstring("/data/whybee1a/user/haupt/Electrons/TNPTREE10/TnP.Oct20thAB.root"),
    #InputFileNames = cms.vstring("/data/whybee1a/user/haupt/Electrons/TNPTREE10/TnP.Oct20thABFULL.root"),     
    #InputFileNames = cms.vstring("/data/whybee1a/user/haupt/Electrons/TNPTREE10/TnP.Oct23JSON.root"),    
    #InputFileNames = cms.vstring("/data/whybee1a/user/haupt/Electrons/TNPTREE10/TnP.Oct26thJSON.root"),    
    #InputFileNames = cms.vstring("/data/whybee1a/user/haupt/Electrons/TNPTREE10/TnpT.NEW5.3.root"),                                             
    #InputFileNames = cms.vstring("/data/whybee1a/user/haupt/Electrons/TNPTREE10/TnP.Dec8th.root"),
    #InputFileNames  = cms.vstring("/data/whybee1a/user/haupt/Electrons/TNPTREE10/TNPDECRERECO.root"),
    #InputFileNames  = cms.vstring("/data/whybee1a/user/haupt/Electrons/TNPTREE10/TnP.NewDec18th.root"),
    #InputFileNames  = cms.vstring("/data/whybee1a/user/haupt/Electrons/TNPTREE10/FullTagProbeTree/TnP.Dec22AN.root"),
    InputFileNames  = cms.vstring("/data/whybee1a/user/haupt/Electrons/TNPTREE10/TnP.DEC22ndFULL.root"),                                    
    #InputFileNames  = cms.vstring("/data/whybee1a/user/haupt/Electrons/TNPTREE10/MCFullTagProbeTree/MCTnP.root"),
                                                                                            
    InputDirectoryName = cms.string("GsfToIso"),
    InputTreeName = cms.string("fitter_tree"),
    OutputFileName = cms.string("testEff_GSFToISO.root"),
    #numbrer of CPUs to use for fitting
    NumCPU = cms.uint32(1),
    # specifies wether to save the RooWorkspace containing the data for each bin and
    # the pdf object with the initial and final state snapshots
    SaveWorkspace = cms.bool(True),
    floatShapeParameters = cms.bool(True),
    fixVars = cms.vstring("mean"),
                                                 
    # defines all the real variables of the probes available in the input tree and intended for use in the efficiencies
    Variables = cms.PSet(
        mass = cms.vstring("Tag-Probe Mass", "40.0", "150.0", "GeV/c^{2}"),
        probe_sc_et = cms.vstring("Probe p_{T}", "0", "1000", "GeV/c"),
        probe_sc_eta = cms.vstring("Probe #eta", "-2.5", "2.5", ""),
        pair_rapidity =  cms.vstring("Z Rapidity", "-3.75", "3.75", "")
    ),

    # defines all the discrete variables of the probes available in the input tree and intended for use in the efficiency calculations
    Categories = cms.PSet(
        mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
        probe_passing = cms.vstring("Probe Passing", "dummy[pass=1,fail=0]"),
        probe_passingIso80 = cms.vstring("Probe Passing Iso 80", "dummy[pass=1,fail=0]"),
        probe_passingId = cms.vstring("Probe Passing Id", "dummy[pass=1,fail=0]"),
        probe_passingId80 = cms.vstring("Probe Passing Id 80", "dummy[pass=1,fail=0]"),
        probe_passing_tight = cms.vstring("Probe Passing Tight HF EID", "dummy[pass=1,fail=0]"),
        probe_passingGsf  = cms.vstring("Probe Passing GSF", "dummy[pass=1,fail=0]"),
        probe_passing_nt_tight = cms.vstring("Probe Passing No Track Tight", "dummy[pass=1,fail=0]"),
        probe_passing_nt_loose = cms.vstring("Probe Passing No Track Loose", "dummy[pass=1,fail=0]"),
        probe_passingWP90 = cms.vstring("Probe Passing WP90", "dummy[pass=1,fail=0]"),
        probe_passingWP85 = cms.vstring("Probe Passing WP85", "dummy[pass=1,fail=0]"),
        probe_passingWP70 = cms.vstring("Probe Passing WP70", "dummy[pass=1,fail=0]"),
        probe_passingWP60 = cms.vstring("Probe Passing WP60", "dummy[pass=1,fail=0]")
    ),

    # defines all the PDFs that will be available for the efficiency calculations; uses RooFit's "factory" syntax;
    # each pdf needs to define "signal", "backgroundPass", "backgroundFail" pdfs, "efficiency[0.9,0,1]" and "signalFractionInPassing[0.9]" are used for initial values  
    PDFs = cms.PSet(
        gaussPlusLinear = cms.vstring(
            "Gaussian::signal(mass, mean[91.2, 89.0, 93.0], sigma[2.3, 0.5, 10.0])",
            "RooExponential::backgroundPass(mass, cPass[0,-10,10])",
            "RooExponential::backgroundFail(mass, cFail[0,-10,10])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
        xxInputPtBinnedPDFsxx
        xxInputEtaBinnedPDFsxx
        xxInputPtEtaBinnedPDFsxx
        xxInputHFPtBinnedPDFsxx
        xxInputHFEtaBinnedPDFsxx
        xxInputHFPtEtaBinnedPDFsxx
        xxInputNTPtBinnedPDFsxx
        xxInputNTEtaBinnedPDFsxx
        xxInputNTPtEtaBinnedPDFsxx
        xxInputRapBinnedPDFsxx
        xxInputHFRapBinnedPDFsxx
        voigtPlusBKG = cms.vstring(
             "Voigtian::signal(mass, mean[91.2,85,96], width[2.495], sigma[2.3,1,9])",
             #"expr::erf('RooMath::erfc((alpha - mass) * beta);',mass,alpha[62.0,35.0,105.0],beta[0.051,0.0,0.2])",
             #"expr::un('(mass-peak)*gamma',mass,peak[91.1876],gamma[0.05, 0.0, 0.1])",
             #"expr::bn(' ( un < -70  )* (1e20) + ( un > 70 )* (0.0) + ( un >= -70 && un <= 70) * exp(-un)',un)",
             #"EXPR::backgroundPass('bn*erf',bn,erf,mass,peak,gamma,beta,alpha)",
             #"EXPR::backgroundFail('bn*erf',bn,erf,mass,peak,gamma,beta,alpha)",
             "EXPR::backgroundPass('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak[91.1876],gamma[0.05, 0.0, 0.1],beta[0.051,0.0,0.2],alpha[62.0,35.0,105.0])",
             "EXPR::backgroundFail('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak,gamma,beta,alpha)",
             "efficiency[0.9,0,1]",
             "signalFractionInPassing[0.9]"
        ),
        voigtPlusBKGBKGFIXED = cms.vstring(
             "Voigtian::signal(mass, mean[91.2,85,96], width[2.495], sigma[2.3,1,9])",
             "EXPR::backgroundPass('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak[91.1876],gamma[0.025],beta[0.095],alpha[49.5])",
             "EXPR::backgroundFail('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak,gamma,beta,alpha)",
             "efficiency[0.9,0,1]",
             "signalFractionInPassing[0.9]"
        ), 
        voigtPlusBKGHFALLFIXED = cms.vstring(
             "Voigtian::signal(mass, mean[93], width[2.495], sigma[6.7])",
             "EXPR::backgroundPass('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak[91.1876],gamma[0.025],beta[0.071],alpha[65.0])",
             "EXPR::backgroundFail('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak,gamma,beta,alpha)",
             "efficiency[0.9,0,1]",
             "signalFractionInPassing[0.9]"
        ),
        ZlinePlusBKGBKGFIXED = cms.vstring(
             #'ZGeneratorLineShape::signal(mass,\"/data/whybee1a/user/haupt/Electrons/TNPTREE10/testProdZEfficiencySmeared_10MTEMPLATE/MCHist.root\",\"mcEff/ECAL80-ECAL95/C07-HLT-GSF/Z0_mass\")',
             #'zg["ZeeGenLevel.root"]'
             #'ms["Mass"]',
             #'#signal ZeeGenLevel.root Mass',
             #'#signal /data/whybee1a/user/haupt/Electrons/TNPTREE10/testProdZEfficiencySmeared_10MTEMPLATE/MCHist.root mcEff/ECAL80-ECAL95/C07-HLT-GSF/Z0_mass',
        '#signal /data/whybee1a/user/haupt/Electrons/TNPTREE10/testProdZEfficiencySmeared_10MTEMPLATE/MCHistZ2New.root mcEff/ECAL80-ECAL95/C07-HLT-GSF/Z0_mass',
             "EXPR::backgroundPass('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak[91.1876],gamma[0.025],beta[0.095],alpha[49.5])",
             "EXPR::backgroundFail('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak,gamma,beta,alpha)",
             "efficiency[0.9,0,1]",
             "signalFractionInPassing[0.9]"
        ),
        ZlinePlusBKGHFALLFIXED = cms.vstring(
             #'#signal /data/whybee1a/user/haupt/Electrons/TNPTREE10/testProdZEfficiencySmeared_10MTEMPLATE/MCHist.root mcEff/ECAL80-HF/C07-HLT-GSF/Z0_mass',
             '#signal /data/whybee1a/user/haupt/Electrons/TNPTREE10/testProdZEfficiencySmeared_10MTEMPLATE/MCHistZ2New.root mcEff/ECAL80-HF/C07-HLT-GSF/Z0_mass',
             #'ZGeneratorLineShape::signal(mass,"/data/whybee1a/user/haupt/Electrons/TNPTREE10/testProdZEfficiencySmeared_10MTEMPLATE/MCHist.root","mcEff/ECAL80-HF/C07-HLT-GSF/Z0_mass")',           
             "EXPR::backgroundPass('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak[91.1876],gamma[0.025],beta[0.071],alpha[65.0])",
             "EXPR::backgroundFail('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak,gamma,beta,alpha)",
             "efficiency[0.9,0,1]",
             "signalFractionInPassing[0.9]"
        ),
        BKGasSignal = cms.vstring(
             "expr::erf('RooMath::erfc((alpha - mass) * beta);',mass,alpha[62.0,35.0,105.0],beta[0.051,0.0,0.23])",
             "expr::un('(mass-peak)*gamma',mass,peak[91.1876],gamma[0.05, 0.0, 0.1])",
             "expr::bn(' ( un < -70  )* (1e20) + ( un > 70 )* (0.0) + ( un >= -70 && un <= 70) * exp(-un)',un)",
             "EXPR::signal('bn*erf',bn,erf)",
             "EXPR::backgroundPass('0.0*mass',mass)",
             "EXPR::backgroundFail('0.0*mass',mass)",
             "efficiency[0.9,0.1.0]",
             "signalFractionInPassing[0.9]"
        ),
        BKGasSplit = cms.vstring(
             "expr::erfp('RooMath::erfc((alphap - mass) * betap);',mass,alphap[62.0,40.0,105.0],betap[0.051,0.0,0.23])",
             "expr::erff('RooMath::erfc((alphaf - mass) * betaf);',mass,alphaf[62.0,40.0,105.0],betaf[0.051,0.0,0.23])",
             "expr::unp('(mass-peakp)*gammap',mass,peakp[91.1876],gammap[0.05, 0.0, 0.1])",
             "expr::unf('(mass-peakf)*gammaf',mass,peakf[91.1876],gammaf[0.05, 0.0, 0.1])",
             "expr::bnp(' ( unp < -70  )* (1e20) + ( unp > 70 )* (0.0) + ( unp >= -70 && unp <= 70) * exp(-unp)',unp)",
             "expr::bnf(' ( unf < -70  )* (1e20) + ( unf > 70 )* (0.0) + ( unf >= -70 && unf <= 70) * exp(-unf)',unf)",
             "EXPR::signal('0.0*mass',mass)",
             "EXPR::backgroundPass('bnp*erfp',bnp,erfp)",
             "EXPR::backgroundFail('bnf*erff',bnf,erff)",
             "efficiency[0.9,0,1]",
             "signalFractionInPassing[0.9]"
        ),
        JustVoigt = cms.vstring(
             "Voigtian::signal(mass, mean[91.2,85,96], width[2.495], sigma[2.3,1,9])",
             "EXPR::backgroundPass('0.0*mass',mass)",
             "EXPR::backgroundFail('0.0*mass',mass)",
             "efficiency[0.9,0,1]",
             "signalFractionInPassing[0.9]"
        )
    ),

    # defines a set of efficiency calculations, what PDF to use for fitting and how to bin the data;
    # there will be a separate output directory for each calculation that includes a simultaneous fit, side band subtraction and counting. 
    Efficiencies = cms.PSet(
        #the name of the parameter set becomes the name of the directory
        pt = cms.PSet(
            #specifies the efficiency of which category and state to measure 
            EfficiencyCategoryAndState = cms.vstring("probe_passing","pass"),
            #specifies what unbinned variables to include in the dataset, the mass is needed for the fit
            UnbinnedVariables = cms.vstring("mass"),
            #specifies the binning of parameters
            BinnedVariables = cms.PSet(
                probe_sc_et = cms.vdouble(20, 25, 30, 35, 40, 50, 120)
                #probe_sc_et = cms.vdouble(20, 30, 50, 120)
            ),
            #first string is the default followed by binRegExp - PDFname pairs
            BinToPDFmap = cms.vstring(xxPtBinMapxx)
        ),
        eta = cms.PSet(
            EfficiencyCategoryAndState = cms.vstring("probe_passing","pass"),
            UnbinnedVariables = cms.vstring("mass"),
            BinnedVariables = cms.PSet(
                probe_sc_eta = cms.vdouble(-2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0,  2.5)
            ),
            BinToPDFmap = cms.vstring(xxEtaBinMapxx)
        ),
	pt_eta = cms.PSet(
            EfficiencyCategoryAndState = cms.vstring("probe_passing","pass"),
            UnbinnedVariables = cms.vstring("mass"),
            BinnedVariables = cms.PSet(
                probe_sc_eta = cms.vdouble(-2.5, -1.5, 0.0, 1.5, 2.5),
                probe_sc_et = cms.vdouble(20, 30, 35, 40, 50, 120)
            ),
            BinToPDFmap = cms.vstring(xxPtEtaBinMapxx)
        ),
        
    )
)


#process.TagProbeFitTreeAnalyzer.Efficiencies.pt.BinToPDFmap = cms.vstring("JustVoigt")
#process.TagProbeFitTreeAnalyzer.Efficiencies.eta.BinToPDFmap = cms.vstring("JustVoigt")
#process.TagProbeFitTreeAnalyzer.Efficiencies.pt_eta.BinToPDFmap = cms.vstring("JustVoigt")

process.TPFTASCToGSF = process.TagProbeFitTreeAnalyzer.clone()
process.TPFTASCToGSF.InputDirectoryName = cms.string("SCToGsf")
process.TPFTASCToGSF.OutputFileName = cms.string("testEff_SCToGSF.root")

process.TPFTAGSFToISO80 = process.TagProbeFitTreeAnalyzer.clone()
process.TPFTAGSFToISO80.OutputFileName = cms.string("testEff_GSFToISO80.root")
process.TPFTAGSFToISO80.Efficiencies.pt.EfficiencyCategoryAndState  = cms.vstring("probe_passingIso80","pass")
process.TPFTAGSFToISO80.Efficiencies.eta.EfficiencyCategoryAndState = cms.vstring("probe_passingIso80","pass")
process.TPFTAGSFToISO80.Efficiencies.pt_eta.EfficiencyCategoryAndState = cms.vstring("probe_passingIso80","pass")


process.TPFTAISOToID = process.TagProbeFitTreeAnalyzer.clone()
process.TPFTAISOToID.InputDirectoryName = cms.string("IsoToId")
process.TPFTAISOToID.OutputFileName = cms.string("testEff_ISOToID.root")

process.TPFTAISOToID80 = process.TagProbeFitTreeAnalyzer.clone()
process.TPFTAISOToID80.InputDirectoryName = cms.string("IsoToId80")
process.TPFTAISOToID80.OutputFileName = cms.string("testEff_ISOToID80.root")

process.TPFTAIDToHLT = process.TagProbeFitTreeAnalyzer.clone()
process.TPFTAIDToHLT.InputDirectoryName = cms.string("IdToHLT")
process.TPFTAIDToHLT.OutputFileName = cms.string("testEff_IDToHLT.root")

process.TPFTAIDToHLT80 = process.TagProbeFitTreeAnalyzer.clone()
process.TPFTAIDToHLT80.InputDirectoryName = cms.string("IdToHLT80")
process.TPFTAIDToHLT80.OutputFileName = cms.string("testEff_IDToHLT80.root")

process.TPFTAGSFToWP95 = process.TagProbeFitTreeAnalyzer.clone()
process.TPFTAGSFToWP95.OutputFileName = cms.string("testEff_GSFToWP95.root")
process.TPFTAGSFToWP95.Efficiencies.pt.EfficiencyCategoryAndState  = cms.vstring("probe_passingId","pass")
process.TPFTAGSFToWP95.Efficiencies.eta.EfficiencyCategoryAndState = cms.vstring("probe_passingId","pass")
process.TPFTAGSFToWP95.Efficiencies.pt_eta.EfficiencyCategoryAndState = cms.vstring("probe_passingId","pass")

process.TPFTAGSFToWP90 = process.TagProbeFitTreeAnalyzer.clone()
process.TPFTAGSFToWP90.OutputFileName = cms.string("testEff_GSFToWP90.root")
process.TPFTAGSFToWP90.Efficiencies.pt.EfficiencyCategoryAndState  = cms.vstring("probe_passingWP90","pass")
process.TPFTAGSFToWP90.Efficiencies.eta.EfficiencyCategoryAndState = cms.vstring("probe_passingWP90","pass")
process.TPFTAGSFToWP90.Efficiencies.pt_eta.EfficiencyCategoryAndState = cms.vstring("probe_passingWP90","pass")

process.TPFTAGSFToWP85 = process.TagProbeFitTreeAnalyzer.clone()
process.TPFTAGSFToWP85.OutputFileName = cms.string("testEff_GSFToWP85.root")
process.TPFTAGSFToWP85.Efficiencies.pt.EfficiencyCategoryAndState  = cms.vstring("probe_passingWP85","pass")
process.TPFTAGSFToWP85.Efficiencies.eta.EfficiencyCategoryAndState = cms.vstring("probe_passingWP85","pass")
process.TPFTAGSFToWP85.Efficiencies.pt_eta.EfficiencyCategoryAndState = cms.vstring("probe_passingWP85","pass")

process.TPFTAGSFToWP80 = process.TagProbeFitTreeAnalyzer.clone()
process.TPFTAGSFToWP80.OutputFileName = cms.string("testEff_GSFToWP80.root")
process.TPFTAGSFToWP80.Efficiencies.pt.EfficiencyCategoryAndState  = cms.vstring("probe_passingId80","pass")
process.TPFTAGSFToWP80.Efficiencies.eta.EfficiencyCategoryAndState = cms.vstring("probe_passingId80","pass")
process.TPFTAGSFToWP80.Efficiencies.pt_eta.EfficiencyCategoryAndState = cms.vstring("probe_passingId80","pass")

process.TPFTAGSFToWP70 = process.TagProbeFitTreeAnalyzer.clone()
process.TPFTAGSFToWP70.OutputFileName = cms.string("testEff_GSFToWP70.root")
process.TPFTAGSFToWP70.Efficiencies.pt.EfficiencyCategoryAndState  = cms.vstring("probe_passingWP70","pass")
process.TPFTAGSFToWP70.Efficiencies.eta.EfficiencyCategoryAndState = cms.vstring("probe_passingWP70","pass")
process.TPFTAGSFToWP70.Efficiencies.pt_eta.EfficiencyCategoryAndState = cms.vstring("probe_passingWP70","pass")

process.TPFTAGSFToWP60 = process.TagProbeFitTreeAnalyzer.clone()
process.TPFTAGSFToWP60.OutputFileName = cms.string("testEff_GSFToWP60.root")
process.TPFTAGSFToWP60.Efficiencies.pt.EfficiencyCategoryAndState  = cms.vstring("probe_passingWP60","pass")
process.TPFTAGSFToWP60.Efficiencies.eta.EfficiencyCategoryAndState = cms.vstring("probe_passingWP60","pass")
process.TPFTAGSFToWP60.Efficiencies.pt_eta.EfficiencyCategoryAndState = cms.vstring("probe_passingWP60","pass")

process.TPFTAGSFToInvWP80 = process.TagProbeFitTreeAnalyzer.clone()
process.TPFTAGSFToInvWP80.OutputFileName = cms.string("testEff_GSFToInvWP80.root")
process.TPFTAGSFToInvWP80.InputDirectoryName = cms.string("InvWP80GsfToIso")
process.TPFTAGSFToInvWP80.Efficiencies.pt.EfficiencyCategoryAndState  = cms.vstring("probe_passingGsf","pass")
process.TPFTAGSFToInvWP80.Efficiencies.pt.BinToPDFmap = cms.vstring("BKGasSignal")
process.TPFTAGSFToInvWP80.Efficiencies.eta.EfficiencyCategoryAndState = cms.vstring("probe_passingGsf","pass")
process.TPFTAGSFToInvWP80.Efficiencies.eta.BinToPDFmap = cms.vstring("BKGasSignal")
process.TPFTAGSFToInvWP80.Efficiencies.pt_eta.EfficiencyCategoryAndState = cms.vstring("probe_passingGsf","pass")
process.TPFTAGSFToInvWP80.Efficiencies.pt_eta.BinToPDFmap = cms.vstring("BKGasSignal")

process.TPFTAHFSCToEID = process.TagProbeFitTreeAnalyzer.clone()
process.TPFTAHFSCToEID.InputDirectoryName = cms.string("HFSCToEID")
process.TPFTAHFSCToEID.OutputFileName = cms.string("testEff_HFSCToEID.root")
process.TPFTAHFSCToEID.Efficiencies.pt.BinnedVariables = cms.PSet(
                probe_sc_et = cms.vdouble(20, 30, 120) )
process.TPFTAHFSCToEID.Efficiencies.eta.BinnedVariables = cms.PSet(           
                probe_sc_eta = cms.vdouble(-5., -3., 3.0,  5.))
process.TPFTAHFSCToEID.Variables.probe_sc_eta = cms.vstring("Probe #eta", "-5.0", "5.0", "")    
process.TPFTAHFSCToEID.Efficiencies.pt_eta.BinnedVariables = cms.PSet(
                probe_sc_et = cms.vdouble(20, 30, 120),
		probe_sc_eta = cms.vdouble(-5., -3., 3.0,  5.))    
process.TPFTAHFSCToEID.Efficiencies.pt.BinToPDFmap = cms.vstring(xxHFPtBinMapxx)
process.TPFTAHFSCToEID.Efficiencies.eta.BinToPDFmap = cms.vstring(xxHFEtaBinMapxx)
process.TPFTAHFSCToEID.Efficiencies.pt_eta.BinToPDFmap = cms.vstring(xxHFPtEtaBinMapxx)


process.TPFTAHFSCToEIDT = process.TPFTAHFSCToEID.clone()
process.TPFTAHFSCToEIDT.Efficiencies.pt.EfficiencyCategoryAndState  = cms.vstring("probe_passing_tight","pass")
process.TPFTAHFSCToEIDT.Efficiencies.eta.EfficiencyCategoryAndState = cms.vstring("probe_passing_tight","pass")
process.TPFTAHFSCToEIDT.Efficiencies.pt_eta.EfficiencyCategoryAndState = cms.vstring("probe_passing_tight","pass")
process.TPFTAHFSCToEIDT.OutputFileName = cms.string("testEff_HFSCToEIDT.root")


process.TPFTASCToNTEID = process.TagProbeFitTreeAnalyzer.clone()
process.TPFTASCToNTEID.InputDirectoryName = cms.string("SCToGsf")
process.TPFTASCToNTEID.OutputFileName = cms.string("testEff_SCToNTEID.root")
process.TPFTASCToNTEID.Efficiencies.pt.EfficiencyCategoryAndState  = cms.vstring("probe_passing_nt_loose","pass")
process.TPFTASCToNTEID.Efficiencies.eta.EfficiencyCategoryAndState = cms.vstring("probe_passing_nt_loose","pass")
process.TPFTASCToNTEID.Efficiencies.pt_eta.EfficiencyCategoryAndState = cms.vstring("probe_passing_nt_loose","pass")
process.TPFTASCToNTEID.Efficiencies.pt.BinnedVariables = cms.PSet(
                probe_sc_et = cms.vdouble(118, 120) )
process.TPFTASCToNTEID.Efficiencies.eta.BinnedVariables = cms.PSet(           
                probe_sc_eta = cms.vdouble(-2.9, -2.5, 2.5,  2.9))
process.TPFTASCToNTEID.Variables.probe_sc_eta = cms.vstring("Probe #eta", "-5.0", "5.0", "")    
process.TPFTASCToNTEID.Efficiencies.pt_eta.BinnedVariables = cms.PSet(
                probe_sc_et = cms.vdouble(20, 30, 120),
		probe_sc_eta = cms.vdouble(-2.9, -2.5, 2.5,  2.9))   
process.TPFTASCToNTEID.Efficiencies.pt.BinToPDFmap = cms.vstring(xxNTPtBinMapxx)
process.TPFTASCToNTEID.Efficiencies.eta.BinToPDFmap = cms.vstring(xxNTEtaBinMapxx)
process.TPFTASCToNTEID.Efficiencies.pt_eta.BinToPDFmap = cms.vstring(xxNTPtEtaBinMapxx)


process.TPFTASCToNTEIDT = process.TPFTASCToNTEID.clone()
process.TPFTASCToNTEIDT.Efficiencies.pt.EfficiencyCategoryAndState  = cms.vstring("probe_passing_nt_tight","pass")
process.TPFTASCToNTEIDT.Efficiencies.eta.EfficiencyCategoryAndState = cms.vstring("probe_passing_nt_tight","pass")
process.TPFTASCToNTEIDT.Efficiencies.pt_eta.EfficiencyCategoryAndState = cms.vstring("probe_passing_nt_tight","pass")
process.TPFTASCToNTEIDT.OutputFileName = cms.string("testEff_SCToNTEIDT.root")


process.TPFTASCToInvWP80 = process.TagProbeFitTreeAnalyzer.clone()
process.TPFTASCToInvWP80.OutputFileName = cms.string("testEff_SCToInvWP80TEST.root")
process.TPFTASCToInvWP80.InputDirectoryName = cms.string("InvWP80SCToGsf")
process.TPFTASCToInvWP80.Efficiencies.pt.BinToPDFmap = cms.vstring("BKGasSplit")
process.TPFTASCToInvWP80.Efficiencies.eta.BinToPDFmap = cms.vstring("BKGasSplit")
process.TPFTASCToInvWP80.Efficiencies.pt_eta.BinToPDFmap = cms.vstring("BKGasSplit")

process.TPFTANTToInvWP80 = process.TPFTASCToInvWP80.clone()
process.TPFTANTToInvWP80.OutputFileName = cms.string("testEff_NTToInvWP80TEST.root")
process.TPFTANTToInvWP80.Efficiencies.pt.EfficiencyCategoryAndState  = cms.vstring("probe_passing_nt_tight","pass")
process.TPFTANTToInvWP80.Efficiencies.eta.EfficiencyCategoryAndState = cms.vstring("probe_passing_nt_tight","pass")
process.TPFTANTToInvWP80.Efficiencies.pt_eta.EfficiencyCategoryAndState = cms.vstring("probe_passing_nt_tight","pass")
process.TPFTANTToInvWP80.Efficiencies.pt.BinnedVariables = cms.PSet(
                probe_sc_et = cms.vdouble(118, 120) )
process.TPFTANTToInvWP80.Efficiencies.eta.BinnedVariables = cms.PSet(           
                probe_sc_eta = cms.vdouble(-2.9, -2.5, 2.5,  2.9))
process.TPFTANTToInvWP80.Variables.probe_sc_eta = cms.vstring("Probe #eta", "-5.0", "5.0", "")    
process.TPFTANTToInvWP80.Efficiencies.pt_eta.BinnedVariables = cms.PSet(
                probe_sc_et = cms.vdouble(20, 30, 120),
		probe_sc_eta = cms.vdouble(-2.9, -2.5, 2.5,  2.9)) 

process.TPFTAHFToInvWP80 = process.TPFTASCToInvWP80.clone()
process.TPFTAHFToInvWP80.InputDirectoryName = cms.string("InvWP80HFSCToEID")
process.TPFTAHFToInvWP80.OutputFileName = cms.string("testEff_HFToInvWP80TEST.root")
process.TPFTAHFToInvWP80.Efficiencies.pt.BinnedVariables = cms.PSet(
                probe_sc_et = cms.vdouble(20, 30, 120) )
process.TPFTAHFToInvWP80.Efficiencies.eta.BinnedVariables = cms.PSet(           
                probe_sc_eta = cms.vdouble(-5., -3., 3.0,  5.))
process.TPFTAHFToInvWP80.Variables.probe_sc_eta = cms.vstring("Probe #eta", "-5.0", "5.0", "")    
process.TPFTAHFToInvWP80.Efficiencies.pt_eta.BinnedVariables = cms.PSet(
                probe_sc_et = cms.vdouble(20, 30, 120),
		probe_sc_eta = cms.vdouble(-5., -3., 3.0,  5.)) 

process.TPFTAGSFToISO = process.TagProbeFitTreeAnalyzer.clone()

process.TPFTAFINAL = process.TagProbeFitTreeAnalyzer.clone()
process.TPFTAFINAL.InputDirectoryName = cms.string("IdToHLTFINAL")
process.TPFTAFINAL.OutputFileName = cms.string("testEff_FINAL.root")
process.TPFTAFINAL.Efficiencies = cms.PSet(
    rap = cms.PSet(
       EfficiencyCategoryAndState = cms.vstring("probe_passingId","pass"),
       UnbinnedVariables = cms.vstring("mass"),
       BinnedVariables = cms.PSet(
          pair_rapidity = cms.vdouble(-5, -4.9, -4.8, -4.7, -4.6, -4.5, -4.4, -4.3, -4.2, -4.1, -4, -3.9, -3.8, -3.7, -3.6, -3.5, -3.4, -3.3, -3.2, -3.1, -3, -2.9, -2.8, -2.7, -2.6, -2.5, -2.4, -2.3, -2.2, -2.1, -2, -1.9, -1.8, -1.7, -1.6, -1.5, -1.4, -1.3, -1.2, -1.1, -1, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5)
       ),
       BinToPDFmap = cms.vstring(xxRapBinMapxx)))

process.TPFTAFINALTEST = process.TPFTAFINAL.clone()
process.TPFTAFINALTEST.OutputFileName = cms.string("testEff_TESTFINAL.root")
#process.TPFTAFINALTEST.Efficiencies.rap.EfficiencyCategoryAndState = cms.vstring("probe_passingId80","pass")
process.TPFTAFINALTEST.Efficiencies.rap.BinnedVariables.pair_rapidity = cms.vdouble(-5,5)

process.TPFTAINVFINAL =  process.TPFTAFINAL.clone()
process.TPFTAINVFINAL.InputDirectoryName = cms.string("InvWP80GsfToIso")
process.TPFTAINVFINAL.OutputFileName = cms.string("testEff_INVFINAL.root")
process.TPFTAINVFINAL.Efficiencies.rap.BinToPDFmap = cms.vstring("BKGasSignal")
process.TPFTAINVFINAL.Efficiencies.rap.EfficiencyCategoryAndState = cms.vstring("probe_passingGsf","pass")

process.TPFTAFHF = process.TPFTAFINAL.clone()
process.TPFTAFHF.InputDirectoryName = cms.string("HFEIDFINAL")
process.TPFTAFHF.OutputFileName = cms.string("testEff_FINALHF.root")
process.TPFTAFHF.Efficiencies.rap.EfficiencyCategoryAndState = cms.vstring("probe_passing","pass")
process.TPFTAFHF.Efficiencies.rap.BinToPDFmap = cms.vstring(xxHFRapBinMapxx)

process.TPFTAFHFTEST = process.TPFTAFHF.clone()
process.TPFTAFHFTEST.OutputFileName = cms.string("testEff_TESTFINALHF.root")
process.TPFTAFHFTEST.Efficiencies.rap.BinnedVariables.pair_rapidity = cms.vdouble(-5,5)


process.TPFTAINVFHF = process.TPFTAFHF.clone()
process.TPFTAINVFHF.InputDirectoryName = cms.string("InvWP80HFSCToEID")
process.TPFTAINVFHF.OutputFileName = cms.string("testEff_INVFINALHF.root")
process.TPFTAINVFHF.Efficiencies.rap.BinToPDFmap = cms.vstring("BKGasSplit")

process.TPFTAFNTT = process.TPFTAFINAL.clone()
process.TPFTAFNTT.InputDirectoryName = cms.string("PhotonToNTFINAL")
process.TPFTAFNTT.OutputFileName = cms.string("testEff_FINALNTT.root")
process.TPFTAFNTT.Efficiencies.rap.EfficiencyCategoryAndState = cms.vstring("probe_passing","pass")
process.TPFTAFNTT.Efficiencies.rap.BinToPDFmap = cms.vstring("voigtPlusBKG")


process.TPFTAMCToSC = process.TagProbeFitTreeAnalyzer.clone()
process.TPFTAMCToSC.InputDirectoryName = cms.string("MCToSC")
process.TPFTAMCToSC.OutputFileName = cms.string("testEff_MCToSC.root")
process.TPFTAMCToSC.Efficiencies.pt.BinnedVariables = cms.PSet(
                probe_sc_et = cms.vdouble(15, 18) )
process.TPFTAMCToSC.Efficiencies.eta.BinnedVariables = cms.PSet(           
                probe_sc_eta = cms.vdouble(-2.9, -2.8, -2.7, -2.6, -2.5, -2.4, -2.3, -2.2, -2.1,
                                           -2.0, -1.9, -1.8, -1.7, -1.6, -1.566, -1.442,  -1.4, 
                                           -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5,
                                           -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 
                                            0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4,  1.442, 1.566, 1.6,
                                            1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6,
                                            2.7, 2.8, 2.9))
process.TPFTAMCToSC.Variables.probe_sc_eta = cms.vstring("Probe #eta", "-5.0", "5.0", "")    
process.TPFTAMCToSC.Efficiencies.pt_eta.BinnedVariables = cms.PSet(
                probe_sc_et = cms.vdouble(15, 25, 40,  120),
		probe_sc_eta = cms.vdouble(-2.9, -2.8, -2.7, -2.5, -2.3,  -2.1,
                                           -1.9, -1.7, -1.6, -1.566, -1.442,  -1.4, 
                                           -1.3, -1.1, -0.9, -0.7,  -0.5,
                                           -0.3, -0.1, 0.1, 0.3, 0.5, 
                                            0.7,  0.9, 1.1, 1.3, 1.4, 1.442, 1.566, 1.6, 
                                            1.7,  1.9, 2.1, 2.3, 2.5, 
                                            2.7, 2.8, 2.9))  
process.TPFTAMCToSC.Efficiencies.pt.BinToPDFmap = cms.vstring("JustVoigt")
process.TPFTAMCToSC.Efficiencies.eta.BinToPDFmap = cms.vstring("JustVoigt")
process.TPFTAMCToSC.Efficiencies.pt_eta.BinToPDFmap = cms.vstring("JustVoigt")

#process.fit = cms.Path(process.TPFTAGSFToISO + process.TPFTAHFSCToEID + process.TPFTAHFSCToEIDT + 
#                       process.TPFTASCToGSF + process.TPFTAGSFToISO80 +   process.TPFTAISOToID +   
#                       process.TPFTAISOToID80 + process.TPFTAIDToHLT + process.TPFTAIDToHLT80 + 
#                       process.TPFTAGSFToWP95 + process.TPFTAGSFToWP90 + process.TPFTAGSFToWP85 + 
#                       process.TPFTAGSFToWP80 + process.TPFTAGSFToWP70 + process.TPFTAGSFToWP60 +
#                       process.TPFTAGSFToInvWP80 + process.TPFTASCToNTEID + process.TPFTASCToNTEIDT +
#                       process.TPFTNTToInvWP80 +process.TPFTHFToInvWP80 
#                       process.TPFTASCToInvWP80 + process.TPFTAFINAL + process.TPFTAFHF + process.TPFTAFNTT )
process.fit = cms.Path( process.TPFTAxxVALUExx )
 
