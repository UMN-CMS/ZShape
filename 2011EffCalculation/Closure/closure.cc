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
#include <TLorentzVector.h>

// Global because the fit functions can only have two arguments, so we need a
// way to sneak these in.

double deltaR( const double eta0, const double phi0, const double eta1, const double phi1 ){
    const double pi = 3.1415926535;
    const double dEta = eta0 - eta1;
    const double dPhi = fabs(fabs(fabs(phi0 - phi1) - pi) - pi);

    return sqrt(dEta*dEta + dPhi * dPhi);
}

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
    ET,
    EBp,
    EBm,
    EEp,
    EEm,
    NTp,
    NTm,
    HFp,
    HFm
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

double getHFSlope( const double eta ){
    static const int arraySize = 13;
    /* Corrections: 29, 30, ..., 41 for positive and negative ieta */
    static const double starts[arraySize] = {2.853, 2.964, 3.139, 3.314, 3.489, 3.664, 3.839, 4.013, 4.191, 4.363, 4.538, 4.716, 4.889};
    static const double ends[arraySize] = {2.964, 3.139, 3.314, 3.489, 3.664, 3.839, 4.013, 4.191, 4.363, 4.538, 4.716, 4.889, 5.191};

    /* MC */
    //static const double main_cor = 0.0785;
    //static const double ieta_30_cor = 0.1516;
    //static const double ieta_30_cor = 0.13; // This looks like the value actually used in: /home/user1/gude/CMS/src/CMSSW_4_4_2_patch10_kevin_thesis_with_corrections/src/ZShape/MakeSmearedZEffTree/src/MakeSmearedZEffTree.cc
    /* Data */
    static const double main_cor = 0.1902;
    static const double ieta_30_cor = 0.1402;

    static const double pos_correction[arraySize] = {main_cor, ieta_30_cor, main_cor, main_cor, main_cor, main_cor, main_cor, main_cor, main_cor, main_cor, main_cor, main_cor, main_cor};
    static const double neg_correction[arraySize] = {main_cor, ieta_30_cor, main_cor, main_cor, main_cor, main_cor, main_cor, main_cor, main_cor, main_cor, main_cor, main_cor, main_cor};
    const double feta = fabs(eta);
    //Check for outside range
    if (feta < starts[0] || feta > ends[arraySize-1]){
        return 0;
    }

    //Binary search for location
    int lower = 0;
    int upper = arraySize-1;
    int location = (arraySize-1)/2;
    while ( ( upper > lower ) ){
        if ( feta < starts[location] ){
            upper = location;
        } else {
            lower = location;
        }
        if ( feta < ends[location] ){
            upper = location;
        } else {
            lower = location;
        }

        const int step = ( upper - lower )/2;
        location = upper - step;
    }

    //Determine Sign of the tower
    if (eta < 0){
        return neg_correction[location];
    } else {
        return pos_correction[location];
    }
}

