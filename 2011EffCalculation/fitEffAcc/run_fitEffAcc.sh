#!/bin/bash

#Input Files
fits='fits_delta.txt'
signal="/local/cms/user/gude/kevin_mc_smearing/FullSimSmeared_effac_ZEffTree/FullSimSmeared_effac_ZEffTree_summed.root"
#zefftree="/local/cms/user/gude/zshape/makezefftree_skimReReco_20120229/makezefftree_skimReReco_20120229_summed.root"
zefftree="/local/cms/user/gude/2012_kevin_thesis_eff/double_electron_trigger_matched/double_electron_trigger_matched_summed.root"

#Mass_Z
mz_low=50
mz_high=150

#Run the fits
##EB EB
tag="EB"
probe="EB"
###PU 0-4
pu_low=0
pu_high=4
####pt 20-30
pt_low=20
pt_high=30
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
echo "./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high"
exit 0
####pt 30-40
pt_low=30
pt_high=40
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 40-55
pt_low=40
pt_high=55
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 55-70
pt_low=55
pt_high=70
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 70-100
pt_low=70
pt_high=100
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
###PU 5-10
pu_low=5
pu_high=10
####pt 20-25
pt_low=20
pt_high=30
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 25-40
pt_low=30
pt_high=40
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 40-55
pt_low=40
pt_high=55
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 55-70
pt_low=55
pt_high=70
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 70-100
pt_low=70
pt_high=100
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
###PU 11-20
pu_low=11
pu_high=20
####pt 20-100
pt_low=20
pt_high=100
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high

#Run the fits
##EB EE
tag="EB"
probe="EE"
###PU 0-4
pu_low=0
pu_high=4
####pt 20-30
pt_low=20
pt_high=30
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 30-40
pt_low=30
pt_high=40
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 40-55
pt_low=40
pt_high=55
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 55-70
pt_low=55
pt_high=70
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 70-100
pt_low=70
pt_high=100
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
###PU 5-10
pu_low=5
pu_high=10
####pt 20-25
pt_low=20
pt_high=30
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 25-40
pt_low=30
pt_high=40
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 40-55
pt_low=40
pt_high=55
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 55-70
pt_low=55
pt_high=70
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 70-100
pt_low=70
pt_high=100
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
###PU 11-20
pu_low=11
pu_high=20
####pt 20-100
pt_low=20
pt_high=100
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high

#Run the fits
##EB NT
tag="EB"
probe="NT"
###PU 0-4
pu_low=0
pu_high=4
####pt 20-30
pt_low=20
pt_high=30
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 30-40
pt_low=30
pt_high=40
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 40-55
pt_low=40
pt_high=55
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 55-70
pt_low=55
pt_high=70
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 70-100
pt_low=70
pt_high=100
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
###PU 5-10
pu_low=5
pu_high=10
####pt 20-25
pt_low=20
pt_high=30
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 25-40
pt_low=30
pt_high=40
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 40-55
pt_low=40
pt_high=55
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 55-70
pt_low=55
pt_high=70
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 70-100
pt_low=70
pt_high=100
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
###PU 11-20
pu_low=11
pu_high=20
####pt 20-100
pt_low=20
pt_high=100
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high

#Run the fits
##EB HF
tag="EB"
probe="HF"
###PU 0-4
pu_low=0
pu_high=4
####pt 20-30
pt_low=20
pt_high=30
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 30-40
pt_low=30
pt_high=40
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 40-55
pt_low=40
pt_high=55
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 55-70
pt_low=55
pt_high=70
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 70-100
pt_low=70
pt_high=100
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
###PU 5-10
pu_low=5
pu_high=10
####pt 20-25
pt_low=20
pt_high=30
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 25-40
pt_low=30
pt_high=40
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 40-55
pt_low=40
pt_high=55
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 55-70
pt_low=55
pt_high=70
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
####pt 70-100
pt_low=70
pt_high=100
outfile="eff_fit_output/${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
