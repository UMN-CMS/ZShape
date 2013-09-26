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
inputFile = "/local/cms/user/gude/2012_kevin_thesis_eff/run_at_fnal_20130920/SingleElectron_ele27_summed.root"

# Mass_Z
minMZ = 50
maxMZ = 150

# Cuts
tagWP = "WP95"
probeWP = "HFTightElectronId-EtaDet"

# Use Phistar (Pt else)
usePhiStar = True

# Program
exe = "./BackgroundFitter.exe"

# Output dir
outdir = mkdtemp(prefix="hf_trigger_background_fits_")
print "# Output directory: ", outdir

# Bins
PUs = ((0, 4), (5, 101))
if usePhiStar:
    Xs = ((0., 0.05), (0.05, 0.1), (0.1, 0.2), (0.2, 1.))
else:
    Xs = ((20, 25), (25, 30), (30, 35), (35, 40), (40, 45), (45, 50), (55, 500))

# List to store points to run over before passing to the multiprocessing pool
inputList = []

for (minPU, maxPU) in PUs:
    for (minX, maxX) in Xs:
        outputFile = "%s/bgfit_tag-%s_probe-%s_minX-%s_maxX-%s_minPU-%s_maxPU-%s_phistar_%s.root" % (
                outdir,
                tagWP,
                probeWP,
                minX,
                maxX,
                minPU,
                maxPU,
                usePhiStar
                )
        command = (
                exe,
                inputFile,
                outputFile,
                tagWP,
                probeWP,
                str(minX),
                str(maxX),
                str(minPU),
                str(maxPU),
                str(minMZ),
                str(maxMZ),
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
