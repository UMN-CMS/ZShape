#include "Background.h"
#include "ZEffTree.h"

#include <string>
#include <sstream>
#include <iostream>
#include <map>
#include <vector>
#include <math.h>

#include "TH1.h"
#include "TF1.h"
#include "TFile.h"
#include "TAxis.h"
#include "TObject.h"
#include "TCanvas.h"
#include <TROOT.h>
#include <TStyle.h>
#include <TLatex.h>

// Global because the fit functions can only have two arguments, so we need a
// way to sneak these in.

struct global{
    TH1F *signalHisto;
    TH1F *backgroundHisto;
    double alpha;
    double beta;
    double gamma;
    double delta;
} GLOBAL;

enum electronLocation{ 
    EB, 
    EE,
    NT,
    HF
};

struct eventRequirements{
    int minPU;
    int maxPU;
    double minMZ;
    double maxMZ;
};

struct bin{
    double minPt;
    double maxPt;
};

struct effs{
    double eff;
    double err;
};

double bgFunc(double x, double alpha, double gamma, double delta){
    double fitval = TMath::Erfc((alpha-x)/delta) * TMath::Exp(-gamma*x);
    return fitval;
}

double functiontofit(double *x, double *par) {
    // Generate values for our signal and our background
    double backgroundVal = par[0] * GLOBAL.backgroundHisto->GetBinContent(GLOBAL.signalHisto->FindBin(x[0]));
    double signalVal = par[1] * GLOBAL.signalHisto->GetBinContent(GLOBAL.signalHisto->FindBin(x[0]));
    return backgroundVal + signalVal;
}

void getBinEdges(std::vector<double> &vec, double minPt, double maxPt){
    double ss = 4;
    double z_min = 80.;
    double z_max = 100.;
    double cur = minPt;
    while (true){
        vec.push_back(cur);
        if (cur >= z_min && cur < z_max){
            ss = 0.5;
        }
        if (cur < z_min || cur >= z_max){
            ss = 4;
        }
        if (cur >= maxPt){
            break;
        }
        cur = cur + ss;
    }
}

effs effFromCounting(TH1F* baseData, TH1F* postData, TH1F* baseBG, TH1F* postBG, double baseP, double baseE, double postP, double postE){
    /* 
     * postD = postData count
     * postP = postData param
     * postB = postBackground count
     * postDerr = postData count error
     * postE = postBackground count error
     */
    effs tmp;
    double minMZ = 60.;
    double maxMZ = 120.;
    double baseD = baseData->Integral(baseData->FindBin(minMZ), baseData->FindBin(maxMZ), "width");
    double postD = postData->Integral(postData->FindBin(minMZ), postData->FindBin(maxMZ), "width");
    double baseB = baseBG->Integral(baseBG->FindBin(minMZ), baseBG->FindBin(maxMZ));
    double postB = postBG->Integral(postBG->FindBin(minMZ), postBG->FindBin(maxMZ));
    double baseDerr = sqrt(baseD);
    double postDerr = sqrt(postD);

    tmp.eff = (postD - (postP*postB)) / (baseD - (baseP*baseB));
    /* Note: dEff = Eff * Sqrt((da^2+db^2)/(a-b)^2 + (dc^2-dd^2)/(c-d)^2) */
    tmp.err = tmp.eff * sqrt( 
            ( ( postE * postE ) + ( postDerr * postDerr ) ) / ( ( postD - postP * postB ) * ( postD - postP * postB ) ) 
            +  ( ( baseE * baseE ) + (baseDerr * baseDerr ) ) / ( ( baseD - baseP * baseB ) * ( baseD - baseP * baseB ) ) 
            );

    return tmp;
}

effs effFromSignal(TH1F* baseSig, TH1F* postSig, double baseP, double baseE, double postP, double postE){
    effs tmp;
    double minMZ = 60.;
    double maxMZ = 120.;
    double baseS = baseSig->Integral(baseSig->FindBin(minMZ), baseSig->FindBin(maxMZ), "width");
    double postS = postSig->Integral(postSig->FindBin(minMZ), postSig->FindBin(maxMZ), "width");

    tmp.eff = ( postS * postP ) / ( baseS * baseP );
    tmp.err = tmp.eff * sqrt( (baseE * baseE)/(( baseS * baseP )*( baseS * baseP )) + (postE * postE) / (( postS * postP )*( postS * postP )) );

    // TODO: Double check formula 
    return tmp;
}

