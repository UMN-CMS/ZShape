# Pull in ROOT
ROOT_INCLUDES=`root-config --cflags`
ROOT_ALL=`root-config --cflags --libs`

#Compiler
CC=g++ -O2
CCC=${CC} -c

all: SmearTuples.exe

SmearTuples.exe: ZEffTree.o ElectronLocation.o
	${CC} -o SmearTuples.exe SmearTuples.cc \
	ZEffTree.o \
	ElectronLocation.o \
	${ROOT_ALL}

ZEffTree.o: ../../MakeZEffTree/src/ZEffTree.h ../../MakeZEffTree/src/ZEffTree.cc
	${CCC} ../../MakeZEffTree/src/ZEffTree.cc ${ROOT_INCLUDES}

ElectronLocation.o: ../ElectronLocation/ElectronLocation.h ../ElectronLocation/ElectronLocation.cc
	${CCC} ../ElectronLocation/ElectronLocation.cc

clean:
	rm -f ZEffTree.o ElectronLocation.o SmearTuples.exe
