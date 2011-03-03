#include "ZShape/EffAcc/interface/EffHistos.h"
#include "ZShape/Base/interface/ZShapeBinning.h"

typedef math::XYZTLorentzVector XYZTLorentzVector;

// for reference
// $ROOTSYS/include/Math/GenVector/LorentzVector.h

void EffHistos::Book(TFileDirectory& tdf,bool mzbin) {

  booked_=true;
  massFinals_=mzbin;

  // add here all extremes, tidily
  const float pi       = 3.141593;
  const float maxPt    = 400;
  const float minZmass = 50;
  const float maxZmass = 150;
  const int   binsZmass  = 50;

  const double ZmassBins[]={ 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
			    51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 
			    71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
			    91, 92, 93, 94, 95, 96, 97, 98, 99,100,101,102,103,104,105,106,107,108,109,110,
			    111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,
			    131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150};

//  float detetaBins[104] = {-5., -4.9, -4.8, -4.7, -4.6, -4.5, -4.4, -4.3, -4.2, -4.1, -4., -3.9, -3.8, -3.7, -3.6,  //14
//                       -3.5, -3.4, -3.3,  -3.2, -3.1, -3., //6
//                       -2.9, -2.8, -2.7, -2.6, -2.5, -2.4, -2.3, -2.2, -2.1, -2.0, -1.89, -1.78, -1.67,  //13
//                       -1.56, -1.4442, -1.35, -1.257, -1.163, -1.127,  -1.02, -0.913, -0.806, -0.770,  //10
//                       -0.667, -.564, -0.461, -0.423, -0.32, -0.22, -0.12, -0.018, 0.018, 0.12, 0.22, 0.32,  0.423, 0.461, 0.564,0.667, //16
//                       0.770, 0.806, 0.913, 1.02, 1.127, 1.163,  1.257, 1.35, 1.4442, //9
//                       1.56, 1.67, 1.78, 1.89, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, //14
//                       3., 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, //10
//                       4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5. }; //11
 
  mZ_  = tdf.make<TH1F>("Z0_mass","Z0_mass;m_{Z} (GeV/c^{2})", binsZmass, minZmass, maxZmass);
  YZ_  = tdf.make<TH1F>("Z0_Y","Z0_Y;Y_{Z0}", zshape::y_bins, -zshape::y_max, zshape::y_max);
  ptZ_  = tdf.make<TH1F>("Z0_Pt","Z0_Pt;p_{T,Z0}", zshape::pt_bins, zshape::pt_binning);
  ptZmon_ = tdf.make<TH1F>("Z0_PtMon","Z0_PtMon;p_{T,Z0}", 200, 0, maxPt);

  YZmasscut_  = tdf.make<TH1F>("Z0_Y_masscut","Z0_Y_masscut;Y_{Z0}", zshape::y_bins, -zshape::y_max, zshape::y_max);
  ptZmasscut_  = tdf.make<TH1F>("Z0_Pt_masscut","Z0_Pt_masscut;p_{T,Z0}", zshape::pt_bins, zshape::pt_binning);

  mZTL_  = tdf.make<TH1F>("Z0_massTL","Z0_M Tree Level;m_{Z0} (GeV/c^{2})", 50, minZmass, maxZmass);
  YZTL_  = tdf.make<TH1F>("Z0_YTL","Z0_Y Tree Level;Y_{Z0}", zshape::y_bins, -zshape::y_max, zshape::y_max);
  ptZTL_  = tdf.make<TH1F>("Z0_PtTL","Z0_PtTL;p_{T,Z0}", zshape::pt_bins, zshape::pt_binning); 
  ptZTLmon_ = tdf.make<TH1F>("Z0_PtTLMon","Z0_Pt Tree Level Mon;p_{T,Z0}", 200, 0, maxPt);

  YZTLmasscut_  = tdf.make<TH1F>("Z0_YTL_masscut","Z0_Y Tree Level_masscut;Y_{Z0}", zshape::y_bins, -zshape::y_max, zshape::y_max);
  ptZTLmasscut_  = tdf.make<TH1F>("Z0_PtTL_masscut","Z0_PtTL_masscut;p_{T,Z0}", zshape::pt_bins, zshape::pt_binning); 

  YZmasscutTL_  = tdf.make<TH1F>("Z0_Y_masscutTL","Z0_Y masscutTL;Y_{Z0}", zshape::y_bins, -zshape::y_max, zshape::y_max);
  ptZmasscutTL_  = tdf.make<TH1F>("Z0_Pt_masscutTL","Z0_Pt masscutTL;p_{T,Z0}", zshape::pt_bins, zshape::pt_binning); 

  
  e1eta_ = tdf.make<TH1F>("e1_eta","e1_eta;detector #eta_{e1}", 50, -5, 5);
  e2eta_ = tdf.make<TH1F>("e2_eta","e2_eta;detector #eta_{e2}", 50, -5, 5);
  eeta_ = tdf.make<TH1F>("e_eta","e_eta;detector #eta_{e}", 50, -5, 5);
  e1phi_ = tdf.make<TH1F>("e1_phi","e1_phi;#phi_{e1}", 50, -pi, pi);
  e2phi_ = tdf.make<TH1F>("e2_phi","e2_phi;#phi_{e2}", 50,  -pi, pi);
  ephi_ = tdf.make<TH1F>("e_phi","e_phi;#phi_{e}", 50,  -pi, pi);
  e1pt_  = tdf.make<TH1F>("e1_P_t","e1_P_t;p_{T,e1}", 200, 0, maxPt);
  e2pt_  = tdf.make<TH1F>("e2_P_t","e2_P_t;p_{T,e2}", 200, 0, maxPt);

  hfeta_ = tdf.make<TH1F>("hf_eta","hf_eta;|#eta|",13*7,3.0,5.0);
 
  //Now make the 2-D histograms

  mZ_Y_ = tdf.make<TH2F>("Z0_Y_v_mass","Z0_Y_v_mass;Y_{Z0};m_{Z0}", zshape::y_bins, -zshape::y_max, zshape::y_max, 3*binsZmass, minZmass-10, maxZmass);
  pt_Y_ = tdf.make<TH2F>("Z0_Y_v_pt","Z0_Y_v_pt;Y_{Z0};p_{T,Z0}", zshape::y_bins, -zshape::y_max, zshape::y_max, zshape::pt_bins, zshape::pt_binning);
  mZ_pt_ = tdf.make<TH2F>("Z0_pt_v_mass","Z0_pt_v_mass;p_{T,Z0};m_{Z0}", zshape::pt_bins,zshape::pt_binning,3*binsZmass, minZmass-10, maxZmass-10);

  e1eta_YZ_    = tdf.make<TH2F>("e1_eta_vs_Z0Y","e1_eta_vs_Z0Y;detector #eta_{e1};Y_{Z0}", 50, -5, 5,zshape::y_bins, -zshape::y_max, zshape::y_max );
  e2eta_YZ_    = tdf.make<TH2F>("e2_eta_vs_Z0Y","e2_eta_vs_Z0Y;detector #eta_{e2};Y_{Z0}", 50, -5, 5,zshape::y_bins, -zshape::y_max, zshape::y_max );
  e1eta_ptZ_   = tdf.make<TH2F>("e1_eta_vs_Ptz","e1_eta_vs_PtZ;detector #eta_{e1};p_{T,Z0}", 50, -5, 5, zshape::pt_bins, zshape::pt_binning);
  e2eta_ptZ_   = tdf.make<TH2F>("e2_eta_vs_Ptz","e2_eta_vs_PtZ;detector #eta_{e2};p_{T,Z0}", 50, -5, 5,zshape::pt_bins, zshape::pt_binning);
  e1eta_e2eta_ = tdf.make<TH2F>("e1_eta_vs_e2_eta","e1_eta_vs_e2_eta;detector #eta_{e1};detector #eta_{e2}", 50, -5, 5,50, -5, 5 );
 
  YZTL_YZ_       = tdf.make<TH2F>("YZTL_vs_YZ","YZTL_vs_YZ;Y_{Z};Y_{ZtreeLevel}",zshape::y_bins,-zshape::y_max,zshape::y_max,zshape::y_bins,-zshape::y_max,zshape::y_max); 
  YZTL_YZ_matrix_= tdf.make<TH2F>("YZTL_vs_YZ_matrix","YZTL_vs_YZ_matrix;Y_{Z};Y_{ZtreeLevel}",zshape::y_bins,-zshape::y_max,zshape::y_max,zshape::y_bins,-zshape::y_max,zshape::y_max); 

  ptZTL_ptZ_       = tdf.make<TH2F>("PtTL_vs_PtZ","PtZTL_vs_PtZ;Pt_{Z};Pt_{ZtreeLevel}",zshape::pt_bins, zshape::pt_binning,zshape::pt_bins, zshape::pt_binning); 
  ptZTL_ptZ_zoom_  = tdf.make<TH2F>("PtTL_vs_PtZ_zoom","PtZTL_vs_PtZ_zoom;Pt_{Z};Pt_{ZtreeLevel}",25,0.0,25.0,25,0.0,25.0);

  //Now make the 2-D histogram
  //  mZ_e2pt_e2eta_ = tdf.make<TH3F>("Z0_mass_vs_e2_pt_vs_e2_eta","Z0_mass_vs_e2_pt_vs_e2_eta;p_{T,e2};#eta_{e2};m_{Z0}", zshape::e_pt_bins,zshape::e_pt_binning,zshape::e_eta_bins,zshape::e_eta_binning,110, ZmassBins );

  if (massFinals_) {
    mZ_binned_finals.e1eta_ = tdf.make<TH2F>("mZ_vs_e1_eta","mZ_vs_e1_eta;detector #eta_{e1};m_{ee}", 50, -5, 5,55,40,150);
    mZ_binned_finals.e2eta_ = tdf.make<TH2F>("mZ_vs_e2_eta","mZ_vs_e2_eta;detector #eta_{e2};m_{ee}", 50, -5, 5,55,40,150);
    mZ_binned_finals.hfeta_ = tdf.make<TH2F>("mZ_vs_hfeta","mZ_vs_hf_eta;detector #eta_{e};m_{ee}", 13*7, 3.0, 5.0,55,40,150);
    mZ_binned_finals.e1phi_ = tdf.make<TH2F>("mZ_vs_e1_phi","mZ_vs_e1_phi;#phi_{e1};m_{ee}", 50, -pi, pi,55,40,150);
    mZ_binned_finals.e2phi_ = tdf.make<TH2F>("mZ_vs_e2_phi","mZ_vs_e2_phi;#phi_{e2};m_{ee}", 50,  -pi, pi,55,40,150);
    mZ_binned_finals.e1pt_  = tdf.make<TH2F>("mZ_vs_e1_P_t","mZ_vs_e1_P_t;p_{T,e1};m_{ee}", 200, 0, maxPt,55,40,150);
    mZ_binned_finals.e2pt_  = tdf.make<TH2F>("mZ_vs_e2_P_t","mZ_vs_e2_P_t;p_{T,e2};m_{ee}", 200, 0, maxPt,55,40,150);
  }

  //Now mkae some Event histograms
  evt_PVz_ =  tdf.make<TH1F>("evt_PVz","PV_z;PV_{z}", 50, -20,20);
  evt_BSz_ =  tdf.make<TH1F>("evt_BSz","BS_z;PBS{z}", 50, -1.5,3);
  evt_MET_ =  tdf.make<TH1F>("evt_MET","Calo MET;MET", 50, 0,100);
  evt_TCMET_ =  tdf.make<TH1F>("evt_TCMET","tcMET;tcMET", 50, 0,100);
  evt_PFMET_ =  tdf.make<TH1F>("evt_PFMET","pfMET;pfMET", 50, 0,100);


} 

