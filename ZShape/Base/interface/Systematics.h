#ifndef ZShape_Base_Systematics_h_included
#define ZShape_Base_Systematics_h_included

#include "ZShapeElectron.h"

namespace zshape {
  
  class EnergyScale {
  public:
    EnergyScale(int ECAL, int HF, bool isEtaDep, double mscale); 
    void rescale(ZShapeElectron& electron);
  private:
    int shiftECAL_,shiftHF_;
    bool isEtaDep_;
    double m_scale;
  };

  class PositionScale {
  public:
    PositionScale(double EBeta, double EBphi,double EEeta,double EEphi,double HFeta,double HFphi);
    void posRescale(ZShapeElectron& electron);
  private:
    double ebpos_[2];
    double eepos_[2];
    double hfpos_[2];
    
  };

}

#endif // ZShape_Base_Systematics_h_included
