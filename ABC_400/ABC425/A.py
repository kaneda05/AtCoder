N = int(input().strip())

if N % 2 == 0:
    k = N // 2
    ans = k*k*(4*k + 3)
else:
    k = (N - 1) // 2
    ans = - (k+1)*(k+1)*(4*k + 1)
print(ans)
