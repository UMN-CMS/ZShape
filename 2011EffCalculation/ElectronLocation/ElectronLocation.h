#include <math.h>

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

bool inAcceptance(const electronLocation Loc, const double eta);

#endif
