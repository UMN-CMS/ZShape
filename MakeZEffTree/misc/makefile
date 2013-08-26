# Pull in ROOT
ROOT_INCLUDES=`root-config --cflags`
ROOT_ALL=`root-config --cflags --libs`

#Compiler
CC=g++ -O2
CCC=${CC} -c

all: PlotZPeak.exe

PlotZPeak.exe: ZEffTree.o ElectronLocation.o
	${CC} -o PlotZPeak.exe PlotZPeak.cc \
	ZEffTree.o \
	ElectronLocation.o \
	${ROOT_ALL}

ZEffTree.o: ../src/ZEffTree.h ../src/ZEffTree.cc
	${CCC} ../src/ZEffTree.cc ${ROOT_INCLUDES}

ElectronLocation.o: ../../2011EffCalculation/ElectronLocation/ElectronLocation.h ../../2011EffCalculation/ElectronLocation/ElectronLocation.cc
	${CCC} ../../2011EffCalculation/ElectronLocation/ElectronLocation.cc

clean:
	rm -f ZEffTree.o ElectronLocation.o PlotZPeak.exe
