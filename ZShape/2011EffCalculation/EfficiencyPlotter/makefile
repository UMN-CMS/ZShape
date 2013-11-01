# Pull in ROOT
ROOT_INCLUDES=`root-config --cflags`
ROOT_ALL=`root-config --cflags --libs`

#Compiler
CC=g++ -O2
CCC=${CC} -c

all: Efficiency_Plotter.exe
	
Efficiency_Plotter.exe: Efficiency_Sheet.o EfficiencyStatistics.o Efficiency_Plotter.cc
	${CC} ${ROOT_ALL} -o Efficiency_Plotter.exe \
	Efficiency_Plotter.cc \
	Efficiency_Sheet.o \
	EfficiencyStatistics.o

Efficiency_Sheet.o: Efficiency_Sheet.cc Efficiency_Sheet.h
	${CCC} Efficiency_Sheet.cc Efficiency_Sheet.h

EfficiencyStatistics.o: EfficiencyStatistics.cc EfficiencyStatistics.h
	${CCC} ${ROOT_ALL} EfficiencyStatistics.cc  EfficiencyStatistics.h

# All .o files rely on the .cc files
%.o:%.cc
	${CCC} ${ROOT_INCLUDES} $< -o $@

# All .o files rely on the .h files
%.o:%.h
	${CCC} ${ROOT_INCLUDES} $< -o $@

clean:
	rm -f Efficiency_Plotter.exe Efficiency_Sheet.o EfficiencyStatistics.o Efficiency_Plotter.o EfficiencyStatistics.h.gch Efficiency_Sheet.h.gch
