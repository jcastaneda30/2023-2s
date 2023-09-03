#include<iostream>
#include<vector>
#include<set>

using namespace std;


int main(){
    int  N,T,R,K;
    cin>>N>>T;
    vector<pair<int,int>> vendores;
    for(int i=0; i<N;i++){
        cin>>R>>K;
        pair<int,int> waos=make_pair(R,K);
        vendores.push_back(waos);
    }
    int i=0,p=1,cantidadFinal;
    pair<int,int> ultimio;
    bool wea=false;
    while (T>0)
    {   
        if(vendores.size()<1){
            wea=true;
            break;
        }
        if(vendores.size()<=i){
            i=0;
        }
        if(p%5==0){
            if(T-vendores[i].second>0) T-=vendores[i].second;
            else {
                ultimio=vendores[i];
                break;
            }
            vendores.erase(vendores.begin()+i);
            i-=1;;
        }else{
            if(T-vendores[i].second>0) T-=vendores[i].second;
            else {
                ultimio=vendores[i];
                break;
            }
        }     
        i++;
        p++;
    }
    if(!wea)cout<<ultimio.first<<" "<<T<<"\n";
    else cout<<"quedaron boletas disponibles\n";
    return 0;
}

//max 6 boletas
//la 5 de cada cinco vuela
//Siempren deben comprar la misma cantidad de boletas
//