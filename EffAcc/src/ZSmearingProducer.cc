// -*- C++ -*-
//
// Package:    ZSmearingProducer
// Class:      ZSmearingProducer
// 
/**\class ZSmearingProducer ZSmearingProducer.cc ZShape/ZSmearingProducer/src/ZSmearingProducer.cc
  
Description: <one line class summary>
Produces pair of electrons (GenParticleCollection) from Z decay as generated with Phytia
Implementation:
<Notes on implementation>
*/



// system include files
#include <memory>
#include <algorithm>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Candidate/interface/Particle.h"

#include "DataFormats/Math/interface/Point3D.h"

#include "DataFormats/Math/interface/LorentzVector.h"

#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "DataFormats/GeometryVector/interface/Phi.h"

#include "Math/VectorUtil.h"

#include "TRandom3.h"

#include "ZShape/Base/interface/ZShapeElectron.h"

#include "PhysicsTools/TagAndProbe/interface/EffTableLoader.h"


#include <TF1.h>
#include <TMath.h>
#include <math.h>

//
// class decleration
//
Double_t crystalBall(Double_t *x, Double_t *par);
Double_t EBRes(Double_t *x,Double_t *par);
Double_t EERes(Double_t *x,Double_t *par);

class ZSmearingProducer : public edm::EDProducer {
public:
  explicit ZSmearingProducer(const edm::ParameterSet&);
  ~ZSmearingProducer();

private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  void smearElectron(math::PtEtaPhiELorentzVector &electron) ;

  enum MyDetType { mdt_EB, mdt_EE, mdt_HF };

  double smearECAL (double eta, double et, MyDetType det);
  double smearECALCB (double eta, double et, MyDetType det);
  double getSigma (double eta, double et, MyDetType det);
      
  // ----------member data ---------------------------

  edm::InputTag m_srcTag;
  edm::InputTag zElectronsTag;
  bool quiet_;
  bool doSmearing_;
  float zElectronsCone_;
  int randomSeed_;
  math::XYZPoint vtx_;
  TRandom3 *randomNum_;
  EffTableLoader *smearTable_;
  TF1 *crystalball_;

  struct {
    double stocastic;
    double constant;
    double mean;
  } HFParams_;
  
  struct {
    double sigma[4];
	double alpha;
	double N;
	double mean;
  } EBPrams_;

  struct {
    double sigma[3];
	double alpha;
	double N;
	double mean;
  } EEPrams_;


};


ZSmearingProducer::ZSmearingProducer(const edm::ParameterSet& iConfig) : 
    m_srcTag(iConfig.getUntrackedParameter<edm::InputTag>("src",edm::InputTag("source"))),
    zElectronsTag(iConfig.getUntrackedParameter<edm::InputTag>("zElectronsCollection",edm::InputTag("ZIntoElectronsEventProducer:ZEventParticles"))),
    quiet_(iConfig.getUntrackedParameter<bool>("quiet",false)),
    doSmearing_(iConfig.getUntrackedParameter<bool>("doSmearing",false)),
    zElectronsCone_(iConfig.getParameter<double>("zElectronsCone")),
    randomSeed_(iConfig.getParameter<int>("randomSeed"))
{
  using namespace reco;
  //Get HF Smearing Parameters
  edm::ParameterSet ps=iConfig.getParameter<edm::ParameterSet>("HF");
  HFParams_.stocastic=ps.getParameter<double>("stocastic");
  HFParams_.constant=ps.getParameter<double>("constant");
  HFParams_.mean=ps.getParameter<double>("mean");

  //Get EB Smearing Parameters
  ps=iConfig.getParameter<edm::ParameterSet>("EB");
  EBPrams_.sigma[0]=ps.getParameter<double>("p0");
  EBPrams_.sigma[1]=ps.getParameter<double>("p1");
  EBPrams_.sigma[2]=ps.getParameter<double>("p2");
  EBPrams_.sigma[3]=ps.getParameter<double>("c");
  EBPrams_.alpha=ps.getParameter<double>("alpha");
  EBPrams_.mean=ps.getParameter<double>("mean");
  EBPrams_.N=ps.getParameter<double>("n");

  //Get EE Smearing Parameters
  ps=iConfig.getParameter<edm::ParameterSet>("EE");
  EEPrams_.sigma[0]=ps.getParameter<double>("p0");
  EEPrams_.sigma[1]=ps.getParameter<double>("p1");
  EEPrams_.sigma[2]=ps.getParameter<double>("p2");
  EEPrams_.alpha=ps.getParameter<double>("alpha");
  EEPrams_.mean=ps.getParameter<double>("mean");
  EEPrams_.N=ps.getParameter<double>("n");

  //register my product
  produces<GenParticleCollection>("ZEventParticles");
  
  //Setting the random number to make things reproducable
  randomNum_ = new TRandom3(randomSeed_);

  edm::FileInPath filePath(iConfig.getParameter<edm::FileInPath>("SmearTable"));
  std::string smeartablefile = filePath.fullPath();
  smearTable_ = new EffTableLoader(smeartablefile);
  crystalball_ =  new TF1("crystal", crystalBall ,0.1,1.3,5,"");
}


