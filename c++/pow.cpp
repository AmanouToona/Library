#include <bits/stdc++.h>
using namespace std;

template <typename T>
T pow(T x, T n) {
    T ret = 1;
    while (n > 0) {
        if (n & 1) ret *= x;  // n の最下位bitが 1 ならば x^(2^i) をかける
        x *= x;
        n >>= 1;  // n を1bit 左にずらす
    }
    return ret;
};

int main() {
    long long x, n;
    cin >> x >> n;
    cout << pow<long long>(x, n) << endl;
    return 0;
}