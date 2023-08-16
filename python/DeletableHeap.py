import heapq
import sys


class DeletableHeap:
    def __init__(self) -> None:
        self.que = []
        self.to_delete = []
        return

    def push(self, x):
        heapq.heappush(self.que, x)
        self._flash()
        return

    def delete(self, x):
        heapq.heappush(self.to_delete, x)
        self._flash()
        return

    def pop(self):
        res = heapq.heappop(self.que)
        self._flash()
        return res

    def top(self):
        return self.que[0]

    def _flash(self):
        while self.que and self.to_delete and self.que[0] == self.to_delete[0]:
            heapq.heappop(self.que)
            heapq.heappop(self.to_delete)
        return


def main():
    # ABC306 E
    N, K, Q = map(int, sys.stdin.readline().strip().split())

    global ans
    ans = 0
    using_num = DeletableHeap()
    unusing_num = DeletableHeap()

    A = [0] * N

    for _ in range(K):
        using_num.push(0)
    for _ in range(K, N):
        unusing_num.push(0)

    def add(x):
        global ans
        ans += x
        using_num.push(x)

        y = using_num.pop()
        ans -= y
        unusing_num.push(-y)

    def delete(x):
        global ans

        if -unusing_num.top() >= x:
            unusing_num.delete(-x)
            return

        ans -= x
        using_num.delete(x)
        y = -unusing_num.pop()
        using_num.push(y)
        ans += y

        return

    for _ in range(Q):
        x, y = map(int, sys.stdin.readline().strip().split())
        x -= 1

        add(y)
        delete(A[x])

        A[x] = y

        print(ans)
    return


if __name__ == "__main__":
    main()
