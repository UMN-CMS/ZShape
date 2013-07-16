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
                            Z0MassHisto->Fill(MZ);
                            Z0MassFineHisto->Fill(MZ);
                            Z0RapidityHisto->Fill(ze->reco.yz);
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
