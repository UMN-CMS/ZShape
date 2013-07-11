#include "../ElectronLocation/ElectronLocation.h"

#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <string>
#include <utility>
#include <iostream>

struct effline{
    double xmin;
    double xmax;
    double etamin;
    double etamax ;
    short pumin;
    short pumax;
    short nparams;
    double eff;
    double systp;
    double systm;
    double den;
    bool phistar;
};

class EfficiencyTable {
  public:
    EfficiencyTable(const std::string textFile);
    double getEff(const double xmin, const double xmax, const double etamin, const double etamax, const short pumin, const short pumax);
    double getEff(const double x, const electronLocation eLoc, const short pu);
    void print();

  private:
    std::vector<effline> values_;
    std::set< std::pair<double, double> > pts_;
    std::set< std::pair<short, short> > pus_;
    std::pair<double, double> locationToEta_(const electronLocation eLoc);
    std::pair<double, double> ptToMinMax_(const double pt);
    std::pair<short, short> puToMinMax_(const short pu);
    bool floatEqual_(const double a, const double b, const double delta=0.001){
        return (a > b - delta && a < b + delta);
    }
};
