void turn2Dinto1Ds(char* myf, char *myh, char* myfo)
{
   
  TFile* mytfile = new TFile(myf);
  TH2* my2dh = (TH2*) mytfile->Get(myh);
  my2dh->SetDirectory(0);
  TFile* myoftile = new TFile(myfo,"RECREATE");
  myoftile->cd();
  //std::vector<TH1*> vechist;
  Int_t ybins = my2dh->GetNbinsX();
  std::cout << " Full bins " << ybins << std::endl;
  std::cout << " Entries " << my2dh->GetEntries();
   
  for (Int_t Ybin = 1; Ybin <= ybins; ++Ybin)
    {
      TH1* onehist = (TH1*) my2dh->ProjectionY(Form("rap%d",Ybin), Ybin,Ybin,"");
      std::cout << " Entries: " << onehist->GetEntries() << std::endl;
     
      onehist->Write();
     
    }
   
  myoftile->Write();
  myoftile->Close();
  mytfile->Close();
   
   
}
