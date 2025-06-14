# 入力の受け取り
N = int(input())
A = list(map(int, input().split()))
K = int(input())

# 出場可能なレースの数をカウント
count = sum(1 for a in A if a >= K)

# 出力
print(count)