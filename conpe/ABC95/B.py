n,x = map(int,input().split())
m = [int(input()) for _ in range(n)]

ans = 0
ans += n
x -= sum(m)
ans += x // min(m)
print(ans)