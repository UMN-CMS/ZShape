#ifndef ZShape_Base_Systematics_h_included
#define ZShape_Base_Systematics_h_included

#include "ZShapeElectron.h"

namespace zshape {
  
  class EnergyScale {
  public:
    EnergyScale(int ECAL, int HF, bool isEtaDep, double mscale); 
    void rescale(ZShapeElectron& electron);
    void energyRescaler(ZShapeElectron& electron,double scale);
  private:
    int shiftECAL_,shiftHF_;
    bool isEtaDep_;
    double m_scale;
  };

  class PositionScale {
  public:
    PositionScale(double HFdx,double HFdy, double HFrot);
    void PositionRescale(ZShapeElectron& electron);//,PositionScale& scale);
    void PositionScalingHF(ZShapeElectron& electron, double dx, double dy, double drotate);
    void PositionScalingEB(ZShapeElectron& electron, double dx, double dy, double drotate);
    void PositionScalingEE(ZShapeElectron& electron, double dx, double dy, double drotate);
  private:
    double bdx_,bdy_,bdrot_;
    double edx_,edy_,edrot_;
    double hdx_,hdy_,hdrot_;
  };

}

#endif // ZShape_Base_Systematics_h_included
