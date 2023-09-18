#include<iostream>
#include<vector>
#include<algorithm>
#include<string>

using namespace std;

int main(){
    int M;
    cin>>M;
    vector<int> array;
    string media;
    while(true){
        int value; cin>>value;
        if(value==0) break;
        array.push_back(value);
        if(array.size()%M==0){
            sort(array.begin(),array.end());
            if(array.size()%2==0){
                if((array[(int)(array.size())/2-1]+array[(int)(array.size())/2])%2==0){
                    media = to_string((array[(int)(array.size())/2-1]+array[(int)(array.size())/2])/2);
                }else media = to_string(array[(int)(array.size())/2-1]+array[(int)(array.size())/2])+"/2"; 
            }else{
                media = to_string(array[(int)array.size()/2]);
            }
            cout<<media<<"\n";
        }
    }
    return 0;
}