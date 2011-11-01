#include "TProfile.h"
#include "ZShape/Base/interface/EfficiencyStatistics.h"
#include "ZShape/EffAcc/interface/ZEfficiencyCalculator.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "Math/VectorUtil.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "PhysicsTools/UtilAlgos/interface/TFileService.h"


//
// constructors and destructor
//
ZEfficiencyCalculator::ZEfficiencyCalculator(const edm::ParameterSet& iConfig) :
  m_srcTag(iConfig.getUntrackedParameter<edm::InputTag>("src",edm::InputTag("source"))),
  zElectronsTag(iConfig.getUntrackedParameter<edm::InputTag>("zElectronsCollection",edm::InputTag("ZIntoElectronsEventProducer:ZEventParticles"))),
  zTreeLevelElectronsTag(iConfig.getUntrackedParameter<edm::InputTag>("zTreeLevelElectronsCollection",edm::InputTag("ZIntoElectronsEventProducer" "ZEventEle3"))),
  quiet_(iConfig.getUntrackedParameter<bool>("quiet",false)),
  zElectronsCone_(iConfig.getParameter<double>("zElectronsCone"))
{
  //
  //now do what ever initialization is needed

  //
  // multiple PSets==Zdefinitions: each electron required to pass a set of cuts
  
  std::vector<edm::ParameterSet> zdefSetups =iConfig.getUntrackedParameter< std::vector<edm::ParameterSet> >("ZDefs");

  for (std::vector<edm::ParameterSet>::iterator i=zdefSetups.begin(); i!=zdefSetups.end(); ++i) {
    std::string name=i->getUntrackedParameter<std::string>("name");
    std::vector<std::string> req1=i->getUntrackedParameter<std::vector<std::string> >("e1");
    std::vector<std::string> req2=i->getUntrackedParameter<std::vector<std::string> >("e2");
    std::vector<std::string> reqZ=i->getUntrackedParameter<std::vector<std::string> >("Z");
    ZShapeZDef* zdef=new ZShapeZDef();
    for (std::vector<std::string>::iterator k=req1.begin(); k!=req1.end(); k++) 
      zdef->addCriterion(ZShapeZDef::crit_E1,*k);
    for (std::vector<std::string>::iterator k=req2.begin(); k!=req2.end(); k++) 
      zdef->addCriterion(ZShapeZDef::crit_E2,*k);
    for (std::vector<std::string>::iterator k=reqZ.begin(); k!=reqZ.end(); k++) 
      zdef->addCriterion(ZShapeZDef::crit_Z,*k);
    zdefs_[name]=zdef;
  }

  //
  // list of all available efficiencies
  
  std::vector<edm::ParameterSet> effs =iConfig.getUntrackedParameter< std::vector<edm::ParameterSet> >("Effs");

  for (std::vector<edm::ParameterSet>::iterator i=effs.begin(); i!=effs.end(); ++i) {
    std::string name=i->getUntrackedParameter<std::string>("name");
    edm::FileInPath filePath(i->getParameter<edm::FileInPath>("effFile")); 
    std::string file=filePath.fullPath(); 
    //std::string var=i->getUntrackedParameter<std::string>("variable");
    loadEfficiency(name,file);
  }

  //
  // setting up trials - done only for one specific efficiency (estat_eff) and one specific Zdef (estat_zdef)

  statsBox_.trials=iConfig.getUntrackedParameter<int>("estat_trials",-1);
  edm::LogInfo("ZShape") << "Number of trials requested: " << statsBox_.trials;
  if (statsBox_.trials>0) {
    statsBox_.targetEffStat=iConfig.getUntrackedParameter<std::string>("estat_eff");

    if (efficiencies_.find(statsBox_.targetEffStat)==efficiencies_.end()) {
      edm::LogError("ZShape") << "Unable to find efficiency '" <<statsBox_.targetEffStat << "' for statistical variations!";
      statsBox_.trials=0;
    }

  }
  

  //
  // setting up systematic variations 
  targetEffSys_  =iConfig.getUntrackedParameter<std::string>("esys_eff","");
  targetZDefSys_ =iConfig.getUntrackedParameter<std::string>("esys_zdef","");
  edm::LogInfo("ZShape") << "esys_eff: " << targetEffSys_ << "   while esys_zdef: "<< targetZDefSys_;  

  createAlternateZDefs(targetZDefSys_,targetEffSys_);

}


