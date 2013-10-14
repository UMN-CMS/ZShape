#include "../BackgroundLibrary/BackgroundFunctions.h"
#include "../ElectronLocation/ElectronLocation.h"
#include "../../MakeZEffTree/src/ZEffTree.h"
#include "../ZSmearer/ZSmearer.h"  // smearEvent()
#include "../FitterLibrary/FitterLibrary.h"  // getBinEdges, EffFromCounting, EffFromSignal, PrintEffs, EffBin, Efficiencies

#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <map>
#include <vector>

#include <TH1.h>
#include <TF1.h>
#include <TFile.h>
#include <TAxis.h>
#include <TObject.h>
#include <TCanvas.h>
#include <TROOT.h>
#include <TStyle.h>
#include <TRandom3.h>
#include <TLorentzVector.h>

TF1* getBGFitFunc(const std::string& name, bg::BinnedBackground& bgfunc, const EffBin& effbin){
    // Set our exclude regions
    //bgfunc.setExclude();
    // Make our function
    TF1* tf1 = new TF1(name.c_str(), bgfunc, effbin.minMZ, effbin.maxMZ, bgfunc.nparams);
    tf1->SetLineWidth(1);
    // Set names
    tf1->SetParName(0, "alpha");
    tf1->SetParName(1, "beta");
    tf1->SetParName(2, "gamma");
    tf1->SetParName(3, "delta");
    //tf1->SetParName(4, "Signal Amplitude");
    // Set limits
    tf1->SetParLimits(0, 0., 10000.);
    tf1->SetParLimits(0, 40., 120.);
    tf1->SetParLimits(1, 0., 100000.);
    tf1->SetParLimits(1, 0.1, 1000000.);
    tf1->SetParLimits(2, 0.0001, 0.3);
    tf1->SetParLimits(3, 3., 80.);
    // Set starting value
    tf1->SetParameter(0, 100.);
    tf1->SetParameter(0, 60.);
    tf1->SetParameter(1, 1000.);
    tf1->SetParameter(1, 1000.);
    tf1->SetParameter(2, 0.01);
    tf1->SetParameter(3, 10.);

    return tf1;
}

