// ZShape Code
#include "../../MakeZEffTree/src/ZEffTree.h"
#include "../ElectronLocation/ElectronLocation.h"

// Root
#include "TH1.h"
#include "TF1.h"
#include "TFile.h"
#include "TAxis.h"
#include "TObject.h"
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
};

int makeTupleCuts(const std::string inputFile, const std::string outFile){
    // Root style
    gROOT->SetStyle("Plain");

    // Prepare output
    TFile* outfile;
    outfile = new TFile(outFile.c_str(), "RECREATE");

    /* Prepare the histogram to put the data in */
    std::vector<analysisHistograms> histos;
    for (short i=0; i < 6; i++){
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
        int EBElectron;
        int EEElectron;
        const double MZ = ze->reco.mz;
        const short PU = ze->reco.nverts;
        /* Assign Electron 0 and 1 */
        if ( inAcceptance(EB, ze->reco.eta[0]) && inAcceptance(EE, ze->reco.eta[1])){
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
        //
        // For the record, someone said "please add in histograms at each
        // step!" and so now we have them
        histos[0].Z0Mass->Fill(MZ);
        histos[0].Z0MassFine->Fill(MZ);
        histos[0].Z0Rapidity->Fill(ze->reco.yz);
        histos[0].Z0pt->Fill(ze->reco.ptz);
        histos[0].e0pt->Fill(ze->reco.pt[EBElectron]);
        histos[0].e0eta->Fill(ze->reco.eta[EBElectron]);
        histos[0].e0phi->Fill(ze->reco.phi[EBElectron]);
        histos[0].e1pt->Fill(ze->reco.pt[EEElectron]);
        histos[0].e1eta->Fill(ze->reco.eta[EEElectron]);
        histos[0].e1phi->Fill(ze->reco.phi[EEElectron]);
        /* Check minimum pt */
        if ( ze->reco.pt[0] > 20. && ze->reco.pt[1] > 20.){
            histos[1].Z0Mass->Fill(MZ);
            histos[1].Z0MassFine->Fill(MZ);
            histos[1].Z0Rapidity->Fill(ze->reco.yz);
            histos[1].Z0pt->Fill(ze->reco.ptz);
            histos[1].e0pt->Fill(ze->reco.pt[EBElectron]);
            histos[1].e0eta->Fill(ze->reco.eta[EBElectron]);
            histos[1].e0phi->Fill(ze->reco.phi[EBElectron]);
            histos[1].e1pt->Fill(ze->reco.pt[EEElectron]);
            histos[1].e1eta->Fill(ze->reco.eta[EEElectron]);
            histos[1].e1phi->Fill(ze->reco.phi[EEElectron]);
            /* Supercluster */
            if ( ze->reco.isSelected(0, "Supercluster-Eta") && ze->reco.isSelected(1, "Supercluster-Eta") ){
                histos[2].Z0Mass->Fill(MZ);
                histos[2].Z0MassFine->Fill(MZ);
                histos[2].Z0Rapidity->Fill(ze->reco.yz);
                histos[2].Z0pt->Fill(ze->reco.ptz);
                histos[2].e0pt->Fill(ze->reco.pt[EBElectron]);
                histos[2].e0eta->Fill(ze->reco.eta[EBElectron]);
                histos[2].e0phi->Fill(ze->reco.phi[EBElectron]);
                histos[2].e1pt->Fill(ze->reco.pt[EEElectron]);
                histos[2].e1eta->Fill(ze->reco.eta[EEElectron]);
                histos[2].e1phi->Fill(ze->reco.phi[EEElectron]);
                /* GSF-GSF */
                if ( ze->reco.isSelected(0, "GsfTrack-EtaDet") && ze->reco.isSelected(1, "GsfTrack-EtaDet") ){
                    histos[3].Z0Mass->Fill(MZ);
                    histos[3].Z0MassFine->Fill(MZ);
                    histos[3].Z0Rapidity->Fill(ze->reco.yz);
                    histos[3].Z0pt->Fill(ze->reco.ptz);
                    histos[3].e0pt->Fill(ze->reco.pt[EBElectron]);
                    histos[3].e0eta->Fill(ze->reco.eta[EBElectron]);
                    histos[3].e0phi->Fill(ze->reco.phi[EBElectron]);
                    histos[3].e1pt->Fill(ze->reco.pt[EEElectron]);
                    histos[3].e1eta->Fill(ze->reco.eta[EEElectron]);
                    histos[3].e1phi->Fill(ze->reco.phi[EEElectron]);
                    /* WP80 */
                    if ( ze->reco.isSelected(0, "WP80") && ze->reco.isSelected(1, "WP80") ){
                        histos[4].Z0Mass->Fill(MZ);
                        histos[4].Z0MassFine->Fill(MZ);
                        histos[4].Z0Rapidity->Fill(ze->reco.yz);
                        histos[4].Z0pt->Fill(ze->reco.ptz);
                        histos[4].e0pt->Fill(ze->reco.pt[EBElectron]);
                        histos[4].e0eta->Fill(ze->reco.eta[EBElectron]);
                        histos[4].e0phi->Fill(ze->reco.phi[EBElectron]);
                        histos[4].e1pt->Fill(ze->reco.pt[EEElectron]);
                        histos[4].e1eta->Fill(ze->reco.eta[EEElectron]);
                        histos[4].e1phi->Fill(ze->reco.phi[EEElectron]);
                        /* MZ */
                        if ( 60 <= MZ && MZ <= 120 ){
                            histos[5].Z0Mass->Fill(MZ);
                            histos[5].Z0MassFine->Fill(MZ);
                            histos[5].Z0Rapidity->Fill(ze->reco.yz);
                            histos[5].Z0pt->Fill(ze->reco.ptz);
                            histos[5].e0pt->Fill(ze->reco.pt[EBElectron]);
                            histos[5].e0eta->Fill(ze->reco.eta[EBElectron]);
                            histos[5].e0phi->Fill(ze->reco.phi[EBElectron]);
                            histos[5].e1pt->Fill(ze->reco.pt[EEElectron]);
                            histos[5].e1eta->Fill(ze->reco.eta[EEElectron]);
                            histos[5].e1phi->Fill(ze->reco.phi[EEElectron]);
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
        std::cout<<"Not enough arguments. Use:\nTupleCutter.exe ZEffFile outputFile\n";
        return 1;
    } else if (argc > argcCorrect){
        std::cout<<"Too many arguments. Use:\nTupleCutter.exe ZEffFile outFile\n";
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
