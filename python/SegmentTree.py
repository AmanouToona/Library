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
    # 区間加算の遅延セグ木
    # 動作検証前
    def __init__(self, n: int) -> None:
        x = 1
        while x < n:
            x *= 2

        self.n = x  # 葉の数
        self.data = [-float("inf")] * (2 * x - 1)  # データ
        self.lazy = [-float("inf")] * (2 * x - 1)  # 遅延評価データ
        return

    def eval(self, k: int, left: int, right: int):
        # 遅延評価
        # 1. 自ノードに、自ノードの遅延配列の値を伝搬させる
        # 2. 子ノードに自ノードの遅延配列の値を伝搬させる
        # 3. 自ノードの遅延配列を空にする
        if self.lazy[k] != 0:
            self.data[k] += self.lazy[k]

            # 最下段ではないならば
            if right - left > 1:
                self.lazy[2 * k + 1] += self.lazy[k] / 2
                self.lazy[2 * k + 2] += self.lazy[k] / 2

        self.lazy[k] = 0

        return

    def update(self, a: int, b: int, x: int, k: int = 0, left: int = 0, right: int = -1):
        if right < 0:
            right = self.n

        if b <= left or right <= a:
            return

        if a <= left and b <= right:
            self.lazy[k] += (right - left) * x
            eval(k, left, right)
            return

        self.update(a, b, x, 2 * k + 1, left, (left + right) / 2)
        self.update(a, b, x, 2 * k + 2, (left + right) / 2, right)
        self.data[k] = self.data[2 * k + 1] + self.data[2 * k + 2]

        return

    def query(self, a: int, b: int):
        return self._query(a, b, 0, 0, self.n)

    def _query(self, a: int, b: int, k: int, left: int, right: int):
        # [a, b) : 要求範囲
        # k: 現在のノード番号
        # [left, right): 探索範囲

        if b <= left or right <= a:
            return 0

        eval(k, left, right)
        if a <= left and right <= b:
            return self.data[k]

        val_left = self._query(a, b, 2 * k + 1, left=left, right=(left + right) / 2)
        val_right = self._query(a, b, 2 * k + 2, left=(left + right) / 2, right=right)

        return val_left + val_right


if __name__ == "__main__":
    tree = SegmentTree(10)
