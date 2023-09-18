#include <iostream>
#include <vector>
#include <queue>
using namespace std;
 
int main() {
    priority_queue<int, vector<int>, greater<int>> min_heap;
    int valor = 0;
    
    while (true) {
        string elemento;
        cin >> elemento;
        
        if (elemento == "end") {
            break;
        }
        
        if (elemento == "sig" && !min_heap.empty()) {
            valor = min_heap.top();
            min_heap.pop();
        } 
        else if (isdigit(elemento[0])) {
            int element = stoi(elemento);
            min_heap.push(element);
        }
    }
 
    if (valor != 0) {
        cout << valor << endl;
    }
 
    return 0;
}