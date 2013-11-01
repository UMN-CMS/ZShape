#include "Efficiency_Sheet.h"
#include "EfficiencyStatistics.h"

#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <map>
#include <vector>
#include <math.h>
#include <algorithm>

#include "TH1.h"
#include "TH1F.h"
#include "TF1.h"
#include "TFile.h"
#include "TAxis.h"
#include "TLegend.h"
#include "TObject.h"
#include "TCanvas.h"
#include <TROOT.h>
#include <TStyle.h>
#include <TGraphAsymmErrors.h>
#include <TMultiGraph.h>

int makePNGs(const std::vector<TGraphAsymmErrors*> graphs, const std::string outputDir, const std::string canvasName, const bool phistar){
    /* Declaring objects inside the function */
    //TH1F* dummy = new TH1F("dummy_name","Dummy_title", 100, 15., 75. );
    TCanvas* canvas = new TCanvas(canvasName.c_str(), canvasName.c_str(), 1200, 900);
    TMultiGraph* mg = new TMultiGraph("multigraph", canvasName.c_str()); 
    TLegend* leg = new TLegend(0.8,0.8,0.9,0.9);
    leg->SetFillColor(0);

    for(std::vector<TGraphAsymmErrors*>::const_iterator stari = graphs.begin(); stari != graphs.end(); ++stari){
        TGraphAsymmErrors* i = *stari;
        if (stari == graphs.begin()){
            i->SetMarkerStyle(20);
            i->SetMarkerColor(kBlack);
            leg->AddEntry(i, "Data", "p");
        } else {
            i->SetMarkerStyle(21);
            i->SetMarkerColor(kRed);
            leg->AddEntry(i, "MC", "p");
        }

        i->SetTitle(canvasName.c_str());

        mg->Add(i,"P");
    }

    std::string pngName = outputDir + "/" + canvasName + ".png";
    mg->Draw("a"); // mg must be drawn to name axises...
    /* Set up the axis and key */
    if (phistar){
        mg->GetXaxis()->SetTitle("Phistar");
    } else {
        mg->GetXaxis()->SetTitle("p_{T} [GeV/c^{2}]");
    }
    mg->GetYaxis()->SetTitle("Efficiency");
    //mg->SetMinimum(0.01);
    //mg->SetMaximum(1.);
    mg->GetXaxis()->SetLimits(20., 500.);
    mg->Draw("a");
    leg->Draw();
    canvas->SetLogy();
    canvas->Draw();

    canvas->Print(pngName.c_str(), "png");
    delete canvas, mg;

    return 0;
}