effs effFromCounting(TH1F* baseData, TH1F* postData, TH1F* baseBG, TH1F* postBG, const double baseP, const double baseE, const double postP, const double postE, const double minMZ=60., const double maxMZ=120.){
    /*
     * postD = postData count
     * postP = postData param
     * postB = postBackground count
     * postDerr = postData count error
     * postE = postBackground count error
     */
    effs tmp;
    const double baseD = baseData->Integral(baseData->FindBin(minMZ), baseData->FindBin(maxMZ), "width");
    const double postD = postData->Integral(postData->FindBin(minMZ), postData->FindBin(maxMZ), "width");
    const double baseB = baseBG->Integral(baseBG->FindBin(minMZ), baseBG->FindBin(maxMZ));
    const double postB = postBG->Integral(postBG->FindBin(minMZ), postBG->FindBin(maxMZ));
    const double baseDerr = sqrt(baseD);
    const double postDerr = sqrt(postD);

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

effs effFromSignal(TH1F* baseSig, TH1F* postSig, const double baseP, const double baseE, const double postP, const double postE, const double minMZ=60., const double maxMZ=120.){
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
    cout << "#XMin XMax EtaMin  EtaMax  PUMin PUMax NumParms eff      systp    systm    den     phistar" << endl;
    cout << left << setw(6) << xBin.minX;
    cout << left << setw(5) << xBin.maxX ;
    switch (probeLoc){
        case EB:
            cout << left << setw(8) << -1.4442;
            cout << left << setw(8) << 1.4442;
            break;
        case EBp:
            cout << left << setw(8) << 0;
            cout << left << setw(8) << 1.4442;
            break;
        case EBm:
            cout << left << setw(8) << -1.4442;
            cout << left << setw(8) << 0;
            break;
        case EE:
            cout << left << setw(8) << 1.566;
            cout << left << setw(8) << 2.5;
            break;
        case EEp:
            cout << left << setw(8) << 1.566;
            cout << left << setw(8) << 2.5;
            break;
        case EEm:
            cout << left << setw(8) << -2.5;
            cout << left << setw(8) << -1.566;
            break;
        case ET:
            cout << left << setw(8) << -2.5;
            cout << left << setw(8) << 2.5;
            break;
        case NT:
            cout << left << setw(8) << 2.5;
            cout << left << setw(8) << 2.850;
            break;
        case NTp:
            cout << left << setw(8) << 2.5;
            cout << left << setw(8) << 2.850;
            break;
        case NTm:
            cout << left << setw(8) << -2.850;
            cout << left << setw(8) << -2.5;
            break;
        case HF:
            cout << left << setw(8) << 3.1;
            cout << left << setw(8) << 4.6;
            break;
        case HFp:
            cout << left << setw(8) << 3.1;
            cout << left << setw(8) << 4.6;
            break;
        case HFm:
            cout << left << setw(8) << -4.6;
            cout << left << setw(8) << -3.1;
            break;
    }
    cout << left << setw(6) << eventrq.minPU;
    cout << left << setw(6) << eventrq.maxPU;
    cout << left << setw(9) << "5"; // Number of params
    const double diff = fabs(sigeff - counteff)/2.;
    const double avg = fabs(sigeff + counteff)/2.;
    cout << left << setw(9) << avg;
    cout << left << setw(9) << avg+diff;
    cout << left << setw(9) << avg-diff;
    cout << left << setw(8) << denom;
    cout << left << setw(8) << usePhiStar << endl;
}

bool inAcceptance(const electronLocation Loc, const double eta){
    const double feta = fabs(eta);
    bool accepted = false;
    switch (Loc){
        case EB:
            if ( feta < 1.4442 ){
                accepted = true;
            }
            break;
        case EBp:
            if ( 0. < eta && eta < 1.4442 ){
                accepted = true;
            }
        case EBm:
            if ( 0. > eta && eta > -1.4442 ){
                accepted = true;
            }
        case EE:
            if (1.566 < feta && feta < 2.5 ){
                accepted = true;
            }
            break;
        case EEp:
            if (1.566 < eta && eta < 2.5 ){
                accepted = true;
            }
            break;
        case EEm:
            if (-1.566 > eta && eta > -2.5 ){
                accepted = true;
            }
            break;
        case ET:
            if ( (feta < 1.4442) || (1.566 < feta && feta < 2.5) ){
                accepted = true;
            }
            break;
        case NT:
            if (2.5 < feta && feta < 2.850 ){
                accepted = true;
            }
            break;
        case NTp:
            if (2.5 < eta && eta < 2.850 ){
                accepted = true;
            }
            break;
        case NTm:
            if (-2.5 > eta && eta > -2.850 ){
                accepted = true;
            }
            break;
        case HF:
            if (3.1 < feta && feta < 4.6 ){
                accepted = true;
            }
            break;
        case HFp:
            if (3.1 < eta && eta < 4.6 ){
                accepted = true;
            }
            break;
        case HFm:
            if (-3.1 > eta && eta > -4.6 ){
                accepted = true;
            }
            break;
    }

    return accepted;
}

void getBinEdges(std::vector<double> &vec, const double minX, const double maxX, const electronLocation probeLoc){
    const double z_min = 80.;
    const double z_max = 100.;
    double ss_peak;
    double ss_tail;
    switch (probeLoc){
        case EB:
        case EBp:
        case EBm:
            ss_peak = 2;
            ss_tail = 10;
            break;
        case EE:
        case EEp:
        case EEm:
        case ET:
        case NT:
        case NTp:
        case NTm:
        case HF:
        case HFp:
        case HFm:
            ss_peak = 5;
            ss_tail = 20;
            break;
    }

    double cur = minX;
    while (true){
        vec.push_back(cur);
        if (cur >= z_min && cur < z_max){
            cur = cur + ss_peak;
        } else if (cur < z_min || cur >= z_max){
            cur = cur + ss_tail;
        }
        if (cur >= maxX){
            break;
        }
    }
}

int fitDistributions(std::string ZEffFile, std::string outFile, std::string electronWP, electronLocation eLoc, eventRequirements eventrq, bin xBin, bool usePhiStar=false){
    using namespace std;
    // Some commont variables
    //const double tagXCutPt = 20.;
    //const double probeXCutPt = 20.;

    // Prepare the histogram to put the signal in
    //std::vector<double> xbins;
    //getBinEdges(xbins, eventrq.minMZ, eventrq.maxMZ, probeLoc);
    //const int nbins = xbins.size() - 1;
    //if (nbins <= 1){
    //    std::cout << "Signal has too few bins." << std::endl;
    //    return 1;
    //}
    //double* xbins_ar = &xbins[0];
    //GLOBAL.signalHisto = new TH1F("signalHisto", "signal", nbins, xbins_ar);

    // Open signal file and make histograms
    TFile ZSFile(ZEffFile.c_str(), "READ");
    ZEffTree* zes;
    zes = new ZEffTree(ZSFile, false);

    int eDenom = 0;
    int eNum = 0;

    bool run1 = true;
    while (run1){
        zes->Entries();
        const double PU = zes->reco.nverts;
        const double MZ = zes->reco.mz;
        if (  // Right number of PU, MZ
                eventrq.minPU <= PU && PU <= eventrq.maxPU
                && eventrq.minMZ <= MZ && MZ <= eventrq.maxMZ
           ){
            /* Do Delta R matching */
            // Require one electron < 0.1 from reco.
            const double dRlimit = 0.1;
            if (
                    deltaR(zes->reco.eta[0], zes->reco.phi[0], zes->gen.eta[0], zes->gen.phi[0]) > dRlimit
                    && deltaR(zes->reco.eta[1], zes->reco.phi[1], zes->gen.eta[1], zes->gen.phi[1]) > dRlimit
                    && deltaR(zes->reco.eta[1], zes->reco.phi[1], zes->gen.eta[0], zes->gen.phi[0]) > dRlimit
                    && deltaR(zes->reco.eta[0], zes->reco.phi[0], zes->gen.eta[1], zes->gen.phi[1]) > dRlimit
               ){
                run1 = zes->GetNextEvent();
                continue;
            }

            /* Check both electrons */
            for (int i=0; i < 2; ++i){
                double eX0;

                if (usePhiStar){
                    eX0 = zes->reco.phistar;
                } else {
                    eX0 = zes->reco.pt[i];
                }
                if ( // Right value of our cut, and in the acceptance
                        xBin.minX < eX0 && eX0 < xBin.maxX
                        && inAcceptance( eLoc, zes->reco.eta[i])
                    ){
                    ++eDenom;
                    //GLOBAL.signalHisto->Fill(MZ);
                    if ( zes->reco.isSelected(i, electronWP)){
                        ++eNum;
                    }
                }
            }
        }
        run1 = zes->GetNextEvent();
    }

    /* Print Effs */
    const double eff = double(eNum)/double(eDenom);
    printEffs(eLoc, eventrq, xBin, eff, eff, eDenom, usePhiStar);

    delete zes;

    //effs countEff = effFromCounting(baseHisto, postcutHisto, GLOBAL.backgroundHisto, GLOBAL.backgroundHisto, baseFitFunc->GetParameter(0), baseFitFunc->GetParError(0), postFitFunc->GetParameter(0), postFitFunc->GetParError(0));
    //effs sigEff = effFromSignal( GLOBAL.signalHisto, GLOBAL.signalHisto, baseFitFunc->GetParameter(1), baseFitFunc->GetParError(1), postFitFunc->GetParameter(1), postFitFunc->GetParError(1));
    //std::cout << "COUNT EFF: " << countEff.eff << " SIG EFF: " << sigEff.eff << std::endl;

    //canvas->cd(0);

    //const std::string name(outFile.begin(), outFile.end()-5);
    //const std::string pngname = name + std::string(".png");
    //canvas->Print(pngname.c_str(), "png");
    //outfile->Write();

    ////Prints eff stats for text file
    //const double baseD = baseHisto->Integral(baseHisto->FindBin(eventrq.minMZ), baseHisto->FindBin(eventrq.maxMZ), "width");
    //const double baseB = GLOBAL.backgroundHisto->Integral(GLOBAL.backgroundHisto->FindBin(eventrq.minMZ), GLOBAL.backgroundHisto->FindBin(eventrq.maxMZ));

    //const double denom = (baseD - (baseFitFunc->GetParameter(0)*baseB));
    //printEffs(probeLoc, eventrq, xBin, sigEff.eff, countEff.eff, denom, usePhiStar);

    return 0;
}

int main(int argc, char* argv[]){
    const int argcCorrect = 12;
    if (argc < argcCorrect) {
        std::cout<<"Not enough arguments. Use:\nfitEffAcc.exe ZEffFile outFile electronLoc electronWP minPU maxPU minMZ maxMZ minX maxX phistar\n";
        return 1;
    } else if (argc > argcCorrect){
        std::cout<<"Too many arguments. Use:\nfitEffAcc.exe ZEffFile outFile electronLoc electronWP minPU maxPU minMZ maxMZ minX maxX phistar\n";
        return 1;
    } else {
        // Read in arguments
        std::istringstream inStream;

        std::string ZEffFile;
        std::string outFile;

        inStream.str(argv[1]);
        inStream >> ZEffFile;
        inStream.clear();
        inStream.str(argv[2]);
        inStream >> outFile;
        inStream.clear();

        std::string eL;

        inStream.str(argv[3]);
        inStream >> eL;
        inStream.clear();
        std::map<std::string, electronLocation> conv;
        conv["EB"] = EB;
        conv["EBp"] = EBp;
        conv["EBm"] = EBm;
        conv["EE"] = EE;
        conv["EEp"] = EEp;
        conv["EEm"] = EEm;
        conv["NT"] = NT;
        conv["NTp"] = NTp;
        conv["NTm"] = NTm;
        conv["HF"] = HF;
        conv["HFp"] = HFp;
        conv["HFm"] = HFm;
        conv["ET"] = ET;
        electronLocation eLoc = conv[eL];

        std::string electronWP;
        inStream.str(argv[4]);
        inStream >> electronWP;
        inStream.clear();

        eventRequirements eventrq;
        inStream.str(argv[5]);
        inStream >> eventrq.minPU;
        inStream.clear();
        inStream.str(argv[6]);
        inStream >> eventrq.maxPU;
        inStream.clear();
        inStream.str(argv[7]);
        inStream >> eventrq.minMZ;
        inStream.clear();
        inStream.str(argv[8]);
        inStream >> eventrq.maxMZ;
        inStream.clear();

        bin xBin;

        inStream.str(argv[9]);
        inStream >> xBin.minX;
        inStream.clear();
        inStream.str(argv[10]);
        inStream >> xBin.maxX;
        inStream.clear();

        bool usePhiStar;
        inStream.str(argv[11]);
        inStream >> usePhiStar;
        inStream.clear();

        std::cout << "#efficiency name: " << electronWP << std::endl;
        std::cout << "#dimension: 1" << std::endl;

        //std::cout << usePhiStar << std::endl;

        //std::cout << " Tag: " << tagWP << " Probe: " << probeWP << " MinPt: " << xBin.minX << " MaxPt: " << xBin.maxX << " MinPU: " << eventrq.minPU << " MaxPU: " << eventrq.maxPU << std::endl;
        return fitDistributions(
            ZEffFile,
            outFile,
            electronWP,
            eLoc,
            eventrq,
            xBin,
            usePhiStar
        );
    }
}

/* Compile time notes:
 *    g++ -O2 -o closure.exe closure.cc ZEffTree.cc Background.cc `root-config --cflags --libs`
 */
