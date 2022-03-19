#include <bits/stdc++.h>
using ll = long long;
using namespace std;

class UnionFind {
    vector<int> p, rank, member_size;

   public:
    UnionFind(int n) : p(n), rank(n, 0), member_size(n, 1) {
        for (int i = 0; i < n; i++) {
            p[i] = i;
        }
    }

    int find(int x) {
        if (p[x] == x) return x;
        p[x] = find(p[x]);
        return p[x];
    }

    void unite(int x, int y) {
        x = find(x);
        y = find(y);

        if (x == y) return;

        if (rank[x] <= rank[y]) {
            p[x] = y;
            member_size[y] += member_size[x];
        } else {
            p[y] = x;
            member_size[x] += member_size[y];
        }

        if (rank[x] == rank[y]) {
            rank[y]++;
        }
        return;
    }

    int same(int x, int y) { return find(x) == find(y); }

    int size(int x) { return member_size[find(x)]; }
};

int main() {
    int N, M;
    cin >> N >> M;

    stack<pair<int, int>> bridge;

    for (int i = 0; i < M; i++) {
        int A, B;
        cin >> A >> B;
        A--;
        B--;
        bridge.push(make_pair(A, B));
    }

    UnionFind island(N);

    ll unconf = 1LL * N * (N - 1) / 2;
    vector<ll> ans;
    while (!bridge.empty()) {
        ans.push_back(unconf);

        auto [a, b] = bridge.top();
        bridge.pop();

        if (island.same(a, b)) {
            continue;
        }

        unconf -= (1LL * island.size(a)) * island.size(b);
        island.unite(a, b);
    }

    reverse(ans.begin(), ans.end());
    for (int i = 0; i < M; i++) {
        cout << ans[i] << endl;
    }
}