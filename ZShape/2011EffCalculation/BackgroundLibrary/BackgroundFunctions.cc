#include "BackgroundFunctions.h"

double bg::analyticBackground(const double *x, const double *par){
    /* 
     * par[0] = alpha
     * par[1] = beta
     * par[2] = gamma
     * par[3] = delta
     */
    const double erfout = TMath::Erfc((par[0] - x[0]) / par[3]);
    const double expout = TMath::Exp(-par[2] * x[0]);
    return par[1] * erfout * expout;
}

/* BinnedBackground Class */
bg::BinnedBackground::BinnedBackground(const double alpha, const double gamma, const double delta, TH1D* bgHisto){
    // Set up function
    bg::BinnedBackground::baseFuncClass_ fitFunc(alpha, gamma, delta);
    // Set up the internal histogram
    backgroundHisto_ = bgHisto;
    // Set up the internal function
    internalFunc_ = new TF1("basefunc", fitFunc, minMZ_, maxMZ_, nparams_);
    // Set up the background histogram
    fillBackgroundHisto_(1., true);
}

bg::BinnedBackground::BinnedBackground(const BackgroundTable bgtab, TH1D* bgHisto){
    // Set up function
    bg::BinnedBackground::baseFuncClass_ fitFunc(bgtab.current->alpha, bgtab.current->gamma, bgtab.current->delta);
    // Set up the internal histogram
    backgroundHisto_ = bgHisto;
    // Set up the internal function
    internalFunc_ = new TF1("basefunc", fitFunc, minMZ_, maxMZ_, nparams_);
    // Set up the background histogram
    fillBackgroundHisto_(1., true);
}

void bg::BinnedBackground::fillBackgroundHisto_(const double beta, const bool normalize){ // normalize defaults to false
    /*
     * Loop over each bin of the internal histogram, and integrate from the low
     * edge to the high edge
     *
     * Note that using "Normalize" will override beta. It defaults to false.
     */
    for (int i = 1; i <= backgroundHisto_->GetNbinsX(); ++i){
        // Find bin edges
        const double xlow = backgroundHisto_->GetBinLowEdge(i);
        const double xhigh = xlow + backgroundHisto_->GetBinWidth(i);
        // Intergrate over the bin
        const double binval = internalFunc_->Integral(xlow, xhigh, &beta);  // 
        // Set bin
        backgroundHisto_->SetBinContent(i, binval);
    }
    // Normalize the area to 1
    if (normalize){
        const double area = backgroundHisto_->Integral();
        backgroundHisto_->Scale(1. / area);
    }
}

TH1D* bg::BinnedBackground::getNormalizedBackgroundHisto(){
    fillBackgroundHisto_(1., true); 
    return backgroundHisto_;
}

TH1D* bg::BinnedBackground::getBackgroundHisto(){
    return backgroundHisto_;
}

TH1D* bg::BinnedBackground::getScaledBackgroundHisto(const double beta){
    fillBackgroundHisto_(beta, false); 
    return backgroundHisto_;
}

double bg::BinnedBackground::operator() (const double *x, const double *par){
    const double histoval = backgroundHisto_->GetBinContent(backgroundHisto_->FindBin(x[0]));
    return par[0] * histoval;
}

/* baseFuncClass_ subclass */
bg::BinnedBackground::baseFuncClass_::baseFuncClass_(const double alpha, const double gamma, const double delta){
    alpha_ = alpha;
    gamma_ = gamma;
    delta_ = delta;
}

double bg::BinnedBackground::baseFuncClass_::baseFunc_(const double *x, const double *par){
    /*  */
    const double erfout = TMath::Erfc((alpha_ - x[0]) / delta_);
    const double expout = TMath::Exp(-gamma_ * x[0]);
    return par[0] * erfout * expout;
}

double bg::BinnedBackground::baseFuncClass_::operator() (const double *x, const double *par){
    return baseFunc_(x, par);
}

/* BinnedBackgroundAndSignal Class */
bg::BinnedBackgroundAndSignal::BinnedBackgroundAndSignal(const double alpha, const double gamma, const double delta, TH1D* signalHisto){
    // Set up function
    bg::BinnedBackgroundAndSignal::baseFuncClass_ fitFunc(alpha, gamma, delta);
    // Set up the internal histograms
    signalHisto_ = signalHisto;
    backgroundHisto_ = (TH1D*)signalHisto->Clone("bghisto");
    // Set up the internal function
    internalFunc_ = new TF1("basefunc", fitFunc, minMZ_, maxMZ_, nparams_);
    // Set up the background histogram
    fillBackgroundHisto_(1., true);
    // Normalize signal histogram
    const double area = signalHisto_->Integral();
    signalHisto_->Scale(1. / area);
}
bg::BinnedBackgroundAndSignal::BinnedBackgroundAndSignal(const BackgroundTable bgtab, TH1D* signalHisto){
    // Set up function
    bg::BinnedBackgroundAndSignal::baseFuncClass_ fitFunc(bgtab.current->alpha, bgtab.current->gamma, bgtab.current->delta);
    // Set up the internal histograms
    signalHisto_ = signalHisto;
    backgroundHisto_ = (TH1D*)signalHisto->Clone("bghisto");
    // Set up the internal function
    internalFunc_ = new TF1("basefunc", fitFunc, minMZ_, maxMZ_, nparams_);
    // Set up the background histogram
    fillBackgroundHisto_(1., true);
    // Normalize signal histogram
    const double area = signalHisto_->Integral();
    signalHisto_->Scale(1. / area);
}

double bg::BinnedBackgroundAndSignal::operator() (const double *x, const double *par){
    const double bgval = par[0] * backgroundHisto_->GetBinContent(backgroundHisto_->FindBin(x[0]));
    const double sigval = par[1] * signalHisto_->GetBinContent(signalHisto_->FindBin(x[0]));
    return bgval + sigval;
}

TH1D* bg::BinnedBackgroundAndSignal::getNormalizedSignalHisto(){
    const double area = signalHisto_->Integral();
    signalHisto_->Scale(1. / area);
    return signalHisto_;
}

TH1D* bg::BinnedBackgroundAndSignal::getSignalHisto(){
    return signalHisto_;
}

TH1D* bg::BinnedBackgroundAndSignal::getScaledSignalHisto(const double beta){
    signalHisto_->Scale(beta);
    return backgroundHisto_;
}
