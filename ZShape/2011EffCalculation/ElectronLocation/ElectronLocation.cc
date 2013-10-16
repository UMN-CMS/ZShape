#include "ElectronLocation.h"

#include <math.h>  // fabs

bool inAcceptance(const electronLocation loc, const double eta){
    const double feta = fabs(eta);
    switch (loc){
        case ALL:
            return true;
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
            if (1.566 < feta && feta < 2.850){
                return true; 
            }
            break;
        case EEp:
            if (1.566 < eta && eta < 2.850){
                return true; 
            }
            break;
        case EEm:
            if (-1.566 > eta && eta > -2.850){
                return true; 
            }
            break;
        case ET:
            if (feta < 1.4442 || (1.566 < feta && feta < 2.850)){
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

std::string electronLocationToString(const electronLocation loc){
    switch (loc){
        case EB:
            return "EB"; 
        case EBp:
            return "EBp";
        case EBm:
            return "EBm";
        case EE:
            return "EE";
        case EEp:
            return "EEp";
        case EEm:
            return "EEm";
        case ET:
            return "ET";
        case NT:
            return "NT";
        case NTp:
            return "NTp";
        case NTm:
            return "NTm";
        case HF:
            return "HF";
        case HFp:
            return "HFp";
        case HFm:
            return "HFm";
        case ALL:
            return "ALL";
        default:
            return "";
    }
    return "Invalid Location";
}

electronLocation electronLocationToString(const std::string& instr){
    if (instr.compare("ET") == 0){
        return ET;
    }
    if (instr.compare("EB") == 0){
        return EB;
    }
    if (instr.compare("EBp") == 0){
        return EBp;
    }
    if (instr.compare("EBm") == 0){
        return EBm;
    }
    if (instr.compare("EE") == 0){
        return EE;
    }
    if (instr.compare("EEp") == 0){
        return EEp;
    }
    if (instr.compare("EEm") == 0){
        return EEm;
    }
    if (instr.compare("NT") == 0){
        return NT;
    }
    if (instr.compare("NTp") == 0){
        return NTp;
    }
    if (instr.compare("NTm") == 0){
        return NTm;
    }
    if (instr.compare("HF") == 0){
        return HF;
    }
    if (instr.compare("HFp") == 0){
        return HFp;
    }
    if (instr.compare("HFm") == 0){
        return HFm;
    }
    if (instr.compare("ALL") == 0){
        return ALL;
    }
    // All at least does not cut out events
    return ALL;
}
