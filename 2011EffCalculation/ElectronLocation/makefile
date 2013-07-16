#Compiler
CC=g++ -O2
CCC=${CC} -c

all: testElectronLocation.exe
	
testElectronLocation.exe: ElectronLocation.o
	${CC} -o testElectronLocation.exe testElectronLocation.cc \
	ElectronLocation.o

ElectronLocation.o: ElectronLocation.h ElectronLocation.cc
	${CCC} ../ElectronLocation/ElectronLocation.cc

clean:
	rm -f ElectronLocation.o testElectronLocation.exe
