#ifndef ZSHAPE_2011EFFCALCULATION_BACKGROUNDLIBRARY_BACKGROUNDFUNCTIONS_H_
#define ZSHAPE_2011EFFCALCULATION_BACKGROUNDLIBRARY_BACKGROUNDFUNCTIONS_H_

#include <TF1.h>  
#include <TH1.h>  // TH1D

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
            BinnedBackground(TH1D* bgHisto);
            BinnedBackground() {};  // Needed for inheritance

            // Histogram
            TH1D* getBackgroundHisto();

            // Set exclude
            void setExclude(const bool ex){ exclude_ = ex; };
            void setExcludeRange(const double xmin, const double xmax){
                exclude_min_ = xmin; exclude_max_ = xmax;
            }

            // Access to the function
            double operator() (const double *x, const double *par);

            // Number of parameters this class needs
            static const int nparams = 4;

        protected:
            // Generated internal quantities
            TH1D* backgroundHisto_;
            TF1* internalFunc_;

            // Functions used to set up the class during construction
            void fillBackgroundHisto_(const double* par);

            // Internal variables used to initialize for baseFunc_
            static const int nparams_ = 4;
            static const double minMZ_ = 0.;
            static const double maxMZ_ = 200.;

            // Internal variables used to ignore rangex
            double exclude_min_;
            double exclude_max_;
            bool exclude_;
    };

    class BinnedBackgroundAndSignal: public BinnedBackground{
        public:
            BinnedBackgroundAndSignal(TH1D* signalHisto);
            BinnedBackgroundAndSignal() {};  // Needed for inheritance

            // Histogram
            TH1D* getSignalHisto();

            // Access to the function
            double operator() (const double *x, const double *par);

            // Number of parameters this class needs
            static const int nparams = 5;

        protected:
            TH1D* signalHisto_;
            // Internal variables used to initialize for baseFunc_
            static const int nparams_ = 2;
    };

}
#endif // define ZSHAPE_2011EFFCALCULATION_BACKGROUNDLIBRARY_BACKGROUNDFUNCTIONS_H_
