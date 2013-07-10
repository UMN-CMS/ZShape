# Pull in root libraries
ROOT_INCLUDES=`root-config --cflags`
CC=g++ -O2
CCC=$(CC) -c

all: ZEffTree.o Background.o ElectronLocation.o
	$(CC) -o fitEffAcc_trigger_with_inbuilt_hf_correction_with_smearing.exe fitEffAcc.cc \
	ZEffTree.o \
	Background.o \
	ElectronLocation.o \
	`root-config --cflags --libs`

ZEffTree.o: ../../MakeZEffTree/src/ZEffTree.h ../../MakeZEffTree/src/ZEffTree.cc
	$(CCC) ../../MakeZEffTree/src/ZEffTree.cc $(ROOT_INCLUDES)

Background.o: ../Background/Background.h ../Background/Background.cc
	$(CCC) ../Background/Background.cc $(ROOT_INCLUDES)

ElectronLocation.o: ../ElectronLocation/ElectronLocation.h ../ElectronLocation/ElectronLocation.cc
	$(CCC) ../ElectronLocation/ElectronLocation.cc

clean:
	rm -f ZEffTree.o Background.o ElectronLocation.o
