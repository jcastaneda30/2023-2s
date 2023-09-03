#include <algorithm>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int binarySearch(const vector<int> &arr, int target) {
    int left = 0;
    int right = arr.size() - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1; // Element not found
}

int main() {
  int C,a,b;
  cin >> C;
  vector<int> l;
  for (int j = 0; j < C; j++) {
    cin >> a;
    l.push_back(a);
  }

  sort(l.begin(),l.end());
    for (int j = 0; j < C; j++) {
    cout<<l[j]<<"  " ;
  }
  int cantidad;
  cin >> cantidad;
  for (int t = 0; t < cantidad; t++) {
      int a, b;
      
      cin >> a >> b;
      
      a = binarySearch(l, a);
      b = binarySearch(l, b);
      cout << "\n";
      cout << a;
  }


  return 0;
}
