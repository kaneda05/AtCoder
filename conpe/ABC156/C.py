n = int(input())
X = list(map(int,input().split()))
ans = 10**9
for p in range(100+10):
    cal = 0
    for x in X:
        cal += (x-p)**2
    ans = min(ans,cal)
    
print(ans)