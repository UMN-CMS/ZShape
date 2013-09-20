#ifndef BACKGROUNDFUNCTIONS_H
#define BACKGROUNDFUNCTIONS_H

#include <TF1.h>  
#include <TMath.h>  // Erfc, Exp
#include <TH1.h>  // TH1D

#include "BackgroundTable.h"  // Background Table

/* 
 * The background function is of the form:
 *
 * beta * erfc((alpha - x) / delta) * exp(-gamma * x)
 *
 * alpha: Controls the location of the peak (although is not the peak
 * location), smaller numbers are at lower x. It also changes the overall
 * amplitude somewhat.
 *
 * beta: Controls the total amplitude, with 0 being no amplitude.
 *
 * gamma: Controls the shape of the exponential tail, with near 0 being a flat
 * tail (like a step function) and near 1 making the fall off so fast that we
 * get something delta function like. It also controls the peak location.
 *
 * delta: Controls the width of the peak and the sharpness of the rise, with a
 * low value being very sharp, and a high value being very broad. This also has
 * the side effect of moving the peak, even if all other values are fixed.
 */

namespace bg{
    double analyticBackground(const double *x, const double *par);

    class BinnedBackground{
        public:
            // Constructor
            BinnedBackground(const double alpha, const double gamma, const double delta, TH1D* bgHisto);
            BinnedBackground(const BackgroundTable bgtab, TH1D* bgHisto);
            BinnedBackground() {}  // Needed because BinnedBackgroundAndSignal calls it

            // Histogram
            TH1D* getNormalizedBackgroundHisto();
            TH1D* getBackgroundHisto();
            TH1D* getScaledBackgroundHisto(const double beta);

            // Access to the function
            double operator() (const double *x, const double *par);

        protected:
            // Generated internal quantities
            TH1D* backgroundHisto_;
            TF1* internalFunc_;

            // Functions used to set up the class during construction
            void fillBackgroundHisto_(const double beta, const bool normalize = false);

            // Internal variables used to initialize for baseFunc_
            static const int nparams_ = 1;
            static const double minMZ_ = 0.;
            static const double maxMZ_ = 200.;

            /*
             * The function we use to make the TF1
             *
             * We use a class because, for some reason I have not figured out,
             * using bg::BinnedBackground::baseFunc_ doesn't work if it is just
             * a function.
             */
            class baseFuncClass_{
                public:
                    baseFuncClass_(const double alpha, const double gamma, const double delta);
                    double operator() (const double *x, const double *par);

                private:
                    double baseFunc_(const double *x, const double *par);
                    double alpha_;
                    double gamma_;
                    double delta_;
            };
    };

    class BinnedBackgroundAndSignal: public BinnedBackground{
        public:
            BinnedBackgroundAndSignal(const double alpha, const double gamma, const double delta,  TH1D* signalHisto);
            BinnedBackgroundAndSignal(const BackgroundTable bgtab, TH1D* signalHisto);

            // Histogram
            double operator() (const double *x, const double *par);

            // Return the signal histogram
            TH1D* getNormalizedSignalHisto();
            TH1D* getSignalHisto();
            TH1D* getScaledSignalHisto(const double beta);

        protected:
            TH1D* signalHisto_;
            // Internal variables used to initialize for baseFunc_
            static const int nparams_ = 2;
    };
}
#endif
