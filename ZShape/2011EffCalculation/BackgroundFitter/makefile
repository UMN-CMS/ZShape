# Pull in ROOT
ROOT_INCLUDES=`root-config --cflags`
ROOT_ALL=`root-config --cflags --libs`

#Compiler
CC=g++ -O2
CCC=${CC} -c

all: BackgroundFitter.exe

BackgroundFitter.exe: ZEffTree.o ElectronLocation.o BackgroundFunctions.o
	${CC} -o BackgroundFitter.exe \
	BackgroundFitter.cc \
	ZEffTree.o \
	ElectronLocation.o \
	BackgroundFunctions.o \
	${ROOT_ALL}

ZEffTree.o: ../../MakeZEffTree/src/ZEffTree.h ../../MakeZEffTree/src/ZEffTree.cc
	${CCC} ../../MakeZEffTree/src/ZEffTree.cc ${ROOT_INCLUDES}

ElectronLocation.o: ../ElectronLocation/ElectronLocation.h ../ElectronLocation/ElectronLocation.cc
	    ${CCC} ../ElectronLocation/ElectronLocation.cc

BackgroundFunctions.o: ../BackgroundLibrary/BackgroundFunctions.h ../BackgroundLibrary/BackgroundFunctions.cc
	${CCC} ../BackgroundLibrary/BackgroundFunctions.cc ${ROOT_INCLUDES}

clean:
	rm -f ZEffTree.o ElectronLocation.o BackgroundFunctions.o BackgroundFitter.exe
