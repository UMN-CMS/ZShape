// ZShape Code
#include "../../MakeZEffTree/src/ZEffTree.h"
#include "../ElectronLocation/ElectronLocation.h"

// Root
#include "TH1.h"
#include "TFile.h"
#include <TROOT.h>  // Pulls in gROOT
#include <TStyle.h>  // Pulls in gStyle
#include <TRandom3.h>  // Needed to generate random numbers for smearing
#include <TLorentzVector.h>  // Used to recalculate MZ after smearing
#include <TF1.h>  // Background function
#include <TMath.h>  // Used to grab Erfc

// STD
#include <string>
#include <sstream>
#include <iostream>  // cout

struct global{
    TH1D* signalHisto;
} GLOBAL;

double bgFunc(const double x, const double alpha, const double gamma, const double delta){
    double fitval = TMath::Erfc((alpha-x)/delta) * TMath::Exp(-gamma*x);
    return fitval;
}

double functiontofit(const double *x, const double *par) {
    // Generate values for our signal and our background
    double backgroundVal = par[0] * bgFunc(x[0], par[2], par[3], par[4]);
    double signalVal = par[1] * GLOBAL.signalHisto->GetBinContent(GLOBAL.signalHisto->FindBin(x[0]));
    return backgroundVal + signalVal;
}

//TH1D* returnBGHisto(const double alpha, const double gamma, const double delta, const TH1D* histoToClone){
//    // Copy the binning of the signal histo
//    TH1D* bgHisto = (TH1D*)histoToClone->Clone("bgHisto");
//    // Turn our analytic function into a histogram
//    for ( int i = 1; i <= bgHisto>GetNbinsX(); ++i) {
//        const double xval = bgHisto->GetBinCenter(i);
//        const double binVal = bgFunc(xval, alpha, gamma, delta);
//        bgHisto->SetBinContent(i, binVal);
//    }
//    return bgHisto;
//}

double compareTH1Ds(const TH1D* h0, const TH1D* h1){
    double chi2 = 0.;

    const int startPT = 50;
    const int endPT = 150;
    // Normalize the two histograms to 1 
    TH1D* hc0 = (TH1D*)h0->Clone("hc0");
    hc0->Scale(1. / hc0->Integral(hc0->FindBin(startPT), hc0->FindBin(endPT)));
    hc0->Sumw2();
    TH1D* hc1 = (TH1D*)h1->Clone("hc1");
    hc1->Scale(1. / hc1->Integral(hc1->FindBin(startPT), hc1->FindBin(endPT)));
    hc1->Sumw2();

    // Loop
    const int n0 = hc0->GetNbinsX();  // Number of bins
    for (int i = 1; i <= n0; ++i){
        double v0 = hc0->GetBinContent(i);
        double dv0 = hc0->GetBinError(i);
        //std::cout << "H0: " << v0 << " " << dv0 << std::endl;

        double v1 = hc1->GetBinContent(i);
        double dv1 = hc1->GetBinError(i);
        //std::cout << "H1: " << v1 << " " << dv1 << std::endl;

        double addtochi2 = (v0 - v1)*(v0 - v1) / (dv0 * dv1);
        chi2 += addtochi2;
    }

    return chi2;
}

