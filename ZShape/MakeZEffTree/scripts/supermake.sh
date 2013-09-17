#!/bin/bash

make clean && make -j 2 \
&& ./PlotZPeak.exe /local/cms/user/gude/2013_zpeak_with_2011_data/gsf_hfsc_2011A_and_B/2011A_and_B_summed.root /local/cms/user/gude/2012_kevin_thesis_eff/gsf_hfsc_mc_july_15_from_kevins_list/gsf_hfsc_mc_july_15_from_kevins_list_summed.root test_gsf.png \
&& ./PlotZPeak.exe /local/cms/user/gude/2013_zpeak_with_2011_data/gsf_hfsc_2011A_and_B/2011A_and_B_summed.root /local/cms/user/gude/2012_kevin_thesis_eff/gsf_hfsc_mc_july_15_from_kevins_list/gsf_hfsc_mc_july_15_from_kevins_list_summed.root test_gsf.pdf \
&& eog test_gsf.png
#&& ./PlotZPeak.exe /local/cms/user/gude/2013_zpeak_with_2011_data/wp90_hfsc_2011A_and_B/2011A_and_B_summed.root /local/cms/user/gude/2012_kevin_thesis_eff/gsf_hfsc_mc_july_15_from_kevins_list/gsf_hfsc_mc_july_15_from_kevins_list_summed.root test_wp90.png \
