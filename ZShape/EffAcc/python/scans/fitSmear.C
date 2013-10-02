#include "TFile.h"
#include "TH1.h"
#include "TGraph.h"
#include "TKey.h"
#include "TF1.h"
#include "TLegend.h"
#include "TCanvas.h"
#include "TROOT.h"
#include "TFitResult.h"
#include <string>
#include <vector>
#include <algorithm>
/*
 root data.root smeared.root
.L fitSmear.C++
fitSmear(_file0,_file1,0) 
last number=1,-1,0 for hf plus, minus, or not hf
*/
//root data/rereco_zfd_Template/Jan31_rereco_zfd_Template_1552.root data/EB_c_Feb06_1540/ 
struct FitSmearPoint {
  std::string dirName, detName;
  float pointVal;
  int ipt;
  int color;
 
  bool operator<(const FitSmearPoint& fsp) const { return pointVal<fsp.pointVal; }
};

float determineChi2(TFile* f_data, TFile* f_smear,TLegend* t1, const FitSmearPoint& pt,int mode);
TH1* bkgRemover(TH1* h1,int i);

void fitSmear(TFile* f_data, TFile* f_smear,int pm) {
  gROOT->SetStyle("Plain");
  TList* items=f_smear->GetListOfKeys();
  
  
  std::vector<FitSmearPoint> fitPoints;
  
  char detector[100],var[100],val[100],name[100];
  float fval;
  int  colors[20]={1,2,3,4,5,6,7,14,38,30,41,46,49,33,25,11};
  for (int i=0; i<items->GetEntries(); i++) {
    const TKey* itemKey=(const TKey*)(items->At(i));
    sscanf(itemKey->GetName(),"%[^X]X%[^X]X%s",detector,var,val);
    if (strchr(val,'X')!=0) *(strchr(val,'X'))='.';
    if (strchr(val,'m')!=0) *(strchr(val,'m'))='-';
    fval=atof(val);
    FitSmearPoint pt;
    pt.dirName=itemKey->GetName();
    pt.detName=detector;
    pt.pointVal=fval;
    pt.ipt=i;
    //    printf("%d %s %s %f\n",i,detector,var,fval);
    fitPoints.push_back(pt);
  }
  
  std::sort(fitPoints.begin(),fitPoints.end());
  
  // now, we scan the points
  int chi2_n=int(fitPoints.size());
  double chi2_x[100],chi2_y[100];
  
  double chi2_min=0, chi2_max=1;
  
  TCanvas* c2=new TCanvas("c2","c2",700,700);
  TLegend* t1=new TLegend(0.10,0.85,0.4,0.98,"");
  for (int i=0; i<chi2_n; i++) {
    fitPoints[i].ipt=i;
    fitPoints[i].color=colors[i];
    chi2_x[i]=fitPoints[i].pointVal;
    chi2_y[i]=determineChi2(f_data,f_smear,t1,fitPoints[i],pm);
    if (i==0 || chi2_y[i]>chi2_max) chi2_max=chi2_y[i];
    if (i==0 || chi2_y[i]<chi2_min) chi2_min=chi2_y[i];
  }
  sprintf(name,"~/public_html/Jeremy/scans/happy_scan_Overlay_%s_%s.png",detector,var);
  t1->Draw("Same");
  c2->Print(name);
  
  TCanvas* c1=new TCanvas("c1_thing","c1_thing",600,600);
  c1->SetRightMargin(0.02);
  c1->SetTopMargin(0.02);
//   c1->cd();
  TH1* dummy=new TH1F("dummy","",20,chi2_x[0]-(chi2_x[1]-chi2_x[0])*0.25,
		      chi2_x[chi2_n-1]+(chi2_x[chi2_n-1]-chi2_x[chi2_n-2])*0.25);
  dummy->SetDirectory(0);
  dummy->SetMinimum(chi2_min-(chi2_max-chi2_min)*0.05);
  dummy->SetMaximum(chi2_max+(chi2_max-chi2_min)*0.05);
  dummy->SetStats(0);

  if (strstr(var,"mean")) sprintf(val,"%s #bar{x}",detector);
  else sprintf(val,"%s %s",detector,var);
  dummy->GetXaxis()->SetTitle(val);

   dummy->Draw();

  TGraph* tg=new TGraph(chi2_n,chi2_x,chi2_y);
  TFitResultPtr fitRes=tg->Fit("pol2","s");
   tg->Draw("*");
  double bestVal=-fitRes->Parameter(1)/(2*fitRes->Parameter(2));  
  printf("Best fit: %f\n",bestVal);
   sprintf(name,"~/public_html/Jeremy/scans/happy_scan_Chi2_%s_%s_bestfit_%0.3f.png",detector,var,bestVal);
    c1->Print(name);

}


