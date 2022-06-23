// 強連結成分のグループ番号を返す
// 動作確認未実施

#include <bits/stdc++.h>
using namespace std;

struct StronglyConnectedComponents {
    vector<vector<int>> g, rg;
    vector<int> groupList, rorder;
    vector<int> used;
    int groupNo = 0;

    StronglyConnectedComponents(vector<vector<int>> &_g) {
        int N = _g.size();

        g = _g;
        rg.resize(N);
        groupList.resize(N, -1);
        used.resize(N, false);

        for (int from = 0; from < N; from++) {
            for (int to : g[from]) {
                rg[to].push_back(from);
            }
        }

        for (int i = 0; i < N; i++) {
            if (used[i]) continue;
            dfs(i);
        }

        reverse(rorder.begin(), rorder.end());
        for (int r : rorder) {
            if (groupList[r] != -1) continue;
            rdfs(r);
            groupNo++;
        }
    }

    void dfs(int u) {
        used[u] = true;
        for (int v : g[u]) {
            if (used[v]) continue;
            dfs(v);
        }
        rorder.push_back(u);
    }

    void rdfs(int u) {
        for (int v : rg[u]) {
            if (groupList[v] != -1) continue;
            rdfs(v);
        }
    }

    int group(int i) { return groupList[i]; }
};