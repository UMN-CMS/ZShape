#include "TFile.h"
#include "TH1.h"
#include "TGraph.h"
#include "TKey.h"
#include "TCanvas.h"
#include "TROOT.h"
#include "TFitResult.h"
#include <string>
#include <vector>
#include <algorithm>

struct FitSmearPoint {
  std::string dirName, detName;
  float pointVal;
  int ipt;
  bool operator<(const FitSmearPoint& fsp) const { return pointVal<fsp.pointVal; }
};

float determineChi2(TFile* f_data, TFile* f_smear, const FitSmearPoint& pt,int mode);

void hffitSmear(TFile* f_data, TFile* f_smear, int mode) {
  int yell=0;
 gROOT->SetStyle("Plain");
 printf("hello\n");
  TList* items=f_smear->GetListOfKeys();
 printf("found keys\n");


  std::vector<FitSmearPoint> fitPoints;

  char detector[100],var[100],val[100];
  float fval;

  for (int i=0; i<items->GetEntries(); i++) {
    printf("in loop %i\n",yell);yell++;

    const TKey* itemKey=(const TKey*)(items->At(i));
    sscanf(itemKey->GetName(),"%[^X]X%[^X]X%s",detector,var,val);
    if (strchr(val,'X')!=0) *(strchr(val,'X'))='.';
    fval=atof(val);
    FitSmearPoint pt;
    pt.dirName=itemKey->GetName();
    pt.detName=detector;
    pt.pointVal=fval;
    pt.ipt=i;
    printf("hey yo %d %s %s %f\n",i,detector,var,fval);
    fitPoints.push_back(pt);
  }
  printf("out of loop\n");

  std::sort(fitPoints.begin(),fitPoints.end());
  printf("sorted\n");

  // now, we scan the points
  int chi2_n=int(fitPoints.size());
  double chi2_x[100],chi2_y[100];
  printf("points and stuf\n");
  double chi2_min=0, chi2_max=1;

  TCanvas* c2=new TCanvas("c2","c2",700,700);

  for (int i=0; i<chi2_n; i++) {
    fitPoints[i].ipt=i;
    chi2_x[i]=fitPoints[i].pointVal;
    chi2_y[i]=determineChi2(f_data,f_smear,fitPoints[i],mode);
    if (i==0 || chi2_y[i]>chi2_max) chi2_max=chi2_y[i];
    if (i==0 || chi2_y[i]<chi2_min) chi2_min=chi2_y[i];
  }
  printf("did chi loop\n");
  // gROOT->SetStyle("Plain");
  TCanvas* c1=new TCanvas("c1","c1",600,600);
  c1->SetRightMargin(0.02);
  c1->SetTopMargin(0.02);
  
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
  printf("sdrew stuff\n");
  TGraph* tg=new TGraph(chi2_n,chi2_x,chi2_y);
  TFitResultPtr fitRes=tg->Fit("pol2","s");
  tg->Draw("*");
  double bestVal=-fitRes->Parameter(1)/(2*fitRes->Parameter(2));  
  printf("Best fit: %f\n",bestVal);
}

float determineChi2(TFile* f_data, TFile* f_smear, const FitSmearPoint& pt,int mode) {
  char smear_h_name[1024];
  char data_h_name[1024];
  char hname[40];
  int bin_low=0, bin_high=0;
  printf("im in the determine chi thing\n");
  

 if (pt.detName=="EB") {
    sprintf(smear_h_name,"%s/EB-EB/C08-m(60,120)/Z0_mass_zoom",pt.dirName.c_str());
    printf("%s",smear_h_name);
    sprintf(data_h_name,"ZFromData/EB-EB/C07-m(60,120)/Z0_mass_zoom");
    bin_low=41;
    bin_high=80;
  }

 if (pt.detName=="EE") {
    sprintf(smear_h_name,"%s/EE-EB/C08-m(60,120)/Z0_mass_zoom",pt.dirName.c_str());
    printf("%s",smear_h_name);
    sprintf(data_h_name,"ZFromData/EE-EB/C07-m(60,120)/Z0_mass_zoom");
    bin_low=41;
    bin_high=80;
  }

  if (pt.detName=="HF" && mode == 1) {
    sprintf(smear_h_name,"%s/EE-HF/C08-m(60,120)/HFpos_mass_zoom",pt.dirName.c_str());
    printf("%s",smear_h_name);
    sprintf(data_h_name,"ZFromData/EE-HF/C06-m(60,120)/HFpos_mass_zoom");
    bin_low=41;
    bin_high=80;
  }else if (pt.detName=="HF" && mode == -1){
    sprintf(smear_h_name,"%s/EE-HF/C08-m(60,120)/HFneg_mass_zoom",pt.dirName.c_str());
    printf("%s",smear_h_name);
    sprintf(data_h_name,"ZFromData/EE-HF/C06-m(60,120)/HFneg_mass_zoom");
    bin_low=41;
    bin_high=80;
  }
  //mode 3 for phi and 5 for eta
  sprintf(hname,"smear_%d",pt.ipt);
  TH1* smear_h=(TH1*)(f_smear->Get(smear_h_name)->Clone(hname));
  TH1* data_h=(TH1*)(f_data->Get(data_h_name));
  
  double rescaler=data_h->Integral(bin_low,bin_high)/smear_h->Integral(bin_low,bin_high);
  
  smear_h->Scale(rescaler);
  if (pt.ipt==0) {
    data_h->SetStats(0);
    data_h->Draw("E");
  }
  smear_h->Draw("SAME HIST");
		      

  double chi2=0;

  for (int ibin=bin_low; ibin<=bin_high; ibin++) {
    double vsmear=smear_h->GetBinContent(ibin);
    double vdata=data_h->GetBinContent(ibin);
    double edata=sqrt(vdata); 
    chi2+=pow(vsmear-vdata,2)/pow(edata,2);
  }
  
  return chi2;
}
