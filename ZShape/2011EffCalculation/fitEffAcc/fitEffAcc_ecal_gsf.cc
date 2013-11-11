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

void checkEvent(
        ZEffTree::ZInfo const * const zinfo, const EffBin& effbin,
        const electronLocation& tag_loc, const int tag_num,
        const electronLocation& probe_loc, const int probe_num,
        TH1D* pre_hist, TH1D* post_hist
        ) {
    // Set up some constants to save typing
    const double PU = zinfo->nverts;
    const double MZ = zinfo->mz;
    const double tag_pt = zinfo->pt[tag_num];
    const double probe_pt = zinfo->pt[probe_num];

    // Check if the event passes our pre-cuts
    if (    // In the Pileup bin, Mass bin, and pt bin
            effbin.minPU <= PU && PU <= effbin.maxPU
            && effbin.minMZ <= MZ && MZ <= effbin.maxMZ
            && effbin.minX <= probe_pt && probe_pt <= effbin.maxX
            // Both electrons are "triggerable"
            && 20. < tag_pt && 20. < probe_pt
            // Check the location of the electrons
            && inAcceptance(probe_loc, zinfo->eta[probe_num])
            && inAcceptance(tag_loc, zinfo->eta[tag_num])
            // Check the hard cut on the tag that emulates the trigger
            && zinfo->isSelected(tag_num, "WP85")
            && zinfo->r9[tag_num] < 0.98
       ) {
        pre_hist->Fill(MZ);
        // Check if the event passes our post-cuts
        if (zinfo->isSelected(probe_num, "GsfTrack-EtaDet")) {
            post_hist->Fill(MZ);
        }
    }
}

