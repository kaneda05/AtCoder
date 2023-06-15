n = int(input())
ans = 10**9
for i in range(n):
    a,p,x = map(int,input().split())
    if x > a and ans > p:
        ans = p

if ans == 10**9:
    print(-1)
else:
    print(ans)