# Pull in ROOT
ROOT_INCLUDES=`root-config --cflags`
ROOT_ALL=`root-config --cflags --libs`

#Compiler
CC=g++ -O2 -g
CCC=${CC} -c

all: fitEffAcc_trigger.exe fitEffAcc.exe fitEffAcc_ecal_trigger.exe

fitEffAcc_trigger.exe: ZEffTree.o ElectronLocation.o BackgroundFunctions.o fitEffAcc_trigger.o FitterLibrary.o ZSmearer.o
	${CC} -o fitEffAcc_trigger.exe \
	fitEffAcc_trigger.o \
	ZEffTree.o \
	BackgroundFunctions.o \
	ElectronLocation.o \
	FitterLibrary.o \
	ZSmearer.o \
	${ROOT_ALL}

fitEffAcc_ecal_trigger.exe: ZEffTree.o ElectronLocation.o BackgroundFunctions.o fitEffAcc_ecal_trigger.o FitterLibrary.o ZSmearer.o
	${CC} -o fitEffAcc_ecal_trigger.exe \
	fitEffAcc_ecal_trigger.o \
	ZEffTree.o \
	BackgroundFunctions.o \
	ElectronLocation.o \
	FitterLibrary.o \
	ZSmearer.o \
	${ROOT_ALL}

fitEffAcc.exe: ZEffTree.o ElectronLocation.o BackgroundFunctions.o fitEffAcc.o ZSmearer.o
	${CC} -o fitEffAcc.exe \
	fitEffAcc.o \
	ZEffTree.o \
	BackgroundFunctions.o \
	ElectronLocation.o \
	ZSmearer.o \
	FitterLibrary.o \
	${ROOT_ALL}

# All .o files rely on the .cc files
%.o:%.cc
	${CCC} ${ROOT_INCLUDES} $< -o $@

# All .o files rely on the .h files
%.o:%.h
	${CCC} ${ROOT_INCLUDES} $< -o $@

ZEffTree.o: ../../MakeZEffTree/src/ZEffTree.h ../../MakeZEffTree/src/ZEffTree.cc
	${CCC} ../../MakeZEffTree/src/ZEffTree.cc ${ROOT_INCLUDES}

BackgroundFunctions.o: ../BackgroundLibrary/BackgroundFunctions.h ../BackgroundLibrary/BackgroundFunctions.cc
	${CCC} ../BackgroundLibrary/BackgroundFunctions.cc ${ROOT_INCLUDES}

ElectronLocation.o: ../ElectronLocation/ElectronLocation.h ../ElectronLocation/ElectronLocation.cc
	${CCC} ../ElectronLocation/ElectronLocation.cc

ZSmearer.o: ../ZSmearer/ZSmearer.h ../ZSmearer/ZSmearer.cc
	${CCC} ../ZSmearer/ZSmearer.cc ${ROOT_INCLUDES}

FitterLibrary.o: ../FitterLibrary/FitterLibrary.h ../FitterLibrary/FitterLibrary.cc
	${CCC} ../FitterLibrary/FitterLibrary.cc ${ROOT_INCLUDES}

clean:
	rm -f ZEffTree.o ElectronLocation.o BackgroundFunctions.o fitEffAcc.exe fitEffAcc_trigger.exe fitEffAcc_ecal_trigger.o fitEffAcc_trigger.o fitEffAcc.o ZSmearer.o FitterLibrary.o
