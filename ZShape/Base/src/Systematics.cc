#include "ZShape/Base/interface/Systematics.h"
#include "ZShape/Base/interface/EtaAcceptance.h"
#include <TMath.h>
#include "TVector3.h"
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


  
  PositionScale::PositionScale(double EBeta, double EBphi,double EEeta,double EEphi,double HFdx,double HFdy, double HFrot): hdx_(HFdx),hdy_(HFdy),hdrot_(HFrot){  
  }


  void PositionScale::PositionRescale(ZShapeElectron& electron,PositionScale& scale){
    EtaAcceptance accept;
    if (accept.isInAcceptance(electron,EtaAcceptance::zone_EB)) {
      PositionScalingEB(electron,scale.hdx_,scale.hdy_,scale.hdrot_);
    } else if (accept.isInAcceptance(electron,EtaAcceptance::zone_EE)) {
      PositionScalingEE(electron,scale.hdx_,scale.hdy_,scale.hdrot_);
    } else if (accept.isInAcceptance(electron,EtaAcceptance::zone_HF)) {
      PositionScalingHF(electron,scale.hdx_,scale.hdy_,scale.hdrot_);
    }
  }//end posRescale
  
  //if delta phi, may need to add  pscale=(eta>0)?(+ebpos_[1]):(-ebpos_[1]);
  void PositionScale::PositionScalingHF(ZShapeElectron& electron, double dx=0, double
dy=0, double drotate=0){
    double eta=electron.p4_.eta();
    double phi=electron.p4_.phi();

    double Dist_T_max=11200*TMath::Tan(2.0*TMath::ATan(TMath::Exp(-2.853)));
    double Rotation=TMath::ATan(drotate/Dist_T_max);
    double Dist_T=11200*TMath::Tan(2.0*TMath::ATan(TMath::Exp(-1.*eta)));
    TVector3 vector;
    vector.SetPtEtaPhi(Dist_T, eta, phi);
    vector.SetY(vector.y()+dy);
    vector.SetX(vector.x()+dx);
    vector.RotateZ(Rotation);
    vector.Eta();
    vector.Phi();

    electron.p4_= math::PtEtaPhiMLorentzVector(electron.p4_.Pt(),
					   vector.Eta(),
					   vector.Phi(),
					   electron.p4_.M());
  
  
  }




  void PositionScale::PositionScalingEB(ZShapeElectron& electron, double dx=0, double
					dy=0, double drotate=0){
  }
  
  void PositionScale::PositionScalingEE(ZShapeElectron& electron, double dx=0, double
					dy=0, double drotate=0){
  }
  
}//end namespace


