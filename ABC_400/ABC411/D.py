import sys
input = sys.stdin.readline
sys.setrecursionlimit(1 << 25)

N, Q = map(int, input().split())

# ノードは (親のインデックス, 追加文字列)
nodes = [(-1, '')]  # 初期空ノード

# 各PCが参照するノードID
pc = [0] * N
server = 0

for _ in range(Q):
    q = input().split()
    t = int(q[0])

    if t == 1:
        p = int(q[1]) - 1
        pc[p] = server

    elif t == 2:
        p = int(q[1]) - 1
        s = q[2]
        nodes.append((pc[p], s))  # 新しいノードを追加
        pc[p] = len(nodes) - 1

    else:  # t == 3
        p = int(q[1]) - 1
        server = pc[p]

# サーバーのノードから再構築
result = []
node_id = server
while node_id != -1:
    parent, s = nodes[node_id]
    result.append(s)
    node_id = parent

# 後ろから構築されているので逆順に出力
print(''.join(reversed(result)))