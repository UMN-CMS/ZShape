#include "ZEffTree.h"

ZEffTree::ZEffTree(TFile& f, const bool writable) : m_file(f) {
    makeBranches(writable);
    prepBitmap();
}

int ZEffTree::cutToBit(const std::string& cut) {
    std::map<std::string,int>::const_iterator i=cutToBits_.find(cut);
    return (i==cutToBits_.end())?(-1):(i->second);
}


bool ZEffTree::ZInfo::isSelected(const int ielec, const std::string& bitname) const {
    int ibit=ZEffTree::cutToBit(bitname);
    if (ibit<0 || ielec<0 || ielec>=2){
        return false;
    }
    return ((bits[ielec] & (1 << ibit)) != 0);
}

void ZEffTree::ZInfo::setBit(const int ielec, const std::string& bitname, const bool val){
    const int ibit=ZEffTree::cutToBit(bitname);
    if (ibit<0 || ielec<0 || ielec>=2){
        return;
    }
    const int mask = 1 << ibit;
    if (val){
        bits[ielec] = (bits[ielec] | mask);
    } else {
        bits[ielec] = (bits[ielec] & ~mask);
    }
}

// Print all the contents
void ZEffTree::Print(){
    std::cout << "ZEffTreeEntry:" << std::endl;
    std::cout << "\tgen.eta[0]: " << gen.eta[0] << std::endl;
    std::cout << "\tgen.eta[1]: " << gen.eta[1] << std::endl;
    std::cout << "\tgen.phi[0]: " << gen.phi[0] << std::endl;
    std::cout << "\tgen.phi[1]: " << gen.phi[1] << std::endl;
    std::cout << "\tgen.pt[0]: " << gen.pt[0] << std::endl;
    std::cout << "\tgen.pt[1]: " << gen.pt[1] << std::endl;
    std::cout << "\tgen.mz: " << gen.mz << std::endl;
    std::cout << "\tgen.yz: " << gen.yz << std::endl;
    std::cout << "\tgen.ptz: " << gen.ptz << std::endl;
    std::cout << "\tgen.bits[0]: " << gen.bits[0] << std::endl;
    std::cout << "\tgen.bits[1]: " << gen.bits[1] << std::endl;
    std::cout << "\tgen.nverts: " << gen.nverts << std::endl;
    std::cout << "\tgen.charge[0]: " << gen.charge[0] << std::endl;
    std::cout << "\tgen.charge[1]: " << gen.charge[1] << std::endl;
    std::cout << "\tgen.phistar: " << gen.phistar << std::endl;
    std::cout << "\treco.eta[0]: " << reco.eta[0] << std::endl;
    std::cout << "\treco.eta[1]: " << reco.eta[1] << std::endl;
    std::cout << "\treco.phi[0]: " << reco.phi[0] << std::endl;
    std::cout << "\treco.phi[1]: " << reco.phi[1] << std::endl;
    std::cout << "\treco.pt[0]: " << reco.pt[0] << std::endl;
    std::cout << "\treco.pt[1]: " << reco.pt[1] << std::endl;
    std::cout << "\treco.mz: " << reco.mz << std::endl;
    std::cout << "\treco.yz: " << reco.yz << std::endl;
    std::cout << "\treco.ptz: " << reco.ptz << std::endl;
    std::cout << "\treco.nverts: " << reco.nverts << std::endl;
    std::cout << "\treco.charge[0]: " << reco.charge[0] << std::endl;
    std::cout << "\treco.charge[1]: " << reco.charge[1] << std::endl;
    std::cout << "\treco.phistar: " << reco.phistar << std::endl;

    // Loop over all the cuts
    std::cout << "\tCuts:" << std::endl;
    typedef std::map<std::string, int>::const_iterator map_it;
    for (map_it i = cutToBits_.begin(); i != cutToBits_.end(); ++i){
        std::cout << "\t\t" << i->first << std::endl;
        std::cout << "\t\t\t";
        std::cout << "Gen e0: " << gen.isSelected(0, i->first);
        std::cout << " e1: " << gen.isSelected(1, i->first);
        std::cout << std::endl;
        std::cout << "\t\t\t";
        std::cout << "Reco e0: " << reco.isSelected(0, i->first);
        std::cout << " e1: " << reco.isSelected(1, i->first);
        std::cout << std::endl;
    }
}

/* Map from names to bitnums  */
std::map<std::string, int> ZEffTree::cutToBits_;

void ZEffTree::prepBitmap() {
    if (!cutToBits_.empty()) {
        return;
    }
    cutToBits_["Supercluster-Eta"] = 0;
    cutToBits_["GsfTrack-EtaDet"] = 1;
    cutToBits_["Iso-Pt"] = 2;
    cutToBits_["ElectronId-EtaDet"] = 3;
    cutToBits_["HLT-EtaDet"] = 4;
    cutToBits_["HFElectronId-EtaDet"] = 5;
    cutToBits_["HFSuperCluster-Et"] = 6;
    cutToBits_["HFTightElectronId-EtaDet"] = 7;
    cutToBits_["EID95"] = 8;
    cutToBits_["ISO95"] = 9;
    cutToBits_["EID90"] = 10;
    cutToBits_["ISO90"] = 11;
    cutToBits_["EID85"] = 12;
    cutToBits_["ISO85"] = 13;
    cutToBits_["EID80"] = 14;
    cutToBits_["ISO80"] = 15;
    cutToBits_["EID70"] = 16;
    cutToBits_["ISO70"] = 17;
    cutToBits_["EID60"] = 18;
    cutToBits_["ISO60"] = 19;
    cutToBits_["HLT-GSF"] = 20;
    cutToBits_["ISO80Only"] = 21;
    cutToBits_["ISO80Conv"] = 22;
    cutToBits_["EID80Only"] = 23;
    cutToBits_["EID80Conv"] = 24;
    cutToBits_["WP95"] = 25;
    cutToBits_["WP90"] = 26;
    cutToBits_["WP85"] = 27;
    cutToBits_["WP80"] = 28;
    cutToBits_["NTLooseElectronId-EtaDet"] = 29;
    //cutToBits_["NTTightElectronId-EtaDet"] = 30;
    //cutToBits_["HFTID"] = 31;
    cutToBits_["HFTID"] = 30;
}
