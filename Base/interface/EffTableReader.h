//  Adapted From:
//----------------
// Original Author:  Fedor Ratnikov Nov 9, 2007
// $Id: EffTableReader.h,v 1.2 2013/02/20 20:45:18 klapoet Exp $
//-----------------------------------------------------------------------


#ifndef EffTableReader_h
#define EffTableReader_h

#include <string>
#include <vector>

class EffTableReader {
 public:
  static int magic_debug;

  class Record {
  public:
    Record () : mEtaMin (0), mEtaMax (0), mEtMax(0), mEtMin(0), mPUmin(0),mPUmax(0) {}
      Record (float fEtaMin, float fEtaMax, float fEtMax, float fEtMin, float fPUmin, float fPUmax, const std::vector<float>& fParameters) 
	: mEtaMin (fEtaMin), mEtaMax (fEtaMax), mEtMax (fEtMax), mEtMin (fEtMin),mPUmin(fPUmin),mPUmax(fPUmax), mParameters (fParameters) {}
    Record (const std::string& fLine);
    float psMin() const {return mEtMin;}
    float psMax() const {return mEtMax;}
    float etaMin() const {return mEtaMin;}
    float etaMax() const {return mEtaMax;}
    float  EtMin() const {return mEtMin;}
    float  EtMax() const {return mEtMax;}
    float PUmin() const {return mPUmin;}
    float PUmax() const {return mPUmax;}
    float Eff() const {return mEff;}
    bool doPhistar() const {return mDoPS;}
    float etaMiddle() const {return 0.5*(etaMin()+etaMax());}
    float  EtMiddle() const {return 0.5*(EtMin()+EtMax());}
    float PUmiddle()const {return 0.5*(PUmin()+ PUmax());}
    unsigned nParameters() const {return mParameters.size();}
    float parameter (unsigned fIndex) const {return mParameters [fIndex];}
    std::vector<float> parameters () const {return mParameters;}
    int operator< (const Record& other) const {return etaMin() < other.etaMin();}
  private:
    float mEtaMin;
    float mEtaMax;
    float mEtMax;
    float mEtMin;
    float mPUmin;
    float mPUmax;
    bool mDoPS;
    float mEff;
    std::vector<float> mParameters;
  };

  EffTableReader () {}
  EffTableReader (const std::string& fFile);
  
  /// total # of bands
  size_t size () const {return mRecords.size();}
  /// get band index for eta and Et
  int bandIndex(float fEt, float fEta, float fPU, float fPS) const;
  /// get record for the band 
  const Record& record (unsigned fBand) const {return mRecords[fBand];}
  private:
  std::vector <Record> mRecords;
};

#endif
