#!/usr/bin/env python

from subprocess import call  # Access external programs
from tempfile import mkdtemp  # Secure methods of generating random directories

# Multiprocessing does not exist on some of the older versions of Scientific
# Linux that we still use at CERN
HasMP = True
NJOBS = 1
try:
    import multiprocessing as mp
except ImportError:
    HasMP = False
else:  # Only runs when try succeeds
    from math import floor
    if HasMP:
        NJOBS = int(floor(mp.cpu_count() * 1.5))

# Input Files
#fitFile = "hf_trigger_background_from_ele27.txt"
#fitFile = "hf_background.txt"
signalFile = "/local/cms/user/gude/2012_kevin_thesis_eff/20130918_gsf_hfsc_mc/20130918_gsf_hfsc_mc_summed.root"
dataFile = "/local/cms/user/gude/2012_kevin_thesis_eff/run_at_fnal_20120914/2012_kevin_thesis_trigger_eff_with_charge/SingleElectron_ele27/res/SingleElectron_ele27_summed.root"
# Mass_Z
minMZ = 50
maxMZ = 150
# Tag Location
tag="ET"
# Use Phistar (Pt else)
usePhiStar = True
# Program
exe = "./fitEffAcc_trigger.exe"

# Output dir
outdir = mkdtemp(prefix="hf_trigger_eff_fits_")
print "# Output directory: ", outdir

# Bins
probeLocs = ("HF",)
PUs = ((0, 4), (5, 101))
#Xs = ((20, 25), (25, 30), (30, 35), (35, 40), (40, 45), (45, 50), (55, 500))
#Xs = ((20, 25), (25, 27.5), (27.5, 30), (30, 32.5), (32.5, 35), (35, 37.5), (37.5, 40), (40, 45), (45, 50), (55, 500))
Xs = ((0., 0.05), (0.05, 0.1), (0.1, 0.2), (0.2, 1.))

# List to store points to run over before passing to the multiprocessing pool
inputList = []

for probe in probeLocs:
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
            inputList.append(command)

# Run jobs in parallel
if HasMP and NJOBS > 1:
    pool = mp.Pool(processes=NJOBS)
    pool.map(call, inputList)  # Note, no return values so we don't care about them
    pool.close()  # No more tasks to add
    pool.join()  # Wait for jobs to finish
else:
    for il in inputList:
        call(il)
