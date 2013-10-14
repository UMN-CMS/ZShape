#include "FitterLibrary.h"

#include <sstream>  // std::stringstream
#include <iostream>  // std::cout, std::endl
#include <iomanip>   // std::setw

void getBinEdges(const double minX, const double maxX, const electronLocation probeLoc, std::vector<double>* vec){
    const double z_min = 80.;
    const double z_max = 100.;
    double ss_peak;
    double ss_tail;
    switch (probeLoc){
        case EB:
        case EBp:
        case EBm:
            ss_peak = 2;
            ss_tail = 2;
            break;
        case EE:
        case EEp:
        case EEm:
        case ET:
        case NT:
        case NTp:
        case NTm:
        case HF:
        case HFp:
        case HFm:
            ss_peak = 2;
            ss_tail = 2;
            break;
    }

    double cur = minX;
    while (true){
        vec->push_back(cur);
        if (cur >= z_min && cur < z_max){
            cur = cur + ss_peak;
        } else if (cur < z_min || cur >= z_max){
            cur = cur + ss_tail;
        }
        if (cur >= maxX){
            break;
        }
    }
}

Efficiencies EffFromCounting(TH1D* baseData,  TH1D*  postData,  TH1D * baseBG,  TH1D* postBG, const double baseE, const double postE, const double minMZ, const double maxMZ){
    /*
     * postD = postData count
     * postP = postData param
     * postB = postBackground count
     * postDerr = postData count error
     * postE = postBackground count error
     */
    Efficiencies tmp;
    const double baseD = baseData->Integral(baseData->FindBin(minMZ), baseData->FindBin(maxMZ));
    const double postD = postData->Integral(postData->FindBin(minMZ), postData->FindBin(maxMZ));
    const double baseB = baseBG->Integral(baseBG->FindBin(minMZ), baseBG->FindBin(maxMZ));
    const double postB = postBG->Integral(postBG->FindBin(minMZ), postBG->FindBin(maxMZ));
    const double baseDerr = sqrt(baseD);
    const double postDerr = sqrt(postD);

    tmp.eff = (postD - postB) / (baseD - baseB);
    /* Note: dEff = Eff * Sqrt((da^2+db^2)/(a-b)^2 + (dc^2-dd^2)/(c-d)^2) */
    tmp.err = tmp.eff * sqrt(
            ( ( postE * postE ) + ( postDerr * postDerr ) ) / ( ( postD - postB ) * ( postD - postB ) )
            +  ( ( baseE * baseE ) + (baseDerr * baseDerr ) ) / ( ( baseD - baseB ) * ( baseD - baseB ) )
            );

    return tmp;
}

Efficiencies EffFromSignal( TH1D*  baseSig,  TH1D*  postSig, const double baseE, const double postE, const double minMZ, const double maxMZ){
    Efficiencies tmp;
    double baseS = baseSig->Integral(baseSig->FindBin(minMZ), baseSig->FindBin(maxMZ));
    double postS = postSig->Integral(postSig->FindBin(minMZ), postSig->FindBin(maxMZ));

    tmp.eff = postS / baseS;
    tmp.err = tmp.eff * sqrt( (baseE * baseE)/(baseS * baseS) + (postE * postE) / (postS * postS) );

    // TODO: Double check formula
    return tmp;
}

void PrintEffs(const electronLocation probeLoc, const EffBin effbin, const double sigeff, const double counteff, const double denom, const bool usePhiStar){
    /* Prints probewp ptmin ptmax etamin etamax pumin pumax sigeff sigerr counteff counterr */
    using namespace std;
    stringstream ss;
    ss << "#XMin XMax EtaMin  EtaMax  PUMin PUMax NumParms eff       systp     systm     den     phistar" << endl;
    ss << left << setw(6) << effbin.minX;
    ss << left << setw(5) << effbin.maxX ;
    switch (probeLoc){
        case EB:
            ss << left << setw(8) << -1.4442;
            ss << left << setw(8) << 1.4442;
            break;
        case EBp:
            ss << left << setw(8) << 0;
            ss << left << setw(8) << 1.4442;
            break;
        case EBm:
            ss << left << setw(8) << -1.4442;
            ss << left << setw(8) << 0;
            break;
        case EE:
            ss << left << setw(8) << 1.566;
            ss << left << setw(8) << 2.5;
            break;
        case EEp:
            ss << left << setw(8) << 1.566;
            ss << left << setw(8) << 2.5;
            break;
        case EEm:
            ss << left << setw(8) << -2.5;
            ss << left << setw(8) << -1.566;
            break;
        case ET:
            ss << left << setw(8) << -2.5;
            ss << left << setw(8) << 2.5;
            break;
        case NT:
            ss << left << setw(8) << 2.5;
            ss << left << setw(8) << 2.850;
            break;
        case NTp:
            ss << left << setw(8) << 2.5;
            ss << left << setw(8) << 2.850;
            break;
        case NTm:
            ss << left << setw(8) << -2.850;
            ss << left << setw(8) << -2.5;
            break;
        case HF:
            ss << left << setw(8) << 3.1;
            ss << left << setw(8) << 4.6;
            break;
        case HFp:
            ss << left << setw(8) << 3.1;
            ss << left << setw(8) << 4.6;
            break;
        case HFm:
            ss << left << setw(8) << -4.6;
            ss << left << setw(8) << -3.1;
            break;
    }
    ss << left << setw(6) << effbin.minPU;
    ss << left << setw(6) << effbin.maxPU + 1; // Kevin's Code requires 0-4 inclusive to report 0-5
    ss << left << setw(9) << "5"; // Number of params
    const double diff = fabs(sigeff - counteff)/2.;
    const double avg = fabs(sigeff + counteff)/2.;
    ss << left << setw(10) << avg;
    ss << left << setw(10) << avg+diff;
    ss << left << setw(10) << avg-diff;
    ss << left << setw(8) << denom;
    ss << left << setw(8) << usePhiStar << endl;
    // Output the String Stream
    cout << ss.str() << flush;
}
