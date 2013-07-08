#!/bin/bash

#Input Files
fits='background_ele27.txt'
signal="/local/cms/user/gude/kevin_mc_smearing/FullSimSmeared_effac_ZEffTree_with_phistar_and_new_hf_correction_march_21/FullSimSmeared_effac_ZEffTree_with_phistar_and_new_hf_correction_march_21_summed.root"
#signal="/local/cms/user/gude/2012_kevin_thesis_eff/gsf_gsf_mc/gsf_gsf_mc_summed.root"
## Uncorrected, correction applied in the code
#zefftree="/local/cms/user/gude/2012_kevin_thesis_eff/gsf_gsf_march_21_update/gsf_gsf_march_21_update_summed.root"
#zefftree="/local/cms/user/gude/2012_kevin_thesis_eff/gsf_gsf_mc/gsf_gsf_mc_summed.root"
zefftree="/local/cms/user/gude/2012_kevin_thesis_eff/gsf_hfsc_mc_may_20/gsf_hfsc_mc_may_20_summed.root"

#Mass_Z 
mz_low=60
mz_high=150

usePhiStar=0
outdir="2013_05_09_data_eff_fits"

# #Run the fits
# ##EB EB
# tag="ET"
# probe="EB"
# ###PU 0-4
# pu_low=0
# pu_high=4
# 
# x_low=20
# x_high=25
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=25
# x_high=30
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=30
# x_high=35
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=35
# x_high=40
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=40
# x_high=45
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=45
# x_high=50
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=50
# x_high=55
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=55
# x_high=60
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=60
# x_high=500
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# ###PU 5-10
# pu_low=5
# pu_high=10
# 
# x_low=20
# x_high=25
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=25
# x_high=30
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=30
# x_high=35
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=35
# x_high=40
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=40
# x_high=45
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=45
# x_high=50
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=50
# x_high=55
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=55
# x_high=60
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=60
# x_high=500
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# ###PU 5-10
# pu_low=11
# pu_high=50
# 
# x_low=20
# x_high=25
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=25
# x_high=30
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=30
# x_high=35
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=35
# x_high=40
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=40
# x_high=45
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=45
# x_high=50
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=50
# x_high=55
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=55
# x_high=60
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=60
# x_high=500
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# ##EB EE
# tag="ET"
# probe="EEp"
# ###PU 0-4
# pu_low=0
# pu_high=4
# 
# x_low=20
# x_high=25
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=25
# x_high=30
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=30
# x_high=35
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=35
# x_high=40
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=40
# x_high=45
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=45
# x_high=50
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=50
# x_high=55
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=55
# x_high=60
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=60
# x_high=500
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# ###PU 5-10
# pu_low=5
# pu_high=10
# 
# x_low=20
# x_high=25
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=25
# x_high=30
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=30
# x_high=35
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=35
# x_high=40
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=40
# x_high=45
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=45
# x_high=50
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=50
# x_high=55
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=55
# x_high=60
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=60
# x_high=500
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# ###PU 5-10
# pu_low=11
# pu_high=50
# 
# x_low=20
# x_high=25
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=25
# x_high=30
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=30
# x_high=35
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=35
# x_high=40
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=40
# x_high=45
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=45
# x_high=50
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=50
# x_high=55
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=55
# x_high=60
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=60
# x_high=500
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# ##EB EE
# tag="ET"
# probe="EEm"
# ###PU 0-4
# pu_low=0
# pu_high=4
# 
# x_low=20
# x_high=25
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=25
# x_high=30
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=30
# x_high=35
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=35
# x_high=40
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=40
# x_high=45
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=45
# x_high=50
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=50
# x_high=55
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=55
# x_high=60
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=60
# x_high=500
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# ###PU 5-10
# pu_low=5
# pu_high=10
# 
# x_low=20
# x_high=25
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=25
# x_high=30
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=30
# x_high=35
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=35
# x_high=40
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=40
# x_high=45
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=45
# x_high=50
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=50
# x_high=55
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=55
# x_high=60
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=60
# x_high=500
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# ###PU 5-10
# pu_low=11
# pu_high=50
# 
# x_low=20
# x_high=25
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=25
# x_high=30
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=30
# x_high=35
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=35
# x_high=40
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=40
# x_high=45
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=45
# x_high=50
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=50
# x_high=55
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=55
# x_high=60
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# x_low=60
# x_high=500
# outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
# ./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
# 
# 
# Switching to HF

