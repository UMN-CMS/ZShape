#include "TF1.h"
#include "TFile.h"
#include "TCanvas.h"
#include "TGraphErrors.h"
#include "TGraph.h"
#include "TH1.h"
#include "TH2.h"
#include <math.h>
#include <algorithm>
#include <list>
#include <iostream>
#include "TROOT.h"
//fd = data file, fs= smeared/scanned file
void scanVarFitter(TFile* fd, TFile* fs,const char* hname,const char* zdef,const char* var,double *vals,int mode=0){
  gROOT->SetStyle("Plain");
  char name[128];
  char mess[128];
  char fullzdef[128];
 

  double chi2[];
  int size=((int)vals.size());
  double unit=(var[size-1]-var[0])1.0/(size-1.0);
  TH1F* h[];
 
 
  //set up chi histo
  TCanvas *c1 = new TCanvas("chi2", "chi2", 500, 500);
  sprintf(name, "chi2",fullzdef,hname);
  sprintf(mess, "Chi Squared for %s %s",fullzdef,var);
  TH1F* hc=new TH1F(name,mess,4+size,vals[0]-2.5*unit,vals[size-1]+2.5*unit);
  
  
  if(zdef=="EB")sprintf(fullsdef,"EB-EB");
  else if(zdef=="EE")sprintf(fullsdef,"EE-EB");
  else if(zdef=="HF")sprintf(fullsdef,"EE-HF");
 
  sprintf(name, "/ZFromData/%s/Acceptance/%s",fullzdef,hname);// if C07-m(60,120) for EE/EB, C06-m(60,120) for HF!
h[0]=(TH1F*)fd->Get(name)->Clone(mess);

 for(int i=1;i<size+1;i++){
    // do stuff for vals[i];
   
   char c[128]; sprintf(c,"%0.3f",vals[i])
		   sprintf(name, "/%sX%sX%cX%s/%s/Acceptance/%s",zdef,var,c[0],c+2,fullzdef,hname);//C08-m(60,120) is good for all zdefs
    sprintf(mess,"cl_%d",i);
    h[i]=(TH1F*)fs->Get(name)->Clone(mess);

    //do the chi2 plot!!!
    double chi2=0;  
    
    for (jj=1;jj<=h[0]->GetNbinsX();jj++){
      double s2exp = (h[0]->GetBinContent(jj));
      double s2obs= (h[1]->GetBinContent(jj));   
      
      if (s2exp==0){
	chi2+=0;
      }else{
	chi2+=((s2obs-s2exp)*(s2obs-s2exp))/((sqrt(s2exp))*(sqrt(s2exp)));
      }
    }
    //end chi2 calc    
    hc->SetBinContent(hchi->FindBin(vals[i]),chi2);


 }//end i loop over vals
 
 
 hc->SetTitle(0);
 TF1* p1=new TF1("p1","[0]+[1]*x+[2]*x*x",vals[0],val[size-1]);
 
 hc->Fit("p1","R");
 hc->Draw(PE);


}
