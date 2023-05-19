a = list(map(int,input().split()))
S = int(input())

n = len(a)        # 配列数
res = n + 1       # 最小区間の初期値（配列数＋１）
s = 0             # 集計開始位置
t = 0             # 集計最終位置
total = 0         # 合計値

while True:
    while t < n and total < S:  # 集計最終位置が配列内かどうか、合計値がSより小さいかどうか
        total += a[t]           # 合計値を算出
        t += 1                  # 集計最終位置を１つうしろにずらす
    if total < S:
        break                   # 合計値が条件(整数S以上)に達していないので終了（集計最終位置が配列を超えた）
    res = min(res, t - s)       # 合計値が条件を満たしている部分列の長さが、より短い場合は更新
    total -= a[s]               # 合計値から先頭の要素をひく
    s -= 1                      # 集計開始位置を１つうしろにずらす

if res > n:       # 配列数より大きいので解がなかった
    res = 0       # 解がなかったため0を設定
print(res)     