{
#include "sigmaEffPlots.C"

TFile *my80    = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffStat100Trials_WP80.root");
TFile *myo80    = new TFile("WP80.root","RECREATE");
TFile *myGSF   = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffStat100Trials_GsfTrack-EtaDet.root");
TFile *myoGSF   = new TFile("GSF.root","RECREATE");
TFile *myHFEID = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffStat100Trials_HFElectronId-EtaDet.root");
TFile *myoHFEID = new TFile("HFEID.root","RECREATE");
TFile *myHFSC  = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffStat100Trials_HFSuperCluster-Et.root");
TFile *myoHFSC  = new TFile("HFSC.root","RECREATE");
TFile *mySC    = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffStat100Trials_Supercluster-Eta.root");
TFile *myoSC    = new TFile("SC.root","RECREATE");
TFile *myHLT   = new TFile("/local/cms/user/klapoetke/sigmaEffs/sigma_trial_EcalEffStat100Trials_HLT-GSF.root");
TFile *myoHLT   = new TFile("HLT.root","RECREATE");

sigPlotStat(my80,myo80);
myo80->Write();

sigPlotStat(myGSF,myoGSF);
myoGSF->Write();
sigPlotStat(myHFEID,myoHFEID);
myoHFEID->Write();
sigPlotStat(myHFSC,myoHFSC);
myoHFSC->Write();
sigPlotStat(mySC,myoSC);
myoSC->Write();
sigPlotStat(myHLT,myoHLT);
myoHLT->Write();

myoHLT->Close();

}

