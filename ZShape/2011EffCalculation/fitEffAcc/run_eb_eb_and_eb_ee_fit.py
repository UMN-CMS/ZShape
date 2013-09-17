#!/usr/bin/python

from subprocess import call  # Access external programs
from os import mkdir

# Input Files
fitFile = "background_ele27.txt"
signalFile = "/local/cms/user/gude/2012_kevin_thesis_eff/gsf_gsf_mc/gsf_gsf_mc_summed.root"
dataFile = "/local/cms/user/gude/2012_kevin_thesis_eff/gsf_gsf_mc/gsf_gsf_mc_summed.root"
# Mass_Z
minMZ = 60
maxMZ = 150
# Tag Location
tag="EB"
# Use Phistar (Pt else)
usePhiStar = False
# Program
exe = "./fitEffAcc_trigger_with_inbuilt_hf_correction_with_smearing.exe"

# Output dir
outdir="/tmp/gsf_gsf_mc_run_as_data"
mkdir(outdir)

# Bins
tagLocs = ("EB", "EE")
PUs = ((0, 4), (5, 10), (11, 101))
Xs = ((20, 25), (25, 30), (30, 35), (35, 40), (40, 45), (45, 50), (55, 60), (60, 500))

for probe in tagLocs:
    for (minPU, maxPU) in PUs:
        for (minX, maxX) in Xs:
            outfile="%s/ele27_%s_%s_mz_%s_%s_pu_%s_%s_x_%s_%s_phistar_%s.root" % (
                    outdir,
                    tag,
                    probe,
                    minMZ,
                    maxMZ,
                    minPU,
                    maxPU,
                    minX,
                    maxX,
                    int(usePhiStar)
                    )
            command = (
                    exe,
                    fitFile,
                    signalFile,
                    dataFile,
                    outfile,
                    tag,
                    probe,
                    str(minPU),
                    str(maxPU),
                    str(minMZ),
                    str(maxMZ),
                    str(minX),
                    str(maxX),
                    str(int(usePhiStar))
                    )
            call(command)
