#include "../BackgroundLibrary/BackgroundTable.h"
#include "../BackgroundLibrary/BackgroundFunctions.h"
#include "../ElectronLocation/ElectronLocation.h"
#include "../../MakeZEffTree/src/ZEffTree.h"

#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <map>
#include <vector>

#include <TH1.h>
#include <TF1.h>
#include <TFile.h>
#include <TAxis.h>
#include <TObject.h>
#include <TCanvas.h>
#include <TROOT.h>
#include <TStyle.h>
#include <TRandom3.h>
#include <TLorentzVector.h>

// Global because the fit functions can only have two arguments, so we need a
// way to sneak these in.

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
            ss_tail = 2;
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
            ss_peak = 2;
            ss_tail = 2;
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

effs effFromCounting(TH1D* baseData, TH1D* postData, TH1D* baseBG, TH1D* postBG, const double baseP, const double baseE, const double postP, const double postE, const double minMZ=60., const double maxMZ=120.){
    /*
     * postD = postData count
     * postP = postData param
     * postB = postBackground count
     * postDerr = postData count error
     * postE = postBackground count error
     */
    effs tmp;
    const double baseD = baseData->Integral(baseData->FindBin(minMZ), baseData->FindBin(maxMZ));
    const double postD = postData->Integral(postData->FindBin(minMZ), postData->FindBin(maxMZ));
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

effs effFromSignal(TH1D* baseSig, TH1D* postSig, const double baseP, const double baseE, const double postP, const double postE, const double minMZ=60., const double maxMZ=120.){
    effs tmp;
    double baseS = baseSig->Integral(baseSig->FindBin(minMZ), baseSig->FindBin(maxMZ));
    double postS = postSig->Integral(postSig->FindBin(minMZ), postSig->FindBin(maxMZ));

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
    stringstream ss;
    ss << "#XMin XMax EtaMin  EtaMax  PUMin PUMax NumParms eff       systp     systm     den     phistar" << endl;
    ss << left << setw(6) << xBin.minX;
    ss << left << setw(5) << xBin.maxX ;
    switch (probeLoc){
        case EB:
            ss << left << setw(8) << -1.4442;
            ss << left << setw(8) << 1.4442;
            break;
        case EBp:
            ss << left << setw(8) << 0;
            ss << left << setw(8) << 1.4442;
            break;
        case EBm:
            ss << left << setw(8) << -1.4442;
            ss << left << setw(8) << 0;
            break;
        case EE:
            ss << left << setw(8) << 1.566;
            ss << left << setw(8) << 2.5;
            break;
        case EEp:
            ss << left << setw(8) << 1.566;
            ss << left << setw(8) << 2.5;
            break;
        case EEm:
            ss << left << setw(8) << -2.5;
            ss << left << setw(8) << -1.566;
            break;
        case ET:
            ss << left << setw(8) << -2.5;
            ss << left << setw(8) << 2.5;
            break;
        case NT:
            ss << left << setw(8) << 2.5;
            ss << left << setw(8) << 2.850;
            break;
        case NTp:
            ss << left << setw(8) << 2.5;
            ss << left << setw(8) << 2.850;
            break;
        case NTm:
            ss << left << setw(8) << -2.850;
            ss << left << setw(8) << -2.5;
            break;
        case HF:
            ss << left << setw(8) << 3.1;
            ss << left << setw(8) << 4.6;
            break;
        case HFp:
            ss << left << setw(8) << 3.1;
            ss << left << setw(8) << 4.6;
            break;
        case HFm:
            ss << left << setw(8) << -4.6;
            ss << left << setw(8) << -3.1;
            break;
    }
    ss << left << setw(6) << eventrq.minPU;
    ss << left << setw(6) << eventrq.maxPU + 1; // Kevin's Code requires 0-4 inclusive to report 0-5
    ss << left << setw(9) << "5"; // Number of params
    const double diff = fabs(sigeff - counteff)/2.;
    const double avg = fabs(sigeff + counteff)/2.;
    ss << left << setw(10) << avg;
    ss << left << setw(10) << avg+diff;
    ss << left << setw(10) << avg-diff;
    ss << left << setw(8) << denom;
    ss << left << setw(8) << usePhiStar << endl;
    // Output the String Stream
    cout << ss.str() << flush;
}

int fitDistributions(const std::string bgfitfile, const std::string signalFile, const std::string ZEffFile, const std::string outFile, const std::string tagWP, const std::string probeWP, const electronLocation tagLoc, const electronLocation probeLoc, const eventRequirements eventrq, const bin xBin, const bool usePhiStar=false){
    // Some commont variables
    const double tagXCutPt = 20.;
    const double probeXCutPt = 20.;
    // Smearing
    const bool smear = false;
    const int randSeed = 123456; //using constant seed for reproducibility
    TRandom3* trand = new TRandom3(randSeed);

    // Prepare the histogram to put the signal in
    std::vector<double> xbins;
    getBinEdges(xbins, eventrq.minMZ, eventrq.maxMZ, probeLoc);
    const int nbins = xbins.size() - 1;
    if (nbins <= 1){
        std::stringstream ss;
        ss << "Signal has too few bins." << std::endl;
        std::cout << ss.str() << std::flush;
        return 1;
    }
    double* xbins_ar = &xbins[0];
    TH1D* signalHisto = new TH1D("signalHisto", "signal", nbins, xbins_ar);

    // Get our background
    bg::BackgroundTable brg(bgfitfile);
    const double midX = (xBin.maxX + xBin.minX)/2.;
    const double midPU = (eventrq.maxPU + eventrq.minPU)/2.;
    brg.setBackground(midX, midPU, usePhiStar); // TODO: Fill in pt, pu
    if (brg.current == 0){
        std::stringstream ss;
         ss << "Failed to get background model for point: midX " << midX << " midPU " << midPU << " usePhiStar " << usePhiStar << std::endl;
         std::cout << ss.str() << std::flush;
        // No background for your area.
        return 1;
    }

    // Open signal file and make histograms
    TFile ZSFile(signalFile.c_str(), "READ");
    ZEffTree* zes;
    zes = new ZEffTree(ZSFile, false);

    bool run1 = true;
    while (run1){
        zes->Entries();
        const double PU = zes->reco.nverts;
        const double MZ = zes->reco.mz;
        if (  // Right number of PU, MZ
                eventrq.minPU <= PU && PU <= eventrq.maxPU
                && eventrq.minMZ <= MZ && MZ <= eventrq.maxMZ
                && 20. <= zes->reco.pt[0] && 20. <= zes->reco.pt[1]
           ){
            /* We set try either electron as the "probe", since this is MC either can be the "tag" */
            double tagX;
            double probeX;

            for (int i=0; i < 2; ++i){
                bool probeMatch = false;
                bool tagMatch = false;
                // Note that j is the PROBE and i is the TAG
                int j;
                if (i==0){
                    j=1;
                } else {
                    j=0;
                }
                double eX0;
                double eX1;
                if (usePhiStar){
                    eX0 = zes->reco.phistar;
                    tagX = -1;
                    eX1 = zes->reco.phistar;
                    probeX = -1;
                } else {
                    eX0 = zes->reco.pt[i];
                    tagX = tagXCutPt;
                    eX1 = zes->reco.pt[j];
                    probeX = probeXCutPt;
                }
                // Now we make sure exactly one e passes the tag region, and one the probe region requirements
                if ( xBin.minX <= eX1 && eX1 <= xBin.maxX && probeX <= eX1){
                    probeMatch = inAcceptance(probeLoc, zes->reco.eta[j]);
                }
                if ( probeMatch && tagX <= eX0 ){
                    tagMatch = inAcceptance(tagLoc, zes->reco.eta[i]);
                }
                // Base Cuts, and Post Cuts which are a strict subset
                if ( tagMatch && probeMatch ){
                    signalHisto->Fill(MZ);
                    break;
                }
            }
        }
        run1 = zes->GetNextEvent();
    }

    delete zes;

    // Set up background fitter object
    bg::BinnedBackgroundAndSignal bgfitfunc(brg, signalHisto);

    // Prepare output
    TFile* outfile;
    outfile = new TFile(outFile.c_str(),"RECREATE");
    gROOT->SetStyle("Plain");
    gStyle->SetOptFit();
    gStyle->SetOptStat(1000011);
    gStyle->SetCanvasBorderMode(0);
    TCanvas *canvas = new TCanvas("canvas", "canvas", 1280, 640);
    canvas->Divide(2);

    canvas->cd(1);
    gPad->SetLogy();
    TH1D *baseHisto = new TH1D("baseHisto", "baseHisto", nbins, xbins_ar);
    baseHisto->SetMarkerStyle(20);
    baseHisto->GetXaxis()->SetTitle("M_{ee} [GeV/c^{2}]");
    baseHisto->GetYaxis()->SetTitle("Count/GeV");

    canvas->cd(2);
    gPad->SetLogy();
    TH1D *postcutHisto = new TH1D("postcutHisto", "postcutHisto", nbins, xbins_ar);
    postcutHisto->SetMarkerStyle(20);
    postcutHisto->GetXaxis()->SetTitle("M_{ee} [GeV/c^{2}]");
    postcutHisto->GetYaxis()->SetTitle("Count/GeV");

    baseHisto->SetDirectory(outfile);
    postcutHisto->SetDirectory(outfile);

    // Open file to fit, and make histograms
    TFile ZFile(ZEffFile.c_str(), "READ");
    ZEffTree* ze;
    ze = new ZEffTree(ZFile, false);

    // Loop over events to create the distributions to fit
    bool run2 = true;
    bool flop = true;

    while (run2){
        /* Select a reproducably random tag and probe */
        int tagNumber;
        int probeNumber;
        if ( !inAcceptance(HF, ze->reco.eta[1])){ // EB HF case, no flop needed
            if (flop) {
                tagNumber = 0;
                probeNumber = 1;
                flop = false;
            } else {
                tagNumber = 1;
                probeNumber = 0;
                flop = true;
            }
        } else {
            tagNumber = 0;
            probeNumber = 1;
        }

        ze->Entries();
        const double PU = ze->reco.nverts;
        /** Adjust Pt via smearing and HF correction **/
        double pt0 = -1.;
        double pt1 = -1.;
        /* Correct HF pt */
        if (3.1 < fabs(ze->reco.eta[tagNumber]) && fabs(ze->reco.eta[tagNumber]) < 4.6){
            pt0 = ze->reco.pt[tagNumber] - PU * getHFSlope(ze->reco.eta[tagNumber]);
        } else {
            pt0 = ze->reco.pt[tagNumber];
        }
        if (3.1 < fabs(ze->reco.eta[probeNumber]) && fabs(ze->reco.eta[probeNumber]) < 4.6){
            pt1 = ze->reco.pt[probeNumber] - PU * getHFSlope(ze->reco.eta[probeNumber]);
        } else {
            pt1 = ze->reco.pt[probeNumber];
        }
        /* Smear Pt */
        if (smear && !usePhiStar){
            if (inAcceptance(EB, ze->reco.eta[0])){
                const double mean = 0.995;
                const double sigma = 0.007;
                pt0 *= ( trand->Gaus(mean,sigma) );
            } else if (inAcceptance(EB, ze->reco.eta[0])){
                const double mean = 0.976;
                const double sigma = 0.013;
                pt0 *= ( trand->Gaus(mean,sigma) );
            }
        }
        /* Recalculate MZ */
        TLorentzVector e0lv;
        TLorentzVector e1lv;
        TLorentzVector Zlv;
        e0lv.SetPtEtaPhiM(pt0, ze->reco.eta[tagNumber], ze->reco.phi[tagNumber], 5.109989e-4);
        e1lv.SetPtEtaPhiM(pt1, ze->reco.eta[probeNumber], ze->reco.phi[probeNumber], 5.109989e-4);
        Zlv = e0lv + e1lv;
        const double MZ = Zlv.M(); // Get the invarient mass from the Z

        /* Check that the event passes our requirements */
        if ( eventrq.minPU <= PU && PU <= eventrq.maxPU && eventrq.minMZ <= MZ && MZ <= eventrq.maxMZ ){
            bool basePass = false;
            bool postPass = false;
            double eX0;
            double eXCut0;
            double eX1;
            double eXCut1;
            if (usePhiStar){
                eX0 = ze->reco.phistar;
                eXCut0 = -1;
                eX1 = ze->reco.phistar;
                eXCut1 = -1;
            } else {
                eX0 = pt0;
                eX1 = pt1;
                eXCut0 = tagXCutPt;
                eXCut1 = probeXCutPt;
            }
            /* Check cuts */
            if (    eXCut0 <= eX0 && eXCut1 <= eX1  // Both Es pass min pt/phistar
                    && xBin.minX <= eX1 && eX1 <= xBin.maxX // Probe in pt bin
               ){
                /* Check the acceptance of the electrons */
                const bool tagPass = inAcceptance(tagLoc, ze->reco.eta[tagNumber]);
                const bool probePass = inAcceptance(probeLoc, ze->reco.eta[probeNumber]);

                if (tagPass && probePass){
                    switch (probeLoc){
                        case EB:
                        case EBp:
                        case EBm:
                        case EE:
                        case EEp:
                        case EEm:
                        case ET:
                            if (ze->reco.isSelected(probeNumber,"Supercluster-Eta") && ze->reco.isSelected(probeNumber,"GsfTrack-EtaDet")){
                                basePass = true;
                            }
                            break;
                        case NT:
                        case NTp:
                        case NTm:
                            // We only check acceptance, and it has already passed
                            basePass = true;
                            break;
                        case HF:
                        case HFp:
                        case HFm:
                            // We only check acceptance, and it has already passed
                            basePass = true;
                            break;
                    }
                }
            }
            // In numerator?
            if (ze->reco.isSelected(probeNumber,probeWP)){
                postPass = true;
            }
            // Base Cuts, and Post Cuts which are a strict subset
            if ( basePass ){
                baseHisto->Fill(MZ);
                if ( postPass ){ // Tag passed all cuts
                    postcutHisto->Fill(MZ);
                    //std::cout << MZ << std::endl;
                }
            }
        }
        run2 = ze->GetNextEvent();
    }

    delete ze;

    // Perform fit
    canvas->cd(1);
    TF1* baseFitFunc = new TF1("baseFitFunc", bgfitfunc, eventrq.minMZ, eventrq.maxMZ, 2);
    baseFitFunc->SetLineWidth(1);
    baseFitFunc->SetParLimits(0, 0.0001, 100000.);
    baseFitFunc->SetParLimits(1, 0.0001, 100000.);
    baseFitFunc->SetParameter(0, 100.);
    baseFitFunc->SetParameter(1, 1000.);
    baseHisto->Sumw2(); // Insure errors are handled correctly when scaled.
    //baseHisto->Scale(1); // Scale by 1, and then divide each bin by its width.
    baseHisto->Fit(baseFitFunc, "RMWLQ");
    baseHisto->Draw("E");
    TH1D* baseBG = (TH1D*)bgfitfunc.getNormalizedBackgroundHisto()->Clone("baseBG");
    baseBG->Scale(baseFitFunc->GetParameter(0));
    baseBG->SetLineStyle(2);
    baseBG->Draw("same");

    // Extract background histo
    TH1D* backgroundHisto = (TH1D*)bgfitfunc.getBackgroundHisto()->Clone("baseBG");

    canvas->cd(2);
    TF1* postFitFunc = new TF1("postFitFunc", bgfitfunc, eventrq.minMZ, eventrq.maxMZ, 2);
    postFitFunc->SetLineWidth(1);
    postFitFunc->SetParLimits(0, 0., 10000.);
    postFitFunc->SetParLimits(1, 0., 100000.);
    postFitFunc->SetParameter(0, 100.);
    postFitFunc->SetParameter(1, 1000.);
    postcutHisto->Sumw2();
    //postcutHisto->Scale(1);
    postcutHisto->Fit(postFitFunc, "RMWLQ");
    postcutHisto->Draw("E");
    TH1D* postBG = (TH1D*)bgfitfunc.getNormalizedBackgroundHisto()->Clone("postBG");
    postBG->Scale(postFitFunc->GetParameter(0));
    postBG->SetLineStyle(2);
    postBG->Draw("same");

    // Calculate Eff
    effs countEff = effFromCounting(baseHisto, postcutHisto, backgroundHisto, backgroundHisto, baseFitFunc->GetParameter(0), baseFitFunc->GetParError(0), postFitFunc->GetParameter(0), postFitFunc->GetParError(0));
    effs sigEff = effFromSignal( signalHisto, signalHisto, baseFitFunc->GetParameter(1), baseFitFunc->GetParError(1), postFitFunc->GetParameter(1), postFitFunc->GetParError(1));

    canvas->cd(0);

    const std::string name(outFile.begin(), outFile.end()-5);
    const std::string pngname = name + std::string(".png");
    canvas->Print(pngname.c_str(), "png");
    outfile->Write();

    //Prints eff stats for text file
    const double baseD = baseHisto->Integral(baseHisto->FindBin(eventrq.minMZ), baseHisto->FindBin(eventrq.maxMZ));
    const double baseB = backgroundHisto->Integral(backgroundHisto->FindBin(eventrq.minMZ), backgroundHisto->FindBin(eventrq.maxMZ));

    const double denom = (baseD - (baseFitFunc->GetParameter(0)*baseB));
    printEffs(probeLoc, eventrq, xBin, sigEff.eff, countEff.eff, denom, usePhiStar);

    return 0;
}

int main(int argc, char* argv[]){
    const int argcCorrect = 14;
    if (argc < argcCorrect) {
        std::cout<<"Not enough arguments. Use:\nfitEffAcc.exe bgfitFile signalFile ZEffFile outFile tagLoc probeLoc minPU maxPU minMZ maxMZ minX maxX\n";
        return 1;
    } else if (argc > argcCorrect){
        std::cout<<"Too many arguments. Use:\nfitEffAcc.exe bgfitFile signalFile ZEffFile outFile tagLoc probeLoc minPU maxPU minMZ maxMZ minX maxX\n";
        return 1;
    } else {
        // Read in arguments
        std::istringstream inStream;

        std::string bgfitFile;
        std::string signalFile;
        std::string ZEffFile;
        std::string outFile;

        inStream.str(argv[1]);
        inStream >> bgfitFile;
        inStream.clear();
        inStream.str(argv[2]);
        inStream >> signalFile;
        inStream.clear();
        inStream.str(argv[3]);
        inStream >> ZEffFile;
        inStream.clear();
        inStream.str(argv[4]);
        inStream >> outFile;
        inStream.clear();

        std::string tagL;
        std::string probeL;

        inStream.str(argv[5]);
        inStream >> tagL;
        inStream.clear();
        inStream.str(argv[6]);
        inStream >> probeL;
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
        electronLocation tagLoc = conv[tagL];
        electronLocation probeLoc = conv[probeL];

        eventRequirements eventrq;
        inStream.str(argv[7]);
        inStream >> eventrq.minPU;
        inStream.clear();
        inStream.str(argv[8]);
        inStream >> eventrq.maxPU;
        inStream.clear();
        inStream.str(argv[9]);
        inStream >> eventrq.minMZ;
        inStream.clear();
        inStream.str(argv[10]);
        inStream >> eventrq.maxMZ;
        inStream.clear();

        bin xBin;

        inStream.str(argv[11]);
        inStream >> xBin.minX;
        inStream.clear();
        inStream.str(argv[12]);
        inStream >> xBin.maxX;
        inStream.clear();

        bool usePhiStar;
        inStream.str(argv[13]);
        inStream >> usePhiStar;
        inStream.clear();

        // Map location to other features
        // Hard coded for now
        std::string tagWP;
        switch (tagLoc){
            case EB:
            case EBp:
            case EBm:
            case EE:
            case EEp:
            case EEm:
            case ET:
                tagWP = "WP80";
                break;
            case NT: // No NT case?
            case NTp:
            case NTm:
                tagWP = "NTTightElectronId-EtaDet";
                break;
            case HF:
            case HFp:
            case HFm:
                tagWP = "HFElectronId-EtaDet";
                break;
        }

        std::string signalTH;
        std::string probeWP; // Wokring point to test

        switch (probeLoc){
            case EB:
            case EBp:
            case EBm:
            case EE:
            case EEp:
            case EEm:
            case ET:
                probeWP = "WP80";
                break;
            case NT: // No NT case?
            case NTp:
            case NTm:
                probeWP = "NTTightElectronId-EtaDet";
                break;
            case HF:
            case HFp:
            case HFm:
                probeWP = "HFTID";
                break;
        }

        std::stringstream ss;
        ss << "#efficiency name: " << probeWP << std::endl;
        ss << "#dimension: 1" << std::endl;
        std::cout << ss.str() << std::flush;

        //std::cout << " Tag: " << tagWP << " Probe: " << probeWP << " MinPt: " << xBin.minX << " MaxPt: " << xBin.maxX << " MinPU: " << eventrq.minPU << " MaxPU: " << eventrq.maxPU << std::endl;
        return fitDistributions(
                bgfitFile,
                signalFile,
                ZEffFile,
                outFile,
                tagWP,
                probeWP,
                tagLoc,
                probeLoc,
                eventrq,
                xBin,
                usePhiStar
                );
    }
}