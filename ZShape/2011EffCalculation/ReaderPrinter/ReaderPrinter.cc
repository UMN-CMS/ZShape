#include "../../MakeZEffTree/src/ZEffTree.h"

#include "TFile.h"

// STD
#include <string>
#include <sstream>
#include <vector>
#include <iostream>

int readAndPrint(const std::string tupleFile){
    // Open signal file and make histograms
    TFile ZSFile(tupleFile.c_str(), "READ");
    ZEffTree* zes;
    zes = new ZEffTree(ZSFile, false);

    bool run1 = true;
    while (run1){
        zes->Entries();
        zes->Print();
        // Advance
        run1 = zes->GetNextEvent();
    }

    return 0;
}

int main(int argc, char* argv[]){
    const short argcCorrect = 2;
    if (argc < argcCorrect) {
        std::cout<<"Not enough arguments. Use:\nReaderPrinter.exe TupleFile\n";
        return 1;
    } else if (argc > argcCorrect){
        std::cout<<"Too many arguments. Use:\nReaderPrinter.exe TupleFile\n";
        return 1;
    } else {
        // Read in arguments
        std::istringstream inStream;

        std::string tupleFile;
        inStream.str(argv[1]);
        inStream >> tupleFile;
        inStream.clear();

        return readAndPrint(tupleFile);
    }
}
