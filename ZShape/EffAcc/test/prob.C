void prob(int n,int k,int val,int d6=6){
 
  double prob=0;
  double p=(double)(d6+1-val)*1.0/d6;
  printf("probability of %i dice being equal or above %i when rolling %id%i",k,val,n,d6);

  for (int i=0;i<(n-k+1);i++){
  int nfac,kifac,xkifac,x,y; 
    y=1;
    x=n;
    while (x>1){
      y=y*(x);  
      x--;
    }
    nfac=y;
    y=1;
    x=(k+i);
    while (x>1){
      y=y*(x);  
      x--;
    }
    kifac=y;
     y=1;
    x=n-(k+i);
    while (x>1){
      y=y*(x);  
      x--;
    }
    xkifac=y;

    
    prob+=(nfac/(kifac*xkifac))*(pow(p,k+i))*(pow(1-p,n-k-i));




  }
  printf("  is %0.3f\n",prob*100.0);
}