void printEffs(electronLocation probeLoc, eventRequirements eventrq, bin ptbin, double sigeff, double counteff, double denom){
    /* Prints probewp ptmin ptmax etamin etamax pumin pumax sigeff sigerr counteff counterr */
    std::cout << "#PtMin PtMax EtaMin EtaMax PUMin PUMax NumParms eff systp systm den" << std::endl;
    std::cout << ptbin.minPt << " ";
    std::cout << ptbin.maxPt << " ";
    switch (probeLoc){
        case EB:
            std::cout << 0 << " ";
            std::cout << 1.4442 << " ";
            break;
        case EE:
            std::cout << 1.566 << " ";
            std::cout << 2.5 << " ";
            break;
        case NT:
            std::cout << 2.5 << " ";
            std::cout << 2.850 << " ";
            break;
        case HF:
            std::cout << 3.1 << " ";
            std::cout << 4.6 << " ";
            break;
    }
    std::cout << eventrq.minPU << " ";
    std::cout << eventrq.maxPU << " ";
    std::cout << "4" << " "; // Number of params
    double diff = fabs(sigeff - counteff);
    std::cout << sigeff << " ";
    std::cout << sigeff+diff << " ";
    std::cout << sigeff-diff << " ";
    std::cout << denom << std::endl;
}

