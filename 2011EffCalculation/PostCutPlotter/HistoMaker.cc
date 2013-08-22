#include "HistoMaker.h"

MakeHistograms::MakeHistograms(TDirectory* td){
    // Make this the current working dir
    tdir = td;
    tdir->cd();
    // Set up all the histograms
    // Z Mass
    Z0Mass = new TH1I("Z0_mass", "Z0_mass", 50, 50., 150.);
    Z0Mass->SetDirectory(tdir);
    Z0Mass->GetXaxis()->SetTitle("m_{ee} [GeV]");
    Z0Mass->GetYaxis()->SetTitle("Counts/GeV");
    // Z Mass Fine
    Z0MassFine = new TH1I("Z0_mass_fine", "Z0_mass_fine", 120, 60., 120.);
    Z0MassFine->SetDirectory(tdir);
    Z0MassFine->GetXaxis()->SetTitle("m_{ee} [GeV]");
    Z0MassFine->GetYaxis()->SetTitle("Counts/GeV");
    // Z Mass Fine
    Z0Rapidity = new TH1I("Z0_rapidity", "Z0_rapidity", 100, -5., 5.);
    Z0Rapidity->SetDirectory(tdir);
    Z0Rapidity->GetXaxis()->SetTitle("Y_{ee}");
    Z0Rapidity->GetYaxis()->SetTitle("Counts");
    // Z pt
    Z0pt = new TH1I("Z0_pt", "Z0_pt", 200, 0., 400.);
    Z0pt->SetDirectory(tdir);
    Z0pt->GetXaxis()->SetTitle("p_{T,Z} [GeV]");
    Z0pt->GetYaxis()->SetTitle("Counts/Gev");
    // e pt
    e0pt = new TH1I("e0_pt", "e0_pt", 200, 0., 400.);
    e0pt->SetDirectory(tdir);
    e0pt->GetXaxis()->SetTitle("p_{T,e_{0}} [GeV]");
    e0pt->GetYaxis()->SetTitle("Counts/Gev");
    e1pt = new TH1I("e1_pt", "e1_pt", 200, 0., 400.);
    e1pt->SetDirectory(tdir);
    e1pt->GetXaxis()->SetTitle("p_{T,e_{0}} [GeV]");
    e1pt->GetYaxis()->SetTitle("Counts/Gev");
    // e phi
    e0phi = new TH1I("e0_phi", "e0_phi", 60, -3.14, 3.14);
    e0phi->SetDirectory(tdir);
    e0phi->GetXaxis()->SetTitle("#phi_{e_{0}}");
    e0phi->GetYaxis()->SetTitle("Counts");
    e1phi = new TH1I("e1_phi", "e1_phi", 60, -3.14, 3.14);
    e1phi->SetDirectory(tdir);
    e1phi->GetXaxis()->SetTitle("#phi_{e_{0}}");
    e1phi->GetYaxis()->SetTitle("Counts");
    // e eta
    e0eta = new TH1I("e0_eta", "e0_eta", 50, -5., 5.);
    e0eta->SetDirectory(tdir);
    e0eta->GetXaxis()->SetTitle("#eta_{e_{0}}");
    e0eta->GetYaxis()->SetTitle("Counts");
    e1eta = new TH1I("e1_eta", "e1_eta", 50, -5., 5.);
    e1eta->SetDirectory(tdir);
    e1eta->GetXaxis()->SetTitle("#eta_{e_{0}}");
    e1eta->GetYaxis()->SetTitle("Counts");
    // Phistar
    phistar = new TH1I("phistar", "phistar", 1000, 0., 1.);
    phistar->SetDirectory(tdir);
    phistar->GetXaxis()->SetTitle("#phi^{*}");
    phistar->GetYaxis()->SetTitle("Counts");
    // Pileup
    pileup = new TH1I("pileup", "pileup", 20, 0., 20.);
    pileup->SetDirectory(tdir);
    pileup->GetXaxis()->SetTitle("Pile Up");
    pileup->GetYaxis()->SetTitle("Counts");
}

