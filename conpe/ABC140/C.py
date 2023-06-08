n = int(input())
b = list(map(int,input().split()))
ans = 0
for i in range(1,n-1):
    ans += min(b[i-1],b[i])

ans += b[0]
ans += b[n-2]
print(ans)