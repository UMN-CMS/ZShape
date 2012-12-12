#include "TFile.h"
#include "TBranch.h"
#include "TTree.h"
#include <map>
#include <string>

#ifndef ZEffTree_h_included
#define ZEffTree_h_included

class ZEffTree {
    public:

        ZEffTree(TFile& f, bool writable);

        static int cutToBit(const std::string& cut);

        struct ZInfo {
            float eta[2];
            float phi[2];
            float pt[2];
            float mz, yz, qtz;
            int bits[2];
            int nverts;
            bool isSelected(int ielec, const std::string& bitname) const;
            void setBit(int ielec, const std::string& bitname, bool val);
            int charge[2];
            float phistar;
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
            gen.qtz = -100;
            gen.bits[0] = 0;
            gen.bits[1] = 0;
            gen.nverts = -1;
            gen.charge[0] = 0;
            gen.charge[1] = 0;
            gen.phistar = -999.;
            reco.eta[0] = -10;
            reco.eta[1] = -10;
            reco.phi[0] = -10;
            reco.phi[1] = -10;
            reco.pt[0] = -1;
            reco.pt[1] = -1;
            reco.mz = -1;
            reco.yz = -100;
            reco.qtz = -100;
            reco.bits[0] = 0;
            reco.bits[1] = 0;
            reco.nverts = -1;
            reco.charge[0] = 0;
            reco.charge[1] = 0;
            reco.phistar = -999.;
        }

    private:
        TFile& m_file;
        TTree* m_tree;
        int nevt;
        TBranch* br_gen, *br_reco;

        void makeBranches(bool writable) {
            nevt=0;
            if (writable) {
                m_file.cd();
                m_tree=new TTree("ZEffs","Minnesota ZEffs");
                br_gen=m_tree->Branch("gen",&gen,"eta0/f:eta1:phi0:phi1:pt0:pt1:mz:yz:qtz:bits0/I:bits1:nverts:charge0:charge1:phistar/f");
                br_reco=m_tree->Branch("reco",&reco,"eta0/f:eta1:phi0:phi1:pt0:pt1:mz:yz:qtz:bits0/I:bits1:nverts:charge0:charge1:phistar/f");
            } else {
                m_tree=(TTree*)m_file.Get("ZEffs");
                m_tree->SetBranchAddress("gen",&gen);
                m_tree->SetBranchAddress("reco",&reco);
            }
        }

        /* Map from names to bitnums  */
        static std::map<std::string, int> cutToBits_;

        void prepBitmap();

};

#endif
