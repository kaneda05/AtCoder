n = int(input())
v = list(map(int,input().split()))
ans = 0
v.sort()
for i in range(n-1):
    if i == 0:
        ans = (v[i]+v[i+1])/2
    else:
        ans = (ans+v[i+1])/2

print(ans)