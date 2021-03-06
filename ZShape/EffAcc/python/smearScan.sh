#!/bin/sh
#./smearScan.sh EE mean 0.96 0.97 0.985 0.99 0.995 1.0 1.005 1.01 1.015 1.02 1.03 1.04

#HF
#EB
#EE
det=$1
shift


#constantp
#constantm
#constantp2
#constantm2
#reseta
#resphi
#c 
var=$1
shift

day=`date +%b%d`
time=`date +%H%M`

vals1_=${*//./_}
vals_=${vals1_// /__}
cfg=scans/${det}_${var}_${day}_${time}_cfg.py
cp TOPLATE.py $cfg
path=scans/path.py
cp PATHPLATE.py $path
for num in $*; do
    num_=${num//./X}
    name=${det}X${var}X${num_}
    Sname=${name}Xsmear

    process=process.$name
process=${process/-/m}
    Sprocess=process.$Sname
Sprocess=${Sprocess/-/m}
# >> $cfg
# >> $path
echo ${Sprocess} \= ZShape.EffAcc.FullSimSmearedElectronProducer_cfi.FullSimSmearedElectronsProducer.clone\(\) >> $cfg
echo ${Sprocess}.$det.$var \= cms.double\($num\) >> $cfg
echo \+ $Sprocess >> $path
echo >> $cfg



echo ${process} \= ZShape.EffAcc.ZEfficiencyUnity_cfi.mcEff.clone\(\) >> $cfg
echo ${process}.zTreeLevelElectronsCollection \= cms.untracked.InputTag\(\"fullSimLoad\",\"ZEventEle3\"\) >> $cfg
echo ${process}.zsrc \= cms.untracked.InputTag\(\"${Sname}\",\"ZEventParticles\"\) >> $cfg
echo ${process}.zElectronsCollection \= cms.untracked.InputTag\(\"${Sname}\",\"ZEventParticles\"\) >> $cfg
echo >> $cfg
echo \+ $process >> $path
done



cat $path >> $cfg
echo \) >> $cfg
rm $path








