// ZShape Code
#include "../../MakeZEffTree/src/ZEffTree.h"
#include "../ElectronLocation/ElectronLocation.h"

// Root
#include "TH1.h"
#include "TFile.h"
#include <TROOT.h>

// STD
#include <string>
#include <sstream>
#include <vector>

struct analysisHistograms{
    TH1I* Z0Mass;
    TH1I* Z0MassFine;
    TH1I* Z0Rapidity;
    TH1I* Z0pt;
    TH1I* e0pt;
    TH1I* e1pt;
    TH1I* e0eta;
    TH1I* e1eta;
    TH1I* e0phi;
    TH1I* e1phi;
    TH1I* phistar;
};

int makeTupleCuts(const std::string inputFile, const std::string outFile){
    // Root style
    gROOT->SetStyle("Plain");

    // Prepare output
    TFile* outfile;
    outfile = new TFile(outFile.c_str(), "RECREATE");

    /* Prepare the histogram to put the data in */
    std::vector<analysisHistograms> histos;
    for (short i=0; i < 2; i++){
        // Initialize Histos
        analysisHistograms histo;

        // Convert i to string
        std::string istr;
        std::ostringstream convert;
        convert << i;
        istr = convert.str();

        // Set up all the histograms
        // Z Mass
        const std::string Z0MassName = "Z0_mass_" + istr;
        histo.Z0Mass = new TH1I(Z0MassName.c_str(), Z0MassName.c_str(), 50, 50., 150.);
        histo.Z0Mass->SetDirectory(outfile);
        histo.Z0Mass->GetXaxis()->SetTitle("m_{ee} [GeV]");
        histo.Z0Mass->GetYaxis()->SetTitle("Counts/GeV");
        // Z Mass Fine
        const std::string Z0MassFineName = "Z0_mass_fine_" + istr;
        histo.Z0MassFine = new TH1I(Z0MassFineName.c_str(), Z0MassFineName.c_str(), 120, 60., 120.);
        histo.Z0MassFine->SetDirectory(outfile);
        histo.Z0MassFine->GetXaxis()->SetTitle("m_{ee} [GeV]");
        histo.Z0MassFine->GetYaxis()->SetTitle("Counts/GeV");
        // Z Mass Fine
        const std::string Z0RapidityName = "Z0_rapidity_" + istr;
        histo.Z0Rapidity = new TH1I(Z0RapidityName.c_str(), Z0RapidityName.c_str(), 100, -5., 5.);
        histo.Z0Rapidity->SetDirectory(outfile);
        histo.Z0Rapidity->GetXaxis()->SetTitle("Y_{ee}");
        histo.Z0Rapidity->GetYaxis()->SetTitle("Counts");
        // Z pt
        const std::string Z0ptName = "Z0_pt_" + istr;
        histo.Z0pt = new TH1I(Z0ptName.c_str(), Z0ptName.c_str(), 200, 0., 400.);
        histo.Z0pt->SetDirectory(outfile);
        histo.Z0pt->GetXaxis()->SetTitle("p_{T,Z} [GeV]");
        histo.Z0pt->GetYaxis()->SetTitle("Counts/Gev");
        // e pt
        const std::string e0ptName = "e0_pt_" + istr;
        histo.e0pt = new TH1I(e0ptName.c_str(), e0ptName.c_str(), 200, 0., 400.);
        histo.e0pt->SetDirectory(outfile);
        histo.e0pt->GetXaxis()->SetTitle("p_{T,e_{0}} [GeV]");
        histo.e0pt->GetYaxis()->SetTitle("Counts/Gev");
        const std::string e1ptName = "e1_pt_" + istr;
        histo.e1pt = new TH1I(e1ptName.c_str(), e1ptName.c_str(), 200, 0., 400.);
        histo.e1pt->SetDirectory(outfile);
        histo.e1pt->GetXaxis()->SetTitle("p_{T,e_{0}} [GeV]");
        histo.e1pt->GetYaxis()->SetTitle("Counts/Gev");
        // e phi
        const std::string e0phiName = "e0_phi_" + istr;
        histo.e0phi = new TH1I(e0phiName.c_str(), e0phiName.c_str(), 60, -3.14, 3.14);
        histo.e0phi->SetDirectory(outfile);
        histo.e0phi->GetXaxis()->SetTitle("#phi_{e_{0}}");
        histo.e0phi->GetYaxis()->SetTitle("Counts");
        const std::string e1phiName = "e1_phi_" + istr;
        histo.e1phi = new TH1I(e1phiName.c_str(), e1phiName.c_str(), 60, -3.14, 3.14);
        histo.e1phi->SetDirectory(outfile);
        histo.e1phi->GetXaxis()->SetTitle("#phi_{e_{0}}");
        histo.e1phi->GetYaxis()->SetTitle("Counts");
        // e eta
        const std::string e0etaName = "e0_eta_" + istr;
        histo.e0eta = new TH1I(e0etaName.c_str(), e0etaName.c_str(), 50, -5., 5.);
        histo.e0eta->SetDirectory(outfile);
        histo.e0eta->GetXaxis()->SetTitle("#eta_{e_{0}}");
        histo.e0eta->GetYaxis()->SetTitle("Counts");
        const std::string e1etaName = "e1_eta_" + istr;
        histo.e1eta = new TH1I(e1etaName.c_str(), e1etaName.c_str(), 50, -5., 5.);
        histo.e1eta->SetDirectory(outfile);
        histo.e1eta->GetXaxis()->SetTitle("#eta_{e_{0}}");
        histo.e1eta->GetYaxis()->SetTitle("Counts");
        // Phistar
        const std::string phistarName = "phistar_" + istr;
        histo.phistar = new TH1I(phistarName.c_str(), phistarName.c_str(), 1000, 0., 1.);
        histo.phistar->SetDirectory(outfile);
        histo.phistar->GetXaxis()->SetTitle("#phi^{*}");
        histo.phistar->GetYaxis()->SetTitle("Counts");

        // Add the histogram to the vector
        histos.push_back(histo);
    }

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
        if (inAcceptance(HF, ze->reco.eta[0]) && inAcceptance(ET, ze->reco.eta[1])){
            HFElectron = 0;
            ETElectron = 1;
        } else if (inAcceptance(HF, ze->reco.eta[1]) && inAcceptance(ET, ze->reco.eta[0])){
            HFElectron = 1;
            ETElectron = 0;
        } else {
            run = ze->GetNextEvent();
            continue;
        }
        /* Cuts */
        /* Tuple Selection Only */
        histos[0].Z0Mass->Fill(MZ);
        histos[0].Z0MassFine->Fill(MZ);
        histos[0].Z0Rapidity->Fill(ze->reco.yz);
        histos[0].Z0pt->Fill(ze->reco.ptz);
        histos[0].e0pt->Fill(ze->reco.pt[ETElectron]);
        histos[0].e0eta->Fill(ze->reco.eta[ETElectron]);
        histos[0].e0phi->Fill(ze->reco.phi[ETElectron]);
        histos[0].e1pt->Fill(ze->reco.pt[HFElectron]);
        histos[0].e1eta->Fill(ze->reco.eta[HFElectron]);
        histos[0].e1phi->Fill(ze->reco.phi[HFElectron]);
        histos[0].phistar->Fill(ze->reco.phistar);
        /* Check minimum pt */
        if (ze->reco.isSelected(HFElectron, "HFTID")){
            histos[1].Z0Mass->Fill(MZ);
            histos[1].Z0MassFine->Fill(MZ);
            histos[1].Z0Rapidity->Fill(ze->reco.yz);
            histos[1].Z0pt->Fill(ze->reco.ptz);
            histos[1].e0pt->Fill(ze->reco.pt[ETElectron]);
            histos[1].e0eta->Fill(ze->reco.eta[ETElectron]);
            histos[1].e0phi->Fill(ze->reco.phi[ETElectron]);
            histos[1].e1pt->Fill(ze->reco.pt[HFElectron]);
            histos[1].e1eta->Fill(ze->reco.eta[HFElectron]);
            histos[1].e1phi->Fill(ze->reco.phi[HFElectron]);
            histos[1].phistar->Fill(ze->reco.phistar);
        }
        run = ze->GetNextEvent();
    }
    outfile->Write();

    return 0;
}

int main(int argc, char* argv[]){
    const short argcCorrect = 3;
    if (argc < argcCorrect) {
        std::cout<<"Not enough arguments. Use:\nCutCounter.exe ZEffFile outputFile\n";
        return 1;
    } else if (argc > argcCorrect){
        std::cout<<"Too many arguments. Use:\nCutCounter.exe ZEffFile outFile\n";
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
