from itertools import combinations
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
edges = set()

for i in range(M):
    a = int(data[2 + 2 * i]) - 1
    b = int(data[3 + 2 * i]) - 1
    edges.add((min(a, b), max(a, b)))

from itertools import permutations

def is_valid_cycle_graph(edge_set):
    degree = [0] * N
    for a, b in edge_set:
        degree[a] += 1
        degree[b] += 1
    return all(d == 2 for d in degree)

all_possible_edges = [(i, j) for i in range(N) for j in range(i + 1, N)]

min_ops = float('inf')

# 全ての辺集合の中から、サイズがNのサブセット（次数2で全頂点カバーする可能性がある）を列挙
for edge_subset in combinations(all_possible_edges, N):
    edge_set = set(edge_subset)
    if is_valid_cycle_graph(edge_set):
        # 差分を計算（追加 + 削除の最小コスト）
        to_add = edge_set - edges
        to_remove = edges - edge_set
        ops = len(to_add) + len(to_remove)
        min_ops = min(min_ops, ops)

print(min_ops)
