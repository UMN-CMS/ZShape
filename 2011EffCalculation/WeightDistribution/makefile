# Pull in ROOT
ROOT_INCLUDES=`root-config --cflags`
ROOT_ALL=`root-config --cflags --libs`

#Compiler
CC=g++ -O2
CCC=${CC} -c

all: WeightDistribution.exe
	
WeightDistribution.exe: ZEffTree.o ElectronLocation.o EfficiencyTable.o
	${CC} -o WeightDistribution.exe WeightDistribution.cc \
	ZEffTree.o \
	ElectronLocation.o \
	EfficiencyTable.o \
	${ROOT_ALL}

ZEffTree.o: ../../MakeZEffTree/src/ZEffTree.h ../../MakeZEffTree/src/ZEffTree.cc
	${CCC} ../../MakeZEffTree/src/ZEffTree.cc ${ROOT_INCLUDES}

ElectronLocation.o: ../ElectronLocation/ElectronLocation.h ../ElectronLocation/ElectronLocation.cc
	${CCC} ../ElectronLocation/ElectronLocation.cc

EfficiencyTable.o: ../EfficiencyTable/EfficiencyTable.h ../EfficiencyTable/EfficiencyTable.cc
	${CCC} ../EfficiencyTable/EfficiencyTable.cc

clean:
	rm -f ZEffTree.o ElectronLocation.o EfficiencyTable.o WeightDistribution.exe
