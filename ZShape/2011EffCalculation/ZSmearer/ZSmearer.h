#ifndef ZSHAPE_2011EFFCALCULATION_ZSMEARER_ZSMEARER_H_
#define ZSHAPE_2011EFFCALCULATION_ZSMEARER_ZSMEARER_H_

#include "../../MakeZEffTree/src/ZEffTree.h"  // ZEffTree::ZInfo
#include <TRandom.h>  // TRandom

void smearEvent(TRandom* trand, ZEffTree::ZInfo* zi);
void smearEvent(TRandom* trand, const double mean, const double sigma, ZEffTree::ZInfo* zi);
void smearEvent(TRandom* trand, const double mean0, const double sigma0, const double mean1, const double sigma1, ZEffTree::ZInfo* zi);

#endif  // ZSHAPE_2011EFFCALCULATION_ZSMEARER_ZSMEARER_H_ 
