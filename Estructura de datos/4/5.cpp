#include<iostream>
#include<queue>
#include <utility>

using namespace std;

int main(){
  int T; cin>>T;
  for(int i=0;i<T;i++){
    int k,N; cin>>N>>k;
    queue<pair<int,bool>> fila;
    int tiempo = 0; 
    for(int j=0;j<N;j++){
      int value;
      cin>>value;
      pair<int,bool> wea=make_pair(value,false);
      
      if(j==k-1){
        fila.push(make_pair(value,true));}
      else fila.push(wea);
    }
    while(true){
      pair<int,bool> elemento = fila.front();
      fila.pop();
      if(elemento.first>0 && !elemento.second){
        fila.push(make_pair(elemento.first-1,elemento.second));
        tiempo+=5;
      }else if(elemento.second){
        if((elemento.first-1)<1){
            tiempo+=5;
            break;
        }else{
        fila.push(make_pair(elemento.first-1,elemento.second));
        tiempo+=5;
        }
      }
    }
    cout<<tiempo<<"\n";
  }

  return 0;
}