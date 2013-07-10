#include "Background.h"

Background::Background(const std::string textFile){
    /* Open file */
    std::ifstream inFile(textFile.c_str());
    std::string line;

    /* Loop through lines */
    while( std::getline(inFile, line) ){
        if (line[0] != '#'){ // Skip comments
            std::string item;
            std::vector<std::string> items;
            std::stringstream ss(line);

            bgNum value;
            ss >> value.minX;
            ss >> value.maxX;
            ss >> value.minPU;
            ss >> value.maxPU;
            ss >> value.minMZ;
            ss >> value.maxMZ;
            ss >> value.nparm;
            ss >> value.alpha;
            ss >> value.beta;
            ss >> value.gamma;
            ss >> value.delta;
            ss >> value.isPhiStar;
            values_.push_back(value);
        }
    }

    /* Close file */
    inFile.close();
}

void Background::setBackground(const double X, const double pu, const bool usePhiStar=false){
    // Loops through loaded backgrounds, if the requested X pu points
    //  exists within one, set that as the current background.
    current = NULL;
    for (std::vector<bgNum>::iterator i = values_.begin(); i != values_.end(); ++i){
        bgNum& bgn = *i;
        if (
                bgn.minX <= X && X <= bgn.maxX
                && bgn.minPU <= pu && pu <= bgn.maxPU
                && bgn.isPhiStar == usePhiStar
           ){
            current = &*i;
            break;
        }
    }
}

Double_t Background::bgFunc(Double_t *v, Double_t *par){
    Double_t fitval = TMath::Erfc((par[0]-v[0])/par[3]) * par[1] * TMath::Exp(-par[2]*v[0]);
    return fitval;
}

void Background::print(const bool printAll){
    if (printAll){
        int j = 0;
        for (std::vector<bgNum>::iterator i = values_.begin(); i != values_.end(); ++i){
            bgNum& bgn = *i;
            std::cout << "Background " << j << ":"<< std::endl;
            std::cout << "\t" << "minX: " << bgn.minX << std::endl;
            std::cout << "\t" << "maxX: " << bgn.maxX << std::endl;
            std::cout << "\t" << "minPU: " << bgn.minPU << std::endl;
            std::cout << "\t" << "maxPU: " << bgn.maxPU << std::endl;
            std::cout << "\t" << "minMZ: " << bgn.minMZ << std::endl;
            std::cout << "\t" << "maxMZ: " << bgn.maxMZ << std::endl;
            std::cout << "\t" << "nparm: " << bgn.nparm << std::endl;
            std::cout << "\t" << "alpha: " << bgn.alpha << std::endl;
            std::cout << "\t" << "beta: " << bgn.beta << std::endl;
            std::cout << "\t" << "gamma: " << bgn.gamma << std::endl;
            std::cout << "\t" << "delta: " << bgn.delta << std::endl;
            std::cout << "\t" << "isPhiStar: " << bgn.isPhiStar << std::endl;
            j++;
        }
    } else {
        if (current != NULL){
            std::cout << "Background: " << std::endl;
            std::cout << "\t" << "minPt: " << current->minX << std::endl;
            std::cout << "\t" << "maxPt: " << current->maxX << std::endl;
            std::cout << "\t" << "minPU: " << current->minPU << std::endl;
            std::cout << "\t" << "maxPU: " << current->maxPU << std::endl;
            std::cout << "\t" << "minMZ: " << current->minMZ << std::endl;
            std::cout << "\t" << "maxMZ: " << current->maxMZ << std::endl;
            std::cout << "\t" << "nparm: " << current->nparm << std::endl;
            std::cout << "\t" << "alpha: " << current->alpha << std::endl;
            std::cout << "\t" << "beta: " << current->beta << std::endl;
            std::cout << "\t" << "gamma: " << current->gamma << std::endl;
            std::cout << "\t" << "delta: " << current->delta << std::endl;
            std::cout << "\t" << "isPhiStar: " << current->isPhiStar << std::endl;
        } else {
            std::cout << "Background is not set" << std::endl;
        }
    }
}

/* Compile time notes:
 *    g++ -O2 -o Background.exe Background.cc `root-config --cflags --libs`
 */
