# ZShape_Analysis

## Setting up a working area

To set up a working area, run the following commands:

```bash
scram project CMSSW CMSSW_4_4_2_patch10
cd CMSSW_4_4_2_patch10
git clone git@github.com:UMN-CMS/ZShape_Analysis.git src/
cmsenv
cd src
scram build -j 4
```