ZSmearingProducer::~ZSmearingProducer()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
ZSmearingProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm; 
  using namespace std; 
  using namespace reco;

  //The collection of new particles
  std::auto_ptr<GenParticleCollection> pZeeParticlesN(  new GenParticleCollection() );

  pZeeParticlesN->clear();

  //Get the collection of orginal particles
  Handle <GenParticleCollection> pZeeParticles;
  iEvent.getByLabel(zElectronsTag,pZeeParticles);

  const GenParticleCollection * ZeeParticles = pZeeParticles.product();
  //std::cout << " Starting the event " << std::endl;
  ////////////////////////
  // looking for electrons
  //int myPid = 11;
  int ne=0;
  int ngot[2]; ngot[0]=0; ngot[1]=0;
  
  GenParticleCollection::const_iterator me[2];
  //math::XYZTLorentzVector elecs[2];
  math::PtEtaPhiELorentzVector elecs[2];

  for(GenParticleCollection::const_iterator ZeeElectron_itr = ZeeParticles->begin();
      ZeeElectron_itr != ZeeParticles->end();
      ZeeElectron_itr++
      )
    if (abs(ZeeElectron_itr->pdgId())==11) {
      if (ne<2) {
	me[ne]=ZeeElectron_itr;
	ne++;
      }
    }

   //Now we look in a cone, we can set the cone to zero to not got any here
  for(
      GenParticleCollection::const_iterator ZeeElectron_itr = ZeeParticles->begin();
      ZeeElectron_itr != ZeeParticles->end();
      ZeeElectron_itr++
      )
    {
      double dR=ROOT::Math::VectorUtil::DeltaR(me[0]->momentum(),ZeeElectron_itr->momentum());
      if (me[0]==ZeeElectron_itr || dR<zElectronsCone_) {
	elecs[0]+=ZeeElectron_itr->p4();
	vtx_=math::XYZPoint(ZeeElectron_itr->vertex().x(),ZeeElectron_itr->vertex().y(),ZeeElectron_itr->vertex().z());
	ngot[0]++;
      } else {
	dR=ROOT::Math::VectorUtil::DeltaR(me[1]->momentum(),ZeeElectron_itr->momentum());
	if (me[1]==ZeeElectron_itr || dR<zElectronsCone_) {
	  elecs[1]+=ZeeElectron_itr->p4();
	  ngot[1]++;
	}
      }
    }
  
  //now correct the energies with the "function"
  for (int electron = 0; electron < ne; ++electron)
    {
      //std::cout << " looking at electron " << electron << std::endl;
        if(doSmearing_) smearElectron(elecs[electron]);
      //std::cout << " NNew E " << elecs[electron].E() << " new eta " << elecs[electron].eta() << " new et " << elecs[electron].Et()<< " new pt " << elecs[electron].pt() << std::endl;
    }  

  //put the corrected electrons back in the event
  for(
      GenParticleCollection::const_iterator ZeeElectron_itr = ZeeParticles->begin();
      ZeeElectron_itr != ZeeParticles->end();
      ZeeElectron_itr++
      )
    {
       for (int electron = 0; electron < ne; ++electron)
         {
         if (me[electron]==ZeeElectron_itr)
           {
             //pdgId = ZeeElectron_itr->
             pZeeParticlesN->push_back( GenParticle(ZeeElectron_itr->charge(),
                                            math::XYZTLorentzVector(elecs[electron]),
                                            vtx_,
                                            ZeeElectron_itr->pdgId(),
                                            ZeeElectron_itr->status(),
                                            true
                                            )
                                );
           }
         }
    }

  iEvent.put(pZeeParticlesN,"ZEventParticles");
  


}

