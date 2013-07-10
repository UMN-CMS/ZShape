#include "Background.h"
#include "ZEffTree.h"

#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
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
    HF,
    ET
};

struct eventRequirements{
    int minPU;
    int maxPU;
    double minMZ;
    double maxMZ;
};

struct bin{
    double minX;
    double maxX;
};

struct effs{
    double eff;
    double err;
};

double bgFunc(const double x, const double alpha, const double gamma, const double delta){
    double fitval = TMath::Erfc((alpha-x)/delta) * TMath::Exp(-gamma*x);
    return fitval;
}

double functiontofit(const double *x, const double *par) {
    // Generate values for our signal and our background
    double backgroundVal = par[0] * GLOBAL.backgroundHisto->GetBinContent(GLOBAL.signalHisto->FindBin(x[0]));
    double signalVal = par[1] * GLOBAL.signalHisto->GetBinContent(GLOBAL.signalHisto->FindBin(x[0]));
    return backgroundVal + signalVal;
}

void getBinEdges(std::vector<double> &vec, double minX, double maxX){
    double ss;
    double z_min = 80.;
    double z_max = 100.;
    double cur = minX;
    while (true){
        vec.push_back(cur);
        if (cur >= z_min && cur < z_max){
            //ss = 0.5;
            ss = 5;
        }
        if (cur < z_min || cur >= z_max){
            //ss = 4;
            ss = 20;
        }
        if (cur >= maxX){
            break;
        }
        cur = cur + ss;
    }
}

effs effFromCounting(TH1F* baseData, TH1F* postData, TH1F* baseBG, TH1F* postBG, double baseP, double baseE, double postP, double postE, double minMZ=60., double maxMZ=120.){
    /* 
     * postD = postData count
     * postP = postData param
     * postB = postBackground count
     * postDerr = postData count error
     * postE = postBackground count error
     */
    effs tmp;
    double baseD = baseData->Integral(baseData->FindBin(minMZ), baseData->FindBin(maxMZ), "width");
    double postD = postData->Integral(postData->FindBin(minMZ), postData->FindBin(maxMZ), "width");
    double baseB = baseBG->Integral(baseBG->FindBin(minMZ), baseBG->FindBin(maxMZ));
    double postB = postBG->Integral(postBG->FindBin(minMZ), postBG->FindBin(maxMZ));
    double baseDerr = sqrt(baseD);
    double postDerr = sqrt(postD);

    //std::cout << "baseD " << baseD << std::endl;
    //std::cout << "postD " << postD << std::endl;
    //std::cout << "baseB " << baseB << std::endl;
    //std::cout << "postB " << postB << std::endl;
    //std::cout << "baseDerr " << baseDerr << std::endl;
    //std::cout << "postDerr " << postDerr << std::endl;

    tmp.eff = (postD - (postP*postB)) / (baseD - (baseP*baseB));
    /* Note: dEff = Eff * Sqrt((da^2+db^2)/(a-b)^2 + (dc^2-dd^2)/(c-d)^2) */
    tmp.err = tmp.eff * sqrt( 
            ( ( postE * postE ) + ( postDerr * postDerr ) ) / ( ( postD - postP * postB ) * ( postD - postP * postB ) ) 
            +  ( ( baseE * baseE ) + (baseDerr * baseDerr ) ) / ( ( baseD - baseP * baseB ) * ( baseD - baseP * baseB ) ) 
            );

    return tmp;
}

effs effFromSignal(TH1F* baseSig, TH1F* postSig, double baseP, double baseE, double postP, double postE, double minMZ=60., double maxMZ=120.){
    effs tmp;
    double baseS = baseSig->Integral(baseSig->FindBin(minMZ), baseSig->FindBin(maxMZ), "width");
    double postS = postSig->Integral(postSig->FindBin(minMZ), postSig->FindBin(maxMZ), "width");

    //std::cout << "baseS " << baseS << std::endl;
    //std::cout << "postS " << postS << std::endl;

    tmp.eff = ( postS * postP ) / ( baseS * baseP );
    tmp.err = tmp.eff * sqrt( (baseE * baseE)/(( baseS * baseP )*( baseS * baseP )) + (postE * postE) / (( postS * postP )*( postS * postP )) );


    // TODO: Double check formula 
    return tmp;
}

