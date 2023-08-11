#include<iostream>
#include<cmath>
using namespace std;
int main(){
    int multiplos[]={2,3,5,7};
    int numero;
    cin>>numero;
    for(int i=0;i<5;i++){
        if(i!=4 && numero%multiplos[i]==0) {
            cout<<"es multiplo de "<<multiplos[i];
            break;}
        if(i==4) cout<<"no es multiplo de ninguno de los primeros cuatro primos";
    }
}