//Function that does the smearing of an electron
void ZSmearingProducer::smearElectron(math::PtEtaPhiELorentzVector &electron)
{
  //Possibly smear these as a function of detector eta rather than physics eta
  //I expect those near the edges either do not get "smeared" into another detector
  //or are cut out by the acceptance cuts
  const double EBEEboundry = 1.5;
  const double EEHFbountry = 3.0;
  double eta = electron.eta();
  double e  = electron.E();
  double et  = electron.Et();
  //double pt = electron.Pt();

  double Efrac = 1.0;
  
  ZShapeElectron myElec;
  myElec.p4_ = math::PtEtaPhiMLorentzVector(electron);
 
  double deteta = myElec.detectorEta(vtx_);
  
  if (fabs(deteta) < EBEEboundry )
  {
    //Do EB stuff
    Efrac = smearECALCB(deteta,e, mdt_EB);
   
  }
  else if (fabs(deteta) < EEHFbountry)
  {
    //Do EE Stuff
    Efrac = smearECALCB(deteta,et, mdt_EE);
  }
  else if (fabs(deteta) < 5.0)
  {
    double mysig = HFParams_.stocastic/sqrt(std::max(e,1.0))+HFParams_.constant;
    double  etaFact=sinh(eta)/sinh(deteta);
    Efrac = randomNum_->Gaus(HFParams_.mean,mysig);
    double newEta=deteta;
    double perc = randomNum_->Uniform(100);
    double unif = randomNum_->Uniform(0.64,0.9);
    double sign = (deteta < 0.) ?(-1.) : (1.); //added to know the + or - sign.
    double etabias=0.0144;
    if((fabs(deteta)>2.964)&&(fabs(deteta)<=3)){
      newEta=deteta;
    }else if ((fabs(deteta)>3)&&(fabs(deteta)<=3.034)){
      if(perc<=15){newEta=deteta;
      }else if((perc>15)&&((perc<=57))){
        newEta=sign*(3.0515+etabias);
      }else if((perc>57)&&((perc<=100))){newEta=sign*(unif*0.175+2.964+etabias);
      }
    }else if ((fabs(deteta)>3.034)&&(fabs(deteta)<=3.104)){
      if(perc<=3){newEta=deteta;
      }else if((perc>3)&&((perc<=51))){
        newEta=sign*(3.0515+etabias);
      }else if((perc>51)&&((perc<=100))){
        newEta=sign*(unif*0.175+2.964+etabias);
      }
    }else if ((fabs(deteta)>3.104)&&(fabs(deteta)<=3.139)){
      if(perc<=30){newEta=sign*(3.0515+etabias);
      }else if((perc>30)&&((perc<=100))){
        newEta=deteta;
      }
    }else if ((fabs(deteta)>3.104)&&(fabs(deteta)<=3.139)){
      if(perc<=30){
        newEta=sign*(3.0515+etabias);
      }else if((perc>30)&&((perc<=100))){
        newEta=deteta;
      }
    }else if ((fabs(deteta)>3.1915)&&(fabs(deteta)<=3.279)){
      if(perc<=53){
        newEta=sign*(3.22650+etabias);
      }else if((perc>53)&&((perc<=100))){
        newEta=deteta;
      }
    }else if ((fabs(deteta)>3.3665)&&(fabs(deteta)<=3.454)){
      if(perc<=42){
        newEta=sign*(3.4015+etabias);
      }else if((perc>42)&&((perc<=100))){
        newEta=deteta;
      }
    }else if ((fabs(deteta)>3.5415)&&(fabs(deteta)<=3.629)){
      if(perc<=35){
        newEta=sign*(3.5765+etabias);
      }else if((perc>35)&&((perc<=100))){
        newEta=deteta;
      }
    }else if ((fabs(deteta)>3.7165)&&(fabs(deteta)<=3.804)){
      if(perc<=25){
        newEta=sign*(3.7515+etabias);
      }else if((perc>25)&&((perc<=100))){
        newEta=deteta;
      }else if ((fabs(deteta)>3.89135)&&(fabs(deteta)<=3.9786)){
      if(perc<=20){
        newEta=sign*(3.926+etabias);
      }else if((perc>20)&&((perc<=100))){
        newEta=deteta;
      }
    
      }

    }
   eta=(asinh(etaFact*sinh(newEta)));
  }
  
  //std::cout << " OLD E " << electron.E() << " new eta " << electron.eta() << " new et " << electron.Et() << " new pt " << electron.pt() <<  " mass : " << electron.M() << std::endl;

  //double pz = electron.pz();
  ///electron.SetE(Efrac*e);
  //electron.SetPt(pow(-e*e*(1-Efrac*Efrac)+pt*pt,0.5));
  ///electron.SetPt(electron.Et());
  electron = math::PtEtaPhiELorentzVector(Efrac*e/cosh(eta),eta,electron.phi(),Efrac*e);
 

  //std::cout << " cosh way " << Efrac*e/cosh(eta) << " Other way " << Efrac*e*sin(electron.theta()) << std::endl;
  //std::cout << " New E " << electron.E() << " new eta " << electron.eta() << " new et " << electron.Et() << " new pt " << electron.pt() <<  " mass : " << electron.M() << std::endl;
}

