n = int(input())
t,a = map(int,input().split())
h = list(map(int,input().split()))
d = abs(int(-60-10**5*0.006))
ans = 0

for x in range(n):
    if abs(a - (t - h[x]*0.006))<=d:
        d = abs(a-t+h[x]*0.006)
        ans = x + 1


print(ans)
