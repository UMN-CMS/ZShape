#include "ElectronLocation.h"

bool inAcceptance(const electronLocation Loc, const double eta){
    const double feta = fabs(eta);
    switch (Loc){
        case EB:
            if (feta < 1.4442){
                return true; 
            }
            break;
        case EBp:
            if (0. < eta && eta < 1.4442){
                return true; 
            }
            break;
        case EBm:
            if (0. > eta && eta > -1.4442){
                return true; 
            }
            break;
        case EE:
            if (1.566 < feta && feta < 2.5){
                return true; 
            }
            break;
        case EEp:
            if (1.566 < eta && eta < 2.5){
                return true; 
            }
            break;
        case EEm:
            if (-1.566 > eta && eta > -2.5){
                return true; 
            }
            break;
        case ET:
            if (feta < 1.4442 || (1.566 < feta && feta < 2.5)){
                return true; 
            }
            break;
        case NT:
            if (2.5 < feta && feta < 2.850){
                return true; 
            }
            break;
        case NTp:
            if (2.5 < eta && eta < 2.850){
                return true; 
            }
            break;
        case NTm:
            if (-2.5 > eta && eta > -2.850){
                return true; 
            }
            break;
        case HF:
            if (3.1 < feta && feta < 4.6){
                return true; 
            }
            break;
        case HFp:
            if (3.1 < eta && eta < 4.6){
                return true; 
            }
            break;
        case HFm:
            if (-3.1 > eta && eta > -4.6){
                return true; 
            }
            break;
    }
    return false;
}
