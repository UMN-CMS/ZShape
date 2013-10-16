#include "ZShape/Base/interface/Systematics.h"
#include "ZShape/Base/interface/EtaAcceptance.h"

namespace zshape {
  

  EnergyScale::EnergyScale(int ecal, int HF, bool isEtaDep,double mscale) : shiftECAL_(ecal), shiftHF_(HF) , isEtaDep_(isEtaDep),m_scale(mscale){
  }
  // the sign of ecal and HF determine whether scale variation is up or down
  // the scale variation is global (isEtaDep=false) or eta-dependent (isEtaDep=true); always global for HF
  // eta-dependent: 0.2% linear with eta along EB, 1.5% further along TK-covered-EE

  void EnergyScale::rescale(ZShapeElectron& electron) {
    EtaAcceptance accept;
    double scale=1.0;
    double absEta=std::fabs(electron.detEta_);

    bool gotshift=false;

    if (accept.isInAcceptance(electron,EtaAcceptance::zone_EB)) {
      gotshift=true;
      if (shiftECAL_>0)         isEtaDep_   ?   (scale=1+0.002*absEta/1.50)   : (scale=1.0+m_scale);//restore by setting m_scale to 1
      else if (shiftECAL_<0)    isEtaDep_   ?   (scale=1-0.002*absEta/1.50)   : (scale=1.0-m_scale);
      else gotshift=false;
    } else if (accept.isInAcceptance(electron,EtaAcceptance::zone_EE)) {
      gotshift=true;
      if (shiftECAL_>0)         isEtaDep_   ?   (scale=1.002+0.015*(absEta-1.50))   : (scale=1.0+3*m_scale);
      else if (shiftECAL_<0)    isEtaDep_   ?   (scale=0.998-0.015*(absEta-1.50))   : (scale=1.0-3*m_scale);
      else gotshift=false;
    } else if (accept.isInAcceptance(electron,EtaAcceptance::zone_HF)) {
      gotshift=true;
      if (shiftHF_>0) scale=1.0+10*m_scale; 
      else if (shiftHF_<0) scale=1.0-10*m_scale; 
      gotshift=false;
    }

    if (gotshift) 
      electron.p4_= math::PtEtaPhiMLorentzVector(electron.p4_.Pt()*scale,
						 electron.p4_.eta(),
						 electron.p4_.phi(),
						 electron.p4_.M()*scale);

  }

}
