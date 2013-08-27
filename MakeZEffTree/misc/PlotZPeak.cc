// ZShape Code
#include "../src/ZEffTree.h"
#include "../../2011EffCalculation/ElectronLocation/ElectronLocation.h"

// Root
#include "TH1.h"
#include "TFile.h"
#include "TCanvas.h"
#include "TLatex.h"  // Used to draw text on the plot
#include <TROOT.h>  // Pulls in gROOT
#include <TStyle.h>  // Pulls in gStyle

// STD
#include <string>
#include <sstream>

int makeTupleCuts(const std::string inputFile, const std::string outFile){
    // Root style
    gROOT->SetStyle("Plain");
    gStyle->SetOptTitle(0);  // Remove title
    gStyle->SetOptStat(0);  // Remove Stats Box
    gStyle->SetHistLineWidth(2);  // Remove Stats Box

    /* Canvas */
    TCanvas* canvas = new TCanvas("ZPeak", "ZPeak", 1200, 900);
    //canvas->SetLeftMargin(0.25);
    canvas->SetRightMargin(0.03);
    canvas->SetTopMargin(0.02);

    /* Text */
    // CMS Preliminary
    //TLatex* cmsPrelim = new TLatex(0.12, 0.97, "CMS Preliminary");
    //cmsPrelim->SetTextAlign(13);  // Align by top left of the words
    TLatex* cmsPrelim = new TLatex(0.95, 0.95, "CMS Preliminary");
    cmsPrelim->SetTextAlign(33);  // Align by top left of the words
    cmsPrelim->SetNDC();  // Draw according to pad coordinates, not unitful coordinates
    // Luminosity
    TLatex* luminosity = new TLatex(0.95, 0.90, "5.5 fb^{-1} at 7 TeV");
    luminosity->SetTextAlign(33);  // Align by top left of the words
    luminosity->SetNDC();  // Draw according to pad coordinates, not unitful coordinates
    // Plot Title
    //TLatex* plotTitle = new TLatex(0.97, 0.97, "ECAL-HF Invarient Mass");
    //plotTitle->SetTextAlign(33);  // Align by top left of the words
    //plotTitle->SetNDC();  // Draw according to pad coordinates, not unitful coordinates

    /* Prepare the histogram to put the data in */
    const std::string Z0MassName = "Z0_mass";
    TH1I* Z0Mass = new TH1I(Z0MassName.c_str(), Z0MassName.c_str(), 100, 50., 150.);
    Z0Mass->GetXaxis()->SetTitle("m_{ee} [GeV]");
    Z0Mass->GetYaxis()->SetTitle("Counts/GeV");
    Z0Mass->GetYaxis()->SetTitleOffset(1.3);  // Move axis title away from side to avoid clipping
    Z0Mass->GetYaxis()->SetTitleSize(0.04);  // Make Axis title larger
    Z0Mass->SetMarkerStyle(20);  // Use black circles for points
    Z0Mass->SetMarkerSize(0.5);  // Make markers half the normal size

    // Open file to fit, and make histograms
    TFile ZEffFile(inputFile.c_str(), "READ");
    ZEffTree* ze;
    ze = new ZEffTree(ZEffFile, false);

    bool run = true;
    while (run){
        ze->Entries();
        int ETElectron;
        int HFElectron;
        const double MZ = ze->reco.mz;
        const short PU = ze->reco.nverts;
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
            //if ( ze->reco.isSelected(ETElectron, "WP80")){
                Z0Mass->Fill(MZ);
            }
        }
        run = ze->GetNextEvent();
    }

    Z0Mass->Draw("E");
    cmsPrelim->Draw();
    luminosity->Draw();
    //plotTitle->Draw();
    //plotTitle->Draw();
    canvas->Print(outFile.c_str());

    return 0;
}

int main(int argc, char* argv[]){
    const short argcCorrect = 3;
    if (argc < argcCorrect) {
        std::cout<<"Not enough arguments. Use:\nPlotZPeak.exe ZEffFile outputFile\n";
        return 1;
    } else if (argc > argcCorrect){
        std::cout<<"Too many arguments. Use:\nPlotZPeak.exe ZEffFile outputFile\n";
        return 1;
    } else {
        // Read in arguments
        std::istringstream inStream;

        std::string inputFile;
        inStream.str(argv[1]);
        inStream >> inputFile;
        inStream.clear();

        std::string outFile;
        inStream.str(argv[2]);
        inStream >> outFile;
        inStream.clear();

        return makeTupleCuts(inputFile, outFile);
    }
}
