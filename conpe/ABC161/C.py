n, k = map(int,input().split())

while True:
    if n > k:
        n -= k*(n//k)
    else:
        if abs(n-k) < n:
            n = abs(n-k)
        else:
            break
print(n)