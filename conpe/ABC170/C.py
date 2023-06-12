x, n = map(int, input().split())
p = set([*map(int, input().split())])

m = 10000
ans = -1
for i in range(300):
    if abs(x - i) < m and i not in p:
        m = abs(x - i)
        ans = i

print(ans)