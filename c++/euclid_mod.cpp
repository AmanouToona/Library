int MOD = 998244353;

long long extGCD(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    extGCD(b, a % b, y, x);
    y -= a / b * x;
    return;
}

inline long long mod(long long a, long long m) { return (a % m + m) % m; }

long long modinv(long long a, long long m) {
    long long x, y;
    extGCD(a, m, x, y);
    return mod(x, m);
}