void MakeHistograms::fill(const ZEffTree::ZInfo* zi, const int e0, const int e1){
    // Fill histos
    Z0Mass->Fill(zi->mz);
    Z0MassFine->Fill(zi->mz);
    Z0Rapidity->Fill(zi->yz);
    Z0pt->Fill(zi->ptz);
    e0pt->Fill(zi->pt[e0]);
    e0eta->Fill(zi->eta[e0]);
    e0phi->Fill(zi->phi[e0]);
    e1pt->Fill(zi->pt[e1]);
    e1eta->Fill(zi->eta[e1]);
    e1phi->Fill(zi->phi[e1]);
    phistar->Fill(zi->phistar);
    pileup->Fill(zi->nverts);
}

void MakeHistograms::print(){
    // Get the name of the TDir
    std::string basename;
    basename.assign(tdir->GetName());

    // Write PNGs
    std::string Z0MassStr = basename + "_Z0Mass.png";
    TCanvas* Z0MassC = new TCanvas(Z0MassStr.c_str(), Z0MassStr.c_str(), 1280, 640);
    Z0Mass->Draw();
    Z0MassC->Print(Z0MassStr.c_str());

    std::string Z0MassFineStr = basename + "_Z0MassFine.png";
    TCanvas* Z0MassFineC = new TCanvas(Z0MassFineStr.c_str(), Z0MassFineStr.c_str(), 1280, 640);
    Z0MassFine->Draw();
    Z0MassFineC->Print(Z0MassFineStr.c_str());

    std::string Z0RapidityStr = basename + "_Z0Rapidity.png";
    TCanvas* Z0RapidityC = new TCanvas(Z0RapidityStr.c_str(), Z0RapidityStr.c_str(), 1280, 640);
    Z0Rapidity->Draw();
    Z0RapidityC->Print(Z0RapidityStr.c_str());

    std::string Z0ptStr = basename + "_Z0pt.png";
    TCanvas* Z0ptC = new TCanvas(Z0ptStr.c_str(), Z0ptStr.c_str(), 1280, 640);
    Z0pt->Draw();
    Z0ptC->Print(Z0ptStr.c_str());

    std::string e0ptStr = basename + "_e0pt.png";
    TCanvas* e0ptC = new TCanvas(e0ptStr.c_str(), e0ptStr.c_str(), 1280, 640);
    e0pt->Draw();
    e0ptC->Print(e0ptStr.c_str());

    std::string e1ptStr = basename + "_e1pt.png";
    TCanvas* e1ptC = new TCanvas(e1ptStr.c_str(), e1ptStr.c_str(), 1280, 640);
    e1pt->Draw();
    e1ptC->Print(e1ptStr.c_str());

    std::string e0etaStr = basename + "_e0eta.png";
    TCanvas* e0etaC = new TCanvas(e0etaStr.c_str(), e0etaStr.c_str(), 1280, 640);
    e0eta->Draw();
    e0etaC->Print(e0etaStr.c_str());

    std::string e1etaStr = basename + "_e1eta.png";
    TCanvas* e1etaC = new TCanvas(e1etaStr.c_str(), e1etaStr.c_str(), 1280, 640);
    e1eta->Draw();
    e1etaC->Print(e1etaStr.c_str());

    std::string e0phiStr = basename + "_e0phi.png";
    TCanvas* e0phiC = new TCanvas(e0phiStr.c_str(), e0phiStr.c_str(), 1280, 640);
    e0phi->Draw();
    e0phiC->Print(e0phiStr.c_str());

    std::string e1phiStr = basename + "_e1phi.png";
    TCanvas* e1phiC = new TCanvas(e1phiStr.c_str(), e1phiStr.c_str(), 1280, 640);
    e1phi->Draw();
    e1phiC->Print(e1phiStr.c_str());

    std::string phistarStr = basename + "_phistar.png";
    TCanvas* phistarC = new TCanvas(phistarStr.c_str(), phistarStr.c_str(), 1280, 640);
    phistar->Draw();
    phistarC->Print(phistarStr.c_str());

    std::string pileupStr = basename + "_pileup.png";
    TCanvas* pileupC = new TCanvas(pileupStr.c_str(), pileupStr.c_str(), 1280, 640);
    pileup->Draw();
    pileupC->Print(pileupStr.c_str());
}
