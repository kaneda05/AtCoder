# 入力
N = int(input())  # 箱の数
Q = int(input())  # ボールの数
X = list(map(int, input().split()))  # 各ボールの指示

counts = [0] * (N + 1)  # 箱ごとのボール数（1-indexed）
result = []  # 各ボールが入った箱番号を記録

for x in X:
    if x >= 1:
        counts[x] += 1
        result.append(x)
    else:
        # 最もボールの少ない箱を探す（番号が小さい方を優先）
        min_count = float('inf')
        chosen_box = -1
        for i in range(1, N + 1):
            if counts[i] < min_count:
                min_count = counts[i]
                chosen_box = i
        counts[chosen_box] += 1
        result.append(chosen_box)

# 出力
for r in result:
    print(r)
