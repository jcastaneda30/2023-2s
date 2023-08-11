#include<iostream>
#include<cmath>
using namespace std;
int main(){
    int A;
    long long B, Aux=0,Aux2=1;
    cin>>A>>B;
    while(Aux<=B){
        Aux=pow(A,Aux2);
        if (Aux<=B) cout<<Aux<<"\n";
        Aux2++;
    }
    return 0;
}