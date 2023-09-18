#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> numeros;
    while (true)
    {
        int numero;
        cin >> numero;
        if (numero == 0)
            break;

        auto it = find(numeros.begin(), numeros.end(), numero);
        auto it2 = find(numeros.begin(), numeros.end(), numero + 1);
        auto it3 = find(numeros.begin(), numeros.end(), numero - 1);

        bool eliminate = false;

        if (it != numeros.end())
        {
            numeros.erase(it);
            eliminate = true;
        }
        else if (it2 != numeros.end())
        {
            numeros.erase(it2);
            eliminate = true;
        }
        else if (it3 != numeros.end())
        {
            numeros.erase(it3);
            eliminate = true;
        }

        if (!eliminate)
        {
            numeros.push_back(numero);
        }
    }

    if (numeros.size() > 0)
    {
        for (int j = 0; j < numeros.size(); j++)
        {
            cout << numeros[j] << " ";
        }
        cout << "\n";
    }
    else
    {
        cout << "0\n";
    }

    return 0;
}
