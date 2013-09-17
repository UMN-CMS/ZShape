  
#thisdir=${HOME}/CMSSW/ZShape/CMSSW_3_8_4_patch3/src/PhysicsTools/TagAndProbe/test/CRAB
template=FullFitTreeAnalyzer_cfg.py
#thatdir=${HOME}/CMSSW/ZShape/CMSSW_3_8_4_patch3/src/PhysicsTools/TagAndProbe/test/CRAB
thisdir=`pwd`
thatdir=`pwd`

#process.fit = cms.Path(process.TPFTAGSFToISO + process.TPFTAHFSCToEID + process.TPFTAHFSCToEIDT +
#                       process.TPFTASCToGSF + process.TPFTAGSFToISO80 +   process.TPFTAISOToID +
#                       process.TPFTAISOToID80 + process.TPFTAIDToHLT + process.TPFTAIDToHLT80 +
#                       process.TPFTAGSFToWP95 + process.TPFTAGSFToWP90 + process.TPFTAGSFToWP85 +
#                       process.TPFTAGSFToWP80 + process.TPFTAGSFToWP70 + process.TPFTAGSFToWP60 +
#                       process.TPFTAGSFToInvWP80 + process.TPFTASCToNTEID + process.TPFTASCToNTEIDT +
#                       process.TPFTASCToInvWP80 )

# GSFToISO HFSCToEID HFSCToEIDT SCToGSF GSFToISO80 ISOToID ISOToID80 IDToHLT IDToHLT80 GSFToWP95 GSFToWP90 GSFToWP85 GSFToWP80 GSFToWP70 GSFToWP60 GSFToInvWP80 SCToNTEID SCToNTEIDT SCToInvWP80 NTToInvWP80 HFToInvWP80 FINAL FHF FNTT

runtype=$1
shift

