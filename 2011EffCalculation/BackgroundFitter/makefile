# Pull in ROOT
ROOT_INCLUDES=`root-config --cflags`
ROOT_ALL=`root-config --cflags --libs`

#Compiler
CC=g++ -O2
CCC=${CC} -c

all: BackgroundFitter.exe
	
BackgroundFitter.exe: ZEffTree.o
	${CC} -o BackgroundFitter.exe \
	BackgroundFitter.cc \
	ZEffTree.o \
	${ROOT_ALL}

ZEffTree.o: ../../MakeZEffTree/src/ZEffTree.h ../../MakeZEffTree/src/ZEffTree.cc
	${CCC} ../../MakeZEffTree/src/ZEffTree.cc ${ROOT_INCLUDES}

clean:
	rm -f ZEffTree.o
