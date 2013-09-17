#!/bin/tcsh -f
###################
#Needs one argument of the python configuration file
python $1

set Jason2="`cat nothing2.txt`"
set Jason3="`cat nothing3.txt`"
set name="plotStatBB"
cat EffStats.C | sed "s@MYSUPERCRUST@${Jason2}@g; s@DARUNMAPCRUST@${Jason3}@g "  > $name.C

g++ $name.C -o $name `root-config --cflags --libs` -L $ROOTSYS/lib -lHtml -lMinuit  -lFoam 
./$name

rm nothing2.txt nothing3.txt 
#end of the file