int IterateSmearing(const std::string inputFile, const std::string inputMCFile){
    // Root style
    gROOT->SetStyle("Plain");
    gStyle->SetOptTitle(0);  // Remove title
    gStyle->SetOptStat(0);  // Remove Stats Box
    gStyle->SetHistLineWidth(2);  // Remove Stats Box

    /* Prepare the histogram to put the data in */
    // Data
    TH1D* Hdata = new TH1D("hdata","hdata", 100, 50., 150.);

    // Open file to fit, and make histograms
    // Data
    TFile ZEffFile(inputFile.c_str(), "READ");
    ZEffTree* ze;
    ze = new ZEffTree(ZEffFile, false);

    bool run = true;
    bool flop = false;
    while (run){
        // Skip everyother event
        if (flop){
            flop = false;
            run = ze->GetNextEvent();
            continue;
        } else {
            flop = true;
        }
        ze->Entries();
        int ETElectron;
        int HFElectron;
        /* Assign Electron 0 and 1 */
        if ( inAcceptance(ET, ze->reco.eta[0]) && inAcceptance(HF, ze->reco.eta[1])){
            ETElectron = 0;
            HFElectron = 1;
        } else if ( inAcceptance(HF, ze->reco.eta[1]) && inAcceptance(ET, ze->reco.eta[0])){
            ETElectron = 1;
            HFElectron = 0;
        } else {
            run = ze->GetNextEvent();
            continue;
        }

        /* Cuts */
        if ( ze->reco.pt[0] > 20. && ze->reco.pt[1] > 20.){
            if ( ze->reco.isSelected(ETElectron, "WP80") && ze->reco.isSelected(HFElectron, "HFTightElectronId-EtaDet" )){
                Hdata->Fill(ze->reco.mz);
            }
        }
        run = ze->GetNextEvent();
    }


    // Smearing MC
    const int randSeed = 123456; //using constant seed for reproducibility
    TRandom3* trand = new TRandom3(randSeed);

    double meanHF;
    double sigmaHF;
    for ( meanHF = 0.85; meanHF < 0.95; meanHF += 0.01){
        for ( sigmaHF = .12; sigmaHF < 0.16; sigmaHF += 0.001){
            // MC
            TH1D* HMC = new TH1D("hmc", "hmc", 100, 50., 150.);

            TFile ZEffMCFile(inputMCFile.c_str(), "READ");
            ZEffTree* zemc;
            zemc = new ZEffTree(ZEffMCFile, false);
            bool runmc = true;

            while (runmc){
                zemc->Entries();
                int ETElectron;
                int HFElectron;
                /* Assign Electron 0 and 1 */
                if ( inAcceptance(ET, zemc->reco.eta[0]) && inAcceptance(HF, zemc->reco.eta[1])){
                    ETElectron = 0;
                    HFElectron = 1;
                } else if ( inAcceptance(HF, zemc->reco.eta[1]) && inAcceptance(ET, zemc->reco.eta[0])){
                    ETElectron = 1;
                    HFElectron = 0;
                } else {
                    runmc = zemc->GetNextEvent();
                    continue;
                }

                /* Smearing */
                double MZ = -1.;
                double ptHF = zemc->reco.pt[HFElectron];

                ptHF *= trand->Gaus(meanHF, sigmaHF);

                /* Recalculate MZ */
                TLorentzVector eET;
                TLorentzVector eHF;
                TLorentzVector Z;
                eET.SetPtEtaPhiM(zemc->reco.pt[ETElectron], zemc->reco.eta[ETElectron], zemc->reco.phi[ETElectron], 5.109989e-4);
                eHF.SetPtEtaPhiM(ptHF, zemc->reco.eta[HFElectron], zemc->reco.phi[HFElectron], 5.109989e-4);
                Z = eET + eHF;
                MZ = Z.M(); // Get the invarient mass from the Z

                //std::cout << "ET: " << zemc->reco.pt[ETElectron] << " " << ptET << std::endl;
                //std::cout << "HT: " << zemc->reco.pt[HFElectron] << " " << ptHF << std::endl;
                //std::cout << "MZ: " << MZ << " " << Z.M() << std::endl;

                /* Cuts */
                if ( zemc->reco.pt[ETElectron] > 20. && ptHF > 20.){
                    if ( zemc->reco.isSelected(ETElectron, "WP80") && zemc->reco.isSelected(HFElectron, "HFTightElectronId-EtaDet" )){
                        HMC->Fill(MZ);
                    }
                }
                runmc = zemc->GetNextEvent();
                //std::cout << Hdata->GetEntries() << " " << HMC->GetEntries() << std::endl;
            }
            /* Normalize our MC Histogram */
            HMC->Scale(1. / HMC->Integral(HMC->FindBin(50.), HMC->FindBin(150.)));
            HMC->Sumw2(); // Recompute errors

            /* Now add a background and fit it */
            GLOBAL.signalHisto = HMC;
            TF1* baseFitFunc = new TF1("baseFitFunc", functiontofit, 50., 150., 5);
            baseFitFunc->SetParLimits(0, 0., 10000.);
            baseFitFunc->SetParLimits(1, 0., 100000.);
            baseFitFunc->SetParLimits(2, 40., 80.);  // Alpha
            baseFitFunc->SetParLimits(3, 0., 0.2); // Gamma
            baseFitFunc->SetParLimits(4, 1., 50.); // Delta
            baseFitFunc->SetParameter(0, 500.);
            baseFitFunc->SetParameter(1, 50000.);
            baseFitFunc->SetParameter(2, 50.);
            baseFitFunc->SetParameter(3, 0.);
            baseFitFunc->SetParameter(4, 2.);

            Hdata->Fit(baseFitFunc, "RMEWLQ");
            std::cout << "\t" << baseFitFunc->GetChisquare();
            std::cout << " Mean: " << meanHF;
            std::cout << " Sigma: " << sigmaHF;
            std::cout << " P0: " << baseFitFunc->GetParameter(0);
            std::cout << " P1: " << baseFitFunc->GetParameter(1);
            std::cout << " P2: " << baseFitFunc->GetParameter(2);
            std::cout << " P3: " << baseFitFunc->GetParameter(3);
            std::cout << " P4: " << baseFitFunc->GetParameter(4);
            std::cout << std::endl;

            //std::cout << compareTH1Ds(Hdata, HMC) << " M: " << meanHF << " S: " << sigmaHF << std::endl;
            delete HMC;
        }
    }

    return 0;
}

int main(int argc, char* argv[]){
    const short argcCorrect = 3;
    if (argc < argcCorrect) {
        std::cout<<"Not enough arguments. Use:\nSmearTuples.exe ZEffFile_data ZEffFile_MC\n";
        return 1;
    } else if (argc > argcCorrect){
        std::cout<<"Too many arguments. Use:\nSmearTuples.exe ZEffFile_data ZEffFile_MC\n";
        return 1;
    } else {
        // Read in arguments
        std::istringstream inStream;

        std::string inputFile;
        inStream.str(argv[1]);
        inStream >> inputFile;
        inStream.clear();

        std::string inputMCFile;
        inStream.str(argv[2]);
        inStream >> inputMCFile;
        inStream.clear();

        return IterateSmearing(inputFile, inputMCFile);
    }
}
