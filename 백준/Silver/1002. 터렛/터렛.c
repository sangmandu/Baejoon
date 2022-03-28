#include<stdio.h>
#include<math.h>

int main(){
    int t;
    int x1, y1, r1;
    int x2, y2, r2;
    int l, r_sup, r_sub;
    
    scanf("%d", &t);
    for(int i=0; i<t; i++){
        scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
        l = pow(x2-x1,2)+pow(y2-y1,2);
        r_sup = pow(r1+r2,2);
        r_sub = pow(r1-r2,2);
        
        
        if(x1==x2 && y1==y2){
            if(r1==r2){
                printf("-1\n");
            }
            else{
                printf("0\n");
            }
        }
        else{
            if(l > r_sup || l < r_sub){
                printf("0\n");
            }
            else if(l == r_sup || l == r_sub){
                printf("1\n");
            }
            else{
                printf("2\n");
            }
        }
    }    
    return 0;
}