int fitDistributions(std::string bgfitfile, std::string signalFile, std::string ZEffFile, std::string outFile, std::string tagWP, std::string probeWP, electronLocation tagLoc, electronLocation probeLoc, eventRequirements eventrq, bin ptbin){
    // Get our background and set variables
    Background bg(bgfitfile);
    double midPt = (ptbin.maxPt + ptbin.minPt)/2.;
    //std::cout << "midPt: " << midPt << std::endl;
    double midPU = (eventrq.maxPU + eventrq.minPU)/2.;
    //std::cout << "midPU: " << midPU << std::endl;
    bg.setBackground(midPt, midPU); // TODO: Fill in pt, pu
    if (bg.current == 0){
        std::cout << "Failed to get background model." <<std::endl;
        // No background for your area.
        return 1;
    }
    GLOBAL.alpha = bg.current->alpha;
    GLOBAL.beta = bg.current->beta;
    GLOBAL.gamma = bg.current->gamma;
    GLOBAL.delta = bg.current->delta;


    // Prepare the histogram to put the signal in
    std::vector<double> xbins;
    getBinEdges(xbins, eventrq.minMZ, eventrq.maxMZ);
    int nbins = xbins.size() - 1;
    if (nbins <= 1){
        std::cout << "Signal has too few bins." << std::endl;
        return 1;
    }
    double* xbins_ar = &xbins[0];
    GLOBAL.signalHisto = new TH1F("signalHisto", "signal", nbins, xbins_ar);

    // Open signal file and make histograms
    TFile ZSFile(signalFile.c_str(), "READ");
    ZEffTree* zes;
    zes = new ZEffTree(ZSFile, false);

    bool run1 = true;
    while (run1){
        zes->Entries();
        double PU = zes->reco.nverts;
        double MZ = zes->reco.mz;
        if (  // Right number of PU, MZ, both electrons over 20 GeV
                //eventrq.minPU <= PU && PU <= eventrq.maxPU 
                eventrq.minMZ <= MZ && MZ <= eventrq.maxMZ 
                && 20. <= zes->reco.pt[0] && 20. <= zes->reco.pt[1]
           ){
            bool probeMatch = false;
            bool tagMatch = false;
            for (int i =0; i < 2; ++i){
                double eeta = zes->reco.eta[i];
                double ept = zes->reco.pt[i];
                // Now we make sure exactly one e passes the tag region, and one the probe region requirements
                if ( probeMatch == false && ptbin.minPt <= ept && ept <= ptbin.maxPt ){
                    switch (probeLoc){
                        case EB:
                            if ( eeta < 1.4442 ){ probeMatch = true; }
                            break;
                        case EE:
                            if (1.566 < eeta && eeta < 2.5 ){ probeMatch = true; }
                            break;
                        case NT:
                            if (2.5 <= eeta && eeta < 2.850 ){ probeMatch = true; }
                            break;
                        case HF:
                            if (3.1 < eeta && eeta < 4.6 ){ probeMatch = true; }
                            break;
                    }
                } 
                if (tagMatch == false){
                    switch (tagLoc){
                        case EB:
                            if ( eeta < 1.4442 ){ tagMatch = true; }
                            break;
                        case EE:
                            if (1.566 < eeta && eeta < 2.5 ){ tagMatch = true; }
                            break;
                        case NT:
                            if (2.5 <= eeta && eeta < 2.850 ){ tagMatch = true; }
                            break;
                        case HF:
                            if (3.1 < eeta && eeta < 4.6 ){ tagMatch = true; }
                            break;
                    }
                }
                // Base Cuts, and Post Cuts which are a strict subset
                if ( tagMatch && probeMatch ){ 
                    GLOBAL.signalHisto->Fill(MZ);
                }
            }
        }
        run1 = zes->GetNextEvent();
    }

    // Set up background histogram
    GLOBAL.backgroundHisto = new TH1F("backgroundHisto", "background histo", nbins, xbins_ar);
    // Turn our analytic function into a histogram
    for ( int i = 1; i <= GLOBAL.backgroundHisto->GetNbinsX(); ++i) {
        double xval = GLOBAL.signalHisto->GetBinCenter(i);
        double binVal = bgFunc(xval, GLOBAL.alpha, GLOBAL.gamma, GLOBAL.delta);
        GLOBAL.backgroundHisto->SetBinContent(i, binVal);
    }

    // Normalize areas
    GLOBAL.signalHisto->Scale(1. / GLOBAL.signalHisto->Integral(GLOBAL.signalHisto->FindBin(eventrq.minMZ), GLOBAL.signalHisto->FindBin(eventrq.maxMZ)),"width");
    GLOBAL.backgroundHisto->Scale(1. / GLOBAL.backgroundHisto->Integral(GLOBAL.backgroundHisto->FindBin(eventrq.minMZ), GLOBAL.backgroundHisto->FindBin(eventrq.maxMZ)));

    // Prepare output
    TFile* outfile;
    outfile = new TFile(outFile.c_str(),"RECREATE");
    gROOT->SetStyle("Plain");
    gStyle->SetOptFit();
    gStyle->SetOptStat(11111);
    gStyle->SetCanvasBorderMode(0);
    TCanvas *canvas = new TCanvas("canvas", "canvas", 1280, 640);
    canvas->Divide(2);
    canvas->cd(1);
    gPad->SetLogy();
    TH1F *baseHisto = new TH1F("baseHisto", "baseHisto", nbins, xbins_ar);
    baseHisto->SetMarkerStyle(20);
    baseHisto->GetXaxis()->SetTitle("M_{ee} [GeV/c^{2}]");
    baseHisto->GetYaxis()->SetTitle("Count/GeV");
    canvas->cd(2);
    gPad->SetLogy();
    TH1F *postcutHisto = new TH1F("postcutHisto", "postcutHisto", nbins, xbins_ar);
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
    while (run2){
        ze->Entries();
        double PU = ze->reco.nverts;
        double MZ = ze->reco.mz;

        if ( eventrq.minPU <= PU && PU <= eventrq.maxPU && eventrq.minMZ <= MZ && MZ <= eventrq.maxMZ ){

            bool basePass = false;
            bool postPass = false;
            double ept = ze->reco.pt[1];

            if (
                    20. <= ze->reco.pt[0] && 20. <= ept
                    && ptbin.minPt <= ept && ept <= ptbin.maxPt
                    && ze->reco.isSelected(0,"Supercluster-Eta") 
                    && ze->reco.isSelected(0,"GsfTrack-EtaDet")
                    && ze->reco.isSelected(0,"WP80")
               ){

                double eeta = fabs(ze->reco.eta[1]);
                switch (probeLoc){
                    case EB:
                        if ( eeta < 1.4442 && ze->reco.isSelected(1,"Supercluster-Eta") && ze->reco.isSelected(1,"GsfTrack-EtaDet")){
                            basePass = true;
                        }
                        break;
                    case EE:
                        if (1.566 < eeta && eeta < 2.5 && ze->reco.isSelected(1,"Supercluster-Eta") && ze->reco.isSelected(1,"GsfTrack-EtaDet")){
                            basePass = true;
                        }
                        break;
                    case NT:
                        if (2.5 <= eeta && eeta < 2.850){
                            basePass = true;
                        }
                        break;
                    case HF:
                        if (3.1 < eeta && eeta < 4.6 && ze->reco.isSelected(1,"HFSuperCluster-Et")){
                            basePass = true;
                        }
                        break;
                }
            } 
            // In numerator?
            if (ze->reco.isSelected(1,probeWP)){
                postPass = true;
            }
            // Base Cuts, and Post Cuts which are a strict subset
            if ( basePass ){ 
                baseHisto->Fill(MZ);
                if ( postPass ){ // Tag passed all cuts
                    postcutHisto->Fill(MZ);
                }
            }
        }
        run2 = ze->GetNextEvent();
    }

    // Perform fit
    canvas->cd(1);
    TF1* baseFitFunc = new TF1("baseFitFunc", functiontofit, eventrq.minMZ, eventrq.maxMZ, 2);
    baseFitFunc->SetLineWidth(1);
    baseFitFunc->SetParLimits(0, 0., 10000.);
    baseFitFunc->SetParLimits(1, 0., 100000.);
    baseFitFunc->SetParameter(0, 100.);
    baseFitFunc->SetParameter(1, 1000.);
    baseHisto->Sumw2(); // Insure errors are handled correctly when scaled.
    baseHisto->Scale(1,"width"); // Scale by 1, and then divide each bin by its width.
    baseHisto->Fit(baseFitFunc, "RMEQ");
    baseHisto->Draw("E");
    TH1F* baseBG = (TH1F*)GLOBAL.backgroundHisto->Clone("baseBG");
    baseBG->Scale(baseFitFunc->GetParameter(0));
    baseBG->SetLineStyle(2);
    baseBG->Draw("same");

    canvas->cd(2);
    TF1* postFitFunc = new TF1("postFitFunc", functiontofit, eventrq.minMZ, eventrq.maxMZ, 2);
    postFitFunc->SetLineWidth(1);
    postFitFunc->SetParLimits(0, 0., 10000.);
    postFitFunc->SetParLimits(1, 0., 100000.);
    postFitFunc->SetParameter(0, 100.);
    postFitFunc->SetParameter(1, 1000.);
    postcutHisto->Sumw2();
    postcutHisto->Scale(1,"width");
    postcutHisto->Fit(postFitFunc, "RMEQ");
    postcutHisto->Draw("E");
    TH1F* postBG = (TH1F*)GLOBAL.backgroundHisto->Clone("postBG");
    postBG->Scale(postFitFunc->GetParameter(0));
    postBG->SetLineStyle(2);
    postBG->Draw("same");

    // Calculate Eff
    effs countEff = effFromCounting(baseHisto, postcutHisto, GLOBAL.backgroundHisto, GLOBAL.backgroundHisto, baseFitFunc->GetParameter(0), baseFitFunc->GetParError(0), postFitFunc->GetParameter(0), postFitFunc->GetParError(0));
    effs sigEff = effFromSignal( GLOBAL.signalHisto, GLOBAL.signalHisto, baseFitFunc->GetParameter(1), baseFitFunc->GetParError(1), postFitFunc->GetParameter(1), postFitFunc->GetParError(1));
    std::cout << "COUNT EFF: " << countEff.eff << " SIG EFF: " << sigEff.eff << std::endl;
    //Format text on plots
    //char postAmp_str[1000];
    //sprintf(postAmp_str,"#splitline{BG: %0.2f}{Sig: %0.2f}",postFitFunc->GetParameter(0),postFitFunc->GetParameter(1));
    //TLatex* postAmp = new TLatex(0.65,0.75,postAmp_str);
    //postAmp->SetNDC(true);
    //postAmp->Draw();

    canvas->cd(0);

    std::string name(outFile.begin(), outFile.end()-5);
    std::string pngname = name + std::string(".png");
    canvas->Print(pngname.c_str(), "png");
    outfile->Write();

    // Prints eff stats for text file
    double baseD = baseHisto->Integral(baseHisto->FindBin(eventrq.minMZ), baseHisto->FindBin(eventrq.maxMZ), "width");
    double baseB = GLOBAL.backgroundHisto->Integral(GLOBAL.backgroundHisto->FindBin(eventrq.minMZ), GLOBAL.backgroundHisto->FindBin(eventrq.maxMZ));

    double denom = (baseD - (baseFitFunc->GetParameter(0)*baseB));
    printEffs(probeLoc, eventrq, ptbin, sigEff.eff, countEff.eff, denom);

    return 0;
}

