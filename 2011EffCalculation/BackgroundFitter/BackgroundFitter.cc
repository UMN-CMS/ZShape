#include "../../MakeZEffTree/src/ZEffTree.h"

#include <TFile.h>
#include <TH1F.h>
#include <TF1.h>
#include <TMath.h>
#include <TCanvas.h>

#include <iostream>
#include <string>

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

int fitBackground(TFile *file, const std::string &outname, const std::string &tagWP, const std::string &probeWP, const tagCuts &cuts, const binningDef &binDef, bool usePhiStar=false) {
    /* Open the EffTree */
    ZEffTree *ze;
    ze = new ZEffTree(*file,false);

    /* Create root objects: Files, Histograms */
    TFile *outfile;
    outfile = new TFile(outname.c_str(),"recreate");
    TCanvas *canvas = new TCanvas;
    TH1F *histoToFit;

    const int nBins = cuts.maxMZ - cuts.minMZ;
    histoToFit = new TH1F("histoToFit", "Z Mass", nBins, cuts.minMZ, cuts.maxMZ);

    bool run = true;
    while (run){
        ze->Entries();
        if ( 
                binDef.minPU <= ze->reco.nverts && ze->reco.nverts <= binDef.maxPU // Must be in the pile up binning window
                && cuts.minMZ <= ze->reco.mz && ze->reco.mz <= cuts.maxMZ          // Must be near Z peak in all cases
                && ze->reco.isSelected(0,tagWP)                                    // Tag must pass a cut
                && !ze->reco.isSelected(1,probeWP)                                 // Probe must fail a cut
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
                    && fabs(ze->reco.eta[1] >= 3.0) // In HF
                    //&& fabs(ze->reco.eta[1]) <= 2.5 
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

    /* If bins have 0s, we need to rebin */
    /*
     *int primes[6] = {2,3,5,7,11,13};
     *int startNBins = histoToFit->GetNbinsX();
     *bool rebin = true;
     *while (rebin){
     *    int binCount = histoToFit->GetNbinsX();
     *    // Check if we have too few bins left
     *    if (binCount <= startNBins / 8){
     *        rebin = false;
     *        break;
     *    } 
     *    // Check for 0 bins
     *    bool has_zero = false;
     *    for(int i=1; i<binCount; ++i){
     *        if (histoToFit->GetBinContent(i) <= 0){ 
     *            has_zero = true;
     *            break;
     *        }
     *    }
     * 
     *    // If 0s, rebin
     *    if (has_zero){
     *        for (int j=0; j<=5; ++j){
     *            // Unfortunately, rebin wants an even divisor, so we check the
     *            // first few primes, which should be good enough for us.
     *            int div = primes[j]; 
     *            if (binCount % div == 0){
     *                histoToFit->Rebin(div);
     *            }
     *        }
     *    } else {
     *        rebin = false;
     *        break;
     *    }
     *} // while
     */

    /* Run fit */
    background->SetParameter(0, 50.);
    background->SetParLimits(0, 40., 60.);
    background->SetParameter(1, 10.);
    background->SetParLimits(1, 0.1, 100.);
    background->SetParameter(2, 0.1);
    background->SetParLimits(2, 0.0001, 10.);
    background->SetParameter(3, 3.);
    background->SetParLimits(3, 1., 25.);
    histoToFit->Fit("background","QMR");

    /* Output to stdout the parameters in order */
    std::cout << "\t" << binDef.minX << "\t" << binDef.maxX << "\t" << binDef.minPU << "\t" << binDef.maxPU << "\t" << cuts.minMZ << "\t" << cuts.maxMZ;
    std::cout << "\t" << paranum << "\t" << background->GetParameter(0) << "\t" << background->GetParameter(1) << "\t" << background->GetParameter(2);
    std::cout << "\t" << background->GetParameter(3) << "\t" << usePhiStar << std::endl;

    /* Set range and draw histogram */
    histoToFit->SetMaximum(300);
    histoToFit->SetMinimum(0);
    histoToFit->Draw();

    /* Save png */
    std::string name(outname.begin(), outname.end()-5);
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
        std::cout<<"Not enough arguments. Use:\neffFit.exe inFile outFile tagWP probeWP minX maxX minPU maxPU minMZ maxMZ [usePhiStar]\n";
        return 1;
    } else if (argc > argnum){
        std::cout<<"Too many arguments. Use:\neffFit.exe inFile outFile tagWP probeWP minX maxX minPU maxPU minMZ maxMZ [usePhiStar]\n";
        return 1;
    } else {
        TFile inFile(argv[1],"READ");
        tagCuts cuts;
        binningDef binDef;
        binDef.minX = atof(argv[5]);
        binDef.maxX = atof(argv[6]);
        binDef.minPU = atoi(argv[7]);
        binDef.maxPU = atoi(argv[8]);
        cuts.minMZ = atoi(argv[9]);
        cuts.maxMZ = atoi(argv[10]);
        bool usePhiStar = atoi(argv[11]);

        fitBackground(&inFile, argv[2], argv[3], argv[4], cuts, binDef, usePhiStar);
    }

    return 0;
}