void printEffs(const electronLocation probeLoc, const eventRequirements eventrq, const bin xBin, const double sigeff, const double counteff, const double denom, const bool usePhiStar){
    /* Prints probewp ptmin ptmax etamin etamax pumin pumax sigeff sigerr counteff counterr */
    using namespace std;
    cout << "#XMin XMax EtaMin EtaMax PUMin PUMax NumParms eff systp systm den phistar" << endl;
    //cout << setw(6) << xBin.minX << " ";
    cout << xBin.maxX << " ";
    switch (probeLoc){
        case EB:
            cout << 0 << " ";
            cout << 1.4442 << " ";
            break;
        case EE:
            cout << 1.566 << " ";
            cout << 2.5 << " ";
            break;
        case ET:
            cout << 0 << " ";
            cout << 2.5 << " ";
            break;
        case NT:
            cout << 2.5 << " ";
            cout << 2.850 << " ";
            break;
        case HF:
            cout << 3.1 << " ";
            cout << 4.6 << " ";
            break;
    }

    cout << eventrq.minPU << " ";
    cout << eventrq.maxPU << " ";
    cout << "4" << " "; // Number of params
    const double diff = fabs(sigeff - counteff)/2.;
    const double avg = fabs((sigeff + counteff)/2.);
    cout << avg << " ";
    cout << avg+diff << " ";
    cout << avg-diff << " ";
    cout << denom << " ";
    cout << usePhiStar << endl;
}

int fitDistributions(std::string bgfitfile, std::string signalFile, std::string ZEffFile, std::string outFile, std::string tagWP, std::string probeWP, electronLocation tagLoc, electronLocation probeLoc, eventRequirements eventrq, bin xBin, bool usePhiStar=false){
    // Get our background and set variables
    Background bg(bgfitfile);
    double midX = (xBin.maxX + xBin.minX)/2.;
    //std::cout << "midX: " << midX << std::endl;
    double midPU = (eventrq.maxPU + eventrq.minPU)/2.;
    //std::cout << "midPU: " << midPU << std::endl;
    bg.setBackground(midX, midPU, usePhiStar); // TODO: Fill in pt, pu
    //std::cout << usePhiStar << std::endl;
    //bg.print();
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
                eventrq.minPU <= PU && PU <= eventrq.maxPU 
                && eventrq.minMZ <= MZ && MZ <= eventrq.maxMZ 
                //&& 20. <= zes->reco.pt[0] && 20. <= zes->reco.pt[1]
                //&& 30. <= zes->reco.pt[0] && 20. <= zes->reco.pt[1]
           ){
            /* We set try either electron as the "probe", since this is MC either can be the "tag" */
            float tagX;
            float probeX;

            for (int i=0; i < 2; ++i){
                bool probeMatch = false;
                bool tagMatch = false;
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
                    eX1 = zes->reco.phistar;
                    tagX = -1;
                    probeX = -1;
                } else {
                    eX0 = zes->reco.pt[i];
                    eX1 = zes->reco.pt[j];
                    tagX = 30;
                    probeX = 20;
                }
                double eeta0 = fabs(zes->reco.eta[i]);
                double eeta1 = fabs(zes->reco.eta[j]);
                // Now we make sure exactly one e passes the tag region, and one the probe region requirements
                if ( xBin.minX <= eX0 && eX0 <= xBin.maxX && probeX <= eX0){
                    switch (probeLoc){
                        case EB:
                            if ( eeta0 < 1.4442 ){ probeMatch = true; }
                            break;
                        case EE:
                            if (1.566 < eeta0 && eeta0 < 2.5 ){ probeMatch = true; }
                            break;
                        case ET:
                            if ( (eeta0 < 1.4442) || (1.566 < eeta0 && eeta0 < 2.5) ){ probeMatch = true; }
                            break;
                        case NT:
                            if (2.5 <= eeta0 && eeta0 < 2.850 ){ probeMatch = true; }
                            break;
                        case HF:
                            if (3.1 < eeta0 && eeta0 < 4.6 ){ probeMatch = true; }
                            break;
                    }
                } 
                if ( probeMatch && tagX <= eX1 ){
                    switch (tagLoc){
                        case EB:
                            if ( eeta1 < 1.4442 ){ tagMatch = true; }
                            break;
                        case EE:
                            if (1.566 < eeta1 && eeta1 < 2.5 ){ tagMatch = true; }
                            break;
                        case ET:
                            if ( (eeta1 < 1.4442) || (1.566 < eeta1 && eeta1 < 2.5) ){ tagMatch = true; }
                            break;
                        case NT:
                            if (2.5 <= eeta1 && eeta1 < 2.850 ){ tagMatch = true; }
                            break;
                        case HF:
                            if (3.1 < eeta1 && eeta1 < 4.6 ){ tagMatch = true; }
                            break;
                    }
                }
                // Base Cuts, and Post Cuts which are a strict subset
                if ( tagMatch && probeMatch ){ 
                    GLOBAL.signalHisto->Fill(MZ);
                    break;
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
                eX0 = ze->reco.pt[0];
                eXCut0 = 30;
                eX1 = ze->reco.pt[1];
                eXCut1 = 20;
            }

            if (
                    eXCut0 <= eX0 && eXCut1 <= eX1
                    && xBin.minX <= eX0 && eX0 <= xBin.maxX
                    && ze->reco.isSelected(0,"HLT-GSF") 
                    && ze->reco.isSelected(0,"WP80")
               ){
                bool tagPass = false;
                double teta = fabs(ze->reco.eta[0]);
                switch (tagLoc){
                    case EB:
                        if ( teta < 1.4442 ){ tagPass = true; }
                        break;
                    case EE:
                        if (1.566 < teta && teta < 2.5 ){ tagPass = true; }
                        break;
                    case ET:
                        if ( (teta < 1.4442) || (1.566 < teta && teta < 2.5) ){ tagPass = true; }
                        break;
                    case NT:
                        if (2.5 <= teta && teta < 2.850 ){ tagPass = true; }
                        break;
                    case HF:
                        if (3.1 < teta && teta < 4.6 ){ tagPass = true; }
                        break;
                }
                if (tagPass){
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
                        case ET:
                            if ( ( (eeta < 1.4442) || (1.566 < eeta && eeta < 2.5) ) && ze->reco.isSelected(1,"Supercluster-Eta") && ze->reco.isSelected(1,"GsfTrack-EtaDet") ){ 
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
                    //std::cout << MZ << std::endl;
                }
            }
        }
        run2 = ze->GetNextEvent();
    }

    std::cout << "TEST" << std::endl;
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
    baseHisto->Fit(baseFitFunc, "RMEWLQ");
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
    postcutHisto->Fit(postFitFunc, "RMEWLQ");
    postcutHisto->Draw("E");
    TH1F* postBG = (TH1F*)GLOBAL.backgroundHisto->Clone("postBG");
    postBG->Scale(postFitFunc->GetParameter(0));
    postBG->SetLineStyle(2);
    postBG->Draw("same");

    // Calculate Eff
    effs countEff = effFromCounting(baseHisto, postcutHisto, GLOBAL.backgroundHisto, GLOBAL.backgroundHisto, baseFitFunc->GetParameter(0), baseFitFunc->GetParError(0), postFitFunc->GetParameter(0), postFitFunc->GetParError(0));
    effs sigEff = effFromSignal( GLOBAL.signalHisto, GLOBAL.signalHisto, baseFitFunc->GetParameter(1), baseFitFunc->GetParError(1), postFitFunc->GetParameter(1), postFitFunc->GetParError(1));
    //std::cout << "COUNT EFF: " << countEff.eff << " SIG EFF: " << sigEff.eff << std::endl;
    
    canvas->cd(0);

    std::string name(outFile.begin(), outFile.end()-5);
    std::string pngname = name + std::string(".png");
    canvas->Print(pngname.c_str(), "png");
    outfile->Write();

    //Prints eff stats for text file
    double baseD = baseHisto->Integral(baseHisto->FindBin(eventrq.minMZ), baseHisto->FindBin(eventrq.maxMZ), "width");
    double baseB = GLOBAL.backgroundHisto->Integral(GLOBAL.backgroundHisto->FindBin(eventrq.minMZ), GLOBAL.backgroundHisto->FindBin(eventrq.maxMZ));

    double denom = (baseD - (baseFitFunc->GetParameter(0)*baseB));
    std::cout << "TEST" << std::endl;
    printEffs(probeLoc, eventrq, xBin, sigEff.eff, countEff.eff, denom, usePhiStar);

    return 0;
}

