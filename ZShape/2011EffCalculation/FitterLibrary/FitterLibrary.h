#ifndef ZSHAPE_2011EFFCALCULATION_FITTERLIBRARY_FITTERLIBRARY_H_
#define ZSHAPE_2011EFFCALCULATION_FITTERLIBRARY_FITTERLIBRARY_H_

#include <TH1.h>  // TH1D
#include <vector>  // std::vector
//#include <string.h>  // std::string
#include "../ElectronLocation/ElectronLocation.h"  // electronLocation

struct EffBin{
    int minPU;
    int maxPU;
    double minMZ;
    double maxMZ;
    double minX;
    double maxX;
};

struct Efficiencies{
    double eff;
    double err;
};

void getBinEdges(const double minX, const double maxX, const electronLocation probeLoc, std::vector<double>* vec);

Efficiencies EffFromCounting(TH1D* baseData,  TH1D* postData,  TH1D* baseBG,  TH1D* postBG, const double baseE, const double postE, const double minMZ=60., const double maxMZ=120.);

Efficiencies EffFromSignal(TH1D*  baseSig, TH1D* postSig, const double baseE, const double postE, const double minMZ=60., const double maxMZ=120.);

void PrintEffs(const electronLocation probeLoc, const EffBin effbin, const double sigeff, const double counteff, const double denom, const bool usePhiStar);

#endif  // ZSHAPE_2011EFFCALCULATION_FITTERLIBRARY_FITTERLIBRARY_H_
