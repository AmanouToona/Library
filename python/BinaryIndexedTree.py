class BinaryIndexedTree:
    # 1-index
    def __init__(self, n: int) -> None:
        x = 1
        while x <= n:
            x <<= 1

        self.n = x
        self.data = [0] * (self.n + 1)
        return

    def update(self, i: int, x: int):
        while i <= self.n:
            self.data[i] += x
            i += i & -i
        return

    def query(self, a: int):
        res = 0

        while a:
            res += self.data[a]
            a -= a & -a

        return res


if __name__ == "__main__":
    # ABC276_F
    import sys

    MOD = 998244353

    _ = int(input())
    A = list(map(int, sys.stdin.readline().strip().split()))
    maA = max(A)
    seg1 = BinaryIndexedTree(maA)
    seg2 = BinaryIndexedTree(maA)

    E = 0
    for k, a in enumerate(A):

        ans = (
            (E * k * k) % MOD
            + 2 * (seg1.query(a - 1) * a + (seg2.query(maA) - seg2.query(a - 1))) % MOD
            + a
        )
        ans %= MOD

        inv = pow(k + 1, MOD - 2)
        ans = (ans * inv) % MOD
        ans = (ans * inv) % MOD
        ans = int(ans)

        seg1.update(a, 1)
        seg2.update(a, a)

        E = ans
        print(E)
