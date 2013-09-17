# Pull in ROOT
ROOT_INCLUDES=`root-config --cflags`
ROOT_ALL=`root-config --cflags --libs`

#Compiler
CC=g++ -O2
CCC=${CC} -c

all: testEfficiencyTable.exe
	
testEfficiencyTable.exe: ElectronLocation.o EfficiencyTable.o
	${CC} -o testEfficiencyTable.exe testEfficiencyTable.cc \
	ElectronLocation.o \
	EfficiencyTable.o \

ElectronLocation.o: ../ElectronLocation/ElectronLocation.h ../ElectronLocation/ElectronLocation.cc
	${CCC} ../ElectronLocation/ElectronLocation.cc

EfficiencyTable.o: ../EfficiencyTable/EfficiencyTable.h ../EfficiencyTable/EfficiencyTable.cc
	${CCC} ../EfficiencyTable/EfficiencyTable.cc

clean:
	rm -f ElectronLocation.o EfficiencyTable.o testEfficiencyTable.exe