int main(int argc, char* argv[]){
    int argcCorrect = 14;
    if (argc < argcCorrect) {
        std::cout<<"Not enough arguments. Use:\nfitEffAcc.exe bgfitFile signalFile ZEffFile outFile tagLoc probeLoc minPU maxPU minMZ maxMZ minX maxX\n";
        return 1;
    } else if (argc > argcCorrect){
        std::cout<<"Too many arguments. Use:\nfitEffAcc.exe bgfitFile signalFile ZEffFile outFile tagLoc probeLoc minPU maxPU minMZ maxMZ minX maxX\n";
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
        conv["ET"] = ET;
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

        bin xBin;

        inStream.str(argv[11]);
        inStream >> xBin.minX;
        inStream.clear();
        inStream.str(argv[12]);
        inStream >> xBin.maxX;
        inStream.clear();

        bool usePhiStar;
        inStream.str(argv[13]);
        inStream >> usePhiStar;
        inStream.clear();

        // Map location to other features
        // Hard coded for now
        std::string tagWP;
        switch (tagLoc){
            case EB:
            case EE:
            case ET:
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
            case EE:
            case ET:
                probeWP = "WP80";
                break;
            case NT: // No NT case?
                probeWP = "NTTightElectronId-EtaDet";
                break;
            case HF:
                probeWP = "HFTID";
        }

        std::cout << "#efficiency name: " << probeWP << std::endl;
        std::cout << "#dimension: 1" << std::endl;

        //std::cout << usePhiStar << std::endl;

        //std::cout << " Tag: " << tagWP << " Probe: " << probeWP << " MinPt: " << xBin.minX << " MaxPt: " << xBin.maxX << " MinPU: " << eventrq.minPU << " MaxPU: " << eventrq.maxPU << std::endl;
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
                xBin,
                usePhiStar
                );

        return runCondition;
    }
}

/* Compile time notes:
 *    g++ -O2 -o fitEffAcc_trigger.exe fitEffAcc.cc ZEffTree.cc Background.cc `root-config --cflags --libs` 
 */
