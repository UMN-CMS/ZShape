// ZShape Code
#include "../../MakeZEffTree/src/ZEffTree.h"
#include "../ElectronLocation/ElectronLocation.h"

// Root
#include "TH1.h"
#include "TF1.h"
#include "TFile.h"
#include "TAxis.h"
#include "TObject.h"
//#include "TCanvas.h"
#include <TROOT.h>

// STD
#include <string>
#include <sstream>

int makeTupleCuts(const std::string inputFile, const std::string outFile){
    // Root style
    gROOT->SetStyle("Plain");

    // Prepare output
    TFile* outfile;
    outfile = new TFile(outFile.c_str(), "RECREATE");

    /* Prepare the histogram to put the data in */
    // Z Mass
    TH1I* Z0MassHisto = new TH1I("Z0_mass", "Z0_mass", 50, 50., 150.);
    Z0MassHisto->SetDirectory(outfile);
    Z0MassHisto->GetXaxis()->SetTitle("m_{ee} [GeV]");
    Z0MassHisto->GetYaxis()->SetTitle("Counts/GeV");
    // Z Mass Fine
    TH1I* Z0MassFineHisto = new TH1I("Z0_mass_fine", "Z0_mass_fine", 120, 60., 120.);
    Z0MassFineHisto->SetDirectory(outfile);
    Z0MassFineHisto->GetXaxis()->SetTitle("m_{ee} [GeV]");
    Z0MassFineHisto->GetYaxis()->SetTitle("Counts/GeV");
    // Z Mass Fine
    TH1I* Z0RapidityHisto = new TH1I("Z0_rapidity", "Z0_rapidity", 100, -5., 5.);
    Z0RapidityHisto->SetDirectory(outfile);
    Z0RapidityHisto->GetXaxis()->SetTitle("Y_{ee}");
    Z0RapidityHisto->GetYaxis()->SetTitle("Counts");
    // Z pt
    TH1I* Z0ptHisto = new TH1I("Z0_pt", "Z0_pt", 200, 0, 400);
    Z0ptHisto->SetDirectory(outfile);
    Z0ptHisto->GetXaxis()->SetTitle("p_{T,Z} [GeV]");
    Z0ptHisto->GetYaxis()->SetTitle("Counts/Gev");
    // e pt
    TH1I* e0ptHisto = new TH1I("e0_pt", "e0_pt", 200, 0, 400);
    e0ptHisto->SetDirectory(outfile);
    e0ptHisto->GetXaxis()->SetTitle("p_{T} [GeV]");
    e0ptHisto->GetYaxis()->SetTitle("Counts/Gev");
    TH1I* e1ptHisto = new TH1I("e1_pt", "e1_pt", 200, 0, 400);
    e1ptHisto->SetDirectory(outfile);
    e1ptHisto->GetXaxis()->SetTitle("p_{T} [GeV]");
    e1ptHisto->GetYaxis()->SetTitle("Counts/Gev");
    // e phi
    TH1I* e0phiHisto = new TH1I("e0_phi", "e0_phi", 60, -3.14, 3.14);
    e0phiHisto->SetDirectory(outfile);
    e0phiHisto->GetXaxis()->SetTitle("p_{T} [GeV]");
    e0phiHisto->GetYaxis()->SetTitle("Counts/Gev");
    TH1I* e1phiHisto = new TH1I("e1_phi", "e1_phi", 60, -3.14, 3.14);
    e1phiHisto->SetDirectory(outfile);
    e1phiHisto->GetXaxis()->SetTitle("p_{T} [GeV]");
    e1phiHisto->GetYaxis()->SetTitle("Counts/Gev");
    // e eta
    TH1I* e0etaHisto = new TH1I("e0_eta", "e0_eta", 50, -5., 5.);
    e0etaHisto->SetDirectory(outfile);
    e0etaHisto->GetXaxis()->SetTitle("p_{T} [GeV]");
    e0etaHisto->GetYaxis()->SetTitle("Counts/Gev");
    TH1I* e1etaHisto = new TH1I("e1_eta", "e1_eta", 50, -5., 5.);
    e1etaHisto->SetDirectory(outfile);
    e1etaHisto->GetXaxis()->SetTitle("p_{T} [GeV]");
    e1etaHisto->GetYaxis()->SetTitle("Counts/Gev");

    // Open file to fit, and make histograms
    TFile ZEffFile(inputFile.c_str(), "READ");
    ZEffTree* ze;
    ze = new ZEffTree(ZEffFile, false);

    bool run = true;
    while (run){
        ze->Entries();
        int EBElectron;
        int EEElectron;
        const double MZ = ze->reco.mz;
        const short PU = ze->reco.nverts;
        /* Assign Electron 0 and 1 */
        if ( inAcceptance(EB, ze->reco.eta[0]) && inAcceptance(EE, ze->reco.eta[0])){
            EBElectron = 0;
            EEElectron = 1;
        } else if ( inAcceptance(EB, ze->reco.eta[1]) && inAcceptance(EE, ze->reco.eta[0])){
            EBElectron = 1;
            EEElectron = 0;
        } else {
            run = ze->GetNextEvent();
            continue;
        }
        /* Cuts */
        // We're going to have a horrible nest of loops, so that we can mimic
        // the cut by cut steps done in Kevin's code, and so when someone
        // (inevitably) says "please add in histograms at each steps" it is
        // literally a drop in fix.
        /* Check minimum pt */
        if ( ze->reco.pt[0] > 20. && ze->reco.pt[1]){
            /* Supercluster */
            if ( ze->reco.isSelected(0, "Supercluster-Eta") && ze->reco.isSelected(1, "Supercluster-Eta") ){
                /* GSF-GSF */
                if ( ze->reco.isSelected(0, "GsfTrack-EtaDet") && ze->reco.isSelected(1, "GsfTrack-EtaDet") ){
                    /* WP80 */
                    if ( ze->reco.isSelected(0, "WP80") && ze->reco.isSelected(1, "WP80") ){
                        if ( 60 <= MZ && MZ <= 120 ){
                            // Z
                            Z0MassHisto->Fill(MZ);
                            Z0MassFineHisto->Fill(MZ);
                            Z0RapidityHisto->Fill(ze->reco.yz);
                            Z0ptHisto->Fill(ze->reco.ptz);
                            // e0
                            e0ptHisto->Fill(ze->reco.pt[0]);
                            e0etaHisto->Fill(ze->reco.eta[0]);
                            e0phiHisto->Fill(ze->reco.phi[0]);
                            // e1
                            e1ptHisto->Fill(ze->reco.pt[1]);
                            e1etaHisto->Fill(ze->reco.eta[1]);
                            e1phiHisto->Fill(ze->reco.phi[1]);
                        }
                    }
                }
            }
        }
        run = ze->GetNextEvent();
    }
    outfile->Write();

    return 0;
}

int main(int argc, char* argv[]){
    const short argcCorrect = 3;
    if (argc < argcCorrect) {
        std::cout<<"Not enough arguments. Use:\nWeightDistribution.exe ZEffFile outputFile\n";
        return 1;
    } else if (argc > argcCorrect){
        std::cout<<"Too many arguments. Use:\nWeightDistribution.exe ZEffFile outFile\n";
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
