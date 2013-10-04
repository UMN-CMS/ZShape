#ifndef ELECTRONLOCATION_H
#define ELECTRONLOCATION_H

#include <math.h>
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
    ALL
};

bool inAcceptance(const electronLocation loc, const double eta);

std::string electronLocationToString(const electronLocation loc);

#endif
