n = int(input())
t = list(map(int,input().split()))
m = int(input())
for i in range(m):
    p,x = map(int,input().split())
    p-=1
    ans = 0
    for k in range(n):
        if k == p:
            ans += x
        else:
            ans += t[k]
    print(ans)