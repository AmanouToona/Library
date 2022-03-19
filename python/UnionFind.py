class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents =  [-1] * n  # 負値 :-size  正:parent を表す
    
    def find(self, x):  # root を返す
        if self.parents[x] < 0:
            return x
        else:
            return self.find(self.parents[x])
    
    def union(self, x, y):  # x, y を結合する
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return
        
        if self.parents[x_root] > self.parents[y_root]:
            x_root, y_root = y_root, x_root

        self.parents[x_root] += self.parents[y_root]
        self.parents[y_root] = x_root            

    def size(self, x):  # x が含まれる木のサイズを返す
        return - self.parents[self.find(x)]
    
    def same(self, x, y):  # x, y が同一の木に含まれるか返す
        return self.find(x) == self.find(y)
    
    def members(self, x):  # x を含む木に含まれるメンバーをかえす
        x_root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == x_root]
    
    def roots(self):   # 根の一覧を返す
        return [i for i in range(self.n) if self.parents[i] < 0]