ZEfficiencyCalculator::~ZEfficiencyCalculator()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void ZEfficiencyCalculator::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace std;
  using namespace cms;
  using namespace reco;

  Handle< HepMCProduct > EvtHandle ;
   
  // find initial (unsmeared, unfiltered,...) HepMCProduct
  iEvent.getByLabel(m_srcTag, EvtHandle ) ;

  //super-fast reconstructed electrons for efficiency propagation step (aka electrons 'cones') 
  Handle <GenParticleCollection> pZeeParticles;
  iEvent.getByLabel(zElectronsTag,pZeeParticles);

  //tree-level electrons ('truth') 
  Handle <GenParticleCollection> pZeeTreeLevelParticles; 
  iEvent.getByLabel(zTreeLevelElectronsTag,pZeeTreeLevelParticles); 

  const GenParticleCollection * ZeeParticles = pZeeParticles.product();
  const GenParticleCollection * ZeeTreeLevelParticles = pZeeTreeLevelParticles.product(); 

  fillEvent(ZeeParticles, ZeeTreeLevelParticles); 

  if (evt_.n_elec!=2) return; // need 2 and only 2
  if (evt_.n_TLelec!=2) return; // need 2 and only 2 

  //
  // fill histograms for before any selection
  allCase_.Fill(evt_.elec(0), evt_.elec(1), evt_.elecTreeLevel(0).polarP4(), evt_.elecTreeLevel(1).polarP4()); 

  // these stages merely _fill_ bits.  They do not apply cuts!
  for (int ne=0; ne<2; ne++) {
    stdCuts_.acceptanceCuts(evt_.elec(ne));
    stdCuts_.ptCuts(evt_.elec(ne));
    stdCuts_.dummyCuts(evt_.elec(ne));
  }

  // fill the generator-level acceptance cuts...
  {
    math::XYZTLorentzVector p1(evt_.elec(0).p4_);
    math::XYZTLorentzVector p2(evt_.elec(1).p4_);
    math::XYZTLorentzVector pZ = p1 + p2 ;


    int necal=(evt_.elec(0).passed("ACC(ECAL+TRK)")?(1):(0))+(evt_.elec(1).passed("ACC(ECAL+TRK)")?(1):(0));
    int ntrk=(evt_.elec(0).passed("ACC(ECAL-TRK)")?(1):(0))+(evt_.elec(1).passed("ACC(ECAL-TRK)")?(1):(0));
    int nhf=(evt_.elec(0).passed("ACC(HF)")?(1):(0))+(evt_.elec(1).passed("ACC(HF)")?(1):(0));

    if (necal==2) accHistos_.ecal_ecal->Fill(pZ.Rapidity());
    else if (necal==1 && ntrk==1) accHistos_.ecal_ntrk->Fill(pZ.Rapidity());
    else if (necal==1 && nhf==1) accHistos_.ecal_hf->Fill(pZ.Rapidity());
    else if (necal==1) accHistos_.ecal_noacc->Fill(pZ.Rapidity());
    else if (ntrk==2)  accHistos_.ntrk_ntrk->Fill(pZ.Rapidity());
    else if (ntrk==1 && nhf==1)  accHistos_.ntrk_hf->Fill(pZ.Rapidity());
    else if (ntrk==1)  accHistos_.ntrk_noacc->Fill(pZ.Rapidity());
    else if (nhf==2)  accHistos_.hf_hf->Fill(pZ.Rapidity());
    else if (nhf==1)  accHistos_.hf_noacc->Fill(pZ.Rapidity());
    else accHistos_.noacc_noacc->Fill(pZ.Rapidity());
  }
    
  EfficiencyCut* keep=0;

  int pass=0;
  do {
    if (statsBox_.trials>=1) {
      // swap to alternate universe
      if (pass==0) keep=theCuts_[statsBox_.targetEffStat];
      // after first iteration, override standard cut with alternate cut
      else theCuts_[statsBox_.targetEffStat]=statsBox_.alternateCuts[pass-1];
    }

    if (pass==0) {
      // apply all cuts and store results into ZEle objects
      for (std::map<std::string,EfficiencyCut*>::iterator cut=theCuts_.begin(); cut!=theCuts_.end(); cut++) {
	for (int ne=0; ne<2; ne++) {
	  //std::cout << " Looking at Cut " << cut->first << " Electron " << ne << std::endl;
	  evt_.elec(ne).cutResult(cut->first,cut->second->passesCut(evt_.elec(ne)));
	}
      }
    } else {
      EfficiencyCut* statCut=theCuts_[statsBox_.targetEffStat];
      for (int ne=0; ne<2; ne++) {
	evt_.elec(ne).cutResult(statsBox_.targetEffStat,statCut->passesCut(evt_.elec(ne),keep->lastRandomLevel()));
      }
    }

    //------------------------------------------------------------------//
    // all what is before this point goes to a separate producer
    //                           ++ decouple ++
    // all what is after this point goes to a separate analyzer
    //------------------------------------------------------------------//
    
    bool pairing;
    
    if (pass==0) {
      if (!quiet_) evt_.dump();

      // selections done at first pass, no matter whether there are trials or not
      for (std::map<std::string,ZShapeZDef*>::const_iterator q=zdefs_.begin(); q!=zdefs_.end(); ++q) {
	// plots is EffHistos object pertaining to the present Z definition
	ZPlots* plots=zplots_[q->first];
	// acceptance is always the first cut
	if (!q->second->pass(evt_,1,1,0,&pairing)) continue;
	
	// fill standard histograms after acceptance
	if (!pairing) plots->acceptance_.Fill(evt_.elec(0), evt_.elec(1), evt_.elecTreeLevel(0).polarP4(), evt_.elecTreeLevel(1).polarP4()); 
	else plots->acceptance_.Fill(evt_.elec(1), evt_.elec(0), evt_.elecTreeLevel(1).polarP4(), evt_.elecTreeLevel(0).polarP4());      

	
	// next n-cuts
	bool ok=true;
	for (int j=1; ok && j<q->second->criteriaCount(ZShapeZDef::crit_E1); j++) {
	  ok=q->second->pass(evt_,j+1,j+1,0,&pairing);
          if (ok) 
            if (!pairing)  
              plots->postCut_[j-1].Fill(evt_.elec(0), evt_.elec(1), evt_.elecTreeLevel(0).polarP4(), evt_.elecTreeLevel(1).polarP4());
            else 
              plots->postCut_[j-1].Fill(evt_.elec(1), evt_.elec(0), evt_.elecTreeLevel(1).polarP4(), evt_.elecTreeLevel(0).polarP4());
	} // now the Z cuts
	for (int j=0; ok && j<q->second->criteriaCount(ZShapeZDef::crit_Z); j++) {
	  ok=q->second->pass(evt_,1000,1000,j+1,&pairing);
	  
          if (ok) 
            if (!pairing)  
              plots->zCut_[j].Fill(evt_.elec(0), evt_.elec(1), evt_.elecTreeLevel(0).polarP4(), evt_.elecTreeLevel(1).polarP4());
            else 
              plots->zCut_[j].Fill(evt_.elec(1), evt_.elec(0), evt_.elecTreeLevel(1).polarP4(), evt_.elecTreeLevel(0).polarP4());	
        }// criteria  
       
      }// Z definitions 
    }// end if pass==0 

    // selections specific in case of trials
    if (statsBox_.trials>0 && pass>0) { 
      for (std::map<std::string,ZShapeZDef*>::const_iterator q=zdefs_.begin(); q!=zdefs_.end(); ++q) {
     
	ZShapeZDef* zdef=q->second; 
	if (zdef->pass(evt_,zdef->criteriaCount(ZShapeZDef::crit_E1),zdef->criteriaCount(ZShapeZDef::crit_E2),0,&pairing)) { 
	  if (!pairing)  
	    statsBox_.hists[q->first][pass-1].Fill(evt_.elec(0), evt_.elec(1), evt_.elecTreeLevel(0).polarP4(), evt_.elecTreeLevel(1).polarP4()); 
	  else 
	    statsBox_.hists[q->first][pass-1].Fill(evt_.elec(1), evt_.elec(0), evt_.elecTreeLevel(1).polarP4(), evt_.elecTreeLevel(0).polarP4()); 
	}
      }
    }
    pass++;

  } while (statsBox_.trials>0 && pass<=statsBox_.trials);
  
  if (keep!=0) theCuts_[statsBox_.targetEffStat]=keep;
}

