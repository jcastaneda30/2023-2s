#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int N, K;
        cin >> N >> K;
        vector<int> valores(N, 0);
        for (int i = 0; i < N; i++)
            valores[i] = i+1;
        int posicion = 0;
        while (valores.size() > 1)
        {
            posicion = (posicion+K-1)%valores.size();
            K = valores[posicion] % (valores.size()-1);
            valores.erase(valores.begin()+posicion);
            if (K == 0)
                K = 1;
        }
        cout << valores[0] << endl;
    }
    return 0;
}