Double_t crystalBall(Double_t *x, Double_t *par)
{
  Double_t t = (x[0]-par[2])/par[3];
  if (par[0] < 0) t = -t;

  Double_t absAlpha = fabs((Double_t)par[0]);

  if (t >= -absAlpha) {
    return par[4]*exp(-0.5*t*t);
  }
  else {
    Double_t a =  TMath::Power(par[1]/absAlpha,par[1])*exp(-0.5*absAlpha*absAlpha);
    Double_t b= par[1]/absAlpha - absAlpha;

    return par[4]*(a/TMath::Power(b - t, par[1]));
  }

}

Double_t EBRes(Double_t *x,Double_t *par) {
  if (x[0] < 0.01 ) return 100.;
  //  Double_t p0 = par[0]/x[0] + par[3];
  //  Double_t p1 = par[1]/x[0];
  //  Double_t p2 = par[2]/x[0];
  Double_t p0 = par[0]/x[0] + par[3];
  Double_t p1 = par[0]*par[1]/x[0];
  Double_t p2 = par[0]*par[2]/x[0];
  return (p0-p1*fabs(x[1])+p2*x[1]*x[1]);
}

Double_t EERes(Double_t *x,Double_t *par) {
  if (x[0] < 0.01 ) return 100.;
  Double_t p0 = par[0]/x[0];
  Double_t p1 = par[1]*par[0]/x[0];
  Double_t p2 = par[2]*par[0]/x[0];
  return (p0-p1*fabs(x[1])+p2*x[1]*x[1]);
}

double ZSmearingProducer::getSigma(double eta, double et, MyDetType det)
{
  double x[2];
  x[0] = (et<1)?(0):sqrt(et); // energy for EB
  x[1] = eta;
  
  if ( det == mdt_EB)
  {
     return (EBRes(x,EBPrams_.sigma));
  }
  else if ( det == mdt_EE)
  {
     return (EERes(x,EEPrams_.sigma));
  }
  else return 1.0;
}

