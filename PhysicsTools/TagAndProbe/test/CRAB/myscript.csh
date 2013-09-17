#!/bin/tcsh -f

~/bin/condor_filelist.perl TPRun2010B146241-146750 FullTagProbeTree_cfg.py /local/cms/user/common/38x/Run2010B/skimOnly_ZtwoLegs-Electron--Run2010B--PromptRECO--146241-146750--2010-10-16--Rev1.7_files.txt 15 -1
~/bin/condor_filelist.perl TPRun2010B146751-147500 FullTagProbeTree_cfg.py /local/cms/user/common/38x/Run2010B/skimOnly_ZtwoLegs-Electron--Run2010B--PromptRECO--146751-147250--2010-10-16--Rev1.7_files.txt 15 -1
~/bin/condor_filelist.perl TPRun2010B147501-148000 FullTagProbeTree_cfg.py /local/cms/user/common/38x/Run2010B/skimOnly_ZtwoLegs-Electron--Run2010B--PromptRECO--147501-148000--2010-10-17--Rev1.7_files.txt 15 -1
#~/bin/condor_filelist.perl TPRun2010BFull147501-148000 FullTagProbeTreeFull_cfg.py /local/cms/user/common/38x/Run2010B/skimOnly_ZtwoLegs-Electron--Run2010B--PromptRECO--147501-148000--2010-10-17--Rev1.7_files.txt 15 -1


#end of script
