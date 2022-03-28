#include<stdio.h>

int main(){
    int t;
    int n;
    int f0[41];
    int f1[41];
    
    f0[0] = 1, f0[1] = 0;
    f1[0] = 0, f1[1] = 1;
    
    for(int i=2; i<41; i++){
        f0[i] = f0[i-1] + f0[i-2];
    }
    for(int i=2; i<41; i++){
        f1[i] = f1[i-1] + f1[i-2];
    }
    
    scanf("%d", &t);
    for(int i=0; i<t; i++){
        scanf("%d", &n);
        printf("%d %d\n",f0[n], f1[n]);
    }
    
    return 0;
}

