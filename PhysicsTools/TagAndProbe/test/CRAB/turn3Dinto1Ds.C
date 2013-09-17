

 void turn2Dinto1Ds(char* myf, char *myh, char* myfo, int bintype, int dettype)
 {
   
   TFile* mytfile = new TFile(myf);
   TH3* my3dh = (TH3*) mytfile->Get(myh);
   my3dh->SetDirectory(0);
   TFile* myoftile = new TFile(myfo,"RECREATE");
   myoftile->cd();
   //std::vector<TH1*> vechist;
   Int_t nxmbins = my3dh->GetNbinsX();
   Int_t nyptbins = my3dh->GetNbinsY();
   Int_t nzetabins = my3dh->GetNbinsZ();
   //std::cout << " Full bins " << ybins << std::endl;
   std::cout << " Entries " << my3dh->GetEntries();
   bool projxm = false, projyp=false, projze=false;
   std::vector<int> mbins, ptbins, etabins;

   if ( bintype == 0 ) 
   {
     std::cout << " Doing a Mass projection in both electron pt and eta " << std::endl;
     projyp=true; projze=true;
     if ( dettype == 0)
     {
       std::cout << " Over ECAL Electrons " << std::endl;
       int mptbins[]={0,2,3,4,5,6};
       int myetabins[]={2,4,7,10,12};
       ptbins.push_back(0);
       ptbins.push_back(2);
       ptbins.push_back(3);
       ptbins.push_back(4);
       ptbins.push_back(5);
       ptbins.push_back(6);
       etabins.push_back(2);
       etabins.push_back(4);
       etabins.push_back(7);
       etabins.push_back(10);
       etabins.push_back(12);
      
       
     }
     else if ( dettype == 1)
     {
       std::cout << " Over HF Electrons " << std::endl;
       int mptbins[]={0,2,6};
       int myetabins[]={0,1,13,14};
       ptbins.push_back(0);
       ptbins.push_back(2);
       ptbins.push_back(6);
       etabins.push_back(0);
       etabins.push_back(1);
       etabins.push_back(13);
       etabins.push_back(14);
   
     }
     else {std::cout << " not ECAL or HF det type " << std::endl; return;}
   }
   else if (bintype == 1)
   {
     std::cout << " Doing a Mass projection in electron eta " << std::endl;
     projze=true;
     if ( dettype == 0)
     {
       std::cout << " Over ECAL Electrons " << std::endl;
       int myetabins[]={2,3,4,5,6,7,8,9,10,11,12};
       etabins.push_back(2);
       etabins.push_back(3);
       etabins.push_back(4);
       etabins.push_back(5);
       etabins.push_back(6);
       etabins.push_back(7);
       etabins.push_back(8);
       etabins.push_back(9);
       etabins.push_back(10);
       etabins.push_back(11);
       etabins.push_back(12);

       
     }
     else if ( dettype == 1)
     {
       std::cout << " Over HF Electrons " << std::endl;
       int myetabins[]={0,1,13,14};
       etabins.push_back(0);
       etabins.push_back(1);
       etabins.push_back(13);
       etabins.push_back(14);      
       
     }
   }
   else if (bintype == 2)
   { 
     std::cout << " Doing a Mass projection in electron pt " << std::endl;
     projyp=true; 
     if ( dettype == 0)
     {
       std::cout << " Over ECAL Electrons " << std::endl;
       int mptbins[]={0,1,2,3,4,5,6};
       ptbins.push_back(0);
       ptbins.push_back(1);
       ptbins.push_back(2);
       ptbins.push_back(3);
       ptbins.push_back(4);
       ptbins.push_back(5);
       ptbins.push_back(6);
       
     }
     else if ( dettype == 1)
     {
       std::cout << " Over HF Electrons " << std::endl;
       int mptbins[]={0,2,6};
       ptbins.push_back(0);
       ptbins.push_back(2);
       ptbins.push_back(6);
       
     }
   }
   /*
   for (Int_t Ybin = 1; Ybin <= ybins; ++Ybin)
   {
     TH1* onehist = (TH1*) my2dh->ProjectionY(Form("rap%d",Ybin), Ybin,Ybin,"");
     std::cout << " Entries: " << onehist->GetEntries() << std::endl;
     
     onehist->Write();
     
   }
   */
   if (projyp && projze )
   {
       for (std::vector<int>::size_type mip = 0; mip < ptbins.size()-1;++mip)
       {
	  for (std::vector<int>::size_type mep = 0; mep < etabins.size()-1;++mep)
	  {
	    
	    TH1* onehist = (TH1*) my3dh->ProjectionZ(Form("pt%deta%d",mip,mep),ptbins[mip]+1,ptbins[mip+1],etabins[mep]+1,etabins[mep+1],"");
	    std::cout << " Entries: " << onehist->GetEntries() << std::endl;
	    onehist->Write();	    
	    
	  }
       }
       
   }
   else if ( projze )
   {
     for (std::vector<int>::size_type mep = 0; mep < etabins.size()-1;++mep)
     {
        std::cout << " mep " << mep << " is " << etabins[mep] << " and " << etabins[mep+1] << std::endl;
	TH1* onehist = (TH1*) my3dh->ProjectionZ(Form("eta%d",mep),0,my3dh->GetNbinsX()+1,etabins[mep]+1,etabins[mep+1],"");
        std::cout << " Entries: " << onehist->GetEntries() << std::endl;
	onehist->Write();

     }     
   }
   else if ( projyp )
   {
     int ptsize = ptbins.size();
     for (std::vector<int>::size_type mip = 0; mip < ptbins.size()-1;++mip)
     {
       TH1* onehist = (TH1*) my3dh->ProjectionZ(Form("pt%d",mip),ptbins[mip]+1,ptbins[mip+1],0,my3dh->GetNbinsY()+1,"");
        std::cout << " Entries: " << onehist->GetEntries() << std::endl;
	onehist->Write();

     }
   }
   else {std::cout << " Sucka fool! You didn't enter a cool enough combination. Sucka" << std::endl;}
   
   
   std::cout << "SHIT did I get this far??" << std::endl;
   
   myoftile->Write();
   myoftile->Close();
   mytfile->Close();
   
   
 }
