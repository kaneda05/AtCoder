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