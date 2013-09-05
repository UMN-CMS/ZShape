#!/usr/bin/python

from subprocess import call  # Access external programs
from tempfile import mkdtemp  # Secure methods of generating random directories

# Input Files
inputFile = "/local/cms/user/gude/2012_kevin_thesis_eff/run_at_fnal_20120914/2012_kevin_thesis_trigger_eff_with_charge/SingleElectron_ele27/res/SingleElectron_ele27_summed.root"

# Mass_Z
minMZ = 50
maxMZ = 150

# Cuts
tagWP = "WP95"
probeWP = "HFTightElectronId-EtaDet"

# Use Phistar (Pt else)
usePhiStar = False

# Program
exe = "./BackgroundFitter.exe"

# Output dir
outdir = mkdtemp(prefix="hf_trigger_background_fits_")
print "# Output directory: ", outdir

# Bins
PUs = ((0, 4), (5, 10), (11, 101))
PUs = ((0, 4), (5, 101))
Xs = ((20, 25), (25, 30), (30, 35), (35, 40), (40, 45), (45, 50), (55, 60), (60, 500))
Xs = ((20, 25), (25, 30), (30, 35), (35, 40), (40, 45), (45, 50), (55, 500))

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
        call(command)
