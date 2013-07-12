#include "EfficiencyTable.h"

EfficiencyTable::EfficiencyTable(const std::string textFile){
    /* Open file */
    std::ifstream inFile(textFile.c_str());
    std::string line;

    /* Loop through lines */
    while( std::getline(inFile, line) ){
        if (line[0] != '#'){ // Skip comments
            std::string item;
            std::vector<std::string> items;
            std::stringstream ss(line);

            effline value;
            ss >> value.xmin;
            ss >> value.xmax;
            ss >> value.etamin;
            ss >> value.etamax;
            ss >> value.pumin;
            ss >> value.pumax;
            ss >> value.nparams;
            ss >> value.eff;
            ss >> value.systp;
            ss >> value.systm;
            ss >> value.den;
            ss >> value.phistar;

            // Kevin's code requires that we add an extra 1 to the ending PU,
            // so we subtract it off here.
            value.pumax -= 1; 

            values_.push_back(value);
        }
    }

    /* Close file */
    inFile.close();

    /* Fill pts_ and pus_ */
    for (std::vector<effline>::const_iterator it = values_.begin(); it != values_.end(); ++it){
        std::pair<double, double> pt(it->xmin, it->xmax);
        std::pair<short, short> pu(it->pumin, it->pumax);
        pts_.insert(pt);
        pus_.insert(pu);
    }
}

double EfficiencyTable::getEff(const double xmin, const double xmax, const double etamin, const double etamax, const short pumin, const short pumax){
    for (std::vector<effline>::const_iterator it = values_.begin(); it != values_.end(); ++it){
        if (    floatEqual_(it->xmin, xmin)
                && floatEqual_(it->xmax, xmax)
                && floatEqual_(it->etamin, etamin)
                && floatEqual_(it->etamax, etamax)
                && it->pumin == pumin
                && it->pumax == pumax
           ) {
            return it->eff;
        }
    }
    return -1.;
}

double EfficiencyTable::getEff(const double x, const electronLocation eLoc, const short pu){
    std::pair<double, double> ept = ptToMinMax_(x);
    std::pair<short, short> epu = puToMinMax_(pu);
    std::pair<double, double> ee = locationToEta_(eLoc);
    return getEff(ept.first, ept.second, ee.first, ee.second, epu.first, epu.second);
}

void EfficiencyTable::print(){
    for (std::vector<effline>::const_iterator it = values_.begin(); it != values_.end(); ++it){
        std::cout << it->xmin << " ";
        std::cout << it->xmax << " ";
        std::cout << it->etamin << " ";
        std::cout << it->etamax << " ";
        std::cout << it->pumin << " ";
        std::cout << it->pumax << " ";
        std::cout << it->nparams << " ";
        std::cout << it->eff << " ";
        std::cout << it->systp << " ";
        std::cout << it->systm << " ";
        std::cout << it->den << " ";
        std::cout << it->phistar << " ";
        std::cout << std::endl;
    }
}

std::pair<double, double> EfficiencyTable::locationToEta_(const electronLocation eLoc){
    switch(eLoc){
        case ET:
            return std::make_pair(-2.5,2.5);
        case EB:
            return std::make_pair(-1.4442, 1.4442);
        case EBp:
            return std::make_pair(0., 1.4442);
        case EBm:
            return std::make_pair(-1.4442, 0.);
        case EE:
        case EEp:
            return std::make_pair(1.566, 2.5);
        case EEm:
            return std::make_pair(-2.5, -1.566);
        case NT:
        case NTp:
            return std::make_pair(2.5, 2.850);
        case NTm:
            return std::make_pair(1.566, 2.5);
        case HF:
        case HFp:
            return std::make_pair(3.1, 4.6);
        case HFm:
            return std::make_pair(-4.6, -3.1);
    }
    return std::make_pair(-1.,-1.);
}

std::pair<double, double> EfficiencyTable::ptToMinMax_(const double pt){
    std::pair<double, double> ept;
    for (std::set<std::pair<double, double> >::const_iterator it = pts_.begin(); it != pts_.end(); ++it){
        if (it->first <= pt && pt <= it->second){
            ept.first = it->first;
            ept.second = it->second;
            return ept;
        }
    }
    ept.first = -1.;
    ept.second = -1.;
    return ept;
}

std::pair<short, short> EfficiencyTable::puToMinMax_(const short pu){
    std::pair<short, short> epu;
    for (std::set<std::pair<short, short> >::const_iterator it = pus_.begin(); it != pus_.end(); ++it){
        if (it->first <= pu && pu <= it->second){
            epu.first = it->first;
            epu.second = it->second;
            return epu;
        }
    }
    epu.first = -1;
    epu.second = -1;
    return epu;
}
