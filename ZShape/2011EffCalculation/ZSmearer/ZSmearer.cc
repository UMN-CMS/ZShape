#include "ZSmearer.h"

#include "../ElectronLocation/ElectronLocation.h"  // electronLocation
#include <TLorentzVector.h>  // TLorentzVector

void smearEvent(TRandom* trand, ZEffTree::ZInfo* zi){
    // Set up the location dependent constants
    const double HFP_MEAN  = 0.983;
    const double HFP_SIGMA = 0.070;
    const double HFM_MEAN  = 0.967;
    const double HFM_SIGMA = 0.070;
    const double EE_MEAN   = 0.968;
    const double EE_SIGMA  = 0.024;
    const double EB_MEAN   = 0.993;
    const double EB_SIGMA  = 0.010;

    // Find the locations of the electrons and assign the constants
    double mean[2];
    double sigma[2];
    for (int i = 0; i <= 1; i++){
        if (inAcceptance(EB, zi->eta[i])){
            mean[i] = EB_MEAN;
            sigma[i] = EB_SIGMA;
        } else if (inAcceptance(EE, zi->eta[i])){
            mean[i] = EE_MEAN;
            sigma[i] = EE_SIGMA;
        } else if (inAcceptance(HFp, zi->eta[i])){
            mean[i] = HFP_MEAN;
            sigma[i] = HFP_SIGMA;
        } else if (inAcceptance(HFm, zi->eta[i])){
            mean[i] = HFM_MEAN;
            sigma[i] = HFM_SIGMA;
        } else {  // Do nothing; we use -1 to reject smearing later.
            mean[i] = -1;
            sigma[i] = -1;
        }
    }

    // Smear the pt with a Gaussian
    for (int i = 0; i <= 1; i++){
        if (mean[i] > 0 && sigma[i] > 0){
            zi->pt[i] *= trand->Gaus(mean[i], sigma[i]);
        }
    }

    // Make Lorentz Vectors from the electrons
    TLorentzVector e0lv;
    TLorentzVector e1lv;
    e0lv.SetPtEtaPhiM(zi->pt[0], zi->eta[0], zi->phi[0], 5.109989e-4);
    e1lv.SetPtEtaPhiM(zi->pt[1], zi->eta[1], zi->phi[1], 5.109989e-4);

    // Recalculate the Z mass
    TLorentzVector Zlv;
    Zlv = e0lv + e1lv;
    zi->mz = Zlv.M();
}
