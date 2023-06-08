n, l = map(int,input().split())
ans = 0
aj = []
for i in range(1,n+1):
    aj.append(l+i-1)

ans = 10**9
for i in range(n) :
    s = abs(sum(aj)-(sum(aj)-aj[i]))
    if s<ans:
        ans = s
        d = sum(aj)-aj[i]

print(d)
