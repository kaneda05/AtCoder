n = int(input())
p = [int(input()) for _ in range(n)]
max_p = max(p)
ans = sum(p)-max_p+max_p//2
print(ans)