#ifndef HISTOMAKER_H_INCLUDED
#define HISTOMAKER_H_INCLUDED

// ZShape Code
#include "../../MakeZEffTree/src/ZEffTree.h"

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

class MakeHistograms{
    public:
        // Constructor
        MakeHistograms(TDirectory* td);

        // Add events
        void fill(const ZEffTree::ZInfo* zi, const int e0 = 0, const int e1 = 1);
        void print();

    private:
        TDirectory* tdir;
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
        TH1I* pileup;
};

#endif
