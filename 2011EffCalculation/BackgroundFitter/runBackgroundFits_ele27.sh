# Global variables
NOTES="--TEST" # You could add -- at the start if you add
tagWP="WP95"
probeWP="HFTightElectronId-EtaDet"
minMZ=50
maxMZ=150

bgfile="/local/cms/user/gude/2012_kevin_thesis_eff/run_at_fnal_20120914/2012_kevin_thesis_trigger_eff_with_charge/SingleElectron_ele27/res/SingleElectron_ele27_summed.root"

# Echo for text file format (-e to recognize tabs)
echo -e "#\tminPt\tmaxPt\tminPU\tmaxPU\tminMZ\tmaxMZ\tNParms\talpha\tbeta\tgamma\tdelta\tusePhiStar"


#Use PhiStar?
usePhiStar=1

# Barrel bins are used. 
## Row 1
minPU=0
maxPU=4

minX=0
maxX=0.05
./BackgroundFitter.exe ${bgfile} bg_fit_output_with_ele27/bgfit_tag-${tagWP}_probe-${probeWP}_minX-${minX}_maxX-${maxX}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minX $maxX $minPU $maxPU $minMZ $maxMZ $usePhiStar

minX=0.05
maxX=0.1
./BackgroundFitter.exe ${bgfile} bg_fit_output_with_ele27/bgfit_tag-${tagWP}_probe-${probeWP}_minX-${minX}_maxX-${maxX}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minX $maxX $minPU $maxPU $minMZ $maxMZ $usePhiStar

minX=0.1
maxX=0.2
./BackgroundFitter.exe ${bgfile} bg_fit_output_with_ele27/bgfit_tag-${tagWP}_probe-${probeWP}_minX-${minX}_maxX-${maxX}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minX $maxX $minPU $maxPU $minMZ $maxMZ $usePhiStar

minX=0.2
maxX=1
./BackgroundFitter.exe ${bgfile} bg_fit_output_with_ele27/bgfit_tag-${tagWP}_probe-${probeWP}_minX-${minX}_maxX-${maxX}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minX $maxX $minPU $maxPU $minMZ $maxMZ $usePhiStar

## Row 2
minPU=5
maxPU=10

minX=0
maxX=0.05
./BackgroundFitter.exe ${bgfile} bg_fit_output_with_ele27/bgfit_tag-${tagWP}_probe-${probeWP}_minX-${minX}_maxX-${maxX}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minX $maxX $minPU $maxPU $minMZ $maxMZ $usePhiStar

minX=0.05
maxX=0.1
./BackgroundFitter.exe ${bgfile} bg_fit_output_with_ele27/bgfit_tag-${tagWP}_probe-${probeWP}_minX-${minX}_maxX-${maxX}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minX $maxX $minPU $maxPU $minMZ $maxMZ $usePhiStar

minX=0.1
maxX=0.2
./BackgroundFitter.exe ${bgfile} bg_fit_output_with_ele27/bgfit_tag-${tagWP}_probe-${probeWP}_minX-${minX}_maxX-${maxX}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minX $maxX $minPU $maxPU $minMZ $maxMZ $usePhiStar

minX=0.2
maxX=1
./BackgroundFitter.exe ${bgfile} bg_fit_output_with_ele27/bgfit_tag-${tagWP}_probe-${probeWP}_minX-${minX}_maxX-${maxX}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minX $maxX $minPU $maxPU $minMZ $maxMZ $usePhiStar
