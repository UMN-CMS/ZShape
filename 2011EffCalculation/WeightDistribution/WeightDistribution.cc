#include "../../MakeZEffTree/src/ZEffTree.h"
#include "../EfficiencyTable/EfficiencyTable.h"
#include "../ElectronLocation/ElectronLocation.h"

#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <math.h>

#include "TH1.h"
#include "TF1.h"
#include "TFile.h"
#include "TAxis.h"
#include "TObject.h"
//#include "TCanvas.h"
#include <TROOT.h>

int makeWeights(std::string ZEffFile, std::string EfficiencyTableFile, std::string outFile){
    // Root style
    gROOT->SetStyle("Plain");

    // Prepare output
    TFile* outfile;
    outfile = new TFile(outFile.c_str(),"RECREATE");

    /* Prepare the histogram to put the data in */
    const int nbins = 105;
    const double lowedge = -0.05;
    const double highedge = 1.05;

    TH1D* EBHisto = new TH1D("EBHisto", "EB", nbins, lowedge, highedge);
    TH1D* EEHisto = new TH1D("EEHisto", "EE", nbins, lowedge, highedge);
    // Associate TH1Ds with rootfile
    EBHisto->SetDirectory(outfile);
    EEHisto->SetDirectory(outfile);
    // XAxis
    EBHisto->GetXaxis()->SetTitle("Efficiency");
    EEHisto->GetXaxis()->SetTitle("Efficiency");
    // YAxis
    EBHisto->GetYaxis()->SetTitle("Count");
    EEHisto->GetYaxis()->SetTitle("Count");
    //gStyle->SetOptFit();
    //gStyle->SetOptStat(11111);
    //gStyle->SetCanvasBorderMode(0);

    // Get our efficiency and set variables
    EfficiencyTable es(EfficiencyTableFile);
    //es.print();

    // Open file to fit, and make histograms
    TFile ZFile(ZEffFile.c_str(), "READ");
    ZEffTree* ze;
    ze = new ZEffTree(ZFile, false);

    // Loop over events to create the distributions to fit
    bool run = true;
    while (run){
        ze->Entries();
        int tagNumber;
        int probeNumber;
        bool isHighPU;
        const electronLocation tagLoc = EB;
        const electronLocation probeLoc = EE;
        const double MZ = ze->reco.mz;
        const short PU = ze->reco.nverts;
        /* Check minimum pt and MZ*/
        if ( ze->reco.pt[0] > 20. && ze->reco.pt[1] > 20. && 40. < MZ && MZ < 150 && PU >= 0){
            /* Select a  tag and probe */
            if ( inAcceptance(tagLoc, ze->reco.eta[0]) && inAcceptance(probeLoc, ze->reco.eta[1])) {
                tagNumber = 0;
                probeNumber = 1;
            } else if ( inAcceptance(tagLoc, ze->reco.eta[1]) && inAcceptance(probeLoc, ze->reco.eta[0])) {
                tagNumber = 1;
                probeNumber = 0;
            } else { // Event is not of interest
                run = ze->GetNextEvent();
                continue;
            }

            const double tagPT = ze->reco.pt[tagNumber];
            const double probePT = ze->reco.pt[probeNumber];
            /* Check that the event passes our requirements */
            if (    ze->reco.isSelected(tagNumber, "HLT-GSF") // Tag is HLT-GSF
                    //&& ze->reco.isSelected(tagNumber, "WP80") // Tag is WP80
                    //&& ze->reco.isSelected(probeNumber, "Supercluster-Eta")
                    && ze->reco.isSelected(probeNumber, "GsfTrack-EtaDet")
               ){
                // EE is split in two, and each side has a measured Eff
                if ( inAcceptance(EEp, ze->reco.eta[probeNumber]) ){
                    const double probeEff = es.getEff(probePT, EEp, PU);
                    EEHisto->Fill(probeEff);
                } else if ( inAcceptance(EEm, ze->reco.eta[probeNumber]) ){
                    const double probeEff = es.getEff(probePT, EEm, PU);
                    EEHisto->Fill(probeEff);
                }
                const double tagEff = es.getEff(tagPT, tagLoc, PU);
                EBHisto->Fill(tagEff);
            }
        }
        run = ze->GetNextEvent();
    }

    delete ze;

    /* Save File */
    //const std::string name(outFile.begin(), outFile.end()-5);
    //const std::string pngname = name + std::string(".png");
    //canvas->Print(pngname.c_str(), "png");
    outfile->Write();

    return 0;
}

int main(int argc, char* argv[]){
    const short argcCorrect = 4;
    if (argc < argcCorrect) {
        std::cout<<"Not enough arguments. Use:\nWeightDistribution.exe ZEffFile EfficiencyTableFile outFile\n";
        return 1;
    } else if (argc > argcCorrect){
        std::cout<<"Too many arguments. Use:\nWeightDistribution.exe ZEffFile EfficiencyTableFile outFile\n";
        return 1;
    } else {
        // Read in arguments
        std::istringstream inStream;

        std::string ZEffFile;
        inStream.str(argv[1]);
        inStream >> ZEffFile;
        inStream.clear();

        std::string EfficiencyTableFile;
        inStream.str(argv[2]);
        inStream >> EfficiencyTableFile;
        inStream.clear();

        std::string outFile;
        inStream.str(argv[3]);
        inStream >> outFile;
        inStream.clear();

        return makeWeights(ZEffFile, EfficiencyTableFile, outFile);
    }
}
