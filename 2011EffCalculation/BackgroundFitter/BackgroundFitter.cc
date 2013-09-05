#include "../../MakeZEffTree/src/ZEffTree.h"
#include "../ElectronLocation/ElectronLocation.h"  // inAcceptance

#include <TFile.h>
#include <TH1F.h>
#include <TF1.h>
#include <TMath.h>
#include <TCanvas.h>
#include <TROOT.h>  // Pulls in gROOT
#include <TStyle.h>  // Pulls in gStyle

#include <iostream>
#include <string>
#include <sstream>

struct tagCuts{
    int minMZ;
    int maxMZ;
};

struct binningDef{
    double minX;
    double maxX;
    int minPU;
    int maxPU;
};

double backgroundFunction(const double *v, const double *par){
    return TMath::Erfc((par[0]-v[0])/par[3])*par[1]*TMath::Exp(-par[2]*v[0]);
}

int fitBackground(const std::string &inFileName, const std::string &outFileName, const std::string &tagWP, const std::string &probeWP, const tagCuts &cuts, const binningDef &binDef, const bool usePhiStar=false) {
    // Root style
    gROOT->SetStyle("Plain");
    gStyle->SetOptTitle(0);  // Remove title
    gStyle->SetOptStat(0);  // Remove Stats Box
    gStyle->SetHistLineWidth(2);  // Remove Stats Box

    /* Open the EffTree */
    TFile ZSFile(inFileName.c_str(), "READ");
    ZEffTree *ze;
    ze = new ZEffTree(ZSFile, false);

    /* Create root objects: Files, Histograms */
    TFile *outfile;
    outfile = new TFile(outFileName.c_str(), "recreate");
    TCanvas *canvas = new TCanvas("bg", "bg", 1200, 900);

    /* Setup Histogram of background */
    const int nBins = cuts.maxMZ - cuts.minMZ;
    TH1F *histoToFit;
    histoToFit = new TH1F("histoToFit", "Z Mass", nBins, cuts.minMZ, cuts.maxMZ);
    histoToFit->SetMarkerStyle(20);  // Use Circles for points

    bool run = true;
    while (run){
        ze->Entries();
        if (
                binDef.minPU <= ze->reco.nverts && ze->reco.nverts <= binDef.maxPU // Must be in the pile up binning window
                && cuts.minMZ <= ze->reco.mz && ze->reco.mz <= cuts.maxMZ          // Must be near Z peak in all cases
                && ze->reco.isSelected(0, tagWP)                                    // Tag must pass a cut
                && !ze->reco.isSelected(1, probeWP)                                 // Probe must fail a cut
           ){
            /* Use Phistar or Pt */
            double eX;
            if (usePhiStar){
                eX = ze->reco.phistar;
            } else {
                eX = ze->reco.pt[1];
            }

            if (
                    binDef.minX <= eX && eX <= binDef.maxX // Must be in Pt binning window
                    && inAcceptance(HF, ze->reco.eta[1])
               ){
                histoToFit->Fill(ze->reco.mz);
            }
        }
        run = ze->GetNextEvent();
    }

    /* Fit our histogram */
    // TF1 *func = new TF1("bg",bgFunc,50,160,3)
    const int paranum = 4;
    TF1 *background = new TF1("background", backgroundFunction, cuts.minMZ, cuts.maxMZ, paranum);
    background->SetParName(0,"alpha");
    background->SetParName(1,"beta");
    background->SetParName(2,"gamma");
    background->SetParName(3,"delta");

    /* Set error near the peak to be very large so that it is ignored by the fit */
    for(int i = 0; i <= nBins+1; i++) {
        const int mass = cuts.minMZ + i;
        if ( 80 <= mass && mass <= 100){ // Around Z Peak
            histoToFit->SetBinError(i,100);
        }
    }

    /* Run fit */
    background->SetParameter(0, 60.);
    background->SetParLimits(0, 40., 120.);
    background->SetParameter(1, 100.);
    background->SetParLimits(1, 0.1, 1000.);
    background->SetParameter(2, 0.1);
    background->SetParLimits(2, 0.0001, 1.);
    background->SetParameter(3, 10.);
    background->SetParLimits(3, 1., 40.);
    histoToFit->Fit("background","QMRWL");

    /* Run Refit */
    //background->SetParameter(0, background->GetParameter(0));
    //background->SetParameter(1, background->GetParameter(1));
    //background->SetParameter(2, background->GetParameter(2));
    //background->SetParameter(3, background->GetParameter(3));
    //histoToFit->Fit("background","QMRWL");

    /* Output to stdout the parameters in order */
    std::cout << "\t" << binDef.minX << "\t" << binDef.maxX << "\t" << binDef.minPU << "\t" << binDef.maxPU << "\t" << cuts.minMZ << "\t" << cuts.maxMZ;
    std::cout << "\t" << paranum << "\t" << background->GetParameter(0) << "\t" << background->GetParameter(1) << "\t" << background->GetParameter(2);
    std::cout << "\t" << background->GetParameter(3) << "\t" << usePhiStar << std::endl;

    /* Set range and draw histogram */
    histoToFit->SetMaximum(300);
    histoToFit->SetMinimum(0);
    histoToFit->Draw();

    /* Save png */
    std::string name(outFileName.begin(), outFileName.end()-5);
    std::string pngname = name + std::string(".png");
    canvas->Print(pngname.c_str(),"png");

    /* Save histogram */
    outfile->Write();
    delete ze;
    delete outfile;

    return 0;
}

int main(int argc, char* argv[]){
    const int argnum = 12;
    if (argc < (argnum -1) ) {
        std::cout<<"Not enough arguments. Use:\neffFit.exe inFile outFile tagWP probeWP minX maxX minPU maxPU minMZ maxMZ usePhiStar\n";
        return 1;
    } else if (argc > argnum){
        std::cout<<"Too many arguments. Use:\neffFit.exe inFile outFile tagWP probeWP minX maxX minPU maxPU minMZ maxMZ usePhiStar\n";
        return 1;
    } else {
        std::istringstream inStream;

        // Input File
        std::string inFileName;
        inStream.str(argv[1]);
        inStream >> inFileName;
        inStream.clear();

        // Output File
        std::string outFileName;
        inStream.str(argv[2]);
        inStream >> outFileName;
        inStream.clear();

        // Working Points
        std::string tagWP;
        inStream.str(argv[3]);
        inStream >> tagWP;
        inStream.clear();

        std::string probeWP;
        inStream.str(argv[4]);
        inStream >> probeWP;
        inStream.clear();

        // Kinematic Binning
        binningDef binDef;

        inStream.str(argv[5]);
        inStream >> binDef.minX;
        inStream.clear();

        inStream.str(argv[6]);
        inStream >> binDef.maxX;
        inStream.clear();

        inStream.str(argv[7]);
        inStream >> binDef.minPU;
        inStream.clear();

        inStream.str(argv[8]);
        inStream >> binDef.maxPU;
        inStream.clear();

        // Cuts
        tagCuts cuts;

        inStream.str(argv[9]);
        inStream >> cuts.minMZ;
        inStream.clear();

        inStream.str(argv[10]);
        inStream >> cuts.maxMZ;
        inStream.clear();

        // Use Phistar
        bool usePhiStar;
        inStream.str(argv[11]);
        inStream >> usePhiStar;
        inStream.clear();

        fitBackground(inFileName, outFileName, tagWP, probeWP, cuts, binDef, usePhiStar);
    }

    return 0;
}
