n,m = map(int,input().split())
A = []
L = [0]*(m+1)
for i in range(n):
    s = list(map(int,input().split()))
    k = s[0]
    A = s[1:]
    for a in A:
        L[a] += 1
        

ans = 0
for i in range(1,m+1):
    if L[i] == n:
        ans += 1
        
print(ans)