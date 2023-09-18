#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

int main() {
    unordered_map<string,priority_queue< int, vector<int>, greater<int> >> equipos;
    int countA=0;
    int countB=0;
    int countC=0;
    while (true) {
        string elemento;
        int A=INT_MAX,B=INT_MAX,C=INT_MAX;

        cin >> elemento;
        
        if (elemento == "fin") {
            break;
        }

        if (elemento == "menores" && (!equipos["A"].empty() || !equipos["B"].empty() || !equipos["C"].empty())) {
            if(!equipos["A"].empty()) A = equipos["A"].top();
            if(!equipos["B"].empty()) B = equipos["B"].top();
            if(!equipos["C"].empty()) C = equipos["C"].top();

            int minimum = min(A,min(B,C));

            if(A==minimum) countA++;
            if(B==minimum) countB++;
            if(C==minimum) countC++;

            if(!equipos["A"].empty())equipos["A"].pop();
            if(!equipos["B"].empty())equipos["B"].pop();
            if(!equipos["C"].empty())equipos["C"].pop();
        } 
        else if(elemento=="A" || elemento=="B" || elemento=="C"){
            int value=0;
            cin>>value;
            equipos[elemento].push(value);
        }
    }

    cout <<"Equipo A: "<<countA << endl;
    cout <<"Equipo B: "<<countB << endl;
    cout <<"Equipo C: "<<countC << endl;

    return 0;
}
