{
//=========Macro generated from canvas: finalK1_ZQT/finalK1_ZQT
//=========  (Wed Jun 22 14:40:20 2011) by ROOT version5.28/00d
   TCanvas *finalK1_ZQT = new TCanvas("finalK1_ZQT", "finalK1_ZQT",0,0,800,600);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   gStyle->SetOptTitle(0);
   finalK1_ZQT->SetHighLightColor(2);
   finalK1_ZQT->Range(-0.6198982,-0.01417621,2.956996,0.07443138);
   finalK1_ZQT->SetFillColor(0);
   finalK1_ZQT->SetBorderMode(0);
   finalK1_ZQT->SetBorderSize(2);
   finalK1_ZQT->SetLogx();
   finalK1_ZQT->SetTickx(1);
   finalK1_ZQT->SetTicky(1);
   finalK1_ZQT->SetLeftMargin(0.13);
   finalK1_ZQT->SetRightMargin(0.05);
   finalK1_ZQT->SetTopMargin(0.05);
   finalK1_ZQT->SetBottomMargin(0.16);
   finalK1_ZQT->SetFrameFillStyle(0);
   finalK1_ZQT->SetFrameLineWidth(2);
   finalK1_ZQT->SetFrameBorderMode(0);
   finalK1_ZQT->SetFrameFillStyle(0);
   finalK1_ZQT->SetFrameLineWidth(2);
   finalK1_ZQT->SetFrameBorderMode(0);
   Double_t xAxis1[19] = {0.7, 2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20, 30, 40, 50, 70, 90, 110, 150, 190, 250, 600}; 
   Double_t yAxis1[21] = {1e-06, 0.003501, 0.007001, 0.010501, 0.014001, 0.017501, 0.021001, 0.024501, 0.028001, 0.031501, 0.035001, 0.038501, 0.042001, 0.045501, 0.049001, 0.052501, 0.056001, 0.059501, 0.063001, 0.066501, 0.070001}; 
   
   TH2F *dummy__1 = new TH2F("dummy__1","",18, xAxis1,20, yAxis1);
   dummy__1->SetDirectory(0);
   dummy__1->SetFillColor(63);
   dummy__1->SetFillStyle(0);
   dummy__1->SetLineStyle(0);
   dummy__1->SetLineWidth(2);
   dummy__1->SetMarkerStyle(20);
   dummy__1->GetXaxis()->SetTitle("p_{T,ee} [GeV/c]");
   dummy__1->GetXaxis()->CenterTitle(true);
   dummy__1->GetXaxis()->SetLabelFont(42);
   dummy__1->GetXaxis()->SetLabelOffset(0.007);
   dummy__1->GetXaxis()->SetLabelSize(0.05);
   dummy__1->GetXaxis()->SetTitleSize(0.06);
   dummy__1->GetXaxis()->SetTitleOffset(1.2);
   dummy__1->GetXaxis()->SetTitleFont(42);
   dummy__1->GetYaxis()->SetTitle("1/#sigma d#sigma/dp_{T} [GeV^{-1}]");
   dummy__1->GetYaxis()->SetLabelFont(42);
   dummy__1->GetYaxis()->SetLabelOffset(0.007);
   dummy__1->GetYaxis()->SetLabelSize(0.05);
   dummy__1->GetYaxis()->SetTitleSize(0.06);
   dummy__1->GetYaxis()->SetTitleOffset(1.05);
   dummy__1->GetYaxis()->SetTitleFont(42);
   dummy__1->GetZaxis()->SetLabelFont(42);
   dummy__1->GetZaxis()->SetLabelOffset(0.007);
   dummy__1->GetZaxis()->SetLabelSize(0.05);
   dummy__1->GetZaxis()->SetTitleSize(0.06);
   dummy__1->GetZaxis()->SetTitleFont(42);
   dummy__1->Draw("");
   
   TGraph *graph = new TGraph(19);
   graph->SetName("Graph");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);
   graph->SetMarkerStyle(24);
   graph->SetPoint(0,1.25,0.01904329);
   graph->SetPoint(1,3.75,0.03953456);
   graph->SetPoint(2,6.25,0.03851732);
   graph->SetPoint(3,8.75,0.03176355);
   graph->SetPoint(4,11.25,0.026244);
   graph->SetPoint(5,13.75,0.02038704);
   graph->SetPoint(6,16.25,0.01552994);
   graph->SetPoint(7,18.75,0.01252741);
   graph->SetPoint(8,25,0.008643602);
   graph->SetPoint(9,35,0.004008645);
   graph->SetPoint(10,45,0.002233421);
   graph->SetPoint(11,60,0.001282618);
   graph->SetPoint(12,80,0.0005444989);
   graph->SetPoint(13,100,0.0003187131);
   graph->SetPoint(14,130,0.0001507079);
   graph->SetPoint(15,170,3.586442e-05);
   graph->SetPoint(16,220,1.4439e-05);
   graph->SetPoint(17,425,6.098766e-07);
   graph->SetPoint(18,2050,0);
   
   TH1F *Graph_Graph1 = new TH1F("Graph_Graph1","Graph",100,1.125,2254.875);
   Graph_Graph1->SetMinimum(0);
   Graph_Graph1->SetMaximum(0.04348801);
   Graph_Graph1->SetDirectory(0);
   Graph_Graph1->SetStats(0);
   Graph_Graph1->SetFillColor(63);
   Graph_Graph1->SetFillStyle(0);
   Graph_Graph1->SetLineStyle(0);
   Graph_Graph1->SetLineWidth(2);
   Graph_Graph1->SetMarkerStyle(20);
   Graph_Graph1->GetXaxis()->SetLabelFont(42);
   Graph_Graph1->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph1->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph1->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph1->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph1->GetXaxis()->SetTitleFont(42);
   Graph_Graph1->GetYaxis()->SetLabelFont(42);
   Graph_Graph1->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph1->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph1->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph1->GetYaxis()->SetTitleOffset(1.05);
   Graph_Graph1->GetYaxis()->SetTitleFont(42);
   Graph_Graph1->GetZaxis()->SetLabelFont(42);
   Graph_Graph1->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph1->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph1->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph1->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph1);
   
   graph->Draw("p");
   
   graph = new TGraph(19);
   graph->SetName("Graph");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);
   graph->SetMarkerStyle(25);
   graph->SetPoint(0,1.25,0.01940249);
   graph->SetPoint(1,3.75,0.040071);
   graph->SetPoint(2,6.25,0.03880498);
   graph->SetPoint(3,8.75,0.03235711);
   graph->SetPoint(4,11.25,0.02673363);
   graph->SetPoint(5,13.75,0.02049185);
   graph->SetPoint(6,16.25,0.01604606);
   graph->SetPoint(7,18.75,0.01280741);
   graph->SetPoint(8,25,0.008773811);
   graph->SetPoint(9,35,0.004070401);
   graph->SetPoint(10,45,0.002318583);
   graph->SetPoint(11,60,0.001335945);
   graph->SetPoint(12,80,0.0005630843);
   graph->SetPoint(13,100,0.0003312261);
   graph->SetPoint(14,130,0.0001545722);
   graph->SetPoint(15,170,3.68029e-05);
   graph->SetPoint(16,220,1.472116e-05);
   graph->SetPoint(17,425,6.309068e-07);
   graph->SetPoint(18,2050,0);
   
   TH1F *Graph_Graph2 = new TH1F("Graph_Graph2","Graph",100,1.125,2254.875);
   Graph_Graph2->SetMinimum(0);
   Graph_Graph2->SetMaximum(0.0440781);
   Graph_Graph2->SetDirectory(0);
   Graph_Graph2->SetStats(0);
   Graph_Graph2->SetFillColor(63);
   Graph_Graph2->SetFillStyle(0);
   Graph_Graph2->SetLineStyle(0);
   Graph_Graph2->SetLineWidth(2);
   Graph_Graph2->SetMarkerStyle(20);
   Graph_Graph2->GetXaxis()->SetLabelFont(42);
   Graph_Graph2->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph2->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph2->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph2->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph2->GetXaxis()->SetTitleFont(42);
   Graph_Graph2->GetYaxis()->SetLabelFont(42);
   Graph_Graph2->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph2->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph2->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph2->GetYaxis()->SetTitleOffset(1.05);
   Graph_Graph2->GetYaxis()->SetTitleFont(42);
   Graph_Graph2->GetZaxis()->SetLabelFont(42);
   Graph_Graph2->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph2->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph2->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph2->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph2);
   
   graph->Draw("p");
   
   TGraphErrors *gre = new TGraphErrors(19);
   gre->SetName("Graph");
   gre->SetTitle("Graph");
   gre->SetFillColor(1);
   gre->SetMarkerStyle(20);
   gre->SetPoint(0,1.25,0.03079786);
   gre->SetPointError(0,1.25,0.002502774);
   gre->SetPoint(1,3.75,0.05991863);
   gre->SetPointError(1,1.25,0.003219918);
   gre->SetPoint(2,6.25,0.05390303);
   gre->SetPointError(2,1.25,0.003198681);
   gre->SetPoint(3,8.75,0.04188526);
   gre->SetPointError(3,1.25,0.002984543);
   gre->SetPoint(4,11.25,0.03595636);
   gre->SetPointError(4,1.25,0.002765184);
   gre->SetPoint(5,13.75,0.02737159);
   gre->SetPointError(5,1.25,0.002498744);
   gre->SetPoint(6,16.25,0.02014037);
   gre->SetPointError(6,1.25,0.002250284);
   gre->SetPoint(7,18.75,0.01614115);
   gre->SetPointError(7,1.25,0.001982233);
   gre->SetPoint(8,25,0.01214224);
   gre->SetPointError(8,5,0.0004476119);
   gre->SetPoint(9,35,0.005635781);
   gre->SetPointError(9,5,0.0003099369);
   gre->SetPoint(10,45,0.003190485);
   gre->SetPointError(10,5,0.0002401275);
   gre->SetPoint(11,60,0.001906722);
   gre->SetPointError(11,10,0.000116633);
   gre->SetPoint(12,80,0.0007875502);
   gre->SetPointError(12,10,7.737363e-05);
   gre->SetPoint(13,100,0.0004522942);
   gre->SetPointError(13,10,5.863744e-05);
   gre->SetPoint(14,130,0.000216537);
   gre->SetPointError(14,20,2.6004e-05);
   gre->SetPoint(15,170,4.795527e-05);
   gre->SetPointError(15,20,1.312956e-05);
   gre->SetPoint(16,220,2.056221e-05);
   gre->SetPointError(16,30,6.48062e-06);
   gre->SetPoint(17,425,8.131971e-07);
   gre->SetPointError(17,175,5.232354e-07);
   gre->SetPoint(18,2050,-3.06032e-11);
   gre->SetPointError(18,1450,0);
   
   TH1F *Graph1 = new TH1F("Graph1","Graph",100,0.375,3849.958);
   Graph1->SetMinimum(-0.006313855);
   Graph1->SetMaximum(0.06945241);
   Graph1->SetDirectory(0);
   Graph1->SetStats(0);
   Graph1->SetFillColor(63);
   Graph1->SetFillStyle(0);
   Graph1->SetLineStyle(0);
   Graph1->SetLineWidth(2);
   Graph1->SetMarkerStyle(20);
   Graph1->GetXaxis()->SetLabelFont(42);
   Graph1->GetXaxis()->SetLabelOffset(0.007);
   Graph1->GetXaxis()->SetLabelSize(0.05);
   Graph1->GetXaxis()->SetTitleSize(0.06);
   Graph1->GetXaxis()->SetTitleOffset(0.9);
   Graph1->GetXaxis()->SetTitleFont(42);
   Graph1->GetYaxis()->SetLabelFont(42);
   Graph1->GetYaxis()->SetLabelOffset(0.007);
   Graph1->GetYaxis()->SetLabelSize(0.05);
   Graph1->GetYaxis()->SetTitleSize(0.06);
   Graph1->GetYaxis()->SetTitleOffset(1.05);
   Graph1->GetYaxis()->SetTitleFont(42);
   Graph1->GetZaxis()->SetLabelFont(42);
   Graph1->GetZaxis()->SetLabelOffset(0.007);
   Graph1->GetZaxis()->SetLabelSize(0.05);
   Graph1->GetZaxis()->SetTitleSize(0.06);
   Graph1->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph1);
   
   gre->Draw("p");
   
   gre = new TGraphErrors(18);
   gre->SetName("Graph");
   gre->SetTitle("Graph");
   gre->SetFillColor(1);
   gre->SetMarkerStyle(0);
   gre->SetPoint(0,1.25,0.03079786);
   gre->SetPointError(0,1.25,0.002685906);
   gre->SetPoint(1,3.75,0.05991863);
   gre->SetPointError(1,1.25,0.003543755);
   gre->SetPoint(2,6.25,0.05390303);
   gre->SetPointError(2,1.25,0.003263169);
   gre->SetPoint(3,8.75,0.04188526);
   gre->SetPointError(3,1.25,0.003004496);
   gre->SetPoint(4,11.25,0.03595636);
   gre->SetPointError(4,1.25,0.002787796);
   gre->SetPoint(5,13.75,0.02737159);
   gre->SetPointError(5,1.25,0.0025198);
   gre->SetPoint(6,16.25,0.02014037);
   gre->SetPointError(6,1.25,0.002280989);
   gre->SetPoint(7,18.75,0.01614115);
   gre->SetPointError(7,1.25,0.002010383);
   gre->SetPoint(8,25,0.01214224);
   gre->SetPointError(8,5,0.0004974383);
   gre->SetPoint(9,35,0.005635781);
   gre->SetPointError(9,5,0.0003344588);
   gre->SetPoint(10,45,0.003190485);
   gre->SetPointError(10,5,0.000258197);
   gre->SetPoint(11,60,0.001906722);
   gre->SetPointError(11,10,0.000130905);
   gre->SetPoint(12,80,0.0007875502);
   gre->SetPointError(12,10,8.330572e-05);
   gre->SetPoint(13,100,0.0004522942);
   gre->SetPointError(13,10,6.146515e-05);
   gre->SetPoint(14,130,0.000216537);
   gre->SetPointError(14,20,2.789575e-05);
   gre->SetPoint(15,170,4.795527e-05);
   gre->SetPointError(15,20,1.51696e-05);
   gre->SetPoint(16,220,2.056221e-05);
   gre->SetPointError(16,30,8.087495e-06);
   gre->SetPoint(17,425,8.131971e-07);
   gre->SetPointError(17,175,8.607813e-07);
   
   TH1F *Graph2 = new TH1F("Graph2","Graph",100,0.375,659.9583);
   Graph2->SetMinimum(-0.006346291);
   Graph2->SetMaximum(0.06980863);
   Graph2->SetDirectory(0);
   Graph2->SetStats(0);
   Graph2->SetFillColor(63);
   Graph2->SetFillStyle(0);
   Graph2->SetLineStyle(0);
   Graph2->SetLineWidth(2);
   Graph2->SetMarkerStyle(20);
   Graph2->GetXaxis()->SetLabelFont(42);
   Graph2->GetXaxis()->SetLabelOffset(0.007);
   Graph2->GetXaxis()->SetLabelSize(0.05);
   Graph2->GetXaxis()->SetTitleSize(0.06);
   Graph2->GetXaxis()->SetTitleOffset(0.9);
   Graph2->GetXaxis()->SetTitleFont(42);
   Graph2->GetYaxis()->SetLabelFont(42);
   Graph2->GetYaxis()->SetLabelOffset(0.007);
   Graph2->GetYaxis()->SetLabelSize(0.05);
   Graph2->GetYaxis()->SetTitleSize(0.06);
   Graph2->GetYaxis()->SetTitleOffset(1.05);
   Graph2->GetYaxis()->SetTitleFont(42);
   Graph2->GetZaxis()->SetLabelFont(42);
   Graph2->GetZaxis()->SetLabelOffset(0.007);
   Graph2->GetZaxis()->SetLabelSize(0.05);
   Graph2->GetZaxis()->SetTitleSize(0.06);
   Graph2->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph2);
   
   gre->Draw("p");
   Double_t xAxis2[20] = {0.7, 2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20, 30, 40, 50, 70, 90, 110, 150, 190, 250, 600, 3500}; 
   
   TH1F *tvis = new TH1F("tvis","tvis",19, xAxis2);
   tvis->SetBinContent(1,0.03473407);
   tvis->SetBinContent(2,0.05803429);
   tvis->SetBinContent(3,0.05035022);
   tvis->SetBinContent(4,0.04179582);
   tvis->SetBinContent(5,0.03391722);
   tvis->SetBinContent(6,0.02715676);
   tvis->SetBinContent(7,0.02192764);
   tvis->SetBinContent(8,0.01783559);
   tvis->SetBinContent(9,0.01160055);
   tvis->SetBinContent(10,0.006239438);
   tvis->SetBinContent(11,0.003679084);
   tvis->SetBinContent(12,0.001879671);
   tvis->SetBinContent(13,0.000793453);
   tvis->SetBinContent(14,0.0003616535);
   tvis->SetBinContent(15,0.0001442802);
   tvis->SetBinContent(16,4.856131e-05);
   tvis->SetBinContent(17,1.568039e-05);
   tvis->SetBinContent(18,1.231318e-06);
   tvis->SetBinContent(19,1.238777e-09);
   tvis->SetEntries(19);
   tvis->SetFillColor(63);
   tvis->SetFillStyle(0);
   tvis->SetLineStyle(0);
   tvis->SetLineWidth(2);
   tvis->SetMarkerStyle(20);
   tvis->GetXaxis()->SetLabelFont(42);
   tvis->GetXaxis()->SetLabelOffset(0.007);
   tvis->GetXaxis()->SetLabelSize(0.05);
   tvis->GetXaxis()->SetTitleSize(0.06);
   tvis->GetXaxis()->SetTitleOffset(0.9);
   tvis->GetXaxis()->SetTitleFont(42);
   tvis->GetYaxis()->SetLabelFont(42);
   tvis->GetYaxis()->SetLabelOffset(0.007);
   tvis->GetYaxis()->SetLabelSize(0.05);
   tvis->GetYaxis()->SetTitleSize(0.06);
   tvis->GetYaxis()->SetTitleOffset(1.05);
   tvis->GetYaxis()->SetTitleFont(42);
   tvis->GetZaxis()->SetLabelFont(42);
   tvis->GetZaxis()->SetLabelOffset(0.007);
   tvis->GetZaxis()->SetLabelSize(0.05);
   tvis->GetZaxis()->SetTitleSize(0.06);
   tvis->GetZaxis()->SetTitleFont(42);
   tvis->Draw("SAMEHIST ][");
   
   TLegend *leg = new TLegend(0.55,0.45,0.94,0.7,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextFont(62);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(19);
   leg->SetFillStyle(0);
   TLegendEntry *entry=leg->AddEntry("Graph","Corrected Data","P");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("Graph","Raw Data","P");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(25);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("Graph","Background-Subtracted Data","P");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(24);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("tvis","POWHEG+CT10 Prediction","l");
   entry->SetLineColor(1);
   entry->SetLineWidth(2);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   leg->Draw();
   TText *text = new TText(0.22,0.97,"CMS preliminary");
   text->SetNDC();
   text->SetTextAlign(22);
   text->SetTextFont(42);
   text->SetTextSize(0.04);
   text->Draw();
   text = new TText(0.82,0.17,"Wed Jun 22 14:40:20 2011");
   text->SetNDC();
   text->SetTextAlign(22);
   text->SetTextFont(42);
   text->SetTextSize(0.02);
   text->Draw();
   TLatex *   tex = new TLatex(0.85,0.97,"36 pb^{-1} at #sqrt{s}=7 TeV");
tex->SetNDC();
   tex->SetTextAlign(22);
   tex->SetTextFont(42);
   tex->SetTextSize(0.035);
   tex->SetLineWidth(2);
   tex->Draw();
   finalK1_ZQT->Modified();
   finalK1_ZQT->cd();
   finalK1_ZQT->SetSelected(finalK1_ZQT);
}