int fitDistributions(const std::string signalFile, const std::string ZEffFile, const std::string outFile, const std::string tagWP, const std::string probeWP, const electronLocation tagLoc, const electronLocation probeLoc, const EffBin effbin, const bool usePhiStar=false){
    // Some commont variables
    const double tagXCutPt = 20.;
    const double probeXCutPt = 20.;

    // Prepare the histogram to put the signal in
    std::vector<double> xbins;
    getBinEdges(effbin.minMZ, effbin.maxMZ, probeLoc, &xbins);
    const int nbins = xbins.size() - 1;
    if (nbins <= 1){
        std::stringstream ss;
        ss << "Signal has too few bins." << std::endl;
        std::cout << ss.str() << std::flush;
        return 1;
    }
    double* xbins_ar = &xbins[0];
    TH1D* mcPreHisto = new TH1D("mcPreHisto", "signal", nbins, xbins_ar);
    TH1D* mcPostHisto = new TH1D("mcPostHisto", "signal", nbins, xbins_ar);

    // Open signal file and make histograms
    TFile ZSFile(signalFile.c_str(), "READ");
    ZEffTree* zes;
    zes = new ZEffTree(ZSFile, false);

    const bool doSmearing = false;
    TRandom3* trand = new TRandom3(123456);

    bool run1 = true;
    while (run1){
        zes->Entries();
        if (doSmearing) {
            smearEvent(trand, &zes->reco);
        }
        const double PU = zes->reco.nverts;
        const double MZ = zes->reco.mz;
        if (  // Right number of PU, MZ
                effbin.minPU <= PU && PU <= effbin.maxPU
                && effbin.minMZ <= MZ && MZ <= effbin.maxMZ
                && 20. <= zes->reco.pt[0] && 20. <= zes->reco.pt[1]
           ){
            /* We set try either electron as the "probe", since this is MC either can be the "tag" */
            double tagX;
            double probeX;

            for (int i=0; i < 2; ++i){
                bool probeMatch = false;
                bool tagMatch = false;
                // Note that j is the PROBE and i is the TAG
                int j;
                if (i==0){
                    j=1;
                } else {
                    j=0;
                }
                double eX0;
                double eX1;
                if (usePhiStar){
                    eX0 = zes->reco.phistar;
                    tagX = -1;
                    eX1 = zes->reco.phistar;
                    probeX = -1;
                } else {
                    eX0 = zes->reco.pt[i];
                    tagX = tagXCutPt;
                    eX1 = zes->reco.pt[j];
                    probeX = probeXCutPt;
                }
                // Now we make sure exactly one e passes the tag region, and one the probe region requirements
                if ( effbin.minX <= eX1 && eX1 <= effbin.maxX && probeX <= eX1
                     && zes->reco.isSelected(i, "HLT-GSF") // Tag is HLT-GSF
                     && zes->reco.isSelected(i, tagWP) // TagWP passes
                     && zes->reco.isSelected(j, "Supercluster-Eta") 
                     && zes->reco.isSelected(j, "GsfTrack-EtaDet")
                   ){
                    probeMatch = inAcceptance(probeLoc, zes->reco.eta[j]);
                }
                if ( probeMatch && tagX <= eX0 ){
                    tagMatch = inAcceptance(tagLoc, zes->reco.eta[i]);
                }
                // Base Cuts, and Post Cuts which are a strict subset
                if ( tagMatch && probeMatch ){
                    mcPreHisto->Fill(MZ);
                    if (zes->reco.isSelected(j, probeWP)){
                        mcPostHisto->Fill(MZ); 
                    }
                    break;
                }
            }
        }
        run1 = zes->GetNextEvent();
    }

    delete zes;

    // Prepare output
    TFile* outfile;
    outfile = new TFile(outFile.c_str(),"RECREATE");
    gROOT->SetStyle("Plain");
    gStyle->SetOptFit();
    gStyle->SetOptStat(1000011);
    gStyle->SetCanvasBorderMode(0);
    TCanvas *canvas = new TCanvas("canvas", "canvas", 1280, 640);
    canvas->Divide(2);

    canvas->cd(1);
    gPad->SetLogy();
    TH1D *baseHisto = new TH1D("baseHisto", "baseHisto", nbins, xbins_ar);
    baseHisto->SetMarkerStyle(20);
    baseHisto->GetXaxis()->SetTitle("M_{ee} [GeV/c^{2}]");
    baseHisto->GetYaxis()->SetTitle("Count/GeV");

    canvas->cd(2);
    gPad->SetLogy();
    TH1D *postcutHisto = new TH1D("postcutHisto", "postcutHisto", nbins, xbins_ar);
    postcutHisto->SetMarkerStyle(20);
    postcutHisto->GetXaxis()->SetTitle("M_{ee} [GeV/c^{2}]");
    postcutHisto->GetYaxis()->SetTitle("Count/GeV");

    baseHisto->SetDirectory(outfile);
    postcutHisto->SetDirectory(outfile);

    // Open file to fit, and make histograms
    TFile ZFile(ZEffFile.c_str(), "READ");
    ZEffTree* ze;
    ze = new ZEffTree(ZFile, false);

    // Loop over events to create the distributions to fit
    bool run2 = true;
    bool flop = true;

    while (run2){
        /* Select a reproducably random tag and probe */
        int tagNumber;
        int probeNumber;
        if ( !inAcceptance(HF, ze->reco.eta[1])){ // EB HF case, no flop needed
            if (flop) {
                tagNumber = 0;
                probeNumber = 1;
                flop = false;
            } else {
                tagNumber = 1;
                probeNumber = 0;
                flop = true;
            }
        } else {
            tagNumber = 0;
            probeNumber = 1;
        }

        ze->Entries();
        /* Check that the event passes our requirements */
        if (    effbin.minPU <= ze->reco.nverts && ze->reco.nverts <= effbin.maxPU 
                && effbin.minMZ <= ze->reco.mz && ze->reco.mz <= effbin.maxMZ 
           ){
            bool basePass = false;
            bool postPass = false;
            double eX0;
            double eXCut0;
            double eX1;
            double eXCut1;
            if (usePhiStar){
                eX0 = ze->reco.phistar;
                eXCut0 = -1;
                eX1 = ze->reco.phistar;
                eXCut1 = -1;
            } else {
                eX0 = ze->reco.pt[tagNumber];
                eX1 = ze->reco.pt[probeNumber];
                eXCut0 = tagXCutPt;
                eXCut1 = probeXCutPt;
            }
            /* Check cuts */
            if (    eXCut0 <= eX0 && eXCut1 <= eX1  // Both Es pass min pt/phistar
                    && effbin.minX <= eX1 && eX1 <= effbin.maxX // Probe in pt bin
                    && ze->reco.isSelected(tagNumber, "HLT-GSF") // Tag is HLT-GSF
                    && ze->reco.isSelected(tagNumber, tagWP) // TagWP passes
               ){
                /* Check the acceptance of the electrons */
                const bool tagPass = inAcceptance(tagLoc, ze->reco.eta[tagNumber]);
                const bool probePass = inAcceptance(probeLoc, ze->reco.eta[probeNumber]);

                if (tagPass && probePass){
                    switch (probeLoc){
                        case EB:
                        case EBp:
                        case EBm:
                        case EE:
                        case EEp:
                        case EEm:
                        case ET:
                            if (ze->reco.isSelected(probeNumber,"Supercluster-Eta") && ze->reco.isSelected(probeNumber,"GsfTrack-EtaDet")){
                                basePass = true;
                            }
                            break;
                        case NT:
                        case NTp:
                        case NTm:
                            // We only check acceptance, and it has already passed
                            basePass = true;
                            break;
                        case HF:
                        case HFp:
                        case HFm:
                            // We only check acceptance, and it has already passed
                            basePass = true;
                            break;
                    }
                }
            }
            // In numerator?
            if (ze->reco.isSelected(probeNumber, probeWP)){
                postPass = true;
            }
            // Base Cuts, and Post Cuts which are a strict subset
            if ( basePass ){
                baseHisto->Fill(ze->reco.mz);
                if ( postPass ){ // Tag passed all cuts
                    postcutHisto->Fill(ze->reco.mz);
                    //std::cout << MZ << std::endl;
                }
            }
        }
        run2 = ze->GetNextEvent();
    }

    delete ze;

    // Fit the post cut first (and use the fit signal size to constrain the
    // first fit
    canvas->cd(2);
    TH1D* signaltemp = new TH1D("signaltemp", "signal", nbins, xbins_ar);
    bg::BinnedBackground bgfunc(signaltemp);

    TF1* postBGFunc = getBGFitFunc(std::string("postBGFunc"), bgfunc, effbin);
    postcutHisto->Sumw2();
    // Fit the Exponential
    postBGFunc->SetParLimits(0, 100., 100.);
    postBGFunc->SetParLimits(3, 10., 10.);
    postcutHisto->Fit(postBGFunc, "MWLQ", "", 110, effbin.maxMZ);

    double var1=postBGFunc->GetParameter(1);
    double var2=postBGFunc->GetParameter(2);
    postBGFunc->SetParLimits(0, 40., 120.);
    postBGFunc->FixParameter(1, var1);
    postBGFunc->FixParameter(2, var2);
    postBGFunc->SetParLimits(3, 3., 80.);

    postcutHisto->Fit(postBGFunc, "MWLQ", "", effbin.minMZ, 75);
 
    double var0=postBGFunc->GetParameter(0);
    double var3=postBGFunc->GetParameter(3);

    // Set up background fitter object
    bg::BinnedBackgroundAndSignal bgfitfunc(mcPostHisto);
    TF1* postBGandSigFunc = new TF1("bgfitfunc", bgfitfunc, effbin.minMZ, effbin.maxMZ, bgfitfunc.nparams);
    postBGandSigFunc->SetParName(0, "alpha");
    postBGandSigFunc->SetParName(1, "beta");
    postBGandSigFunc->SetParName(2, "gamma");
    postBGandSigFunc->SetParName(3, "delta");
    postBGandSigFunc->SetParName(4, "Signal Amplitude");
    postBGandSigFunc->FixParameter(0, var0);
    postBGandSigFunc->FixParameter(1, 0);
    postBGandSigFunc->FixParameter(2, var2);
    postBGandSigFunc->FixParameter(3, var3);
    //postBGandSigFunc->SetParameter(1, var1);
    //postBGandSigFunc->SetParLimits(1, 0., var1*2);
    postBGandSigFunc->SetParameter(4, 1.);
    postBGandSigFunc->SetParLimits(4, 0., 250000);

    postcutHisto->Fit(postBGandSigFunc, "MWLQ");

    // Draw histograms
    postcutHisto->Draw("E");

    TH1D* postSignal = (TH1D*)bgfitfunc.getSignalHisto()->Clone("postSignal");
    postSignal->Scale(postBGandSigFunc->GetParameter(4));  // Scale by fit parameter
    postSignal->SetLineStyle(2);
    postSignal->SetLineColor(kRed);
    postSignal->Draw("same");

    TH1D* postBG = (TH1D*)bgfitfunc.getBackgroundHisto()->Clone("postBG");
    postBG->SetLineStyle(2);
    postBG->SetLineColor(kBlack);
    postBG->Draw("same");

    // Perform a fit of the pre-cut histogram
    canvas->cd(1);
    // Fit the background function
    TF1* preBGFunc = getBGFitFunc(std::string("preBGFunc"), bgfunc, effbin);
    baseHisto->Sumw2();
    // Fit the Exponential
    preBGFunc->SetParLimits(0, 100., 100.);
    preBGFunc->SetParLimits(3, 10., 10.);
    baseHisto->Fit(preBGFunc, "MWLQ", "", 110, effbin.maxMZ);

    var1=preBGFunc->GetParameter(1);
    var2=preBGFunc->GetParameter(2);
    preBGFunc->SetParLimits(0, 40., 120.);
    preBGFunc->FixParameter(1, var1);
    preBGFunc->FixParameter(2, var2);
    preBGFunc->SetParLimits(3, 3., 80.);

    baseHisto->Fit(preBGFunc, "MWLQ", "", effbin.minMZ, 75);
 
    var0=preBGFunc->GetParameter(0);
    var3=preBGFunc->GetParameter(3);

    // Set up background fitter object
    bg::BinnedBackgroundAndSignal bgfitfunc2(mcPreHisto);
    TF1* preBGandSigFunc = new TF1("bgfitfunc2", bgfitfunc2, effbin.minMZ, effbin.maxMZ, bgfitfunc2.nparams);
    preBGandSigFunc->SetParName(0, "alpha");
    preBGandSigFunc->SetParName(1, "beta");
    preBGandSigFunc->SetParName(2, "gamma");
    preBGandSigFunc->SetParName(3, "delta");
    preBGandSigFunc->SetParName(4, "Signal Amplitude");
    preBGandSigFunc->FixParameter(0, var0);
    preBGandSigFunc->FixParameter(1, 0);
    preBGandSigFunc->FixParameter(2, var2);
    preBGandSigFunc->FixParameter(3, var3);
    //preBGandSigFunc->SetParameter(1, var1);
    //preBGandSigFunc->SetParLimits(1, 0., var1*2);
    preBGandSigFunc->SetParameter(4, 1.);
    preBGandSigFunc->SetParLimits(4, 0., 250000);

    baseHisto->Fit(preBGandSigFunc, "MWLQ");

    // Draw histograms
    baseHisto->Draw("E");
    TH1D* preSignal = (TH1D*)bgfitfunc2.getSignalHisto()->Clone("preSignal");
    preSignal->Scale(preBGandSigFunc->GetParameter(4));  // Scale by fit parameter
    preSignal->SetLineStyle(2);
    preSignal->SetLineColor(kRed);
    preSignal->Draw("same");
    TH1D* preBG = (TH1D*)bgfitfunc2.getBackgroundHisto()->Clone("preBG");
    preBG->SetLineStyle(2);
    preBG->SetLineColor(kBlack);
    preBG->Draw("same");

    // Calculate Eff
    Efficiencies countEff = EffFromCounting(
            baseHisto,
            postcutHisto,
            preBG,
            postBG,
            preBGandSigFunc->GetParError(1),
            postBGandSigFunc->GetParError(1)
            );
    Efficiencies sigEff = EffFromSignal( 
            preSignal,
            postSignal,
            preBGandSigFunc->GetParError(1),
            postBGandSigFunc->GetParError(1)
            );

    canvas->cd(0);

    const std::string name(outFile.begin(), outFile.end()-5);
    const std::string pngname = name + std::string(".png");
    canvas->Print(pngname.c_str(), "png");
    outfile->Write();

    //Prints eff stats for text file
    const double baseD = baseHisto->Integral(baseHisto->FindBin(effbin.minMZ), baseHisto->FindBin(effbin.maxMZ));
    const double baseB = preBG->Integral(preBG->FindBin(effbin.minMZ), preBG->FindBin(effbin.maxMZ));

    const double denom = (baseD - baseB);
    PrintEffs(probeLoc, effbin, sigEff.eff, countEff.eff, denom, usePhiStar);

    return 0;
}

