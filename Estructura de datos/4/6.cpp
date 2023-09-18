#include<iostream>
#include<unordered_map>
#include<stack>

using namespace std;

int main() {
    int C, N;
    cin >> C;

    for (int i = 0; i < C; i++) {
        cin >> N;        
        unordered_map<char, stack<int>> hanoi;
        hanoi['A'] = stack<int>();
        hanoi['B'] = stack<int>();
        hanoi['C'] = stack<int>();
        for (int j = N; j > 0; j--) 
            hanoi['A'].push(j);

        bool invalido = false;
        bool completar = false;

        while (true) {
            char P, Q;
            cin >> P >> Q;
            if (P == 'X' && Q == 'X') break;
            if (P == Q) continue;
            if (hanoi[P].empty()) {
                invalido = true;
                continue;
            }
            if (!hanoi[Q].empty() && (hanoi[P].top() > hanoi[Q].top())) invalido = true;

            int elemento = hanoi[P].top();
            hanoi[Q].push(elemento);
            hanoi[P].pop();
        }

        if((hanoi['A'].size()==0 && hanoi['B'].size()==0 && hanoi['C'].size()!=0) || 
        (hanoi['A'].size()==0 && hanoi['B'].size()!=0 && hanoi['C'].size()==0) || 
        (hanoi['A'].size()!=0 && hanoi['B'].size()==0 && hanoi['C'].size()==0)) completar = true;

        if (invalido) {
            cout << "secuencia invalida\n";
        } else if (completar) {
            cout << "soluciona la torre\n";
        } else {
            cout << "no soluciona la torre\n";
        }
    }

    return 0;
}
