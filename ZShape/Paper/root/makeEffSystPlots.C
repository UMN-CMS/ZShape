{
#include "sigmaEffPlots.C"
//#include "makefinal.C"


TFile *my80bb    = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffSystEB-EBDef_WP80.root");
TFile *my80ee    = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffSystEE-EBDef_WP80.root");
TFile *my80hf  = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffSystEE-HFDef_WP80.root");
TFile *myo80p  = new TFile("WP80P.root","RECREATE");


TFile *myGSFbb   = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffSystEB-EBDef_GsfTrack-EtaDet.root");
TFile *myGSFee   = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffSystEE-EBDef_GsfTrack-EtaDet.root");
TFile *myGSFhf = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffSystEE-HFDef_GsfTrack-EtaDet.root");
TFile *myoGSFp = new TFile("GSFP.root","RECREATE");


TFile *myHFEIDbb   = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffSystEE-HFDef_HFElectronId-EtaDet.root");
TFile *myHFEIDee   = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffSystEE-HFDef_HFElectronId-EtaDet.root");
TFile *myHFEIDhf = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffSystEE-HFDef_HFElectronId-EtaDet.root");
TFile *myoHFEIDp = new TFile("HFEIDP.root","RECREATE");


TFile *myHFSCbb   = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffSystEE-HFDef_HFSuperCluster-Et.root");
TFile *myHFSCee   = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffSystEE-HFDef_HFSuperCluster-Et.root");
TFile *myHFSChf = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffSystEE-HFDef_HFSuperCluster-Et.root");
TFile *myoHFSCp = new TFile("HFSCP.root","RECREATE");


TFile *mySCbb    = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffSystEB-EBDef_Supercluster-Eta.root");
TFile *mySCee    = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffSystEE-EBDef_Supercluster-Eta.root");
TFile *mySChf  = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffSystEE-HFDef_Supercluster-Eta.root");
TFile *myoSCp   = new TFile("SCP.root","RECREATE");


TFile *myHLTbb   = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffSystEB-EBDef_HLT-GSF.root");
TFile *myHLTee   = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffSystEE-EBDef_HLT-GSF.root");
TFile *myHLThf = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffSystEE-HFDef_HLT-GSF.root");
TFile *myoHLTp = new TFile("HLTP.root","RECREATE");

sigPlotSyst(my80bb,my80ee,my80hf, myo80p);
myo80p->Write();

sigPlotSyst(myGSFbb,myGSFee,myGSFhf, myoGSFp);
myoGSFp->Write();

sigPlotSyst(mySCbb,mySCee,mySChf,myoSCp);
myoSCp->Write();

sigPlotSyst(myHLTbb,myHLTee,myHLThf,myoHLTp);
myoHLTp->Write();

sigPlotSyst(myHFEIDbb,myHFEIDee,myHFEIDhf,myoHFEIDp);
myoHFEIDp->Write();

sigPlotSyst(myHFSCbb,myHFSCee,myHFSChf,myoHFSCp);
myoHFSCp->Write();
myoHFSCp->Close();

}

