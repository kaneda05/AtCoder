import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.black_count = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.black_count[x] += self.black_count[y]

    def add_black(self, x, val):
        """ 頂点xの属する成分の黒頂点数を val (±1) 更新 """
        r = self.find(x)
        self.black_count[r] += val

    def has_black(self, x):
        """ 頂点xの属する成分に黒が存在するか """
        return self.black_count[self.find(x)] > 0


N, Q = map(int, input().split())
uf = UnionFind(N)
is_black = [False] * N

ans = []

for _ in range(Q):
    query = input().split()
    t = int(query[0])
    if t == 1:
        u, v = int(query[1]) - 1, int(query[2]) - 1
        uf.unite(u, v)
    elif t == 2:
        v = int(query[1]) - 1
        if is_black[v]:
            is_black[v] = False
            uf.add_black(v, -1)
        else:
            is_black[v] = True
            uf.add_black(v, +1)
    else:
        v = int(query[1]) - 1
        if uf.has_black(v):
            ans.append("Yes")
        else:
            ans.append("No")

print("\n".join(ans))