void ZEfficiencyCalculator::fillEvent(const reco::GenParticleCollection* ZeeParticles, 
				      const reco::GenParticleCollection* ZeeTreeLevelParticles) 
{
  
  using namespace reco;

  ////////////////////////
  // looking for electrons
  int myPid = 11;
  evt_.clear();
  int ne=0;
  int ngot[2]; ngot[0]=0; ngot[1]=0;
  
  GenParticleCollection::const_iterator me[2];
  math::XYZTLorentzVector elecs[2];

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


  // iterating over all particles checking if they fall in cone around electron 
  for(
      GenParticleCollection::const_iterator ZeeElectron_itr = ZeeParticles->begin();
      ZeeElectron_itr != ZeeParticles->end();
      ZeeElectron_itr++
      )
    {

      double dR=ROOT::Math::VectorUtil::DeltaR(me[0]->momentum(),ZeeElectron_itr->momentum()); 
      // if particle is ele_0 or falls in its cone, add 4momentum to the cone_0 
      if (me[0]==ZeeElectron_itr || dR<zElectronsCone_) {
	elecs[0]+=ZeeElectron_itr->p4();
	evt_.vtx_=math::XYZPoint(ZeeElectron_itr->vertex().x(),ZeeElectron_itr->vertex().y(),ZeeElectron_itr->vertex().z());
	ngot[0]++;
      } else {  // if particle is ele_1 or falls in its cone, add 4momentum to the cone_1
	dR=ROOT::Math::VectorUtil::DeltaR(me[1]->momentum(),ZeeElectron_itr->momentum());
	if (me[1]==ZeeElectron_itr || dR<zElectronsCone_) {
	  elecs[1]+=ZeeElectron_itr->p4();
	  ngot[1]++;
	}
      }
    }
  // storing cones as electrons 
  //(note: in case cones were fed in in the first place, they are used) 
  evt_.elec(0).p4_=elecs[0];
  evt_.elec(1).p4_=elecs[1];
  
  // end loop on particles
  evt_.n_elec=ne;

  
  /*
  std::cout << ngot[0] << "->" << elecs[0].energy() <<
    " " << elecs[0].eta() << " " << elecs[0].phi() << std::endl;
  std::cout << ngot[1] << "->" << elecs[1].energy() <<
    " " << elecs[1].eta() << " " << elecs[1].phi() << std::endl;
  */
  //
  // check than we have 2 and only 2 electrons
 
  if (ne!= 2)
    {
      edm::LogWarning("ZEfficiencyCalculator") << " we need two electrons (pid: " << myPid << " ) while we have: " << ne;
      return;
    }


  evt_.elec(0).detEta_=evt_.elec(0).detectorEta(evt_.vtx_);
  evt_.elec(1).detEta_=evt_.elec(1).detectorEta(evt_.vtx_);

  //
  // reorder electrons in pT
  float pt1 = evt_.elec(0).p4_.Pt();
  float pt2 = evt_.elec(1).p4_.Pt();

  // flipping order only if necessary
  if (pt2 > pt1){
    std::swap( evt_.elec(0), evt_.elec(1));
  }
  //  evt_.dump(std::cout);


  // take care of tree-level electrons 
  ne=0; 
  for(GenParticleCollection::const_iterator ZeeTreeLevelElectron_itr = ZeeTreeLevelParticles->begin(); 
      ZeeTreeLevelElectron_itr != ZeeTreeLevelParticles->end(); 
      ZeeTreeLevelElectron_itr++ 
      ){ 
    if (abs(ZeeTreeLevelElectron_itr->pdgId())==11)  
      { 
        if (ne<2) { 
          me[ne]=ZeeTreeLevelElectron_itr; 
          ne++; } 
      } 
  } 
   
  // end loop on particles 
  evt_.n_TLelec=ne;

  if (ne!= 2) 
    { 
      edm::LogWarning("ZEfficiencyCalculator") << " we need two tree-level electrons (pid: " << myPid << " ) while we have: " << ne; 
      return; 
    } 
 
  evt_.elecTreeLevel(0).setP4(me[0]->p4()); 
  evt_.elecTreeLevel(0).setCharge(me[0]->charge()); 
  evt_.elecTreeLevel(0).setVertex(me[0]->vertex()); 
  evt_.elecTreeLevel(0).setPdgId(me[0]->pdgId()); 
  evt_.elecTreeLevel(0).setStatus(me[0]->status()); 
 
  evt_.elecTreeLevel(1).setP4(me[1]->p4()); 
  evt_.elecTreeLevel(1).setCharge(me[1]->charge()); 
  evt_.elecTreeLevel(1).setVertex(me[1]->vertex()); 
  evt_.elecTreeLevel(1).setPdgId(me[1]->pdgId()); 
  evt_.elecTreeLevel(1).setStatus(me[1]->status());

  evt_.afterLoad();
}  
  





