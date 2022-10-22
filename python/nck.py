MOD = 10**9 + 7

MAX = 510000
fac = [-1] * MAX  # n! の計算
finv = [-1] * MAX  # n! ^ -1 の計算
inv = [-1] * MAX  # mod における i の逆元


def COMinit():
    fac[0] = 1
    fac[1] = 1
    inv[1] = 1

    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

    return


def com(n: int, k: int):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


if __name__ == "__main__":
    COMinit()

    print(com(4, 2))
