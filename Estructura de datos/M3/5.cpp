#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

int main(){
    int c;
    cin>>c;
    cin.ignore();  // Ignorar el salto de línea después de leer 'casos'

    vector<int> numeros;

    for (int i = 0; i < c; i++) {
        string linea;
        getline(cin, linea);
        string num;
        for(int j=0;j<linea.size();j++){
            if(linea[j]!=' '){
                num+=linea[j];
            }else if(linea[j]!='\n'){
                numeros.push_back(stoi(num));
                string num="";
            }
        }        
        for (int i = 0; i < numeros.size(); ++i) {
            cout << numeros[i] << " ";
        }
        cout << endl;
    }

    return 0;
}