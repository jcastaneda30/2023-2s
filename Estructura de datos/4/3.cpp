#include<iostream>
#include<queue>
#include<deque>
#include<string>
using namespace std;
int main(){
    deque<int> a;
    bool wea=false;

    while(true){
        string comando;
        cin>>comando;
        if(comando=="agrega"){
            int numero; cin>>numero;
            a.push_back(numero);
        }else if(comando=="engulle"){
            if(a.size()==1) a.pop_back();
            else if(a.size()>0){
                if(a.front()>a.back()) a.pop_back();
                else a.pop_front();
            }else{
                wea=true;
            }
        }else{
            break;
        }
    }
    if(!wea && a.size()>0)cout<<"cabeza "<<a.front()<<" cola "<<a.back()<<"\n";
    else cout<<"uroboro vacio\n";
    return 0;
}