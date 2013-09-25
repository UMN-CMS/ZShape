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
            int reject;
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

        void Clear() {
            gen.eta[0] = -10;
            gen.eta[1] = -10;
            gen.phi[0] = -10;
            gen.phi[1] = -10;
            gen.pt[0] = -1;
            gen.pt[1] = -1;
            gen.mz = -1;
            gen.yz = -100;
            gen.ptz = -100;
            gen.bits[0] = 0;
            gen.bits[1] = 0;
            gen.nverts = -1;
            gen.charge[0] = 0;
            gen.charge[1] = 0;
            gen.phistar = -999.;
            gen.esel[0] = -1.;
            gen.esel[1] = -1.;
            gen.e9e25[0] = -1.;
            gen.e9e25[1] = -1.;
            gen.ece9[0] = -1.;
            gen.ece9[1] = -1.;
            gen.reject = -1;
            reco.eta[0] = -10;
            reco.eta[1] = -10;
            reco.phi[0] = -10;
            reco.phi[1] = -10;
            reco.pt[0] = -1;
            reco.pt[1] = -1;
            reco.mz = -1;
            reco.yz = -100;
            reco.ptz = -100;
            reco.bits[0] = 0;
            reco.bits[1] = 0;
            reco.nverts = -1;
            reco.charge[0] = 0;
            reco.charge[1] = 0;
            reco.phistar = -999.;
            reco.esel[0] = -1.;
            reco.esel[1] = -1.;
            reco.e9e25[0] = -1.;
            reco.e9e25[1] = -1.;
            reco.ece9[0] = -1.;
            reco.ece9[1] = -1.;
            reco.reject = -1;
        }

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
                br_gen=m_tree->Branch("gen", &gen, "eta0/f:eta1:phi0:phi1:pt0:pt1:mz:yz:ptz:bits0/I:bits1:nverts:charge0:charge1:phistar/f:ece90:ece91:e9e250:e9e250:esel0:esel1:reject/I");
                br_reco=m_tree->Branch("reco", &reco, "eta0/f:eta1:phi0:phi1:pt0:pt1:mz:yz:ptz:bits0/I:bits1:nverts:charge0:charge1:phistar/f:ece90:ece91:e9e250:e9e250:esel0:esel1:reject/I");
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
