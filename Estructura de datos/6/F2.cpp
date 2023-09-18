#include <iostream>
#include <vector>
#include <queue>
using namespace std;
 
int main() {
    int C; cin>>C;
    while (C--)
    {
        int N,A,B; cin>>N>>A>>B;
        priority_queue<int, vector<int>, greater<int>> min_heap;
        for(int i=0;i<N;i++) min_heap.push(i+1);

        while(min_heap.size()>1){
            priority_queue<int, vector<int>, greater<int>> min_heap_copy=min_heap;
            priority_queue<int, vector<int>, greater<int>> aux;
            while(!min_heap_copy.empty()){
                int value = (min_heap_copy.top()*A)%B;
                min_heap_copy.pop();
                aux.push(value);
            }
            int tamano;
            if(aux.size()%2==0){
                tamano=aux.size()/2;
            }else{
                tamano=(aux.size()-1)/2;
            }
            for(int i=0;i<tamano;i++){
                aux.pop();
            }
            min_heap=aux;
        }
        cout<<min_heap.top()<<endl;
        
    }
 
    return 0;
}