#include<iostream>
#include<cmath>
using namespace std;
int main(){
    int numero,aux;
    cin>>numero;
    aux=numero;
    while(aux!=1 && aux>1){
        if(aux%2==0) {
            cout<<aux<<"\n";
            aux=aux/2;
        }
        else{
            cout<<aux<<"\n";
            aux=3*aux+1;
        }
    }
    cout<<aux;
}