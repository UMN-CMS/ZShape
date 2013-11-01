#ifndef Efficiency_Sheet
#define Efficiency_Sheet

#include <vector>
#include <map>
#include <string>

class EffSheet{

    public:
        EffSheet(const std::string textFile);

        struct EffLine{
            double xmin;
            double xmax;
            double etamin;
            double etamax;
            double pumin;
            double pumax;
            int numparms;
            double eff;
            double systp;
            double systm;
            double den;
            bool phistar;
        };
        struct EffMapKey{
            double etamin;
            double etamax;
            double pumin;
            double pumax;
            bool phistar;
            bool operator()(const EffSheet::EffMapKey one, const EffSheet::EffMapKey other);
        };

        EffLine* current;

        std::map<EffSheet::EffMapKey, std::vector<EffSheet::EffLine>, EffSheet::EffMapKey > values;
};

#endif
