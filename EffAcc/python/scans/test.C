
#include <math.h>
#include <algorithm>
#include <list>
#include <iostream>
#include <stdio.h>
#include <string.h>

void test(double *vals, int s){
  for(int i=0;i<s;i++){
    double val=vals[i];
    char c[128],d[128];
    sprintf(c,"%0.3f",val);
    printf("HEY its %s\n",c);
    sprintf(d,"meanX%cX%s",c[0],c+2);
    
    printf("HEY its %s\n",d);
  }
}
