#include<iostream>
#include<vector>
#include <set>
#include <string>
using namespace std;
 
int main(){
    set<pair<string,int>> fila;
    while(true){
        string letra;
        int maximo;
        cin>>letra>>maximo;
        if(letra=="0") break;
        if(maximo<=fila.size()) continue;
        set<pair<string,int>> Eliminar;
        for (set<pair<string, int>>::reverse_iterator it = fila.rbegin(); it != fila.rend(); ++it) {
            if((*it).second<fila.size()+1) {
                Eliminar.insert(*it);
                break;
            }
        }
        for (const auto& elemento : Eliminar) {
            fila.erase(elemento);
        }
        fila.insert(make_pair(letra,maximo));
    }
    cout<<fila.size()<<"\n";
    return 0;
}
