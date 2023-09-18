#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

int main() {
    int C; cin>>C;
    while (C--)
    {
        int N; cin>>N;
        vector<char> valores(N,0);
        for(int i=0;i<N;i++) cin>>valores[i];
        sort(valores.begin(),valores.end());
        string cadena1="",cadena2="";
        for(int i=0;i<N;i++){
            if(i%2==0){
                cadena1+=valores[i];
            }else{
                cadena2+=valores[i];
            }
        }
        long long numero;
        if(cadena1.size()>0 && cadena2.size()>0) numero = stoll(cadena1)+stoll(cadena2);
        else if(cadena1.size()==0) numero = stoll(cadena2);
        else if(cadena2.size()==0) numero = stoll(cadena1);
        cout<<numero<<endl;
    }
    
    return 0;
}
