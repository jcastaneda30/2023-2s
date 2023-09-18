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
        int N,A,B; cin>>N>>A>>B;
        vector<bool> values(N,0);
        for(int i=0;i<N;i++) values[i]=i+1;
        while (values.size()>1)
        {
            for(int i=0;i<values.size();i++) values[i]=(values[i]*A)%B;
            sort(values.begin(),values.end());
            int ss = values.size()/2;
            values.erase(values.begin(),values.begin()+ss-1);
        }
        cout<<values.size()<<endl;
        
    }
    
    return 0;
}