for numb in $@
    do
    #fabs=${numb/-/m}
    #cleannumb=${fabs/./_}
    name=EffFit_cfg.py
  
    cp $thisdir/$template $thatdir/$name
    sed -i "s/xxVALUExx/$numb/g" $thatdir/$name
    if [ $runtype == 0 ]
	then
	echo "first fitting method, using default parameters"
	for myinp in xxInputPtBinnedPDFsxx xxInputEtaBinnedPDFsxx xxInputPtEtaBinnedPDFsxx xxInputHFPtBinnedPDFsxx xxInputHFEtaBinnedPDFsxx xxInputHFPtEtaBinnedPDFsxx xxInputNTPtBinnedPDFsxx xxInputNTEtaBinnedPDFsxx xxInputNTPtEtaBinnedPDFsxx xxInputRapBinnedPDFsxx  xxInputHFRapBinnedPDFsxx
	do
	    sed -i "s/$myinp//g" $thatdir/$name
	done
	for myinp in xxPtBinMapxx xxEtaBinMapxx xxPtEtaBinMapxx xxHFPtBinMapxx xxHFEtaBinMapxx xxHFPtEtaBinMapxx xxNTPtBinMapxx xxNTEtaBinMapxx xxNTPtEtaBinMapxx  xxRapBinMapxx xxHFRapBinMapxx
	do
	    sed -i "s/$myinp/'voigtPlusBKG'/g" $thatdir/$name
	done
	
	
    fi
    if [ $runtype == 1 ]
	then
	mytemp=mytemp.py
        mytemp2=mytemp2.py

	replaceFileParameterWithFileContent $thatdir/$name $mytemp xxInputPtBinnedPDFsxx  ouputconfSGNEWPt.py
	replaceFileParameterWithFileContent $mytemp $mytemp2 xxPtBinMapxx  mapouputconfSGNEWPt.py

	cp $mytemp2 $thatdir/$name

	replaceFileParameterWithFileContent $thatdir/$name $mytemp xxInputEtaBinnedPDFsxx  ouputconfSGNEWEta.py
	replaceFileParameterWithFileContent $mytemp $mytemp2 xxEtaBinMapxx  mapouputconfSGNEWEta.py

	cp $mytemp2 $thatdir/$name

	replaceFileParameterWithFileContent $thatdir/$name $mytemp xxInputPtEtaBinnedPDFsxx  ouputconfSGNEW.py
	replaceFileParameterWithFileContent $mytemp $mytemp2 xxPtEtaBinMapxx  mapouputconfSGNEW.py

	cp $mytemp2 $thatdir/$name

	replaceFileParameterWithFileContent $thatdir/$name $mytemp xxInputHFPtBinnedPDFsxx  ouputconfSGNEWHFPt.py
	replaceFileParameterWithFileContent $mytemp $mytemp2 xxHFPtBinMapxx  mapouputconfSGNEWHFPt.py

	cp $mytemp2 $thatdir/$name

	replaceFileParameterWithFileContent $thatdir/$name $mytemp xxInputHFEtaBinnedPDFsxx  ouputconfSGNEWHFEta.py
	replaceFileParameterWithFileContent $mytemp $mytemp2 xxHFEtaBinMapxx  mapouputconfSGNEWHFEta.py

	cp $mytemp2 $thatdir/$name

	replaceFileParameterWithFileContent $thatdir/$name $mytemp xxInputHFPtEtaBinnedPDFsxx  ouputconfSGNEWHF.py
	replaceFileParameterWithFileContent $mytemp $mytemp2 xxHFPtEtaBinMapxx  mapouputconfSGNEWHF.py

	cp $mytemp2 $thatdir/$name

	replaceFileParameterWithFileContent $thatdir/$name $mytemp xxInputNTPtBinnedPDFsxx  ouputconfSGNEWNTPt.py
	replaceFileParameterWithFileContent $mytemp $mytemp2 xxNTPtBinMapxx  mapouputconfSGNEWNTPt.py

	cp $mytemp2 $thatdir/$name

	replaceFileParameterWithFileContent $thatdir/$name $mytemp xxInputNTEtaBinnedPDFsxx  ouputconfSGNEWNTEta.py
	replaceFileParameterWithFileContent $mytemp $mytemp2 xxNTEtaBinMapxx  mapouputconfSGNEWNTEta.py

	cp $mytemp2 $thatdir/$name

	replaceFileParameterWithFileContent $thatdir/$name $mytemp xxInputNTPtEtaBinnedPDFsxx  ouputconfSGNEWNT.py
	replaceFileParameterWithFileContent $mytemp $mytemp2 xxNTPtEtaBinMapxx  mapouputconfSGNEWNT.py

	cp $mytemp2 $thatdir/$name

	replaceFileParameterWithFileContent $thatdir/$name $mytemp xxInputRapBinnedPDFsxx  ouputconfSGFINAL.py
	replaceFileParameterWithFileContent $mytemp $mytemp2 xxRapBinMapxx  mapouputconfSGFINAL.py

	cp $mytemp2 $thatdir/$name

	replaceFileParameterWithFileContent $thatdir/$name $mytemp xxInputHFRapBinnedPDFsxx ouputconfSGFINALHF.py
	replaceFileParameterWithFileContent $mytemp $mytemp2 xxHFRapBinMapxx  mapouputconfSGFINALHF.py

	cp $mytemp2 $thatdir/$name

	#echo "using default parameters for HF and NT for the moment"
	#for myinp in xxInputHFPtBinnedPDFsxx xxInputHFEtaBinnedPDFsxx xxInputHFPtEtaBinnedPDFsxx xxInputNTPtBinnedPDFsxx xxInputNTEtaBinnedPDFsxx xxInputNTPtEtaBinnedPDFsxx
	#do
	#    sed -i "s/$myinp//g" $thatdir/$name
	#done
	#for myinp in xxHFPtBinMapxx xxHFEtaBinMapxx xxHFPtEtaBinMapxx xxNTPtBinMapxx xxNTEtaBinMapxx xxNTPtEtaBinMapxx 
	#do
	#    sed -i "s/$myinp/'voigtPlusBKG'/g" $thatdir/$name
	#done

	rm $mytemp
	rm $mytemp2
    fi
    if [ $runtype == 2 ]
	then
	echo "first fitting method, using default parameters"
	for myinp in xxInputPtBinnedPDFsxx xxInputEtaBinnedPDFsxx xxInputPtEtaBinnedPDFsxx xxInputHFPtBinnedPDFsxx xxInputHFEtaBinnedPDFsxx xxInputHFPtEtaBinnedPDFsxx xxInputNTPtBinnedPDFsxx xxInputNTEtaBinnedPDFsxx xxInputNTPtEtaBinnedPDFsxx xxInputRapBinnedPDFsxx  xxInputHFRapBinnedPDFsxx
	do
	    sed -i "s/$myinp//g" $thatdir/$name
	done
	for myinp in xxPtBinMapxx xxEtaBinMapxx xxPtEtaBinMapxx xxHFPtBinMapxx xxHFEtaBinMapxx xxHFPtEtaBinMapxx xxNTPtBinMapxx xxNTEtaBinMapxx xxNTPtEtaBinMapxx 
	do
	    sed -i "s/$myinp/'voigtPlusBKG'/g" $thatdir/$name
	done
	sed -i "s/xxHFRapBinMapxx/'voigtPlusBKGHFALLFIXED'/g" $thatdir/$name
	sed -i "s/xxRapBinMapxx/'voigtPlusBKGBKGFIXED'/g" $thatdir/$name
	
	
    fi
    if [ $runtype == 3 ]
	then
	echo "first fitting method, using default parameters"
	for myinp in xxInputPtBinnedPDFsxx xxInputEtaBinnedPDFsxx xxInputPtEtaBinnedPDFsxx xxInputHFPtBinnedPDFsxx xxInputHFEtaBinnedPDFsxx xxInputHFPtEtaBinnedPDFsxx xxInputNTPtBinnedPDFsxx xxInputNTEtaBinnedPDFsxx xxInputNTPtEtaBinnedPDFsxx xxInputRapBinnedPDFsxx  xxInputHFRapBinnedPDFsxx
	do
	    sed -i "s/$myinp//g" $thatdir/$name
	done
	for myinp in xxPtBinMapxx xxEtaBinMapxx xxPtEtaBinMapxx xxHFPtBinMapxx xxHFEtaBinMapxx xxHFPtEtaBinMapxx xxNTPtBinMapxx xxNTEtaBinMapxx xxNTPtEtaBinMapxx 
	do
	    sed -i "s/$myinp/'voigtPlusBKG'/g" $thatdir/$name
	done
	sed -i "s/xxHFRapBinMapxx/'ZlinePlusBKGHFALLFIXED'/g" $thatdir/$name
	sed -i "s/xxRapBinMapxx/'ZlinePlusBKGBKGFIXED'/g" $thatdir/$name
	
	
    fi

    #Submit The JOBS
    ${HOME}/bin/condor_onePy.perl $numb EffFit_cfg.py $numb 1

    rm EffFit_cfg.py
    # sed -i "s/xxxx/$/g" $thatdir/$name
done
