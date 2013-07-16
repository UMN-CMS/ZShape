#include "ElectronLocation.h"

#include <iostream>
#include <map>
#include <string>

int main(){
    const double etas[] = { 
        -1, -1.444, -1.5 -1.567, -2., -2.49, -2.51, -2.7, -2.849, -2.851,
        -3.09, -3.11, -4.59, -4.61, 0., 1, 1.444, 1.5 ,1.567, 2., 2.49, 2.51,
        2.7, 2.849, 2.851, 3.09, 3.11, 4.59, 4.61
    };

    const electronLocation locs[13] = {
        EB, EBp, EBm, EE, EEp, EEm, ET, NT, NTp, NTm, HF, HFp, HFm
    };

    for (int i = 0; i < 13; i++){
        const electronLocation curLoc = locs[i];
        const std::string curName = electronLocationToString(curLoc);
        std::cout << curName << std::endl;
        for (int j = 0; j < 29; j++){
            const double curEta = etas[j];
            const bool passed = inAcceptance(curLoc, curEta);
            if (passed){
                std::cout << "\t" << curEta;
                std::cout << ": " << passed;
                std::cout << std::endl;
            }
        }
    }
}
