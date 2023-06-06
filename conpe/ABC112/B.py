n,T = map(int,input().split())
ans = 10**9
for i in range(n):
    c,t = map(int,input().split())
    if t<=T:
        ans = min(ans,c)

print("TLE" if ans==10**9 else ans)