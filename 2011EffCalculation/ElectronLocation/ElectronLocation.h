#include <math.h>
#include <string>

#ifndef ELECTRONLOCATION_H
#define ELECTRONLOCATION_H

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
    HFm
};

bool inAcceptance(const electronLocation loc, const double eta);

std::string electronLocationToString(const electronLocation loc);

#endif