int main(int argc, char* argv[]){
    int argcCorrect = 13;
    if (argc < argcCorrect) {
        std::cout<<"Not enough arguments. Use:\nfitEffAcc.exe bgfitFile signalFile ZEffFile outFile tagLoc probeLoc minPU maxPU minMZ maxMZ minPt maxPt\n";
        return 1;
    } else if (argc > argcCorrect){
        std::cout<<"Too many arguments. Use:\nfitEffAcc.exe bgfitFile signalFile ZEffFile outFile tagLoc probeLoc minPU maxPU minMZ maxMZ minPt maxPt\n";
        return 1;
    } else {
        // Read in arguments
        std::istringstream inStream;

        std::string bgfitFile;
        std::string signalFile;
        std::string ZEffFile;
        std::string outFile;

        inStream.str(argv[1]);
        inStream >> bgfitFile;
        inStream.clear();
        inStream.str(argv[2]);
        inStream >> signalFile;
        inStream.clear();
        inStream.str(argv[3]);
        inStream >> ZEffFile;
        inStream.clear();
        inStream.str(argv[4]);
        inStream >> outFile;
        inStream.clear();

        std::string tagL;
        std::string probeL;

        inStream.str(argv[5]);
        inStream >> tagL;
        inStream.clear();
        inStream.str(argv[6]);
        inStream >> probeL;
        inStream.clear();
        std::map<std::string, electronLocation> conv;
        conv["EB"] = EB;
        conv["EE"] = EE;
        conv["NT"] = NT;
        conv["HF"] = HF;
        electronLocation tagLoc = conv[tagL];
        electronLocation probeLoc = conv[probeL];

        eventRequirements eventrq;
        inStream.str(argv[7]);
        inStream >> eventrq.minPU;
        inStream.clear();
        inStream.str(argv[8]);
        inStream >> eventrq.maxPU;
        inStream.clear();
        inStream.str(argv[9]);
        inStream >> eventrq.minMZ;
        inStream.clear();
        inStream.str(argv[10]);
        inStream >> eventrq.maxMZ;
        inStream.clear();

        bin ptbin;

        inStream.str(argv[11]);
        inStream >> ptbin.minPt;
        inStream.clear();
        inStream.str(argv[12]);
        inStream >> ptbin.maxPt;
        inStream.clear();


        // Map location to other features
        // Hard coded for now
        std::string tagWP;
        switch (tagLoc){
            case EB:
            case EE:
                tagWP = "WP80";
                break;
            case NT: // No NT case?
                tagWP = "NTTightElectronId-EtaDet";
                break;
            case HF:
                tagWP = "HFElectronId-EtaDet";
        }

        std::string signalTH;
        std::string probeWP; // Wokring point to test

        switch (probeLoc){
            case EB:
                probeWP = "WP80";
                break;
            case EE:
                probeWP = "WP80";
                break;
            case NT: // No NT case?
                probeWP = "NTTightElectronId-EtaDet";
                break;
            case HF:
                probeWP = "HFElectronId-EtaDet";
        }

        std::cout << "#efficiency name: " << probeWP << std::endl;
        std::cout << "#dimension: 1" << std::endl;


        //std::cout << " Tag: " << tagWP << " Probe: " << probeWP << " MinPt: " << ptbin.minPt << " MaxPt: " << ptbin.maxPt << " MinPU: " << eventrq.minPU << " MaxPU: " << eventrq.maxPU << std::endl;
        int runCondition = fitDistributions(
                bgfitFile,
                signalFile,
                ZEffFile,
                outFile,
                tagWP,
                probeWP,
                tagLoc,
                probeLoc,
                eventrq,
                ptbin
                );

        return runCondition;
    }
}

/* Compile time notes:
 *    g++ -O2 -o fitEffAcc.exe fitEffAcc.cc ZEffTree.cc Background.cc `root-config --cflags --libs` 
 */
