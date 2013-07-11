# Pull in ROOT
ROOT_INCLUDES=`root-config --cflags`
ROOT_ALL=`root-config --cflags --libs`

#Compiler
CC=g++ -O2
CCC=${CC} -c

all: fitEffAcc_trigger_with_inbuilt_hf_correction_with_smearing.exe 
	
fitEffAcc_trigger_with_inbuilt_hf_correction_with_smearing.exe: ZEffTree.o BackgroundTable.o ElectronLocation.o
	${CC} -o fitEffAcc_trigger_with_inbuilt_hf_correction_with_smearing.exe \
	fitEffAcc.cc \
	ZEffTree.o \
	BackgroundTable.o \
	ElectronLocation.o \
	${ROOT_ALL}

ZEffTree.o: ../../MakeZEffTree/src/ZEffTree.h ../../MakeZEffTree/src/ZEffTree.cc
	${CCC} ../../MakeZEffTree/src/ZEffTree.cc ${ROOT_INCLUDES}

BackgroundTable.o: ../BackgroundTable/BackgroundTable.h ../BackgroundTable/BackgroundTable.cc
	${CCC} ../BackgroundTable/BackgroundTable.cc ${ROOT_INCLUDES}

ElectronLocation.o: ../ElectronLocation/ElectronLocation.h ../ElectronLocation/ElectronLocation.cc
	${CCC} ../ElectronLocation/ElectronLocation.cc

clean:
	rm -f ZEffTree.o BackgroundTable.o ElectronLocation.o
