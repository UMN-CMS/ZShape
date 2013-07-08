#!/bin/bash

#Input Files
zefftree="/local/cms/user/gude/2012_kevin_thesis_eff/gsf_gsf_mc/gsf_gsf_mc_summed.root"

#Mass_Z 
mz_low=60
mz_high=150

usePhiStar=0
outdir="closure_test_mc"

cut="WP80"

#Run the fits
##EB EB
loc="EB"

###PU 0-4
pu_low=0
pu_high=4

x_low=20
x_high=25
outfile="${outdir}/ele27_${log}_${cut}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=25
x_high=30
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=30
x_high=35
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=35
x_high=40
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=40
x_high=45
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=45
x_high=50
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=50
x_high=55
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=55
x_high=60
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=60
x_high=70
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

###PU 5-10
pu_low=5
pu_high=10

x_low=20
x_high=25
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=25
x_high=30
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=30
x_high=35
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=35
x_high=40
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=40
x_high=45
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=45
x_high=50
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=50
x_high=55
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=55
x_high=60
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=60
x_high=70
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

loc="EEm"

###PU 0-4
pu_low=0
pu_high=4

x_low=20
x_high=25
outfile="${outdir}/ele27_${log}_${cut}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=25
x_high=30
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=30
x_high=35
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=35
x_high=40
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=40
x_high=45
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=45
x_high=50
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=50
x_high=55
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=55
x_high=60
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=60
x_high=70
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

###PU 5-10
pu_low=5
pu_high=10

x_low=20
x_high=25
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=25
x_high=30
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=30
x_high=35
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=35
x_high=40
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=40
x_high=45
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=45
x_high=50
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=50
x_high=55
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=55
x_high=60
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=60
x_high=70
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

loc="EEp"

###PU 0-4
pu_low=0
pu_high=4

x_low=20
x_high=25
outfile="${outdir}/ele27_${log}_${cut}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=25
x_high=30
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=30
x_high=35
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=35
x_high=40
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=40
x_high=45
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=45
x_high=50
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=50
x_high=55
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=55
x_high=60
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=60
x_high=70
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

###PU 5-10
pu_low=5
pu_high=10

x_low=20
x_high=25
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=25
x_high=30
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=30
x_high=35
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=35
x_high=40
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=40
x_high=45
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=45
x_high=50
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=50
x_high=55
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=55
x_high=60
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar

x_low=60
x_high=70
outfile="${outdir}/ele27_${tag}_${probe}_mz_${mz_low}_${mz_high}_pu_${pu_low}_${pu_high}_x_${x_low}_${x_high}_phistar_${usePhiStar}.root"
./closure.exe $zefftree $outfile $loc $cut $pu_low $pu_high $mz_low $mz_high $x_low $x_high $usePhiStar
