N = int(input())
ans = 0
for i in range(1,N+1):
    ans += 10000*i
ans //= N
print(ans)