// ------------ method called once each job just before starting event loop  ------------
void 
ZEfficiencyCalculator::beginJob()
{
  // file to write out the histograms produced by the ZEfficiencyCalculator
  edm::Service<TFileService> fs;

  // one directory for histos of event before any selection
  TFileDirectory subDir=fs->mkdir("All");  
  allCase_.Book(subDir);

  const float maxY=5.5;
  const int yBinsPerUnit=4;

  accHistos_.ecal_ecal=subDir.make<TH1F>("ECAL-ECAL","ECAL-ECAL", int((maxY*2)*yBinsPerUnit), -maxY, maxY);
  accHistos_.ecal_ntrk=subDir.make<TH1F>("ECAL-NTRK","ECAL-NTRK", int((maxY*2)*yBinsPerUnit), -maxY, maxY);
  accHistos_.ecal_hf=subDir.make<TH1F>("ECAL-HF","ECAL-HF", int((maxY*2)*yBinsPerUnit), -maxY, maxY);
  accHistos_.ecal_noacc=subDir.make<TH1F>("ECAL-NOACC","ECAL-NOACC", int((maxY*2)*yBinsPerUnit), -maxY, maxY);
  accHistos_.ntrk_ntrk=subDir.make<TH1F>("NTRK-NTRK","NTRK-NTRK", int((maxY*2)*yBinsPerUnit), -maxY, maxY);
  accHistos_.ntrk_hf=subDir.make<TH1F>("NTRK-HF","NTRK-HF", int((maxY*2)*yBinsPerUnit), -maxY, maxY);
  accHistos_.ntrk_noacc=subDir.make<TH1F>("NTRK-NOACC","NTRK-NOACC", int((maxY*2)*yBinsPerUnit), -maxY, maxY);
  accHistos_.hf_hf=subDir.make<TH1F>("HF-HF","HF-HF", int((maxY*2)*yBinsPerUnit), -maxY, maxY);
  accHistos_.hf_noacc=subDir.make<TH1F>("HF-NOACC","HF-NOACC", int((maxY*2)*yBinsPerUnit), -maxY, maxY);
  accHistos_.noacc_noacc=subDir.make<TH1F>("NOACC-NOACC","NOACC-NOACC", int((maxY*2)*yBinsPerUnit), -maxY, maxY);  

  //
  // one directory for plots for each Z definition
  for (std::map<std::string,ZShapeZDef*>::const_iterator q=zdefs_.begin(); q!=zdefs_.end(); ++q) {
    
    // struct holding histograms for acc+all_cuts for each definition
    ZPlots* zplots=new ZPlots(q->second->criteriaCount(ZShapeZDef::crit_E1)-1,q->second->criteriaCount(ZShapeZDef::crit_Z)); // -1 for acceptance
    
    TFileDirectory sd = fs->mkdir(q->first.c_str());

    // organize in sub-directories in order to have histograms at each step

    TFileDirectory td = sd.mkdir("Acceptance");
    zplots->acceptance_.Book(td);


    // looping over cuts foreseen in given Z definition (for E1 and E2 simultaneously)
    for (int i=1; i<q->second->criteriaCount(ZShapeZDef::crit_E1); ++i) {
      char dirname[1024];
      std::string c1=q->second->criteria(ZShapeZDef::crit_E1,i);

      std::string c2=q->second->criteria(ZShapeZDef::crit_E2,i);

      // name is combination of the cut on E1 and E2, when both available
      if (c1==c2 || i>=q->second->criteriaCount(ZShapeZDef::crit_E2)) 
	sprintf(dirname,"C%02d-%s",i,c1.c_str());
      else 
	sprintf(dirname,"C%02d-%s-%s",i,c1.c_str(),c2.c_str());

      // one sub-dir for each step of selection
      td = sd.mkdir(dirname);
      zplots->postCut_[i-1].Book(td);
    }
    int iOffset=q->second->criteriaCount(ZShapeZDef::crit_E1);
    for (int i=0; i<q->second->criteriaCount(ZShapeZDef::crit_Z); ++i) {
      char dirname[1024];
      std::string c1=q->second->criteria(ZShapeZDef::crit_Z,i);

      sprintf(dirname,"C%02d-%s",i+iOffset,c1.c_str());

      // one sub-dir for each step of selection
      td = sd.mkdir(dirname);
      zplots->zCut_[i].Book(td);
    }    

    zplots_[q->first]=zplots;
  }
 
  // book trials histograms
  if (statsBox_.trials>0) {
    char dirname[1024];
    edm::LogInfo("ZShape") << "Making histograms for " << statsBox_.trials << " trials";
    std::map<std::string, ZShapeZDef*>::const_iterator defs;

    sprintf(dirname,"EffStats_%s",statsBox_.targetEffStat.c_str());     
    TFileDirectory pd = fs->mkdir(dirname);

    TH1* val=efficiencies_[statsBox_.targetEffStat]->getValuesHisto1D();

    snprintf(dirname,1024,"Variations_%s",statsBox_.targetEffStat.c_str());
    statsBox_.cutsProfile=pd.make<TProfile>(dirname,dirname,val->GetXaxis()->GetNbins(),val->GetXaxis()->GetXmin(),val->GetXaxis()->GetXmax());

    for (int j=0; j<statsBox_.trials;j++) {
      createAlternateEfficiencies(j, pd);
    }

    for (defs=zdefs_.begin(); defs!=zdefs_.end(); defs++) {
      TFileDirectory dd = pd.mkdir(defs->first);
      statsBox_.hists[defs->first]=std::vector<EffHistos>(statsBox_.trials);

      for (int j=0; j<statsBox_.trials;j++) {
	sprintf(dirname,"Trial%d",j+1);      
	TFileDirectory td = dd.mkdir(dirname);      
	statsBox_.hists[defs->first][j].Book(td);
      }
    }
  }





}


