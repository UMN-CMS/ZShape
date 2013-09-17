#!/bin/tcsh -f
############################################################
# You need to change the default location of the root files
############################################################
#The only option allows you to use different number 1, 10, 37 etc.
#############3

set TP="/data/whybee1a/user/haupt/Electrons/TNPTREE10"
set numb=""
set mnumb=""
if ($#argv > 0) then
    echo " ha ha, we have two args "
    set numb="_${1}"
    set mnumb="${1}"
endif
echo $numb

#First we turn the root files into text files

effFitRoot2Txt $TP/testEff_GSFToInvWP80.root Fit$numb.txt Iso pt_eta -2.5 2.5 1 0
effFitRoot2Txt $TP/testEff_GSFToInvWP80.root FitPt$numb.txt Iso pt -2.5 2.5 1 0
effFitRoot2Txt $TP/testEff_GSFToInvWP80.root FitEta$numb.txt Iso eta 20 120 1 0

#The NT and HF are different as the Sig and Bkg have split backgrounds (Pass/Fail)
#This means we can use either the signal or the background PDF, SC or EID...
#I am opting to use JUST the signal PDF. However this means that I need two templates
#as the GSF one uses 'alpha' and the split one uses 'alpha1','alpha2'. 
#I COULD JUST USE ONE TEMPLATE and set this as a parameter... I will think about it

effFitRoot2Txt $TP/testEff_NTToInvWP80TEST.root NTFit$numb.txt Iso pt_eta -2.9 2.9 0 1
effFitRoot2Txt $TP/testEff_NTToInvWP80TEST.root NTFitPt$numb.txt Iso pt -2.9 2.9 0 1
effFitRoot2Txt $TP/testEff_NTToInvWP80TEST.root NTFitEta$numb.txt Iso eta 20 120 0 1

effFitRoot2Txt $TP/testEff_HFToInvWP80TEST.root HFFit$numb.txt Iso pt_eta -2.5 2.5 0 1
effFitRoot2Txt $TP/testEff_HFToInvWP80TEST.root HFFitPt$numb.txt Iso pt -2.5 2.5 0 1
effFitRoot2Txt $TP/testEff_HFToInvWP80TEST.root HFFitEta$numb.txt Iso eta 20 120 0 1

#NEXT NEXT  
#Then we use templates to run the background text into configuration language.

effFitConfig SigFit.txt 0 template.py 0 ouputconfSGNEW.py 0
effFitConfig SigFitEta.txt 0 template.py 0 ouputconfSGNEWEta.py 0
effFitConfig SigFitPt.txt 0 template.py 0 ouputconfSGNEWPt.py 0

effFitConfig BkgNTFit.txt 0 templateSPLITNT.py 0 ouputconfSGNEWNT.py 0
effFitConfig BkgNTFitEta.txt 0 templateSPLITNT.py 0 ouputconfSGNEWNTEta.py 0
effFitConfig BkgNTFitPt.txt 0 templateSPLITNT.py 0 ouputconfSGNEWNTPt.py 0

effFitConfig BkgHFFit.txt 0 templateSPLITHF.py 0 ouputconfSGNEWHF.py 0
effFitConfig BkgHFFitEta.txt 0 templateSPLITHF.py 0 ouputconfSGNEWHFEta.py 0
effFitConfig BkgHFFitPt.txt 0 templateSPLITHF.py 0 ouputconfSGNEWHFPt.py 0

##Now for the final ones
####################Now for the final ones.
effFitRoot2Txt $TP/testEff_INVFINAL.root FinalFit$numb.txt Iso rap -2.5 2.5 1 0
effFitConfig SigFinalFit.txt 0 template.py 0 ouputconfSGFINAL.py 0

effFitRoot2Txt $TP/testEff_INVFINALHF.root HFFinalFit$numb.txt Iso rap -2.5 2.5 0 1
effFitConfig BkgHFFinalFit.txt 0 templateHF.py 0 ouputconfSGFINALHF.py 0


#end of this silly script

