import sys

# 再帰の深さの上限を増やす
sys.setrecursionlimit(10**6 + 5)

def solve():
    """
    問題全体を解くメイン関数
    """
    # N, Qの入力
    try:
        N, Q = map(int, sys.stdin.readline().split())
    except (IOError, ValueError):
        return

    # Union-Find木のためのデータ構造を初期化
    # parent[i]: 要素iの親のインデックス
    # size[i]: 要素iが根である場合の、そのグループの要素数
    # インデックスを1からN+1まで使えるようにN+2のサイズを確保
    parent = list(range(N + 2))
    size = [1] * (N + 1) + [0] # size[0]は未使用, size[N+1]は番兵用

    def find(i: int) -> int:
        """
        要素iが属するグループの根（代表元）を返す（経路圧縮付き）
        """
        if parent[i] == i:
            return i
        # 親をたどりながら根を探し、その過程で親を根に直接つなぎ替える（経路圧縮）
        parent[i] = find(parent[i])
        return parent[i]

    def union(i: int, j: int):
        """
        要素iが属するグループと要素jが属するグループを統合する
        """
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            # サイズが小さい方を大きい方につなぐ（Union by Size）
            if size[root_i] < size[root_j]:
                root_i, root_j = root_j, root_i
            parent[root_j] = root_i
            size[root_i] += size[root_j]
            size[root_j] = 0

    # Q回のクエリを処理
    for _ in range(Q):
        X, Y = map(int, sys.stdin.readline().split())
        
        upgraded_count = 0
        root_y = find(Y)
        
        # v: 次にアップグレード対象となるバージョンの根
        # find(1)から始め、X以下のバージョンを順に処理
        v = find(1)
        while v <= X:
            # vが代表するグループのPC台数を加算
            upgraded_count += size[v]
            
            # 次にチェックすべきバージョンはv+1以降の根
            # vを統合する前に次のジャンプ先を確保しておく
            next_v = find(v + 1)
            
            # vのグループをYのグループに統合する
            # これにより、vのPCはYと同じバージョンになる
            union(v, root_y)
            
            # 次の未統合バージョンへジャンプ
            v = next_v
            
        print(upgraded_count)

if __name__ == "__main__":
    solve()