#!/bin/tcsh -f
########################################
# Input and outpur directory arguments
#
#
########################################

set outdir=$1
set filetype=$2
set deffile="/home/grad/haupt/CMSSW/ZShape/CMSSW_3_6_5/src/ZShape/EffAcc/data"

root -l -b <<!
#include <map>
typedef std::vector<std::string> zdef;
gROOT->SetStyle("Plain");
gStyle->SetPalette(1);
gStyle->SetOptStat(10);
.L tdrstyle.C
setTDRStyle();

zdef zdefvec;

std::cout << " I'm Trying here " << std::endl;
std::map<std::string, zdef> zdefvecvec;
//zdefvec.push_back("Tight-EB-Loose-ECAL");
//zdefvec.push_back("Tight-ECAL-Loose-EE");
zdefvec.push_back("Tight-ECAL-Loose-ECAL"); 
zdefvec.push_back("Tight-ECAL-HF");
//zdefvec.push_back("Golden-EB-EB");


gStyle->SetTitleAlign(22);

.L compareEffAcc.C+
//81.17
//8.0593665
//16.118733
//6.88835 for M20.... (cross fingers)...
//13.7767
//4.6675 For original Summer09
//4.88 or 5.0057
//2.4153439 for the combined
//3.9 For the full full but some must not have gone, so 4.031

EffAccHistos *myEffAccHistos = new EffAccHistos("/data/whybee0c/user/haupt/Electrons/TNPTREE10/ZeeFromDataJeremyTEMPLATE/histoJason10_only1hlt_TRIAL_ZFULL.root","/data/whybee0c/user/haupt/Electrons/TNPTREE10/ZeeFromDataJeremyTEMPLATE/TFSCPairSkimmer2-ZSKIM3_047-ZFDBEAM10.root",zdefvec, 1.0);
myEffAccHistos->getFiles();
myEffAccHistos->getHistos();
myEffAccHistos->printSumHistos("${filetype}");
myEffAccHistos->printIndividualHistos("${filetype}");
myEffAccHistos->MakeResultFiles("${deffile}");

!

##echo "now we are making the webpages"
if (! -d $outdir) then
mkdir ${outdir}
endif

if (! -d $outdir/Compare ) then
mkdir ${outdir}/Compare
endif

if (! -d $outdir/FinalCompare ) then
mkdir ${outdir}/FinalCompare
endif

cp Z* ${outdir}/.

mv ${outdir}/Z_Compare* ${outdir}/Compare/.
./makeEffAccWebPage.csh ${outdir} ${filetype}


echo "That's all folks"
rm Z*${filetype}

##End of Efficiency*Acceptance Script
