#include<iostream>
#include<vector>
#include<unordered_set>
#include<set>
#include<algorithm>

using namespace std;

void primos(set<int> &sett){
    sett.insert(1);
    for(int i=2;i<=10000;i++){
        bool es_primo = true;
        for(int j=2;j<i;j++){
            if(i%j==0){
                es_primo = false;
                break;
            }
           
        }
        if(es_primo) sett.insert(i);
    }
}

int main(){
    int C;
    cin>>C;
    set<int> primes;
    primos(primes);
    while(C--){
        vector<pair<int,int>> actuales;
        int numeroA;
        cin>>numeroA;
        for(auto numeroB:primes){
            if(numeroB>numeroA) break;
            if(primes.find(numeroA-numeroB)!=primes.end()){
                int maximo=max(numeroA-numeroB,numeroB);
                int minimo=min(numeroA-numeroB,numeroB);
                pair<int,int> par=make_pair(minimo,maximo);
                bool encontrado = false;
                for (auto& elemento : actuales) {
                    if (elemento == par) {
                        encontrado = true;
                        break; // Si se encuentra el par, puedes salir del bucle
                    }
                }
                if(!encontrado) actuales.push_back(par);
            }
        }
        cout<<actuales.size()<<endl;
    }
}
