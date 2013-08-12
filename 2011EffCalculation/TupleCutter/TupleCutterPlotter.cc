// Root
#include "TH1.h"
#include "TF1.h"
#include "TFile.h"
#include "TAxis.h"
#include "TObject.h"
#include "TCanvas.h"
#include "TLegend.h"
#include <TROOT.h>

// STD
#include <string>
#include <sstream>
#include <vector>

int makeCombinedPlots(const std::string cutFile, const std::string zFromDataFile, const std::string kevinFile, const std::string outFile){
    // Root style
    gROOT->SetStyle("Plain");


    // Prepare input
    TFile* cutTFile = new TFile(cutFile.c_str(), "READ");
    TFile* zFromDataTFile = new TFile(zFromDataFile.c_str(), "READ");
    TFile* kevinTFile = new TFile(kevinFile.c_str(), "READ");

    // Prepare output
    TFile* outTFile = new TFile(outFile.c_str(), "RECREATE");
    outTFile->cd();

    // Get the histograms
    // GSF-GSF
    TH1I* gsfgsf_Cuts_E0Eta = (TH1I*)cutTFile->Get("e0_eta_3");
    TH1I* gsfgsf_Cuts_E1pt = (TH1I*)cutTFile->Get("e1_pt_3");
    TH1I* gsfgsf_zAlex_E0Eta = (TH1I*)zFromDataTFile->Get("/ZFromDataAlex/EB-EE/C04-GsfTrack-EtaDet/e1_eta");
    TH1I* gsfgsf_zKevin_E0Eta = (TH1I*)zFromDataTFile->Get("/ZFromDataKevin/EB-EE/C04-GsfTrack-EtaDet/e1_eta");
    TH1I* gsfgsf_zAlex_E1pt = (TH1I*)zFromDataTFile->Get("/ZFromDataAlex/EB-EE/C04-GsfTrack-EtaDet/e2_P_t");
    TH1I* gsfgsf_zKevin_E1pt = (TH1I*)zFromDataTFile->Get("/ZFromDataKevin/EB-EE/C04-GsfTrack-EtaDet/e2_P_t");
    TH1I* gsfgsf_justKevin_E0Eta = (TH1I*)kevinTFile->Get("/ZFromData/EE-EB/C04-GsfTrack-EtaDet/e2_eta");
    TH1I* gsfgsf_justKevin_E1pt = (TH1I*)kevinTFile->Get("/ZFromData/EE-EB/C04-GsfTrack-EtaDet/e1_P_t");
    
    // All cuts
    TH1I* allCuts_Cuts_E0Eta = (TH1I*)cutTFile->Get("e0_eta_5");
    TH1I* allCuts_Cuts_E1pt = (TH1I*)cutTFile->Get("e1_pt_5");
    TH1I* allCuts_zAlex_E0Eta = (TH1I*)zFromDataTFile->Get("/ZFromDataAlex/EB-EE/C06-m(60,120)/e1_eta");
    TH1I* allCuts_zKevin_E0Eta = (TH1I*)zFromDataTFile->Get("/ZFromDataKevin/EB-EE/C06-m(60,120)/e1_eta");
    TH1I* allCuts_zAlex_E1pt = (TH1I*)zFromDataTFile->Get("/ZFromDataAlex/EB-EE/C06-m(60,120)/e2_P_t");
    TH1I* allCuts_zKevin_E1pt = (TH1I*)zFromDataTFile->Get("/ZFromDataKevin/EB-EE/C06-m(60,120)/e2_P_t");
    TH1I* allCuts_justKevin_E0Eta = (TH1I*)kevinTFile->Get("/ZFromData/EE-EB/C06-m(60,120)/e2_eta");
    TH1I* allCuts_justKevin_E1pt = (TH1I*)kevinTFile->Get("/ZFromData/EE-EB/C06-m(60,120)/e1_P_t");

    // Set colors and lines
    gsfgsf_Cuts_E0Eta->SetLineColor(1);
    allCuts_Cuts_E0Eta->SetLineColor(1);
    gsfgsf_Cuts_E1pt->SetLineColor(1);
    allCuts_Cuts_E1pt->SetLineColor(1);

    gsfgsf_zAlex_E0Eta->SetLineColor(2);
    allCuts_zAlex_E0Eta->SetLineColor(2);
    gsfgsf_zAlex_E1pt->SetLineColor(2);
    allCuts_zAlex_E1pt->SetLineColor(2);

    gsfgsf_zKevin_E0Eta->SetLineColor(3);
    allCuts_zKevin_E0Eta->SetLineColor(3);
    gsfgsf_zKevin_E1pt->SetLineColor(3);
    allCuts_zKevin_E1pt->SetLineColor(3);

    gsfgsf_justKevin_E0Eta->SetLineColor(4);
    allCuts_justKevin_E0Eta->SetLineColor(4);
    gsfgsf_justKevin_E1pt->SetLineColor(4);
    allCuts_justKevin_E1pt->SetLineColor(4);

    // Make canvases
    TCanvas* e0_eta_gsf = new TCanvas("e0_eta_gsf", "e0_eta_gsf");
    gsfgsf_zAlex_E0Eta->Draw();
    gsfgsf_zKevin_E0Eta->Draw("samehist");
    gsfgsf_Cuts_E0Eta->Draw("samehist");
    gsfgsf_justKevin_E0Eta->Draw("samehist");
    //TLegend* tl0 = new TLegend(0.1,0.7,0.2,0.89);
    //tl0->AddEntry(gsfgsf_zAlex_E0Eta, "zAlex", "l");
    //tl0->Draw();
    e0_eta_gsf->Write();

    TCanvas* e0_eta_all = new TCanvas("e0_eta_all", "e0_eta_all");
    allCuts_zAlex_E0Eta->Draw();
    allCuts_zKevin_E0Eta->Draw("samehist");
    allCuts_Cuts_E0Eta->Draw("samehist");
    allCuts_justKevin_E0Eta->Draw("samehist");
    e0_eta_all->Write();

    TCanvas* e1_pt_gsf = new TCanvas("e1_pt_gsf", "e1_pt_gsf");
    gsfgsf_zAlex_E1pt->Draw();
    gsfgsf_zKevin_E1pt->Draw("samehist");
    gsfgsf_Cuts_E1pt->Draw("samehist");
    gsfgsf_justKevin_E1pt->Draw("samehist");
    e1_pt_gsf->Write();

    TCanvas* e1_pt_all = new TCanvas("e1_pt_all", "e1_pt_all");
    allCuts_zAlex_E1pt->Draw();
    allCuts_zKevin_E1pt->Draw("samehist");
    allCuts_Cuts_E1pt->Draw("samehist");
    allCuts_justKevin_E1pt->Draw("samehist");
    e1_pt_all->Write();
    
    // Save output
    outTFile->Write();

    return 0;
}

int main(int argc, char* argv[]){
    const short argcCorrect = 5;
    if (argc < argcCorrect) {
        std::cout<<"Not enough arguments. Use:\nTupleCutter.exe CutFile ZFromDateFile KevinFile outputFile\n";
        return 1;
    } else if (argc > argcCorrect){
        std::cout<<"Too many arguments. Use:\nTupleCutter.exe CutFile ZFromDateFile KevinFile outputFile\n";
        return 1;
    } else {
        // Read in arguments
        std::istringstream inStream;

        std::string cutFile;
        inStream.str(argv[1]);
        inStream >> cutFile;
        inStream.clear();

        std::string zFromDataFile;
        inStream.str(argv[2]);
        inStream >> zFromDataFile;
        inStream.clear();

        std::string kevinFile;
        inStream.str(argv[3]);
        inStream >> kevinFile;
        inStream.clear();

        std::string outFile;
        inStream.str(argv[4]);
        inStream >> outFile;
        inStream.clear();

        return makeCombinedPlots(cutFile, zFromDataFile, kevinFile, outFile);
    }
}
