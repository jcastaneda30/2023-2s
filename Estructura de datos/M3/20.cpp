#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <string>

using namespace std;

int main() {
    int entrada;
    cin >> entrada;

    for (int i = 0; i < entrada; ++i) {
        vector<int> valores;
        string linea;
        getline(cin, linea);
        
        stringstream ss(linea);
        int num;

        while (ss >> num) {
            cout<<"----------"<<num;
            valores.push_back(num);
        }

        sort(valores.begin(), valores.end());
        int count = 1;

        for (int j = 0; j < valores.size() - 1; ++j) {
            if (valores[j] == valores[j + 1]) {
                count++;
            } else {
                cout << count << " ";
                count = 1;
            }
        }

        cout << count << "\n";
    }

    return 0;
}