void ZEfficiencyCalculator::loadEfficiency(const std::string& name, const std::string& fname) {

  if (fname.find(".root")!=std::string::npos) {
    TFile effFile(fname.c_str(),"READ");
    
    edm::LogInfo("ZShape") << "Reading ROOT " << fname << " for efficiency " << name;
    EfficiencyStore* effs       = new EfficiencyStore(&effFile, name); //Will need to put in a third parameter for the effbin format here
    TH1F* histo = effs->getValuesHisto1D();
    EfficiencyCut* theCut  = new   EfficiencyCut(histo,effs->indexer());
    efficiencies_[name]=effs;
    theCuts_[name]=theCut;
  } else {
    edm::LogInfo("ZShape") << "Reading TEXT " << fname << " for efficiency " << name;
    EfficiencyStore* effs       = new EfficiencyStore(fname);
    TH1F* histo = effs->getValuesHisto1D();
    EfficiencyCut* theCut  = new   EfficiencyCut(histo,effs->indexer());
    efficiencies_[name]=effs;
    theCuts_[name]=theCut;
  }
}



// ------------ method called once each job just after ending the event loop  ------------
void 
ZEfficiencyCalculator::endJob() {
  
  // normalize matrix pre-cuts  
  allCase_.WrapUp(); 
  
  // looping over Z definitions 
  for (std::map<std::string,ZShapeZDef*>::const_iterator q=zdefs_.begin(); q!=zdefs_.end(); ++q) { 
    
    zplots_[q->first]->acceptance_.WrapUp(); 
    
    // looping over cuts foreseen in given Z definition, normalize matrix for each (Zdef,cut) 
    //    for (int i=1; i<q->second->criteriaCount(ZShapeZDef::crit_E1); ++i) { 
    for (unsigned int i=1; i<=zplots_[q->first]->postCut_.size(); ++i) { 
      
      zplots_[q->first]->postCut_[i-1].WrapUp(); 
      
    }// cuts of given z definition 
    for (unsigned int i=0; i<zplots_[q->first]->zCut_.size(); ++i) { 
      
      zplots_[q->first]->zCut_[i].WrapUp(); 
      
    }// cuts of given z definition 
  }// Z definitions 
  
}

