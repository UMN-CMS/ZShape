#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <TF1.h>
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

class Background {
  public:
    Background(const std::string textFile);
    void setBackground(const double X, const double pu,const  bool usePhiStar);
    Double_t bgFunc(Double_t *v, Double_t *par);
    void print(const bool printAll=true);
    bgNum* current;

  private:
    std::vector<bgNum> values_;
};
