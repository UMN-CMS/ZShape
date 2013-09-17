//---------------------------------------------------------------------------
// Adapted From Following Description:
// Original Author:  Fedor Ratnikov Nov 9, 2007
// $Id: EffTableReader.cc,v 1.3 2013/02/20 20:45:18 klapoet Exp $
// Generic parameters for Jet corrections
//----------------------------------------------------------------------------
#include "ZShape/Base/interface/EffTableReader.h"
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include "FWCore/Utilities/interface/Exception.h"

namespace {
  float getFloat (const std::string& token) {
    char* endptr;
    float result = strtod (token.c_str(), &endptr);
    if (endptr == token.c_str()) {
     throw cms::Exception ("SimpleEffCorrectorParameters")
	<< "can not convert token " << token << " to float value";
    }
    return result;
  }
  unsigned getUnsigned (const std::string& token) {
    char* endptr;
    unsigned result = strtoul (token.c_str(), &endptr, 0);
    if (endptr == token.c_str()) {
     throw cms::Exception ("SimpleEffCorrectorParameters") 
	<< "can not convert token " << token << " to unsigned value";
     throw "EffTableReader: failed to convert token to unsigned value";
  }
    return result;
  }
}


int EffTableReader::magic_debug=0;

EffTableReader::Record::Record (const std::string& fLine) 
  : mEtaMin (0), mEtaMax (0), mEtMax(0), mEtMin(0),mPUmin(0),mPUmax(0) 
{
  // quckly parse the line
  std::vector<std::string> tokens;
  std::string currentToken;
  for (unsigned ipos = 0; ipos < fLine.length (); ++ipos) {
    char c = fLine[ipos];
    if (c == '#') break; // ignore comments
    else if (c == ' ') { // flush current token if any
      if (!currentToken.empty()) {
	tokens.push_back (currentToken);
	currentToken.clear();
      }
    }
    else {
      currentToken += c;
    }
  }
  if (!currentToken.empty()) tokens.push_back (currentToken); // flush end
  if (!tokens.empty ()) { // pure comment line
    if (tokens.size() < 5) {
      throw cms::Exception ("EffTableReader") << "at least 7 tokens are expected: minEta, maxEta,"
					      <<  " minEt, maxEt , minPU, maxPU,  # of parameters.," 
					      << tokens.size() << " are provided.\n" 
					      << "Line ->>" << fLine << "<<-";  
    } 
    else if (tokens.size() >= 11){
      // get parameters
      mEtMin = getFloat (tokens[0]);
      mEtMax = getFloat (tokens[1]);
      mEtaMin = getFloat (tokens[2]);
      mEtaMax = getFloat (tokens[3]);
      mPUmin = getFloat (tokens[4]);
      mPUmax = getFloat (tokens[5]);
      mEff=getFloat (tokens[7]);
      unsigned nParam = getUnsigned (tokens[6]);
      if(tokens.size() >= 12){
	unsigned psdo= getUnsigned (tokens[11]);
	mDoPS=((psdo==0)?(false):(true));
      }else{mDoPS=false;}
      if (nParam != tokens.size() - 7) {
	throw cms::Exception ("EffTableReader") << "Actual # of parameters " 
						<< tokens.size() - 7 
						<< " doesn't correspond to requested #: " << nParam << "\n"
						<< "Line ->>" << fLine << "<<-";  
      }
      for (unsigned i = 6; i < tokens.size(); ++i) {
	mParameters.push_back (getFloat (tokens[i]));
      }
      
    }//end token ==11
   
    else if (tokens.size() == 9){
      // get parameters
      mDoPS=false;
      mEtMin = getFloat (tokens[0]);
      mEtMax = getFloat (tokens[1]);
      mEtaMin = getFloat (tokens[2]);
      mEtaMax = getFloat (tokens[3]);
      mPUmin = 0;
      mPUmax = 100;
      mEff=getFloat (tokens[5]);
      unsigned nParam = getUnsigned (tokens[4]);
      if (nParam != tokens.size() - 5) {
	throw cms::Exception ("EffTableReader") << "Actual # of parameters " 
						<< tokens.size() - 7 
						<< " doesn't correspond to requested #: " << nParam << "\n"
						<< "Line ->>" << fLine << "<<-";  
      }
      for (unsigned i = 4; i < tokens.size(); ++i) {
	mParameters.push_back (getFloat (tokens[i]));
      }
      
    } 
    
  }//end !token=empty
}


EffTableReader::EffTableReader (const std::string& fFile) {
  std::ifstream input (fFile.c_str());
  std::string line;
  while (std::getline (input, line)) {
    Record record (line);
    if (!(record.etaMin() == 0. && record.etaMax() == 0. && record.nParameters() == 0)) {
      mRecords.push_back (record);
    }
  }
  if (mRecords.empty()) mRecords.push_back (Record ());

}


int EffTableReader::bandIndex (float fEt, float fEta, float fPU, float fPS) const{
  int bandInd = -1; //new default value says it isn't in a band (bin)
  float val;
  for (unsigned i = 0; i < mRecords.size(); ++i) {
    if(mRecords[i].doPhistar()){
      val=fPS;
    }else{
      val=fEt;
    }

    if (magic_debug==5) {
      printf("%da %.2f %.2f %.2f \n",i,val,mRecords[i].EtMin(),mRecords[i].EtMax());
    }

    if(val>=mRecords[i].EtMin() && val<mRecords[i].EtMax()){
      if (magic_debug==5) printf("%db %.2f %.2f %.2f \n",i,fEta,mRecords[i].etaMin(),mRecords[i].etaMax());
      if(fEta>=mRecords[i].etaMin() && fEta<mRecords[i].etaMax()){
      if (magic_debug==5) printf("%dc %.2f %.2f %.2f \n",i,fPU,mRecords[i].PUmin(),mRecords[i].PUmax());
	if(fPU>=mRecords[i].PUmin() && fPU<mRecords[i].PUmax()){
	  bandInd=i;
	  break;                        
	}
      }
    }
  }
  return bandInd;
}

