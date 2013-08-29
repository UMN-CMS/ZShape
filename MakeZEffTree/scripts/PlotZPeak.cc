// ZShape Code
#include "../src/ZEffTree.h"
#include "../../2011EffCalculation/ElectronLocation/ElectronLocation.h"

// Root
#include "TH1.h"
#include "TFile.h"
#include "TCanvas.h"
#include "TF1.h"  // BG Function
#include <TMath.h>  // Erfc function and exp
#include "TLatex.h"  // Used to draw text on the plot
#include <TROOT.h>  // Pulls in gROOT
#include <TStyle.h>  // Pulls in gStyle
#include <TRandom3.h>  // Needed to generate random numbers for smearing
#include <TLorentzVector.h>  // Used to recalculate MZ after smearing
#include <TLegend.h>  // Legend
#include <TPDF.h>  // PDF output

// STD
#include <string>
#include <sstream>
#include <iostream>  // cout

double bgFunc(const double x, const double alpha, const double gamma, const double delta){
    return TMath::Erfc((alpha-x)/delta) * TMath::Exp(-gamma*x);
}

TH1D* makeCombinedHisto(const double alpha, const double gamma, const double delta, const double bgAmp, const double mcAmp, const TH1D* mcHisto){
    TH1D* toReturn = (TH1D*)mcHisto->Clone("combo");
    // Turn our analytic function into a histogram
    for ( int i = 1; i <= toReturn->GetNbinsX(); ++i) {
        const double xval = toReturn->GetBinCenter(i);
        const double binVal = bgAmp * bgFunc(xval, alpha, gamma, delta);
        const double mcVal = mcAmp * mcHisto->GetBinContent(i);
        toReturn->SetBinContent(i, binVal + mcVal);
    }

    return toReturn;
}

TH1D* makeBGHisto(const double alpha, const double gamma, const double delta, TH1D* bgHisto){
    // Turn our analytic function into a histogram
    for ( int i = 1; i <= bgHisto->GetNbinsX(); ++i) {
        const double xval = bgHisto->GetBinCenter(i);
        const double binVal = bgFunc(xval, alpha, gamma, delta);
        bgHisto->SetBinContent(i, binVal);
        //std::cout << i << " " << binVal << std::endl;
    }

    return bgHisto;
}

