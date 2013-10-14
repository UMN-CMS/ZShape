#ifndef ZSHAPE_2011EFFCALCULATION_ELECTRONLOCATION_ELECTRONLOCATION_H_
#define ZSHAPE_2011EFFCALCULATION_ELECTRONLOCATION_ELECTRONLOCATION_H_

#include <string>

enum electronLocation{
    ET,
    EB,
    EBp,
    EBm,
    EE,
    EEp,
    EEm,
    NT,
    NTp,
    NTm,
    HF,
    HFp,
    HFm,
    ALL,
};

bool inAcceptance(const electronLocation loc, const double eta);

std::string electronLocationToString(const electronLocation loc);

electronLocation electronLocationToString(const std::string& instr);

#endif // ZSHAPE_2011EFFCALCULATION_ELECTRONLOCATION_ELECTRONLOCATION_H_