void ZEfficiencyCalculator::createAlternateEfficiencies(int cycle,TFileDirectory& fd) {
  EfficiencyStore* es=efficiencies_[statsBox_.targetEffStat];

  // the target efficiency to be smeared 
  TH1* val=es->getValuesHisto1D();
  TH1* denom=es->getDenominatorHisto1D();

  char name[1024];
  snprintf(name,1024,"StatEff_%s_%d",statsBox_.targetEffStat.c_str(),cycle+1);
  TH1F* randy=fd.make<TH1F>(name,name,val->GetXaxis()->GetNbins(),val->GetXaxis()->GetXmin(),val->GetXaxis()->GetXmax());

  for (int j=1; j<=val->GetXaxis()->GetNbins(); j++) {
    double ave=val->GetBinContent(j);
    int den=int(denom->GetBinContent(j));
    double rv=0;
    if (den>0 && ave>0) { // HACK! (ave should be able to be zero) 
      EfficiencyStatistics esd(ave,den);
      esd.setRandom(&randomNum);
      rv=esd.rand();
    }
    randy->Fill(val->GetBinCenter(j),rv);
    statsBox_.cutsProfile->Fill(val->GetBinCenter(j),rv);
  }
  statsBox_.rawHists.push_back(randy);
  statsBox_.alternateCuts.push_back(new EfficiencyCut(randy,es->indexer()));
}


