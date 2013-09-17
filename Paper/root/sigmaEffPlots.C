#include "tdrstyle.C"
#include "zrapidityStandard.C"
#include "TFile.h"
#include "TCanvas.h"
#include "TF1.h"
#include "TLegend.h"
void sigPlotStat(TFile* f, TFile* of=0, /*const char* dir="WP80",*/const char* var="wZ0_phiStar") {
  setTDRStyle();
  char name[128];

  char zdef[10][128];
  sprintf(zdef[0],"EB-EB");
  sprintf(zdef[1],"EE-EB");
  sprintf(zdef[2],"EE-HF");
  printf("New SET");
  for(int zd=0;zd<3;zd++){

    TDirectory* dir_0=(TDirectory*)f->Get("mcEff");
    of->cd();
    // TH1* h_0=((TDirectory*)dir_0->Get("All"))->Get(var);

    TList* TOkeys=dir_0->GetListOfKeys();
    TDirectory* dir_sig=0,* dir_base=0,* last_base=0;
    TString ctitle;
    for (int j=0; j<TOkeys->GetSize(); j++) {
      TString q(TOkeys->At(j)->GetName());
      //printf("%s\n",q.Data());
      if (q.Index("EffStats")!=-1) {
	dir_sig=(TDirectory*)dir_0->Get(q.Data());
      }
      if (q.Index("EffStats")==-1 && q.Index(zdef[zd])!=-1){
	dir_base=(TDirectory*)dir_0->Get(q.Data());
      }
    }
    
    TList* lastBase= dir_base->GetListOfKeys();
    for (int j=0; j<lastBase->GetSize(); j++) {
      TString q(lastBase->At(j)->GetName());
      if (q.Index("HLT-GSF")!=-1) {
	last_base=(TDirectory*)dir_base->Get(q.Data());
	printf("last base dir is %s\n",q.Data());
      }
    }//end of last dir loop


    TH1* h_0=(TH1*)((TDirectory*)last_base->Get(var));

    TCanvas* c1=new TCanvas("c1","c1",700,600);
    TLegend* tl=new TLegend(0.5,0.8,0.95,0.95);
    TDirectory* ebeb=(TDirectory*)dir_sig->Get(zdef[zd]);
    int ntrials=ebeb->GetListOfKeys()->GetSize();

    // pass 1, we get the average number of entries
    double aveEntries=0;
    TH1F* b_[100];
    char dname[120];
    for(int i=1;i<h_0->GetNbinsX()+1;i++){
      sprintf(dname,"b_%i",i);
      b_[i]=new TH1F(dname,dname,500,-1,1);
    }//end make b_ loop

    for (int i=0; i<ntrials; i++) {
      sprintf(dname,"Trial%d",i+1);
      TH1* h_ebeb=(TH1*)((TDirectory*)ebeb->Get(dname))->Get(var);
      // TH1* h_eehf=((TDirectory*)eehf->Get(dname))->Get(var);
      aveEntries+=h_ebeb->GetEntries();
    }
    
    aveEntries/=ntrials;
    printf("average entries: %f\n",aveEntries);

    TH1* fe=0,*s=0,*ss=0;
    sprintf(name,"EffStat%s",zdef[zd]);
    fe=(TH1F*)h_0->Clone(name);
    

    for (int i=1; i<=ntrials; i++) {
      sprintf(dname,"Trial%d",i); 
      sprintf(name,"clone%i_Trial%d",zd,i);
      TH1* work=(TH1*)((TDirectory*)ebeb->Get(dname))->Get(var)->Clone(name);
      for(int j=1;j<h_0->GetNbinsX()+1;j++){
	b_[j]->Fill((work->GetBinContent(j)-h_0->GetBinContent(j))/(1.0*h_0->GetBinContent(j)));
	
      }//end loop over bins
    }//loop over fill b_[i]
    
      ///more work!!!!!
    for (int k=1; k<h_0->GetNbinsX()+1; k++) {
      sprintf(name,"f%1i",k);
      TF1 *f1=new TF1(name,"gaus",-1,1);
      b_[k]->Fit(name,"QR");
      double sig_=fabs(f1->GetParameter(2));
      fe->Fill(k,sig_);
     //  double ave=s->GetBinContent(k)/ntrials;
//       if (ave>0) {
// 	double rms=ss->GetBinContent(k)/ntrials;
// 	//      printf("bin %d %f %f %f \n",k,ave,rms,ave*ave);
// 	rms=sqrt(fabs(rms-ave*ave));
// 	//      fe->Fill(p->GetBinCenter(k),p->GetBinError(k)/p->GetBinContent(k));
// 	fe->Fill(s->GetBinCenter(k),rms/ave);
//       }
    }
    fe->Draw();
    if (of!=0){ fe->Write();}
  }//end zd loop



}

///////////////////////////////////////////////////////////////////////////////////////////////////


