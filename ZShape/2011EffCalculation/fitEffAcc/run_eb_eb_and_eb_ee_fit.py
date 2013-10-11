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
signalFile = "/local/cms/user/gude/2012_kevin_thesis_eff/20131003_gsf_gsf_mc/20131003_gsf_gsf_mc_summed.root"
#dataFile = "/local/cms/user/gude/2012_kevin_thesis_eff/20131004_gsf_gsf_data/20131004_gsf_gsf_data_summed.root"
dataFile = "/local/cms/user/gude/2012_kevin_thesis_eff/20131003_gsf_gsf_mc/20131003_gsf_gsf_mc_summed.root"
# Mass_Z
minMZ = 60
maxMZ = 150
# Tag Location
tag="EB"
# Use Phistar (Pt else)
usePhiStar = False
if usePhiStar:
    formatstring = "%s/WP80_%s_%s_pu_%s_%s_phistar_%s_%s.root"
else:
    formatstring = "%s/WP80_%s_%s_pu_%s_%s_pt_%s_%s.root"
# Program
exe = "./fitEffAcc.exe"

# Output dir
outdir = mkdtemp(prefix="gsf_gsf_mc_run_as_data_")
print "# Output directory: ", outdir

# Bins
probeLocs = ("EB", "EEp", "EEm")
PUs = ((0, 4), (5, 101))
Xs = ((20, 25), (25, 30), (30, 35), (35, 40), (40, 45), (45, 50), (50, 55), (55, 60), (60, 500))

# List to store points to run over before passing to the multiprocessing pool
inputList = []

for probe in probeLocs:
    for (minPU, maxPU) in PUs:
        for (minX, maxX) in Xs:
            outfile = formatstring % (
                    outdir,
                    tag,
                    probe,
                    minPU,
                    maxPU,
                    minX,
                    maxX
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
NJOBS=1  # Force non-parallel
if HasMP and NJOBS > 1:
    pool = mp.Pool(processes=NJOBS)
    pool.map(call, inputList)  # Note, no return values so we don't care about them
    pool.close()  # No more tasks to add
    pool.join()  # Wait for jobs to finish
else:
    for il in inputList:
        call(il)
