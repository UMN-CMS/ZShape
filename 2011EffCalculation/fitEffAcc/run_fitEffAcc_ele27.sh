#!/bin/bash

#Input Files
fits='background_ele27.txt'
signal="/local/cms/user/gude/kevin_mc_smearing/FullSimSmeared_effac_ZEffTree_with_phistar/FullSimSmeared_effac_ZEffTree_with_phistar_summed.root"
#zefftree="/local/cms/user/gude/2012_kevin_thesis_eff/run_at_fnal_20120827/DoubleElectron_ele27/res/ "
zefftree="/local/cms/user/gude/2012_kevin_thesis_eff/run_at_fnal_20120914/2012_kevin_thesis_trigger_eff_with_charge/SingleElectron_ele27/res/SingleElectron_ele27_summed.root"

#Mass_Z 
mz_low=60
mz_high=150

# #Run the fits
# ##EB HF
# tag="EB"
# probe="HF"
# ###PU 0-4
# pu_low=0
# pu_high=20
# ####pt 20-30
# x_low=20
# x_high=100
# outfile="eff_fit_output/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high

usePhiStar=1

#Run the fits
##EE HF
tag="EE"
tag="ET"
probe="HF"
###PU 0-4
pu_low=0
pu_high=4

x_low=0
x_high=0.05
outfile="eff_fit_output/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=0.05
x_high=0.1
outfile="eff_fit_output/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=0.1
x_high=0.2
outfile="eff_fit_output/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=0.2
x_high=1
outfile="eff_fit_output/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

###PU 5-10
pu_low=5
pu_high=10

x_low=0
x_high=0.05
outfile="eff_fit_output/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=0.05
x_high=0.1
outfile="eff_fit_output/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=0.1
x_high=0.2
outfile="eff_fit_output/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=0.2
x_high=1
outfile="eff_fit_output/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
