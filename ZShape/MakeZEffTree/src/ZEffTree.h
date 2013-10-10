#ifndef ZEffTree_h_included
#define ZEffTree_h_included

#include "TFile.h"
#include "TTree.h"
#include <map>
#include <string>

class ZEffTree {
    public:
        ZEffTree(TFile& f, const bool writable);

        static int cutToBit(const std::string& cut);

        struct ZInfo {
            float eta[2];
            float phi[2];
            float pt[2];
            float mz, yz, ptz;
            int bits[2];
            int nverts;
            bool isSelected(const int ielec, const std::string& bitname) const;
            void setBit(const int ielec, const std::string& bitname, const bool val);
            int charge[2];
            float phistar;
            float ece9[2];
            float e9e25[2];
            float esel[2];
            int ntp;
            bool trigprobe[2];
            bool trigtag[2];
            float trigeta[2];
            float trigphi[2];
            float trigpt[2];
            float trigmz, trigyz, trigptz;
            float r9[2];
        } gen, reco;

        void Fill() {
            m_tree->Fill();
        }

        void Write() {
            m_file.Write();
        }

        int Entries() {
            return m_tree->GetEntries();
        }

        bool GetNextEvent() {
            if (nevt==Entries()) {
                return false;
            }
            m_tree->GetEntry(nevt);
            nevt++;
            return true;
        }

        void Clear();
        void Print();

    private:
        TFile& m_file;
        TTree* m_tree;
        int nevt;
        TBranch* br_gen, *br_reco;

        void makeBranches(const bool writable) {
            nevt=0;
            if (writable) {
                m_file.cd();
                m_tree = new TTree("ZEffs", "Minnesota ZEffs");
                br_gen=m_tree->Branch("gen", &gen, "eta0/f:eta1:phi0:phi1:pt0:pt1:mz:yz:ptz:bits0/I:bits1:nverts:charge0:charge1:phistar/f:ece90:ece91:e9e250:e9e251:esel0:esel1:ntp/I:trigtag0/O:trigtag1:trigprobe0:trigprobe1:trigeta0/f:trigeta1:trigphi0:trigphi1:trigpt0:trigpt1:trigmz:trigyz:trigptz:r90:r91");
                br_reco=m_tree->Branch("reco", &reco, "eta0/f:eta1:phi0:phi1:pt0:pt1:mz:yz:ptz:bits0/I:bits1:nverts:charge0:charge1:phistar/f:ece90:ece91:e9e251:e9e250:esel0:esel1:ntp/I:trigtag0/O:trigtag1:trigprobe0:trigprobe1:trigeta0/f:trigeta1:trigphi0:trigphi1:trigpt0:trigpt1:trigmz:trigyz:trigptz:r90:r91");
            } else {
                m_tree = (TTree*)m_file.Get("ZEffs");
                m_tree->SetBranchAddress("gen", &gen);
                m_tree->SetBranchAddress("reco", &reco);
            }
        }

        /* Map from names to bitnums  */
        static std::map<std::string, int> cutToBits_;

        void prepBitmap();
};

#endif
