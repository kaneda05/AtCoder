class UnionFind:
    def __init__(self, size):
        self.par = list(range(size))
        self.size = [1] * size

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.par[y] = x
        self.size[x] += self.size[y]

    def get_size(self, x):
        return self.size[self.find(x)]

# 入力受け取り
N, M = map(int,input().split())

# UnionFind のサイズを N + 1 に（1-indexed に対応）
uf = UnionFind(N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    uf.unite(a, b)

# 1〜N の各ノードのサイズを見て、最大を出力
max_group_size = max(uf.get_size(i) for i in range(1, N + 1))
print(max_group_size)