# 強連結成分分解


import sys

sys.setrecursionlimit(10**8)


def scc(N, G):
    used = [False] * N
    order = []

    def dfs(u):
        for v in G[u]:
            if used[v]:
                continue
            used[v] = True
            dfs(v)

        order.append(u)

    for u in range(N):
        if used[u]:
            continue
        used[u] = True
        dfs(u)

    RG = [[] for _ in range(len(G))]

    for i, g in enumerate(G):
        for u in g:
            RG[u].append(i)

    groups = []
    used = [False] * N

    def rdfs(u):
        groups[-1].append(u)

        for v in RG[u]:
            if used[v]:
                continue
            used[v] = True
            rdfs(v)
        return

    while order:
        u = order.pop()

        if used[u]:
            continue
        groups.append(list())

        used[u] = True
        rdfs(u)

    return groups


if __name__ == "__main__":
    # Atcoder Library Practice Contest G-SCC
    input = sys.stdin.readline

    N, M = map(int, input().strip().split())

    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().strip().split())

        G[a].append(b)

    groups = scc(N, G)

    print(len(groups))
    for group in groups:
        print(len(group), " ".join([str(i) for i in group]))
