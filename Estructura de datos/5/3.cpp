#include<iostream>
#include<string>
#include<vector>

using namespace std;

int main() {
    string numeros = "0123456789";
    vector<int> numero;
    while (true) {
        string elemento;
        cin >> elemento;
        bool esNumber = false;
        for (int i = 0; i < numeros.size(); i++) {
            if (numeros[i] == elemento[0]) {
                esNumber = true;
                break;
            }
        }
        if(esNumber){
            int value=stoi(elemento);
            numero.push_back(value);
        }
        else if(elemento=="C"){
            if(numero.size()>0) numero.pop_back();
        }else if(elemento=="M"){
            int i,j;
            cin>>i>>j;
            if(j>numero.size()) continue;
            i--;
            j--;
            for(int k=i;k<=j;k++){
                cout<<numero[k];
            }
            cout<<"\n";
        }else if(elemento=="D"){
            int D;
            cin>>D;
            if(D>numero.size()) continue;
            for(int k=0;k<D;k++){
                numero.pop_back();
            }
        }else if(elemento=="end") break;

    }
    return 0;
}