int main(int argc, char* argv[]){
    const int argcCorrect = 13;
    if (argc < argcCorrect) {
        std::cout<<"Not enough arguments. Use:\nfitEffAcc.exe signalFile ZEffFile outFile tagLoc probeLoc minPU maxPU minMZ maxMZ minX maxX\n";
        return 1;
    } else if (argc > argcCorrect){
        std::cout<<"Too many arguments. Use:\nfitEffAcc.exe signalFile ZEffFile outFile tagLoc probeLoc minPU maxPU minMZ maxMZ minX maxX\n";
        return 1;
    } else {
        // Read in arguments
        std::istringstream inStream;

        std::string signalFile;
        std::string ZEffFile;
        std::string outFile;

        inStream.str(argv[1]);
        inStream >> signalFile;
        inStream.clear();
        inStream.str(argv[2]);
        inStream >> ZEffFile;
        inStream.clear();
        inStream.str(argv[3]);
        inStream >> outFile;
        inStream.clear();

        std::string tagL;
        std::string probeL;

        inStream.str(argv[4]);
        inStream >> tagL;
        inStream.clear();
        inStream.str(argv[5]);
        inStream >> probeL;
        inStream.clear();
        electronLocation tagLoc = electronLocationToString(tagL);
        electronLocation probeLoc = electronLocationToString(probeL);

        EffBin effbin;
        inStream.str(argv[6]);
        inStream >> effbin.minPU;
        inStream.clear();
        inStream.str(argv[7]);
        inStream >> effbin.maxPU;
        inStream.clear();
        inStream.str(argv[8]);
        inStream >> effbin.minMZ;
        inStream.clear();
        inStream.str(argv[9]);
        inStream >> effbin.maxMZ;
        inStream.clear();
        inStream.str(argv[10]);
        inStream >> effbin.minX;
        inStream.clear();
        inStream.str(argv[11]);
        inStream >> effbin.maxX;
        inStream.clear();

        bool usePhiStar;
        inStream.str(argv[12]);
        inStream >> usePhiStar;
        inStream.clear();

        // Map location to other features
        // Hard coded for now
        std::string tagWP;
        switch (tagLoc){
            case EB:
            case EBp:
            case EBm:
            case EE:
            case EEp:
            case EEm:
            case ET:
                tagWP = "WP80";
                break;
            case NT: // No NT case?
            case NTp:
            case NTm:
                tagWP = "NTTightElectronId-EtaDet";
                break;
            case HF:
            case HFp:
            case HFm:
                tagWP = "HFElectronId-EtaDet";
                break;
        }

        std::string signalTH;
        std::string probeWP; // Wokring point to test

        switch (probeLoc){
            case EB:
            case EBp:
            case EBm:
            case EE:
            case EEp:
            case EEm:
            case ET:
                probeWP = "WP80";
                break;
            case NT: // No NT case?
            case NTp:
            case NTm:
                probeWP = "NTTightElectronId-EtaDet";
                break;
            case HF:
            case HFp:
            case HFm:
                probeWP = "HFElectronId-EtaDet";
                break;
        }

        std::stringstream ss;
        ss << "#efficiency name: " << probeWP << std::endl;
        ss << "#dimension: 1" << std::endl;
        std::cout << ss.str() << std::flush;

        return fitDistributions(
                signalFile,
                ZEffFile,
                outFile,
                tagWP,
                probeWP,
                tagLoc,
                probeLoc,
                effbin,
                usePhiStar
                );
    }
}
