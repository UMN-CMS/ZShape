#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <TMath.h>

struct bgNum{
    double minX;
    double maxX;
    int minPU;
    int maxPU;
    double minMZ;
    double maxMZ;
    int nparm;
    double alpha;
    double beta;
    double gamma;
    double delta;
    bool isPhiStar;
};

class BackgroundTable {
  public:
    BackgroundTable(const std::string textFile);
    void setBackground(const double X, const double pu,const  bool usePhiStar);
    double bgFunc(const double *v, const double *par);
    void print(const bool printAll=true);
    bgNum* current;

  private:
    std::vector<bgNum> values_;
};
