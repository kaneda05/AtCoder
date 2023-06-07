n = int(input())
w = list(map(int,input().split()))
ans = 10 ** 9
for t in range(1,n):
    s1 = sum(w[:t])
    s2 = sum(w[t:])

    ans = min(abs(s1-s2), ans)

print(ans)