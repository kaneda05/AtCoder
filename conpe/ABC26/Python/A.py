A = int(input())
ans = -10**9
for x in range(A):
    for y in range(A):
        if x + y == A:
            ans = max(ans, x*y)
print(ans)