float determineChi2(TFile* f_data, TFile* f_smear, TLegend* t1,const FitSmearPoint& pt,int mode) {
  char smear_h_name[1024];
  char data_h_name[1024];
  char hname[40];
  int bin_low=0, bin_high=120;

  if (pt.detName=="EB") {
    sprintf(smear_h_name,"%s/EB-EB/C06-FULL-WP/Z0_mass_zoom",pt.dirName.c_str());
    sprintf(data_h_name,"ZFromData/EB-EB/C04-WP80/Z0_mass_zoom");
    bin_low=41;
    bin_high=80;
  }
  if (pt.detName=="EE") {
    sprintf(smear_h_name,"%s/EE-EB/C06-FULL-WP/Z0_mass_zoom",pt.dirName.c_str());
    sprintf(data_h_name,"ZFromData/EE-EB/C04-WP80/Z0_mass_zoom");
    bin_low=41;
    bin_high=80;
  }

 if (pt.detName=="HF" && mode == 1) {
    sprintf(smear_h_name,"%s/EE-HF/C07-PT20-HFElectronId-EtaDet/HFpos_mass_zoom",pt.dirName.c_str());
    printf("%s",smear_h_name);
    sprintf(data_h_name,"ZFromData/EE-HF/C04-WP80/HFpos_mass_zoom");
    bin_low=41;
    bin_high=80;
  }else if (pt.detName=="HF" && mode == -1){
    sprintf(smear_h_name,"%s/EE-HF/C07-PT20-HFElectronId-EtaDet/HFneg_mass_zoom",pt.dirName.c_str());
    printf("%s",smear_h_name);
    sprintf(data_h_name,"ZFromData/EE-HF/C04-WP80/HFneg_mass_zoom");
    bin_low=41;
    bin_high=80;
  }else if (pt.detName=="HF" && mode == 0){
    sprintf(smear_h_name,"%s/EE-HF/C08-m(60,120)/Z0_mass_zoom",pt.dirName.c_str());
    printf("%s",smear_h_name);
    sprintf(data_h_name,"ZFromData/EE-HF/C06-m(60,120)/Z0_mass_zoom");
    bin_low=41;
    bin_high=80;
  }

  sprintf(hname,"smear_%d",pt.ipt);
  TH1* smear_h=(TH1*)(f_smear->Get(smear_h_name)->Clone(hname));
  sprintf(hname,"smear_%d_1",pt.ipt);
  TH1* data_h=(TH1*)(f_data->Get(data_h_name)->Clone(hname));
   
  //background remover!!

  //data_h=bkgRemover(data_h,pt.ipt);



  double rescaler=data_h->Integral(bin_low,bin_high)/smear_h->Integral(bin_low,bin_high);
  double chi2=0;
  
  smear_h->Scale(rescaler);
  
  
  for (int ibin=bin_low; ibin<=bin_high; ibin++) {
    double vsmear=smear_h->GetBinContent(ibin);
    double vdata=data_h->GetBinContent(ibin);
    double edata=sqrt(vdata); 
    chi2+=pow(vsmear-vdata,2)/pow(edata,2);
  }
  
  //data_h->Rebin(3);
  //smear_h->Rebin(3);
  smear_h->SetLineColor(pt.color);
  smear_h->SetLineWidth(2);
  
  if (pt.ipt==0) {
    data_h->SetStats(0);
    //  data_h->Rebin(3);
     data_h->Draw("E");
  }
  // smear_h->Rebin(3);
  smear_h->Draw("SAME HIST");
  
  
  t1->AddEntry(smear_h,pt.dirName.c_str());
  
  
  return chi2;
}

TH1* bkgRemover(TH1* h1,int i){
 
  //remove later
  // h1->Rebin(3);
  //end remove
  char name[256];  
 sprintf(name,"c_%i",i);
  TCanvas* c1=new TCanvas(name,"The Heck",600,600);
  c1->cd();
  
  sprintf(name,"clone_%i",i);
  TH1* h2=(TH1*)h1->Clone(name);
  h2->Reset();
 
    TF1 *f1 = new TF1 ("f1","([0]*exp(-0.5*((x-[1])/[2])**2))+(exp([3]+[4]*x))",60,120);
    f1->SetParLimits(0,10,200);
    f1->SetParLimits(1,80,100);
    f1->SetParLimits(2,0.5,10);
    f1->SetParLimits(3,0,100);
    f1->SetParLimits(4,-1,0.001);
    
    
    h1->Fit("f1","R");
    double amp=f1->GetParameter(3);  
    double thing=f1->GetParameter(4);
    
    TF1 *ff2 = new TF1 ("ff2","expo(0)",60,120);
    ff2->SetParameter(0,amp);
    ff2->SetParameter(1,thing);
    // ff2->SetParameter(2,thing);
    // ff=ff2;
  
  ff2->SetLineColor(2);
  ff2->SetLineWidth(2);
  ff2->SetLineStyle(2);
  h2->SetLineColor(2);
  for (int j=1;j<h2->GetNbinsX();j++){
    double bval=ff2->Eval(h2->GetBinCenter(j));
    h2->SetBinContent(j,h1->GetBinContent(j)-bval);
    
  }
  //  if (i==15){
  //     sprintf(name,"c_%i",i);
  //     TCanvas* c1=new TCanvas(name,"The Heck",600,600);
  //     c1->cd();
  //     h1->Draw("Hist");
  //     h2->Draw("same Hist");
  //     ff2->Draw("same");
  //   }
  c1->Close();
  return h2;
}