int makeTupleCuts(const std::string inputFile, const std::string inputMCFile, const std::string outFile){
    /* Fit params */
    const double meanHF = 0.93;
    const double sigmaHF = 0.097;
    const double bgAmp = 638.778;
    const double mcAmp = 100677;
    const double alpha = 61.9994;
    const double gamma = 0.0201975;
    const double delta = 13.1204;

    // Root style
    gROOT->SetStyle("Plain");
    gStyle->SetOptTitle(0);  // Remove title
    gStyle->SetOptStat(0);  // Remove Stats Box
    gStyle->SetHistLineWidth(2);  // Remove Stats Box

    /* Canvas */
    TCanvas* canvas = new TCanvas("ZPeak", "ZPeak", 1200, 900);
    canvas->SetRightMargin(0.03);
    canvas->SetTopMargin(0.07);
    //canvas->SetLogy();

    /* Text */
    // CMS Preliminary
    TLatex* cmsPrelim = new TLatex(0.10, 0.935, "CMS Preliminary");
    cmsPrelim->SetTextAlign(11);  // Align by top left of the words
    cmsPrelim->SetNDC();  // Draw according to pad coordinates, not unitful coordinates
    // Luminosity
    // We had 5.49799553508 recorded, 5.72404865529 delivered according to lumiCalc
    TLatex* luminosity = new TLatex(0.97, 0.935, "5.5 fb^{-1} at 7 TeV");
    luminosity->SetTextAlign(31);
    luminosity->SetNDC();
    // Leptons
    TLatex* leptons = new TLatex(0.13, 0.92, "#splitline{|#eta_{1}| < 2.5}{3.1 < |#eta_{2}| < 4.6}");
    leptons->SetTextAlign(13);
    leptons->SetNDC();  // Draw according to pad coordinates, not unitful coordinates
    leptons->SetTextSize(0.05);

    /* Prepare the histogram to put the data in */
    // Data
    const std::string Z0MassName = "Z0_mass";
    TH1I* Z0Mass = new TH1I(Z0MassName.c_str(), Z0MassName.c_str(), 100, 50., 150.);
    Z0Mass->GetXaxis()->SetTitle("M_{ee} [GeV]");
    Z0Mass->GetYaxis()->SetTitle("Counts/GeV");
    Z0Mass->GetYaxis()->SetTitleOffset(1.3);  // Move axis title away from side to avoid clipping
    Z0Mass->GetYaxis()->SetTitleSize(0.04);  // Make Axis title larger
    Z0Mass->SetMarkerStyle(20);  // Use black circles for points
    Z0Mass->SetMarkerSize(1);  // Make markers half the normal size
    // MC
    const std::string Z0MassMCName = "Z0_mass_MC";
    TH1D* Z0MassMC = new TH1D(Z0MassMCName.c_str(), Z0MassMCName.c_str(), 100, 50., 150.);
    Z0MassMC->SetLineColor(2);  // Red line
    // BG
    const std::string bgName = "bg";
    TH1D* bgHisto = new TH1D(bgName.c_str(), bgName.c_str(), 100, 50., 150.);
    bgHisto->SetLineStyle(2);  // Dotted line
    bgHisto->SetLineColor(2);  // Red line

    /* Legend */
    //TLegend* legend = new TLegend(0.82, 0.77, 0.97, .925);
    TLegend* legend = new TLegend(0.70, 0.77, 0.95, .925);
    legend->AddEntry(Z0Mass, " Data");
    legend->AddEntry(Z0MassMC, " MC + BG");
    legend->AddEntry(bgHisto, " BG Only");
    legend->SetFillColor(0);  // White background
    legend->SetBorderSize(0);  // Remove border
    legend->SetTextSize(.06);  // Make text bigger

    // Open file to fit, and make histograms
    // Data
    TFile ZEffFile(inputFile.c_str(), "READ");
    ZEffTree* ze;
    ze = new ZEffTree(ZEffFile, false);

    bool runMC = true;
    while (runMC){
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
            runMC = ze->GetNextEvent();
            continue;
        }

        /* Cuts */
        if ( ze->reco.pt[0] > 20. && ze->reco.pt[1] > 20.){
            if ( ze->reco.isSelected(ETElectron, "WP80") && ze->reco.isSelected(HFElectron, "HFTightElectronId-EtaDet" )){
                Z0Mass->Fill(ze->reco.mz);
            }
        }
        runMC = ze->GetNextEvent();
    }

    // MC
    TFile ZEffMCFile(inputMCFile.c_str(), "READ");
    ZEffTree* zemc;
    zemc = new ZEffTree(ZEffMCFile, false);

    // Smearing MC
    const bool doSmear = true;
    const int randSeed = 123456; //using constant seed for reproducibility
    TRandom3* trand = new TRandom3(randSeed);

    bool run = true;
    while (run){
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
            run = zemc->GetNextEvent();
            continue;
        }

        /* Smearing */
        double MZ = zemc->reco.mz;
        double ptET = zemc->reco.pt[ETElectron];
        double ptHF = zemc->reco.pt[HFElectron];

        if (doSmear){ // Smear only HF
            ptHF *= trand->Gaus(meanHF, sigmaHF);

            /* Recalculate MZ */
            TLorentzVector eET;
            TLorentzVector eHF;
            TLorentzVector Z;
            eET.SetPtEtaPhiM(ptET, zemc->reco.eta[ETElectron], zemc->reco.phi[ETElectron], 5.109989e-4);
            eHF.SetPtEtaPhiM(ptHF, zemc->reco.eta[HFElectron], zemc->reco.phi[HFElectron], 5.109989e-4);
            Z = eET + eHF;
            MZ = Z.M(); // Get the invarient mass from the Z
        }

        /* Cuts */
        if ( ptET > 20. && ptHF > 20.){
            if ( zemc->reco.isSelected(ETElectron, "WP80") && zemc->reco.isSelected(HFElectron, "HFTightElectronId-EtaDet" )){
                Z0MassMC->Fill(MZ);
            }
        }
        run = zemc->GetNextEvent();
    }

    // Make the combined histogram of Background + MC
    Z0MassMC->Scale(1 / Z0MassMC->Integral(Z0MassMC->FindBin(50), Z0MassMC->FindBin(150))); // Normalize
    TH1D* comboHisto = makeCombinedHisto(alpha, gamma, delta, bgAmp, mcAmp, Z0MassMC);
    // Make BG Histo 
    bgHisto = makeBGHisto(alpha, gamma, delta, bgHisto);

    // Scale histograms and preserve erros
    Z0Mass->Sumw2();
    const double areaData = Z0Mass->Integral(Z0Mass->FindBin(50), Z0Mass->FindBin(150));
    comboHisto->Sumw2();
    const double areaMC = comboHisto->Integral(comboHisto->FindBin(50), comboHisto->FindBin(150));
    comboHisto->Scale(areaData/areaMC);
    bgHisto->Scale(bgAmp);

    Z0Mass->Draw("E");
    bgHisto->Draw("Hist Same");
    comboHisto->Draw("Hist Same");
    Z0Mass->Draw("E Same"); // redraw to put it on top
    cmsPrelim->Draw();
    luminosity->Draw();
    leptons->Draw();
    legend->Draw();
    canvas->Print(outFile.c_str());

    return 0;
}

int main(int argc, char* argv[]){
    const short argcCorrect = 4;
    if (argc < argcCorrect) {
        std::cout<<"Not enough arguments. Use:\nPlotZPeak.exe ZEffFile_data ZEffFile_MC outputFile\n";
        return 1;
    } else if (argc > argcCorrect){
        std::cout<<"Too many arguments. Use:\nPlotZPeak.exe ZEffFile_data ZEffFile_MC outputFile\n";
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

        std::string outFile;
        inStream.str(argv[3]);
        inStream >> outFile;
        inStream.clear();

        return makeTupleCuts(inputFile, inputMCFile, outFile);
    }
}