int makePlots(const std::string inputFile0, const std::string outputDir, const std::string inputFile1 = std::string("")){ // Only One Input
    const bool verbose = false;
    bool doOverlay = true;
    if (inputFile1.compare("") == 0) { // They are equal
        doOverlay = false;
    }
    if (verbose){ std::cout << "First File: " << inputFile0 << " Second File: " << inputFile1 << std::endl; }

    /* Pretty plots */
    gROOT->SetStyle("Plain");
    gStyle->SetOptFit();
    gStyle->SetOptStat(11111);
    gStyle->SetCanvasBorderMode(0);

    /* Read the data */
    EffSheet* efs0 = new EffSheet(inputFile0);
    EffSheet* efs1;
    if (doOverlay){
        efs1 = new EffSheet(inputFile1);
    }

    /* Loop through bins, then loop through data points and fill our histograms */
    typedef std::vector<EffSheet::EffLine> VEffLine;
    typedef std::map<EffSheet::EffMapKey, std::vector<EffSheet::EffLine>, EffSheet::EffMapKey > MEffValue;
    for(MEffValue::const_iterator i = efs0->values.begin(); i != efs0->values.end(); ++i){
        const double etamin = i->first.etamin;
        const double etamax = i->first.etamax;
        const double pumin = i->first.pumin;
        const double pumax = i->first.pumax;
        const bool phistar = i->first.phistar;

        if (verbose){std::cout << etamin << " " << etamax << " " << pumin << " " << pumax << " " << phistar << std::endl;}

        /* Create vectors of data */
        std::vector<double> binLowEdges;
        std::vector<double> binCenters;
        std::vector<double> pointVal;
        std::vector<double> errorP;
        std::vector<double> errorM;
        std::vector<double> errorYM;
        std::vector<double> errorYP;

        std::vector<TGraphAsymmErrors*> graphs;

        for(VEffLine::const_iterator j = i->second.begin(); j != i->second.end(); ++j){
            if (verbose){
                std::cout << "\tBase Data" << std::endl;
                std::cout << "\t" << j->xmin << std::endl;
                std::cout << "\t" << (j->xmax + j->xmin)/2. << std::endl;
                std::cout << "\t" << j->eff << std::endl;
                std::cout << "\t" << j->systp << std::endl;
                std::cout << "\t" << j->systm << std::endl << std::endl;
            }
            /* Calculate uncertainty */
            EfficiencyStatistics effStat(j->eff, int(j->den));
            const double statErrP = effStat.sigma(1) - j->eff;
            const double statErrM = j->eff - effStat.sigma(-1);

            const double sysErrP = j->systp - j->eff;
            const double sysErrM = j->eff - j->systm;

            const double ErrP = sqrt( statErrP * statErrP + sysErrP * sysErrP);
            const double ErrM = sqrt( statErrM * statErrM + sysErrM * sysErrM);

            //std::cout << "ErrP " << ErrP << " ErrM " << ErrM << std::endl;

            /* Fill vectors for the TGraph */
            const double binCenter = (j->xmax + j->xmin)/2.;
            binLowEdges.push_back(j->xmin);
            binCenters.push_back(binCenter);
            pointVal.push_back(j->eff);
            errorP.push_back(ErrP);
            errorM.push_back(ErrM);
            errorYP.push_back(j->xmax - binCenter);
            errorYM.push_back(binCenter - j->xmin);
        }
        /* Set up data structures for plotting */
        std::ostringstream converter;
        converter << "EtaMin_" << etamin << "_EtaMax_" << etamax;
        converter << "_PUMin_" << pumin << "_PUMax_" << pumax;
        converter << "_PhiStar_" << phistar;
        const std::string canvasName = converter.str();

        const int nbins = binLowEdges.size() - 1; // nbins should be one less than the array size
        double* xbins_ar = &binLowEdges[0];

        TGraphAsymmErrors* baseGraph = new TGraphAsymmErrors(binCenters.size(), &binCenters[0], &pointVal[0], &errorYM[0], &errorYP[0], &errorM[0], &errorP[0]); 
        graphs.push_back(baseGraph);

        if (doOverlay){
            VEffLine secondData= efs1->values[i->first]; // Get the vector that corrisponds to the first set of data
            std::vector<double> binLowEdges1;
            std::vector<double> binCenters1;
            std::vector<double> pointVal1;
            std::vector<double> errorP1;
            std::vector<double> errorM1;
            std::vector<double> errorYM1;
            std::vector<double> errorYP1;
            for(VEffLine::const_iterator j = secondData.begin(); j != secondData.end(); ++j){
                if (verbose){
                    std::cout << "\tOverlay Data" << std::endl;
                    std::cout << "\t" << j->xmin << std::endl;
                    std::cout << "\t" << (j->xmax + j->xmin)/2. << std::endl;
                    std::cout << "\t" << j->eff << std::endl;
                    std::cout << "\t" << j->systp << std::endl;
                    std::cout << "\t" << j->systm << std::endl << std::endl;
                }
                /* Calculate uncertainty */
                EfficiencyStatistics effStat(j->eff, int(j->den));
                const double statErrP = effStat.sigma(1) - j->eff;
                const double statErrM = j->eff - effStat.sigma(-1);

                const double sysErrP = j->systp - j->eff;
                const double sysErrM = j->eff - j->systm;

                const double ErrP = sqrt( statErrP * statErrP + sysErrP * sysErrP);
                const double ErrM = sqrt( statErrM * statErrM + sysErrM * sysErrM);

                //std::cout << "ErrP " << ErrP << " ErrM " << ErrM << std::endl;

                /* Fill vectors for the TGraph */
                const double binCenter1 = (j->xmax + j->xmin)/2.;
                binLowEdges1.push_back(j->xmin);
                binCenters1.push_back(binCenter1);
                pointVal1.push_back(j->eff);
                errorP1.push_back(ErrP);
                errorM1.push_back(ErrM);
                errorYP1.push_back(j->xmax - binCenter1);
                errorYM1.push_back(binCenter1 - j->xmin);
            }
            TGraphAsymmErrors* baseGraph1 = new TGraphAsymmErrors(binCenters1.size(), &binCenters1[0], &pointVal1[0], &errorYM1[0], &errorYP1[0], &errorM1[0], &errorP1[0]); 
            graphs.push_back(baseGraph1);
        }

        // Need to update
        makePNGs(graphs, outputDir, canvasName, phistar);

    }
    return 0;
}

int main(int argc, char* argv[]){
    const int argcLow = 2;
    const int argcHigh = 5;
    if (argc <= argcLow) {
        std::cout<<"Not enough arguments. Use:\n inputFile outputDir\n";
        return 1;
    } else if (argc >= argcHigh){
        std::cout<<"Too many arguments. Use:\n inputFile outputDir\n";
        return 1;
    } else if (argc == 3){
        /* Set up stringstream to read in arguments */
        std::istringstream inStream;

        std::string inputFile;
        std::string outputDir;

        /* Parse arguments */
        inStream.str(argv[1]);
        inStream >> inputFile;
        inStream.clear();
        inStream.str(argv[2]);
        inStream >> outputDir;
        inStream.clear();

        return makePlots(inputFile, outputDir);
    } else {
        /* Set up stringstream to read in arguments */
        std::istringstream inStream;

        std::string inputFile0;
        std::string inputFile1;
        std::string outputDir;

        /* Parse arguments */
        inStream.str(argv[1]);
        inStream >> inputFile0;
        inStream.clear();
        inStream.str(argv[2]);
        inStream >> outputDir;
        inStream.clear();
        inStream.str(argv[3]);
        inStream >> inputFile1;
        inStream.clear();

        std::cout << inputFile0 << " " << outputDir << " " << inputFile1 << std::endl;

        return makePlots(inputFile0, outputDir, inputFile1);
    }
}

/* Compile time notes:
 *    g++ -O2 -o Efficiency_Plotter.exe Efficiency_Plotter.cc EfficiencyStatistics.cc `root-config --cflags --libs` 
 */