void ZEfficiencyCalculator::createAlternateZDefs(const std::string& targetZDefSys, const std::string& targetEffSys) {
  
  EfficiencyStore* targetEff;
  ZShapeZDef*      targetZDef;
  targetEff=0; targetZDef=0;

  if (zdefs_.find(targetZDefSys)!=zdefs_.end())
    targetZDef=zdefs_[targetZDefSys];
  else
    edm::LogError("ZShape") << "Unable to find Z-definition '" <<targetZDefSys << "' for systematic variations!";
  
  if (efficiencies_.find(targetEffSys)!=efficiencies_.end())
    targetEff=efficiencies_[targetEffSys];
  else
    edm::LogError("ZShape") << "Unable to find efficiency '" <<targetEffSys << "' for systematic variations!";
  
  // checking that target ZDef and Eff are among the existing
  if (!targetZDef || !targetEff) return;

  // defining the two modified cuts: +syst and -syst
  TH1* val  =targetEff->getValuesHisto1D();
  TH1* plus =targetEff->getSystPlusHisto1D();
  TH1* minus=targetEff->getSystMinusHisto1D();

  char name[1024];
  snprintf(name,1024,"%s_SysPlus",targetEffSys.c_str());
  TH1F* dPlusH=new TH1F(name,name,val->GetXaxis()->GetNbins(),val->GetXaxis()->GetXmin(),val->GetXaxis()->GetXmax());
  std::string dPlusName(name);

  snprintf(name,1024,"%s_SysMin",targetEffSys.c_str());
  TH1F* dMinusH=new TH1F(name,name,val->GetXaxis()->GetNbins(),val->GetXaxis()->GetXmin(),val->GetXaxis()->GetXmax());
  std::string dMinusName(name);
  
  for (int j=1; j<=val->GetXaxis()->GetNbins(); j++) {
    double ave=val->GetBinContent(j);
    double dPlus=plus->GetBinContent(j);
    double dMinus=minus->GetBinContent(j);
    dPlusH ->Fill(val->GetBinCenter(j), ave+dPlus);
    dMinusH->Fill(val->GetBinCenter(j), ave+dMinus);
  }

  EfficiencyCut* thePlusCut  = new   EfficiencyCut(dPlusH, targetEff->indexer());
  EfficiencyCut* theMinusCut  = new   EfficiencyCut(dMinusH, targetEff->indexer());
  theCuts_[dPlusName]=thePlusCut;
  theCuts_[dMinusName]=theMinusCut;

  // two new ZDefinitions: all cuts stay the same except target Eff which gets +syst and -syst
  ZShapeZDef* zDefPlus=new ZShapeZDef();
  ZShapeZDef* zDefMinus=new ZShapeZDef();
  
  for (int i=0; i<targetZDef->criteriaCount(ZShapeZDef::crit_E1); i++){
    std::string criterion = targetZDef->criteria(ZShapeZDef::crit_E1, i);
    if (criterion==targetEffSys){	
      zDefPlus ->addCriterion(ZShapeZDef::crit_E1,dPlusName);
      zDefMinus->addCriterion(ZShapeZDef::crit_E1,dMinusName);
    }
    else{
      zDefPlus ->addCriterion(ZShapeZDef::crit_E1,criterion);
      zDefMinus->addCriterion(ZShapeZDef::crit_E1,criterion);
    }
  }
  
  
  for (int i=0; i<targetZDef->criteriaCount(ZShapeZDef::crit_E2); i++){
    std::string criterion = targetZDef->criteria(ZShapeZDef::crit_E2, i);
    if (criterion==targetEffSys){	
      zDefPlus ->addCriterion(ZShapeZDef::crit_E2,dPlusName);
      zDefMinus->addCriterion(ZShapeZDef::crit_E2,dMinusName);
    }
    else{
      zDefPlus ->addCriterion(ZShapeZDef::crit_E2,criterion);
      zDefMinus->addCriterion(ZShapeZDef::crit_E2,criterion);
    }
  }  

  // adding 2 new ZDefs to standard list
  snprintf(name,1024,"%s-SysPlus_%s",targetZDefSys.c_str(),targetEffSys.c_str());
  std::string dPlusNameZ(name);
  snprintf(name,1024,"%s-SysMinus_%s",targetZDefSys.c_str(),targetEffSys.c_str());
  std::string dMinusNameZ(name);
  zdefs_[dPlusNameZ]=zDefPlus;
  zdefs_[dMinusNameZ]=zDefMinus;
  
}




//define this as a plug-in
DEFINE_FWK_MODULE(ZEfficiencyCalculator);
