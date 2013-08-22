# Pull in ROOT
ROOT_INCLUDES=`root-config --cflags`
ROOT_ALL=`root-config --cflags --libs`

#Compiler
CC=g++ -O2
CCC=${CC} -c

all: PostCutPlotter.exe

PostCutPlotter.exe: ZEffTree.o ElectronLocation.o HistoMaker.o
	${CC} -o PostCutPlotter.exe PostCutPlotter.cc \
	ZEffTree.o \
	ElectronLocation.o \
	HistoMaker.o \
	${ROOT_ALL}

ZEffTree.o: ../../MakeZEffTree/src/ZEffTree.h ../../MakeZEffTree/src/ZEffTree.cc
	${CCC} ../../MakeZEffTree/src/ZEffTree.cc ${ROOT_INCLUDES}

ElectronLocation.o: ../ElectronLocation/ElectronLocation.h ../ElectronLocation/ElectronLocation.cc
	${CCC} ../ElectronLocation/ElectronLocation.cc

HistoMaker.o: HistoMaker.h HistoMaker.cc
	${CCC} HistoMaker.cc ${ROOT_INCLUDES}

clean:
	rm -f ZEffTree.o ElectronLocation.o HistoMaker.o PostCutPlotter.exe