void sigPlotSyst(TFile* fb, TFile* fe, TFile *fh,  TFile* fnew, int maxzdef=3, const char* var="wZ0_phiStar") {
  setTDRStyle();
  char name[128];
  
  char zdef[10][128];
  sprintf(zdef[0],"EB-EB");
  sprintf(zdef[1],"EE-EB");
  sprintf(zdef[2],"EE-HF");
  char varpm[10][128];
  sprintf(varpm[1],"Plus");
  sprintf(varpm[0],"Minus");

  TFile* f[10];
  f[0]=fb;f[1]=fe;f[2]=fh;
  
  TH1F* h_base[10];
  TH1F* h_syst[10];
  TH1F* h_sigma[10];
 

  TH1F* h_sum[10];//=h_0->Clone("Sum of sigmas");
  //std::string mys = "C07-HLT-GSF";
  printf("NEW LOOOOOP!!!!\n");
  //big old zdef loop
  for(int zd=0; zd<maxzdef;zd++){
    for(int pm=0; pm < 2; pm++){//1=plus,0=minus
      int zint=2*zd+pm;
      TDirectory* dir_0=(TDirectory*)f[zd]->Get("mcEff");
      TList* TOkeys=dir_0->GetListOfKeys();
      TH1* h_0=(TH1*)((TDirectory*)dir_0->Get("All"))->Get(var);
      h_0->Reset();
      
      
      TDirectory* dir_sig=0,* dir_base=0,* last_sig=0,* last_base=0;
      
      for (int j=0; j<TOkeys->GetSize(); j++) {
	TString q(TOkeys->At(j)->GetName());
	if (q.Index(varpm[pm])!=-1 && q.Index(zdef[zd])!=-1) {
	  dir_sig=(TDirectory*)dir_0->Get(q.Data());
	  printf("syst dir is %s\n",q.Data());
	}//find important directory
 	if (q.Index("Plus")==-1 && q.Index("Minus")==-1 &&q.Index(zdef[zd])!=-1) {
	  dir_base=(TDirectory*)dir_0->Get(q.Data());
	  printf("base dir is %s\n",q.Data());
	}//find important base directory
      }//end dir_sig loop
     
      //find last sigma dir to compare to in the end
      TList* lastKey= dir_sig->GetListOfKeys();
      for (int j=0; j<lastKey->GetSize(); j++) {
	TString q(lastKey->At(j)->GetName());
	if (q.Index("HLT-GSF")!=-1) {
	  last_sig=(TDirectory*)dir_sig->Get(q.Data());
	  printf("last sig dir is %s\n",q.Data());
	}
      }//end of last dir loop
      if(!last_sig){printf("I will not be doing a sigma at all/n");}

      //find last base dir to compare to in the end
      TList* lastBase= dir_base->GetListOfKeys();
      for (int j=0; j<lastBase->GetSize(); j++) {
	TString q(lastBase->At(j)->GetName());
	if (q.Index("HLT-GSF")!=-1) {
	  last_base=(TDirectory*)dir_base->Get(q.Data());
	  printf("last base dir is %s\n",q.Data());
	}
      }//end of last dir loop
      if(!last_base){printf("I am broken and will not work /n");}
 
      //  sprintf(name,"c1_zd%i_pm%i",zd,pm);
      //  TCanvas* c1=new TCanvas(name,name,700,600);
      printf("ok\n");
      sprintf(name,"base_zd%i_pm%i",zd,pm);
      h_base[zint]=(TH1F*)((TDirectory*)last_base->Get(var)->Clone(name));
      printf("ok2\n"); 
      printf("ok   %i\n",(int)h_base[zint]->Integral());
      //make the syst histo
      h_syst[zint]=(TH1F*)((TDirectory*)last_sig->Get(var)->Clone(Form("syst_zd%i_pm%i",zd,pm)));
      h_syst[zint]->Scale((double (h_base[zint]->Integral()))/ ( double (h_syst[zint]->Integral())));
      printf("ok4\n");
      // = (TH1*) feb->Clone("MYH");
      //fe->SetTitle("FractionalError");
      sprintf(name,"sigma_zd%i_pm%i",zd,pm);
      printf("ok5 %s\n",name);
      h_sigma[zint]=(TH1F*)(h_base[zint]->Clone(name));
      printf("ok6\n");
      h_sigma[zint]->Add(h_syst[zint],-1.);
      printf("ok7\n");
      h_sigma[zint]->Divide(h_syst[zint]);
      printf("ok8\n");
    }//end pm loop loop
  }//end zdef loop
  printf("ok9\n");
  //loop over zdef to ave PM
  for(int zd=0;zd<3;zd++){
    printf("ok10\n");
    h_sum[zd]=(TH1F*)h_sigma[2*zd]->Clone(Form("EffSyst%s",zdef[zd]));
    h_sum[zd]->Reset();
    for(int i=1;i<h_sum[zd]->GetNbinsX()+1;i++){
      h_sum[zd]->SetBinContent(i,0.5*(fabs(h_sigma[2*zd]->GetBinContent(i))+fabs(h_sigma[2*zd+1]->GetBinContent(i))));
    }
    printf("ok11\n");
    if (fnew!=0) { fnew->cd(); h_sum[zd]->Write();}
    printf("ok12\n");

  }//end summ maker


}//end of function











// void makefinal(TFile* fp, TFile *fm,  TFile* of=0) {
//   setTDRStyle();
  
//   TH1 *hp = (TH1*) fp->Get("MYHA");
//   TH1 *hm = (TH1*) fm->Get("MYHA");
  
//   TH1 *h = hp->Clone("MYNA");
//   for (int k=1; k<=h->GetNbinsX(); k++) {
//     std::cout << hp->GetBinContent(k) <<  " " << hm->GetBinContent(k) << std::endl;
//     h->SetBinContent(k,hp->GetBinContent(k)*.5 +hm->GetBinContent(k)*.5);
//     std::cout << " NEW " << h->GetBinContent(k) << std::endl;
//     //h->SetBinEntries(k,1);
//   }
  
//   if (of!=0) { of->cd(); h->Write();}

  
// }