double ZSmearingProducer::smearECALCB(double eta, double et, MyDetType det)
{
  double params[5];
  params[3] = getSigma(eta, et, det);
  params[0] = ( det == mdt_EB ) ? (EBPrams_.alpha) : (EEPrams_.alpha);
  params[1] = ( det == mdt_EB ) ? (EBPrams_.N) : (EEPrams_.N);
  params[2] = ( det == mdt_EB) ? (EBPrams_.mean) : (1.0);
  params[4] = 100.;
  double sf = ( det == mdt_EB) ? (1.0) : (EEPrams_.mean);
  crystalball_->SetParameters(params);
  return crystalball_->GetRandom()*sf;
  /*Crystal Ball from a binned file.
  //First I need to find which efficiency bin we need
  int index = smearTable_->GetBandIndex(et,eta);
  //Then I need to get the crystal ball paramters from that bin
  std::vector<float> parVals = smearTable_->correctionEff(index);
  double myVals[10];
  for ( uint val = 0; val < parVals.size(); ++val)
  {
      myVals[val] = parVals[val]; 
  }
  //Then I need to set the crystal ball parameters for the function
  //crystalBall *cryballfunc = new crystalBall();
  crystalball_->SetParameters(&myVals[1]);
  //lastly, I need to get a random number from the function
  return crystalball_->GetRandom();
  */

}

//Method for smearing ECAL
double ZSmearingProducer::smearECAL(double eta, double et, MyDetType det)
{
  double p0r = 0.;
  double p1r = 0.;
  double p2r = 0.;
  double p0l = 0.;
  double p1l = 0.;
  double p2l = 0.;

  if ( det == mdt_EB ) 
    {
      //First the right, then the left sides sigma
      p0r = 0.0028 + 0.380/et;
      p1r = 0.0267 - 0.617/et;
      p2r = -0.0146 + 0.597/et;

      p0l = 0.0057 + 0.321/et;
      p1l = 0.0185 - 0.410/et;
      p2l = -0.010 + 0.789/et;
    }
  else if ( det == mdt_EE ) 
    {
      p0r = +6.29/et;
      p1r = -4.53/et;
      p2r = +0.95/et;

      p0l = +7.98/et;
      p1l = -5.56/et;
      p2l = +1.25/et;
    }
  else return -1000.;

  double sigmaL = p0l + p1l*fabs(eta) + p2l*eta*eta;
  double sigmaR = p0r + p1r*fabs(eta) + p2r*eta*eta;
  //std::cout << " Side " << det << " sigmaL " << sigmaL << " sigmaR " << sigmaR << std::endl;

  double randomnumber = randomNum_->Uniform(0,1); //(between 0 and 1)
  double leftfraction = (1.0/(1.0+sigmaR/sigmaL));
  double meancor = (sigmaR*sigmaR - sigmaL*sigmaL)/(pow(2.0*3.141596,0.5)*(sigmaL + sigmaR));
  //std::cout << " Mean is " << meancor << std::endl;
  double frac = -1001.;
  if (randomnumber < leftfraction)
    {
      double myfrac = randomNum_->Gaus(1.0-meancor,sigmaL);
      frac = (1.0-meancor-fabs(1.0-meancor-myfrac));
      //std::cout << " Went Left Myfac is " << myfrac << " and final Frac is " << frac << std::endl; 
    }
  else
    {
      double myfrac = randomNum_->Gaus(1.0-meancor,sigmaR);
      frac = (1.0-meancor+fabs(1.0-meancor-myfrac));
      //std::cout << " Went Right Myfac is " << myfrac << " and final Frac is " << frac << std::endl; 
    }

  return frac;
}



// ------------ Method called once each job just before starting event loop  ------------
void ZSmearingProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
ZSmearingProducer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(ZSmearingProducer);
