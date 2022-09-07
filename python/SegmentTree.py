class SegmentTree:
    def __init__(self, n: int) -> None:
        x = 1
        while x < n:
            x *= 2

        self.n = x  # 葉の数
        self.data = [-float("inf")] * (2 * x - 1)  # データ
        return

    def update(self, i: int, x: int):
        i += self.n - 1
        self.data[i] = x

        while i > 0:
            i = (i - 1) // 2
            self.data[i] = min(self.data[i * 2 + 1], self.data[i * 2 + 2])
        return

    def query(self, a: int, b: int):
        return self._query(a, b, 0, 0, self.n)

    def _query(self, a: int, b: int, k: int, left: int, right: int):
        # [a, b) : 要求範囲
        # k: 現在のノード番号
        # [left, right): 探索範囲

        if b <= left or a >= right:
            return float("inf")

        if a <= left and right <= b:
            return self.data[k]

        value_left = self._query(a, b, k * 2 + 1, left, (left + right) // 2)
        value_right = self._query(a, b, k * 2 + 2, (left + right) // 2, right)

        return min(value_left, value_right)


class LazySegmentTree:
    def __init__(self, n: int) -> None:
        x = 1
        while x < n:
            x *= 2

        self.n = x  # 葉の数
        self.data = [-float("inf")] * (2 * x - 1)  # データ
        self.lazy = [-float("inf")] * (2 * x - 1)
        return

    def eval(self, k: int, left: int, right: int):
        # 遅延評価
        return

    def update(self, a: int, b: int, k: int = 0, left: int = 0, right: int = -1):
        return

    def query(self, a: int, b: int):
        return

    def _query(self, a: int, b: int):
        return


if __name__ == "__main__":
    tree = SegmentTree(10)
