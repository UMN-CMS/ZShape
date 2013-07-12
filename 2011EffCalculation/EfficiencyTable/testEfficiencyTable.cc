#include "../EfficiencyTable/EfficiencyTable.h"
#include "../ElectronLocation/ElectronLocation.h"

#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>

int makeWeights(std::string EfficiencyTableFile){
    // Get our efficiency
    EfficiencyTable es(EfficiencyTableFile);
    es.print();

    // Loop over pts
    for (int PU = 0; PU < 15; PU++){
        for (int PT = 20; PT < 100; PT++){
            std::cout << PU << " ";
            std::cout << PT << " ";
            std::cout << EEp << " ";
            std::cout << es.getEff((double)PT, EEm, PU);
            std::cout << std::endl;
        }
    }

    return 0;
}

int main(int argc, char* argv[]){
    const short argcCorrect = 2;
    if (argc < argcCorrect) {
        std::cout<<"Not enough arguments. Use:\ntestEfficiencyTable.exe EfficiencyTableFile\n";
        return 1;
    } else if (argc > argcCorrect){
        std::cout<<"Too many arguments. Use:\ntestEfficiencyTable.exe EfficiencyTableFile\n";
        return 1;
    } else {
        // Read in arguments
        std::istringstream inStream;

        std::string EfficiencyTableFile;
        inStream.str(argv[1]);
        inStream >> EfficiencyTableFile;
        inStream.clear();

        return makeWeights(EfficiencyTableFile);
    }
}
