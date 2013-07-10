#!/bin/bash

#Input Files
fits='fits_delta.txt'
signal="/local/cms/user/gude/kevin_mc_smearing/FullSimSmeared_effac_ZEffTree/FullSimSmeared_effac_ZEffTree_summed.root"
zefftree="/local/cms/user/gude/2012_kevin_thesis_eff/run_at_fnal_20120905/2012_kevin_thesis_trigger_eff_crab_test/res/DoubleElectron_ele17_summed.root"

#Mass_Z
mz_low=60
mz_high=150

#Run the fits
##EB HF
tag="EB"
probe="HF"
###PU 0-4
pu_low=0
pu_high=20
####pt 20-30
pt_low=20
pt_high=100
outfile="eff_fit_output/ele17_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high

#Run the fits
##EB HF
tag="EE"
probe="HF"
###PU 0-4
pu_low=0
pu_high=20
####pt 20-30
pt_low=20
pt_high=100
outfile="eff_fit_output/ele17_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_pt_${pt_low}_${pt_high}.root"
./fitEffAcc.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $pt_low $pt_high
