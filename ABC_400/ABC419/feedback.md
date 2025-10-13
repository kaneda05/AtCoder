# ABC426


## [C問題](https://atcoder.jp/contests/abc426/tasks/abc419_c)
**チェビシェフ距離**を使った問題。
チェビシェフ距離とは、各座標の差の絶対値の最大値を2点間の距離とする計算方法。
今回の問題は２次元の場合におけるものとなっている。


#### 行方向・列方向の広がりを計算
- `X`は行方向の最大値と最小値の差
- `Y`は列方向の最大値と最小値の差

```python
X = max(x) - min(x)
Y = max(y) - min(y)
```

#### 集合に必要な最小時刻を計算
- 8方向に移動できる（キングの動き）ため、最短時間は「チェビシェフ距離」
- 最大の広がり方向`（max(X, Y)）`が基準となり、その半分（切り上げ）が最短時刻

```python
ans = (max(X, Y) + 1) // 2
```

```python
N = int(input())
x, y = [], []
for i in range(N):
    xi, yi = map(int,input().split())
    x.append(xi)
    y.append(yi)

X = max(x) - min(x)
Y = max(y) - min(y)
ans = (max(X, Y) + 1) // 2
print(ans)
```