zefftree="/local/cms/user/gude/2012_kevin_thesis_eff/gsf_hfsc_mc_may_20/gsf_hfsc_mc_may_20_summed.root"

##ET HF
tag="ET"
probe="HFp"
###PU 0-4
pu_low=0
pu_high=4

x_low=20
x_high=25
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=25
x_high=30
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=30
x_high=35
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=35
x_high=40
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=40
x_high=45
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=45
x_high=50
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=50
x_high=55
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=55
x_high=60
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=60
x_high=500
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

###PU 5-10
pu_low=5
pu_high=10

x_low=20
x_high=25
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=25
x_high=30
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=30
x_high=35
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=35
x_high=40
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=40
x_high=45
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=45
x_high=50
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=50
x_high=55
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=55
x_high=60
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=60
x_high=500
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

# 11-50 PU

pu_low=11
pu_high=50

x_low=20
x_high=25
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=25
x_high=30
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=30
x_high=35
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=35
x_high=40
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=40
x_high=45
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=45
x_high=50
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=50
x_high=55
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=55
x_high=60
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=60
x_high=500
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

##ET HF
tag="ET"
probe="HFm"
###PU 0-4
pu_low=0
pu_high=4

x_low=20
x_high=25
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=25
x_high=30
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=30
x_high=35
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=35
x_high=40
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=40
x_high=45
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=45
x_high=50
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=50
x_high=55
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=55
x_high=60
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=60
x_high=70
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

###PU 5-10
pu_low=5
pu_high=10

x_low=20
x_high=25
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=25
x_high=30
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=30
x_high=35
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=35
x_high=40
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=40
x_high=45
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=45
x_high=50
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=50
x_high=55
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=55
x_high=60
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=60
x_high=70
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

#Run the fits
##ET HF
tag="ET"
probe="HFp"
###PU 0-4
pu_low=0
pu_high=4

x_low=20
x_high=25
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=25
x_high=30
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=30
x_high=35
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=35
x_high=40
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=40
x_high=45
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=45
x_high=50
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=50
x_high=55
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=55
x_high=60
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=60
x_high=70
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

###PU 5-10
pu_low=5
pu_high=10

x_low=20
x_high=25
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=25
x_high=30
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=30
x_high=35
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=35
x_high=40
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=40
x_high=45
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=45
x_high=50
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=50
x_high=55
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=55
x_high=60
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=60
x_high=70
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

##EB EB
tag="ET"
probe="HFm"
###PU 0-4
pu_low=0
pu_high=4

x_low=20
x_high=25
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=25
x_high=30
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=30
x_high=35
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=35
x_high=40
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=40
x_high=45
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=45
x_high=50
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=50
x_high=55
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=55
x_high=60
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=60
x_high=500
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

###PU 5-10
pu_low=5
pu_high=10

x_low=20
x_high=25
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=25
x_high=30
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=30
x_high=35
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=35
x_high=40
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=40
x_high=45
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=45
x_high=50
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=50
x_high=55
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=55
x_high=60
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=60
x_high=500
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

###PU 11-50
pu_low=11
pu_high=50

x_low=20
x_high=25
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=25
x_high=30
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=30
x_high=35
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=35
x_high=40
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=40
x_high=45
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=45
x_high=50
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=50
x_high=55
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=55
x_high=60
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=60
x_high=500
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./fitEffAcc_trigger_with_inbuilt_hf_correction.exe $fits $signal $zefftree $outfile $tag $probe $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
