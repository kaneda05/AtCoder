n,m,c = map(int,input().split())
b = list(map(int,input().split()))

cnt = 0
for i in range(n):
    a = list(map(int,input().split()))
    ans = 0
    for j in range(m):
        ans += a[j]*b[j]
    if ans + c > 0:
        cnt += 1

print(cnt)