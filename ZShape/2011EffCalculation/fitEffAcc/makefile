# Pull in ROOT
ROOT_INCLUDES=`root-config --cflags`
ROOT_ALL=`root-config --cflags --libs`

#Compiler
CC=g++ -O2 -g
CCC=${CC} -c

all: fitEffAcc_trigger.exe fitEffAcc.exe

fitEffAcc_trigger.exe: ZEffTree.o ElectronLocation.o BackgroundFunctions.o fitEffAcc_trigger.o
	${CC} -o fitEffAcc_trigger.exe \
	fitEffAcc_trigger.o \
	ZEffTree.o \
	BackgroundFunctions.o \
	ElectronLocation.o \
	${ROOT_ALL}

fitEffAcc.exe: ZEffTree.o ElectronLocation.o BackgroundFunctions.o fitEffAcc.o
	${CC} -o fitEffAcc.exe \
	fitEffAcc.o \
	ZEffTree.o \
	BackgroundFunctions.o \
	ElectronLocation.o \
	${ROOT_ALL}

%.o:%.cc
	${CCC} ${ROOT_INCLUDES} $< -o $@

ZEffTree.o: ../../MakeZEffTree/src/ZEffTree.h ../../MakeZEffTree/src/ZEffTree.cc
	${CCC} ../../MakeZEffTree/src/ZEffTree.cc ${ROOT_INCLUDES}

BackgroundFunctions.o: ../BackgroundLibrary/BackgroundFunctions.h ../BackgroundLibrary/BackgroundFunctions.cc
	${CCC} ../BackgroundLibrary/BackgroundFunctions.cc ${ROOT_INCLUDES}

ElectronLocation.o: ../ElectronLocation/ElectronLocation.h ../ElectronLocation/ElectronLocation.cc
	${CCC} ../ElectronLocation/ElectronLocation.cc

clean:
	rm -f ZEffTree.o ElectronLocation.o BackgroundFunctions.o fitEffAcc.exe fitEffAcc_trigger.exe fitEffAcc_trigger.o fitEffAcc.o