void EffHistos::Fill(const  ZShapeElectron& e1, const  ZShapeElectron& e2, 
		     const ::math::PtEtaPhiMLorentzVector& eTL1, const ::math::PtEtaPhiMLorentzVector& eTL2, double wgt, bool doMC) { 

  if (!booked_) {
    std::cerr << "Attempt to fill without booking!\n";
    return;
  }

  
  XYZTLorentzVector p1(e1.p4_);
  XYZTLorentzVector p2(e2.p4_);

  XYZTLorentzVector pTL1(eTL1); 
  XYZTLorentzVector pTL2(eTL2); 

  XYZTLorentzVector pZ = p1 + p2 ;
  XYZTLorentzVector pTLZ = pTL1 + pTL2 ; 

  //  debug
  //  std::cout << "this is e1:"  << p1 << std::endl;
  //  std::cout << "this is e2:"  << p2 << std::endl;
  //  std::cout << "this is Z:"  << pZ << std::endl;
  //  float rapidity = 0.5 * log( ( pZ.E()+pZ.Pz() ) / ( pZ.E()-pZ.Pz() ) );  
  //  std::cout << "rapidity calculated: " << rapidity  << " while from method: " << pZ.Rapidity() << std::endl;
  //   rapidity = 0.5 * log( ( pTLZ.E()+pTLZ.Pz() ) / ( pTLZ.E()-pTLZ.Pz() ) );   
  //   std::cout << "rapidity calculated: " << rapidity  << " while from method: " << pTLZ.Rapidity() << std::endl;

  float zMass = sqrt ( pZ.Dot(pZ) );
  float zY    = pZ.Rapidity();
  float zPt   = pZ.Pt();

  float e1eta = e1.detEta_;
  float e1phi = p1.Phi();
  float e1Pt  = p1.Pt();
  
  float e2eta = e2.detEta_;
  float e2phi = p2.Phi();
  float e2Pt  = p2.Pt();

  float zTLMass = sqrt ( pTLZ.Dot(pTLZ) );
  float zTLY    = pTLZ.Rapidity();
  float zTLPt   = pTLZ.Pt();
  

  mZ_  -> Fill(zMass,wgt);
  YZ_  -> Fill(zY,wgt);
  ptZ_ -> Fill(zPt,wgt);
  
  if (zMass >= massWindowLow_ && zMass < massWindowHigh_) {
    YZmasscut_  -> Fill(zY,wgt);
    ptZmasscut_ -> Fill(zPt,wgt);    

    // tree level rapidity VS fast reco-ed rapidity 
    if (doMC && zTLMass >= massWindowLow_ && zTLMass <=massWindowHigh_){
      YZTL_YZ_ -> Fill(zY,zTLY,wgt); 
      ptZTL_ptZ_  -> Fill(zPt,zTLPt,wgt); 
      ptZTL_ptZ_zoom_  -> Fill(zPt,zTLPt,wgt); 
    }
  }

  ptZmon_ -> Fill(zPt,wgt);

  if (doMC) 
    {
      mZTL_  -> Fill(zTLMass,wgt);
      YZTL_  -> Fill(zTLY,wgt);
      ptZTL_-> Fill(zTLPt,wgt);
      ptZTLmon_ -> Fill(zTLPt,wgt);

      if (zTLMass >= massWindowLow_ && zTLMass <=massWindowHigh_) {
	YZTLmasscut_  -> Fill(zTLY,wgt);
	ptZTLmasscut_ -> Fill(zTLPt,wgt);    
	YZmasscutTL_  -> Fill(zY,wgt);
	ptZmasscutTL_ -> Fill(zPt,wgt);    
      }
   
    }
  e1eta_ -> Fill(e1eta,wgt);
  e1pt_  -> Fill(e1Pt,wgt);
  e1phi_ -> Fill(e1phi,wgt);

  e2eta_ -> Fill(e2eta,wgt);
  e2pt_  -> Fill(e2Pt,wgt);
  e2phi_ -> Fill(e2phi,wgt);

  eeta_ -> Fill(e1eta,wgt);
  eeta_ -> Fill(e2eta,wgt);
  ephi_ -> Fill(e1phi,wgt);
  ephi_ -> Fill(e2phi,wgt);

  if (fabs(e1eta)>3.0 && fabs(e1eta)<5.0)
    hfeta_ -> Fill(fabs(e1eta),wgt);
  if (fabs(e2eta)>3.0 && fabs(e2eta)<5.0)
    hfeta_ -> Fill(fabs(e2eta),wgt);

  
  //Now Fill the 2-D Histograms
  mZ_Y_->Fill(zY,zMass,wgt);
  mZ_pt_->Fill(zPt,zMass,wgt);
  pt_Y_->Fill(zY,zPt,wgt);
  
  e1eta_YZ_  -> Fill(e1eta,zY,wgt);
  e2eta_YZ_  -> Fill(e2eta,zY,wgt);
  e1eta_ptZ_ -> Fill(e1eta,zPt,wgt);
  e2eta_ptZ_ -> Fill(e2eta,zPt,wgt);
  
  e1eta_e2eta_ -> Fill(e1eta,e2eta,wgt);

  //Now Fill the 3-D Histogram
  //  mZ_e2pt_e2eta_ -> Fill(e2Pt,e2eta,zMass,wgt);

  if (massFinals_) {
    mZ_binned_finals.e1eta_ -> Fill(e1eta,zMass,wgt);
    mZ_binned_finals.e1pt_  -> Fill(e1Pt,zMass,wgt);
    mZ_binned_finals.e1phi_ -> Fill(e1phi,zMass,wgt);

    mZ_binned_finals.e2eta_ -> Fill(e2eta,zMass,wgt);
    mZ_binned_finals.e2pt_  -> Fill(e2Pt,zMass,wgt);
    mZ_binned_finals.e2phi_ -> Fill(e2phi,zMass,wgt);

    if (fabs(e2eta)>3.0 && fabs(e2eta)<5.0)
      mZ_binned_finals.hfeta_ -> Fill(fabs(e2eta),zMass,wgt);
    
  }

}


