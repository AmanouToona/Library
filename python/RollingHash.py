class RollingHash:
    def __init__(self, s: str, b: int, m: int) -> None:
        self.s = s
        self.b = b
        self.m = m

        self.h = [0] * (len(s) + 1)
        self.b_pow = [1] * (len(s) + 1)

        for i, c in enumerate(s):
            self.h[i + 1] = ord(c) * self.b + self.h[i] * self.b
            self.h[i + 1] %= self.m

            self.b_pow[i + 1] *= self.b_pow[i] * self.b
            self.b_pow[i + 1] %= self.m

        return

    def get(self, left, right) -> int:
        # [left, right)
        res = (self.h[right] - self.h[left] * self.b_pow[right - left]) % self.m

        return res


if __name__ == "__main__":
    # test: ABC141 E
    import sys

    N = int(input())
    S = sys.stdin.readline().strip()

    # rolling hash
    B = [2 ** 61 - 1, 114514, 1919, 893, 364364]  # base
    M = [10 ** 9 + 7, 10 ** 9 + 7, 10 ** 9 + 7, 10 ** 9 + 7, 10 ** 9 + 7]  # mod

    rollinghash1 = RollingHash(S, B[0], M[0])
    rollinghash2 = RollingHash(S, B[1], M[1])
    rollinghash3 = RollingHash(S, B[2], M[2])

    long = N
    short = 0
    while long - short > 1:
        mid = (long + short) // 2

        hash1 = set()
        hash2 = set()
        hash3 = set()

        for i in range(mid, N - mid + 1):
            h1 = rollinghash1.get(i - mid, i)
            h2 = rollinghash2.get(i - mid, i)
            h3 = rollinghash3.get(i - mid, i)

            hash1.add(h1)
            hash2.add(h2)
            hash3.add(h3)

            h1 = rollinghash1.get(i, i + mid)
            h2 = rollinghash2.get(i, i + mid)
            h3 = rollinghash3.get(i, i + mid)

            if h1 in hash1 and h2 in hash2 and h3 in hash3:
                short = mid
                break

        if short != mid:
            long = mid

    print(short)
