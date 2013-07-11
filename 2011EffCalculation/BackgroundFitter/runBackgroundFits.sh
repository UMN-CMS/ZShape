# Global variables
NOTES="--TEST" # You could add -- at the start if you add
tagWP="WP95"
probeWP="WP95"
minMZ=50
maxMZ=150

# Pre HF correction
#bgfile="/local/cms/user/gude/2012_kevin_thesis_eff/run_at_fnal_20120905/res/ele27_summed.root"
#outdir="bg_fit_output_with_ele27/"
# Post HF correction
bgfile="/local/cms/user/gude/kevin_data_smearing/ZEffTree_with_phistar_and_0.1902_all_hf_correction_data_sc_sc_with_json/ZEffTree_with_phistar_and_0.1902_all_hf_correction_data_sc_sc_with_json_summed.root"
outdir="bg_fit_output_with_hf_correction/"


# Echo for text file format (-e to recognize tabs)
echo -e "#\tminPt\tmaxPt\tminPU\tmaxPU\tminMZ\tmaxMZ\tNParms\talpha\tbeta\tgamma\tdelta"

usePhiStar=1

# Barrel bins are used. 
## Row 1
minPU=0
maxPU=4

minPt=20
maxPt=30
echo ./BackgroundFitter.exe ${bgfile} ${outdir}/bgfit_tag-${tagWP}_probe-${probeWP}_minPt-${minPt}_maxPt-${maxPt}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minPt $maxPt $minPU $maxPU $minMZ $maxMZ $usePhiStar
./BackgroundFitter.exe ${bgfile} ${outdir}/bgfit_tag-${tagWP}_probe-${probeWP}_minPt-${minPt}_maxPt-${maxPt}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minPt $maxPt $minPU $maxPU $minMZ $maxMZ $usePhiStar

minPt=30
maxPt=40
./BackgroundFitter.exe ${bgfile} ${outdir}/bgfit_tag-${tagWP}_probe-${probeWP}_minPt-${minPt}_maxPt-${maxPt}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minPt $maxPt $minPU $maxPU $minMZ $maxMZ $usePhiStar

minPt=40
maxPt=55
./BackgroundFitter.exe ${bgfile} ${outdir}/bgfit_tag-${tagWP}_probe-${probeWP}_minPt-${minPt}_maxPt-${maxPt}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minPt $maxPt $minPU $maxPU $minMZ $maxMZ $usePhiStar

minPt=55
maxPt=70
./BackgroundFitter.exe ${bgfile} ${outdir}/bgfit_tag-${tagWP}_probe-${probeWP}_minPt-${minPt}_maxPt-${maxPt}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minPt $maxPt $minPU $maxPU $minMZ $maxMZ $usePhiStar

minPt=70
maxPt=500
./BackgroundFitter.exe ${bgfile} ${outdir}/bgfit_tag-${tagWP}_probe-${probeWP}_minPt-${minPt}_maxPt-${maxPt}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minPt $maxPt $minPU $maxPU $minMZ $maxMZ $usePhiStar

## Row 2
minPU=5
maxPU=10

minPt=20
maxPt=25
./BackgroundFitter.exe ${bgfile} ${outdir}/bgfit_tag-${tagWP}_probe-${probeWP}_minPt-${minPt}_maxPt-${maxPt}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minPt $maxPt $minPU $maxPU $minMZ $maxMZ $usePhiStar

minPt=25
maxPt=40
./BackgroundFitter.exe ${bgfile} ${outdir}/bgfit_tag-${tagWP}_probe-${probeWP}_minPt-${minPt}_maxPt-${maxPt}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minPt $maxPt $minPU $maxPU $minMZ $maxMZ $usePhiStar

minPt=40
maxPt=55
./BackgroundFitter.exe ${bgfile} ${outdir}/bgfit_tag-${tagWP}_probe-${probeWP}_minPt-${minPt}_maxPt-${maxPt}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minPt $maxPt $minPU $maxPU $minMZ $maxMZ $usePhiStar

minPt=55
maxPt=70
./BackgroundFitter.exe ${bgfile} ${outdir}/bgfit_tag-${tagWP}_probe-${probeWP}_minPt-${minPt}_maxPt-${maxPt}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minPt $maxPt $minPU $maxPU $minMZ $maxMZ $usePhiStar

minPt=70
maxPt=500
./BackgroundFitter.exe ${bgfile} ${outdir}/bgfit_tag-${tagWP}_probe-${probeWP}_minPt-${minPt}_maxPt-${maxPt}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minPt $maxPt $minPU $maxPU $minMZ $maxMZ $usePhiStar

## Row 2
minPU=11
maxPU=50

minPt=20
maxPt=25
./BackgroundFitter.exe ${bgfile} ${outdir}/bgfit_tag-${tagWP}_probe-${probeWP}_minPt-${minPt}_maxPt-${maxPt}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minPt $maxPt $minPU $maxPU $minMZ $maxMZ $usePhiStar

minPt=25
maxPt=40
./BackgroundFitter.exe ${bgfile} ${outdir}/bgfit_tag-${tagWP}_probe-${probeWP}_minPt-${minPt}_maxPt-${maxPt}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minPt $maxPt $minPU $maxPU $minMZ $maxMZ $usePhiStar

minPt=40
maxPt=55
./BackgroundFitter.exe ${bgfile} ${outdir}/bgfit_tag-${tagWP}_probe-${probeWP}_minPt-${minPt}_maxPt-${maxPt}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minPt $maxPt $minPU $maxPU $minMZ $maxMZ $usePhiStar

minPt=55
maxPt=70
./BackgroundFitter.exe ${bgfile} ${outdir}/bgfit_tag-${tagWP}_probe-${probeWP}_minPt-${minPt}_maxPt-${maxPt}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minPt $maxPt $minPU $maxPU $minMZ $maxMZ $usePhiStar

minPt=70
maxPt=500
./BackgroundFitter.exe ${bgfile} ${outdir}/bgfit_tag-${tagWP}_probe-${probeWP}_minPt-${minPt}_maxPt-${maxPt}_minPU-${minPU}_maxPU-${maxPU}${NOTES}.root $tagWP $probeWP $minPt $maxPt $minPU $maxPU $minMZ $maxMZ $usePhiStar
