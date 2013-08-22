// ZShape Code
#include "../../MakeZEffTree/src/ZEffTree.h"
#include "../ElectronLocation/ElectronLocation.h"

// Root
#include "TH1.h"
#include "TFile.h"
#include <TROOT.h>
#include "TCanvas.h"
#include "TDirectory.h"

// STD
#include <string>
#include <sstream>
#include <vector>

// Plotting code
#include "HistoMaker.h"


int makeTupleCuts(const std::string inputFile, const std::string outFile){
    // Root style
    gROOT->SetStyle("Plain");

    // Prepare output
    TFile* outfile;
    outfile = new TFile(outFile.c_str(), "RECREATE");

    // Prepare plot makers
    TDirectory* td0 = outfile->mkdir("0_Acceptance", "0_Acceptance");
    MakeHistograms* p0 = new MakeHistograms(td0);
    TDirectory* td1 = outfile->mkdir("1_HFTID", "1_HFTID");
    MakeHistograms* p1 = new MakeHistograms(td1);

    // Open file to fit, and make histograms
    TFile ZEffFile(inputFile.c_str(), "READ");
    ZEffTree* ze;
    ze = new ZEffTree(ZEffFile, false);

    bool run = true;
    while (run){
        ze->Entries();
        int ETElectron;
        int HFElectron;
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
        p0->fill(&ze->reco, ETElectron, HFElectron);
        /* Check minimum pt */
        if (ze->reco.isSelected(HFElectron, "HFTID")){
            p1->fill(&ze->reco, ETElectron, HFElectron);
        }
        run = ze->GetNextEvent();
    }
    outfile->Write();

    /* Write PNGs */
    p0->print();
    p1->print();

    return 0;
}

int main(int argc, char* argv[]){
    const short argcCorrect = 3;
    if (argc < argcCorrect) {
        std::cout<<"Not enough arguments. Use:\nPostCutPlotter.exe ZEffFile outputFile\n";
        return 1;
    } else if (argc > argcCorrect){
        std::cout<<"Too many arguments. Use:\nPostCutPlotter.exe ZEffFile outFile\n";
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
