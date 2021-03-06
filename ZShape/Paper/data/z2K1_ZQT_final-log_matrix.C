{
//=========Macro generated from canvas: finalz2K1_ZQTLog/finalz2K1_ZQTLog
//=========  (Wed Jun 22 14:38:09 2011) by ROOT version5.28/00d
   TCanvas *finalz2K1_ZQTLog = new TCanvas("finalz2K1_ZQTLog", "finalz2K1_ZQTLog",0,0,800,600);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   gStyle->SetOptTitle(0);
   finalz2K1_ZQTLog->SetHighLightColor(2);
   finalz2K1_ZQTLog->Range(-0.6198982,-6.981287,2.956996,-0.8482436);
   finalz2K1_ZQTLog->SetFillColor(0);
   finalz2K1_ZQTLog->SetBorderMode(0);
   finalz2K1_ZQTLog->SetBorderSize(2);
   finalz2K1_ZQTLog->SetLogx();
   finalz2K1_ZQTLog->SetLogy();
   finalz2K1_ZQTLog->SetTickx(1);
   finalz2K1_ZQTLog->SetTicky(1);
   finalz2K1_ZQTLog->SetLeftMargin(0.13);
   finalz2K1_ZQTLog->SetRightMargin(0.05);
   finalz2K1_ZQTLog->SetTopMargin(0.05);
   finalz2K1_ZQTLog->SetBottomMargin(0.16);
   finalz2K1_ZQTLog->SetFrameFillStyle(0);
   finalz2K1_ZQTLog->SetFrameLineWidth(2);
   finalz2K1_ZQTLog->SetFrameBorderMode(0);
   finalz2K1_ZQTLog->SetFrameFillStyle(0);
   finalz2K1_ZQTLog->SetFrameLineWidth(2);
   finalz2K1_ZQTLog->SetFrameBorderMode(0);
   Double_t xAxis3[19] = {0.7, 2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20, 30, 40, 50, 70, 90, 110, 150, 190, 250, 600}; 
   Double_t yAxis2[21] = {1e-06, 0.003501, 0.007001, 0.010501, 0.014001, 0.017501, 0.021001, 0.024501, 0.028001, 0.031501, 0.035001, 0.038501, 0.042001, 0.045501, 0.049001, 0.052501, 0.056001, 0.059501, 0.063001, 0.066501, 0.070001}; 
   
   TH2F *logdummy__2 = new TH2F("logdummy__2","",18, xAxis3,20, yAxis2);
   logdummy__2->SetDirectory(0);
   logdummy__2->SetFillColor(63);
   logdummy__2->SetFillStyle(0);
   logdummy__2->SetLineStyle(0);
   logdummy__2->SetLineWidth(2);
   logdummy__2->SetMarkerStyle(20);
   logdummy__2->GetXaxis()->SetTitle("p_{T,ee} [GeV/c]");
   logdummy__2->GetXaxis()->CenterTitle(true);
   logdummy__2->GetXaxis()->SetLabelFont(42);
   logdummy__2->GetXaxis()->SetLabelOffset(0.007);
   logdummy__2->GetXaxis()->SetLabelSize(0.05);
   logdummy__2->GetXaxis()->SetTitleSize(0.06);
   logdummy__2->GetXaxis()->SetTitleOffset(1.2);
   logdummy__2->GetXaxis()->SetTitleFont(42);
   logdummy__2->GetYaxis()->SetTitle("1/#sigma d#sigma/dp_{T} [GeV^{-1}]");
   logdummy__2->GetYaxis()->SetLabelFont(42);
   logdummy__2->GetYaxis()->SetLabelOffset(0.007);
   logdummy__2->GetYaxis()->SetLabelSize(0.05);
   logdummy__2->GetYaxis()->SetTitleSize(0.06);
   logdummy__2->GetYaxis()->SetTitleOffset(1.05);
   logdummy__2->GetYaxis()->SetTitleFont(42);
   logdummy__2->GetZaxis()->SetLabelFont(42);
   logdummy__2->GetZaxis()->SetLabelOffset(0.007);
   logdummy__2->GetZaxis()->SetLabelSize(0.05);
   logdummy__2->GetZaxis()->SetTitleSize(0.06);
   logdummy__2->GetZaxis()->SetTitleFont(42);
   logdummy__2->Draw("");
   
   TGraph *graph = new TGraph(19);
   graph->SetName("raw log");
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
   
   TH1F *Graph_Graph_Graph13 = new TH1F("Graph_Graph_Graph13","Graph",100,1.125,2254.875);
   Graph_Graph_Graph13->SetMinimum(0);
   Graph_Graph_Graph13->SetMaximum(0.04348801);
   Graph_Graph_Graph13->SetDirectory(0);
   Graph_Graph_Graph13->SetStats(0);
   Graph_Graph_Graph13->SetFillColor(63);
   Graph_Graph_Graph13->SetFillStyle(0);
   Graph_Graph_Graph13->SetLineStyle(0);
   Graph_Graph_Graph13->SetLineWidth(2);
   Graph_Graph_Graph13->SetMarkerStyle(20);
   Graph_Graph_Graph13->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph13->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph13->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph13->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph13->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph_Graph13->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph13->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph13->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph13->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph13->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph13->GetYaxis()->SetTitleOffset(1.05);
   Graph_Graph_Graph13->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph13->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph13->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph13->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph13->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph13->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph13);
   
   graph->Draw("p");
   
   graph = new TGraph(19);
   graph->SetName("rawsub log");
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
   
   TH1F *Graph_Graph_Graph24 = new TH1F("Graph_Graph_Graph24","Graph",100,1.125,2254.875);
   Graph_Graph_Graph24->SetMinimum(0);
   Graph_Graph_Graph24->SetMaximum(0.0440781);
   Graph_Graph_Graph24->SetDirectory(0);
   Graph_Graph_Graph24->SetStats(0);
   Graph_Graph_Graph24->SetFillColor(63);
   Graph_Graph_Graph24->SetFillStyle(0);
   Graph_Graph_Graph24->SetLineStyle(0);
   Graph_Graph_Graph24->SetLineWidth(2);
   Graph_Graph_Graph24->SetMarkerStyle(20);
   Graph_Graph_Graph24->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph24->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph24->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph24->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph24->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph_Graph24->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph24->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph24->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph24->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph24->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph24->GetYaxis()->SetTitleOffset(1.05);
   Graph_Graph_Graph24->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph24->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph24->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph24->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph24->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph24->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph24);
   
   graph->Draw("p");
   
   TGraphErrors *gre = new TGraphErrors(19);
   gre->SetName("final log");
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
   
   TH1F *Graph13 = new TH1F("Graph13","Graph",100,0.375,3849.958);
   Graph13->SetMinimum(-0.006313855);
   Graph13->SetMaximum(0.06945241);
   Graph13->SetDirectory(0);
   Graph13->SetStats(0);
   Graph13->SetFillColor(63);
   Graph13->SetFillStyle(0);
   Graph13->SetLineStyle(0);
   Graph13->SetLineWidth(2);
   Graph13->SetMarkerStyle(20);
   Graph13->GetXaxis()->SetLabelFont(42);
   Graph13->GetXaxis()->SetLabelOffset(0.007);
   Graph13->GetXaxis()->SetLabelSize(0.05);
   Graph13->GetXaxis()->SetTitleSize(0.06);
   Graph13->GetXaxis()->SetTitleOffset(0.9);
   Graph13->GetXaxis()->SetTitleFont(42);
   Graph13->GetYaxis()->SetLabelFont(42);
   Graph13->GetYaxis()->SetLabelOffset(0.007);
   Graph13->GetYaxis()->SetLabelSize(0.05);
   Graph13->GetYaxis()->SetTitleSize(0.06);
   Graph13->GetYaxis()->SetTitleOffset(1.05);
   Graph13->GetYaxis()->SetTitleFont(42);
   Graph13->GetZaxis()->SetLabelFont(42);
   Graph13->GetZaxis()->SetLabelOffset(0.007);
   Graph13->GetZaxis()->SetLabelSize(0.05);
   Graph13->GetZaxis()->SetTitleSize(0.06);
   Graph13->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph13);
   
   gre->Draw("p");
   
   gre = new TGraphErrors(18);
   gre->SetName("finalsys log");
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
   
   TH1F *Graph24 = new TH1F("Graph24","Graph",100,0.375,659.9583);
   Graph24->SetMinimum(-0.006346291);
   Graph24->SetMaximum(0.06980863);
   Graph24->SetDirectory(0);
   Graph24->SetStats(0);
   Graph24->SetFillColor(63);
   Graph24->SetFillStyle(0);
   Graph24->SetLineStyle(0);
   Graph24->SetLineWidth(2);
   Graph24->SetMarkerStyle(20);
   Graph24->GetXaxis()->SetLabelFont(42);
   Graph24->GetXaxis()->SetLabelOffset(0.007);
   Graph24->GetXaxis()->SetLabelSize(0.05);
   Graph24->GetXaxis()->SetTitleSize(0.06);
   Graph24->GetXaxis()->SetTitleOffset(0.9);
   Graph24->GetXaxis()->SetTitleFont(42);
   Graph24->GetYaxis()->SetLabelFont(42);
   Graph24->GetYaxis()->SetLabelOffset(0.007);
   Graph24->GetYaxis()->SetLabelSize(0.05);
   Graph24->GetYaxis()->SetTitleSize(0.06);
   Graph24->GetYaxis()->SetTitleOffset(1.05);
   Graph24->GetYaxis()->SetTitleFont(42);
   Graph24->GetZaxis()->SetLabelFont(42);
   Graph24->GetZaxis()->SetLabelOffset(0.007);
   Graph24->GetZaxis()->SetLabelSize(0.05);
   Graph24->GetZaxis()->SetTitleSize(0.06);
   Graph24->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph24);
   
   gre->Draw("p");
   Double_t xAxis4[20] = {0.7, 2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20, 30, 40, 50, 70, 90, 110, 150, 190, 250, 600, 3500}; 
   
   TH1F *truth log = new TH1F("truth log","tvis",19, xAxis4);
   truth log->SetBinContent(1,0.0245661);
   truth log->SetBinContent(2,0.05519114);
   truth log->SetBinContent(3,0.05647393);
   truth log->SetBinContent(4,0.04593645);
   truth log->SetBinContent(5,0.03557687);
   truth log->SetBinContent(6,0.02778909);
   truth log->SetBinContent(7,0.02213628);
   truth log->SetBinContent(8,0.0180193);
   truth log->SetBinContent(9,0.01165765);
   truth log->SetBinContent(10,0.00624561);
   truth log->SetBinContent(11,0.0036788);
   truth log->SetBinContent(12,0.001879864);
   truth log->SetBinContent(13,0.0007935914);
   truth log->SetBinContent(14,0.0003624776);
   truth log->SetBinContent(15,0.0001432999);
   truth log->SetBinContent(16,4.793382e-05);
   truth log->SetBinContent(17,1.55668e-05);
   truth log->SetBinContent(18,1.239851e-06);
   truth log->SetBinContent(19,1.153091e-09);
   truth log->SetEntries(19);
   truth log->SetFillColor(63);
   truth log->SetFillStyle(0);
   truth log->SetLineStyle(0);
   truth log->SetLineWidth(2);
   truth log->SetMarkerStyle(20);
   truth log->GetXaxis()->SetLabelFont(42);
   truth log->GetXaxis()->SetLabelOffset(0.007);
   truth log->GetXaxis()->SetLabelSize(0.05);
   truth log->GetXaxis()->SetTitleSize(0.06);
   truth log->GetXaxis()->SetTitleOffset(0.9);
   truth log->GetXaxis()->SetTitleFont(42);
   truth log->GetYaxis()->SetLabelFont(42);
   truth log->GetYaxis()->SetLabelOffset(0.007);
   truth log->GetYaxis()->SetLabelSize(0.05);
   truth log->GetYaxis()->SetTitleSize(0.06);
   truth log->GetYaxis()->SetTitleOffset(1.05);
   truth log->GetYaxis()->SetTitleFont(42);
   truth log->GetZaxis()->SetLabelFont(42);
   truth log->GetZaxis()->SetLabelOffset(0.007);
   truth log->GetZaxis()->SetLabelSize(0.05);
   truth log->GetZaxis()->SetTitleSize(0.06);
   truth log->GetZaxis()->SetTitleFont(42);
   truth log->Draw("SAMEHIST ][");
   
   TLegend *leg = new TLegend(0.2,0.2,0.62,0.38,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextFont(62);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(19);
   leg->SetFillStyle(0);
   TLegendEntry *entry=leg->AddEntry("final log","Corrected Data","P");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("rawsub log","Raw Data","P");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(25);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("raw log","Background-Subtracted Data","P");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(24);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("truth log","POWHEG+CT10 Prediction","l");
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
   text = new TText(0.82,0.17,"Wed Jun 22 14:38:09 2011");
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
   finalz2K1_ZQTLog->Modified();
   finalz2K1_ZQTLog->cd();
   finalz2K1_ZQTLog->SetSelected(finalz2K1_ZQTLog);
}
