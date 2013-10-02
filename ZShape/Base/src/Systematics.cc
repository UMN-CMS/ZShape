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

    if (accept.isInAcceptance(electron,EtaAcceptance::zone_EB)) {
      if (shiftECAL_>0)         isEtaDep_   ?   (scale=1+0.002*absEta/1.50)   : (scale=1.0+m_scale);//restore by setting m_scale to 1
      else if (shiftECAL_<0)    isEtaDep_   ?   (scale=1-0.002*absEta/1.50)   : (scale=1.0-m_scale);
    } else if (accept.isInAcceptance(electron,EtaAcceptance::zone_EE)) {
      if (shiftECAL_>0)         isEtaDep_   ?   (scale=1.002+0.015*(absEta-1.50))   : (scale=1.0+3*m_scale);
      else if (shiftECAL_<0)    isEtaDep_   ?   (scale=0.998-0.015*(absEta-1.50))   : (scale=1.0-3*m_scale);
    } else if (accept.isInAcceptance(electron,EtaAcceptance::zone_HF)) {
      if (shiftHF_>0) scale=1.0+10*m_scale; 
      else if (shiftHF_<0) scale=1.0-10*m_scale; 
    }

    electron.p4_= math::PtEtaPhiMLorentzVector(electron.p4_.Pt()*scale,
					       electron.p4_.eta(),
					       electron.p4_.phi(),
					       electron.p4_.M()*scale);

  }


  
  PositionScale::PositionScale(double EBeta, double EBphi,double EEeta,double EEphi,double HFeta,double HFphi){  ebpos_[0]=(EBeta);ebpos_[1]=(EBphi); eepos_[0]=(EEeta);eepos_[1]=(EEphi);hfpos_[0]=(HFeta);hfpos_[1]=(HFphi);
  }


  void PositionScale::posRescale(ZShapeElectron& electron){
    EtaAcceptance accept;
   double escale=0;
    double pscale=0;
    if (accept.isInAcceptance(electron,EtaAcceptance::zone_EB)) {
      escale=ebpos_[0];
      pscale= ebpos_[1];
    } else if (accept.isInAcceptance(electron,EtaAcceptance::zone_EE)) {
      escale=eepos_[0];
      pscale= eepos_[1];
    } else if (accept.isInAcceptance(electron,EtaAcceptance::zone_HF)) {
      escale=hfpos_[0];
      pscale= hfpos_[1];
      
    }
    electron.p4_= math::PtEtaPhiMLorentzVector(electron.p4_.Pt(),
					       electron.p4_.eta()+escale,
					       electron.p4_.phi()+pscale,
					       electron.p4_.M());
    
  }//end posRescale
  
  //if delta phi, may need to add  pscale=(eta>0)?(+ebpos_[1]):(-ebpos_[1]);
  
  
}//end namespace