int fitDistributions(
        const std::string& signalFile, const std::string& ZEffFile,
        const std::string& outFile, const electronLocation& tag_loc,
        const electronLocation& probe_loc, const EffBin& effbin
        ) {
    // Some commont variables
    // Prepare the histogram to put the signal in
    std::vector<double> xbins;
    getBinEdges(effbin.minMZ, effbin.maxMZ, probe_loc, &xbins);
    const int nbins = xbins.size() - 1;
    if (nbins <= 1){
        std::stringstream ss;
        ss << "Signal has too few bins." << std::endl;
        std::cout << ss.str() << std::flush;
        return 1;
    }
    double* xbins_ar = &xbins[0];
    TH1D* signalPreHisto = new TH1D("signalPreHisto", "signal", nbins, xbins_ar);
    TH1D* signalPostHisto = new TH1D("signalPostHisto", "signal", nbins, xbins_ar);

    // Open signal file and make histograms
    TFile ZSFile(signalFile.c_str(), "READ");
    ZEffTree* zes;
    zes = new ZEffTree(ZSFile, false);

    const bool doSmearing = true;
    TRandom3* trand = new TRandom3(123456);

    bool run1 = true;
    while (run1) {
        zes->Entries();
        if (doSmearing) {
            smearEvent(trand, &zes->reco);
        }
        /* We set try either electron as the "probe", since this is MC either can be the "tag" */
        for (int tagNumber=0; tagNumber < 2; ++tagNumber){
            int probeNumber;
            if (tagNumber==0){
                probeNumber=1;
            } else {
                probeNumber=0;
            }

            // Fill our histograms
            checkEvent(&zes->reco, effbin, tag_loc, tagNumber, probe_loc, probeNumber, signalPreHisto, signalPostHisto);
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
        ze->Entries();
        // Select a reproducably random tag and probe
        if (flop) {
            flop = false;
            // Check that the selection trigger passes
            if (ze->reco.trigtag[0] && ze->reco.trigprobe[0] && ze->reco.trigprobe[1]) {
                checkEvent(&ze->reco, effbin, tag_loc, 0, probe_loc, 1, baseHisto, postcutHisto);
            }
        } else {
            flop = true;
            // Check that the selection trigger passes
            if (ze->reco.trigtag[1] && ze->reco.trigprobe[1] && ze->reco.trigprobe[0]) {
                checkEvent(&ze->reco, effbin, tag_loc, 1, probe_loc, 0, baseHisto, postcutHisto);
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
    bg::BinnedBackgroundAndSignal bgfitfunc(signalPostHisto);
    TF1* postBGandSigFunc = new TF1("bgfitfunc", bgfitfunc, effbin.minMZ, effbin.maxMZ, bgfitfunc.nparams);
    postBGandSigFunc->SetParName(0, "alpha");
    postBGandSigFunc->SetParName(1, "beta");
    postBGandSigFunc->SetParName(2, "gamma");
    postBGandSigFunc->SetParName(3, "delta");
    postBGandSigFunc->SetParName(4, "Signal Amplitude");
    postBGandSigFunc->SetParameter(0, var0);
    postBGandSigFunc->SetParameter(1, var1);
    postBGandSigFunc->SetParameter(2, var2);
    postBGandSigFunc->SetParameter(3, var3);
    postBGandSigFunc->SetParLimits(0, 40., 80.);
    postBGandSigFunc->SetParLimits(1, 0., var1*100);
    postBGandSigFunc->SetParLimits(2, .0, .2);
    postBGandSigFunc->SetParLimits(3, 10., 50.);
    postBGandSigFunc->SetParameter(4, 100.);
    postBGandSigFunc->SetParLimits(4, 0., 25000);

    postcutHisto->Fit(postBGandSigFunc, "MWLQ");

    const double signal_limit = postBGandSigFunc->GetParameter(4);

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
    bg::BinnedBackgroundAndSignal bgfitfunc2(signalPreHisto);
    TF1* preBGandSigFunc = new TF1("bgfitfunc2", bgfitfunc2, effbin.minMZ, effbin.maxMZ, bgfitfunc2.nparams);
    preBGandSigFunc->SetParName(0, "alpha");
    preBGandSigFunc->SetParName(1, "beta");
    preBGandSigFunc->SetParName(2, "gamma");
    preBGandSigFunc->SetParName(3, "delta");
    preBGandSigFunc->SetParName(4, "Signal Amplitude");
    preBGandSigFunc->SetParameter(0, var0);
    preBGandSigFunc->SetParameter(1, var1);
    preBGandSigFunc->SetParameter(2, var2);
    preBGandSigFunc->SetParameter(3, var3);
    preBGandSigFunc->SetParLimits(0, 40., 80.);
    preBGandSigFunc->SetParLimits(1, 0., var1*100);
    preBGandSigFunc->SetParLimits(2, .0, .2);
    preBGandSigFunc->SetParLimits(3, 10., 50.);
    //preBGandSigFunc->SetParLimits(0, 0., var0*2);
    //preBGandSigFunc->SetParLimits(1, 0., var1*2);
    //preBGandSigFunc->SetParLimits(2, 0., var2*2);
    //preBGandSigFunc->SetParLimits(3, 0., var3*2);
    preBGandSigFunc->SetParameter(4, signal_limit * 1.3 );
    preBGandSigFunc->SetParLimits(4, signal_limit, signal_limit * 4);

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
    PrintEffs(probe_loc, effbin, sigEff.eff, countEff.eff, denom, false);

    return 0;
}

int main(int argc, char* argv[]){
    const int argcCorrect = 12;
    if (argc < argcCorrect) {
        std::cout<<"Not enough arguments. Use:\nfitEffAcc_ecal_gsf.exe signalFile ZEffFile outFile tag_loc probe_loc minPU maxPU minMZ maxMZ minX maxX\n";
        return 1;
    } else if (argc > argcCorrect){
        std::cout<<"Too many arguments. Use:\nfitEffAcc_ecal_gsf.exe signalFile ZEffFile outFile tag_loc probe_loc minPU maxPU minMZ maxMZ minX maxX\n";
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
        electronLocation tag_loc = electronLocationToString(tagL);
        electronLocation probe_loc = electronLocationToString(probeL);

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

        std::stringstream ss;
        ss << "#efficiency name: GSF (Data)" << std::endl;
        ss << "#dimension: 1" << std::endl;
        std::cout << ss.str() << std::flush;

        return fitDistributions(
                signalFile,
                ZEffFile,
                outFile,
                tag_loc,
                probe_loc,
                effbin
                );
    }
}
