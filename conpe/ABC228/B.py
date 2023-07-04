n, x = map(int,input().split())
a = list(map(int,input().split()))
print(len(set(a)))

s = [0] * (n-1)
t = x
for i in range(n+1):
    s[t] = 1
    b = a[t-1]
    if s[b] == 1:
        break
    else:
        t = b

ans = 0
for i in range(n+1):
    ans += s[i]

print(ans)