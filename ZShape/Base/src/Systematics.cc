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
    // EtaAcceptance accept;
    double scale=1.00000;
    double absEta=std::fabs(electron.detEta_);
    
    //    if (accept.isInAcceptance(electron,EtaAcceptance::zone_EB)) {
    if(absEta<1.4442){
      if(shiftECAL_==0){
	return;
      }else if (shiftECAL_>0){
	scale=1.0+m_scale; 
	energyRescaler(electron,scale);
      }else if (shiftECAL_<0){
	scale=1.0-m_scale;
	energyRescaler(electron,scale);
      }
      //} else if (accept.isInAcceptance(electron,EtaAcceptance::zone_EE)) {
    }else if((absEta>1.566) && (absEta<2.850)){
      if(shiftECAL_==0){
	return;
      }else if (shiftECAL_>0){
	scale=1.0+3*m_scale;
	energyRescaler(electron,scale);
      }else if (shiftECAL_<0){
	scale=1.0-3*m_scale;
	energyRescaler(electron,scale);
      }
      //} else if (accept.isInAcceptance(electron,EtaAcceptance::zone_HF)) {
    }else if((absEta>3.10) && (absEta<4.60)){
      if(shiftHF_==0){
	return;
      }else if (shiftHF_>0){
	scale=1.0+m_scale; 
	energyRescaler(electron,scale);
      }
      else if (shiftHF_<0){
	scale=1.0-m_scale; 
	energyRescaler(electron,scale);
      }
    }
  }
  

   void EnergyScale::energyRescaler(ZShapeElectron& electron,double scale){

     electron.p4_= math::PtEtaPhiMLorentzVector(electron.p4_.Pt()*scale,
						electron.p4_.eta(),
						electron.p4_.phi(),
						electron.p4_.M()*scale);
     
   }
  
  
  PositionScale::PositionScale(double HFdx,double HFdy, double HFrot): hdx_(HFdx),hdy_(HFdy),hdrot_(HFrot){  
  }


  void PositionScale::PositionRescale(ZShapeElectron& electron){//,PositionScale& scale){
    //EtaAcceptance accept;
    double absEta=std::fabs(electron.detEta_);
    if(absEta<1.4442){
      return;
      // if (accept.isInAcceptance(electron,EtaAcceptance::zone_EB)) {
      // PositionScalingEB(electron,scale.hdx_,scale.hdy_,scale.hdrot_);
    }else if((absEta>1.566) && (absEta<2.850)){
      return;
      //} else if (accept.isInAcceptance(electron,EtaAcceptance::zone_EE)) {
      //PositionScalingEE(electron,scale.hdx_,scale.hdy_,scale.hdrot_);
    }else if((absEta>3.10) && (absEta<4.60)){
      
      // } else if (accept.isInAcceptance(electron,EtaAcceptance::zone_HF)) {
      PositionScalingHF(electron,hdx_,hdy_,hdrot_);//scale.hdx_,scale.hdy_,scale.hdrot_);
    }
  }//end posRescale
  
  
  void PositionScale::PositionScalingHF(ZShapeElectron& electron, double dx=0, double dy=0, double drotate=0){
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




//   void PositionScale::PositionScalingEB(ZShapeElectron& electron, double dx=0, double
// 					dy=0, double drotate=0){
//   }
  
//   void PositionScale::PositionScalingEE(ZShapeElectron& electron, double dx=0, double
// 					dy=0, double drotate=0){
//  }
  
}//end namespace