void EffHistos::WrapUp(){ 

  if( YZTL_YZ_==0 &&  YZTL_YZ_matrix_==0) return; 

  if (!booked_) {
    std::cerr << "Attempt to finish without booking!\n";
    return;
  }
 
  int numBinX =  YZTL_YZ_ ->GetNbinsX(); 
  int numBinY =  YZTL_YZ_ ->GetNbinsY(); 
   
  // filling migration matricex with by normalixing migration histograms 
  float integral; 
  for (int binY=1; binY<=numBinY; binY++) 
    { 
      integral=0; 
      for (int binX=1; binX<=numBinX; binX++) 
	{   integral += YZTL_YZ_->GetBinContent(binX,binY); } 
     
      if (integral==0) continue; 
      for (int binX=1; binX<=numBinX; binX++) 
	{   YZTL_YZ_matrix_->SetBinContent(binX,binY,   YZTL_YZ_->GetBinContent(binX,binY) / integral); } 
 
    } 
  
  // debug 
  //    std::cout << "\n num entries HIS: " << numBinX << " " << numBinY << " " << YZTL_YZ_->GetEntries() << std::endl; 
  //    std::cout << "\n num entries MATR: " << YZTL_YZ_matrix_->GetNbinsX() << " " << YZTL_YZ_matrix_->GetNbinsY()  
  //        << " " << YZTL_YZ_matrix_->GetEntries() << std::endl; 
  
} 

void EffHistos::FillEvt(const  ZShapeEvent& zevt, bool justPV) { 

  if (!booked_) {
    std::cerr << "Attempt to fill without booking!\n";
    return;
  }
  if (justPV )evt_PVz_->Fill(zevt.vtx_.z()/10.);
  else {
    evt_PVz_->Fill(zevt.EvtPVz()); 
    evt_BSz_->Fill(zevt.EvtBSz()); 
    evt_MET_->Fill(zevt.EvtMET()); 
    evt_TCMET_->Fill(zevt.EvtTCMET());    
    evt_PFMET_->Fill(zevt.EvtPFMET());  
  }
}
