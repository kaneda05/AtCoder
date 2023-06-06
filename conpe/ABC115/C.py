n, k = list(map(int, input().split()))
h = [int(input()) for x in range(n)]
h.sort()
result = float('inf')
for i in range(n-k+1):
    result = min(result, h[i+k-1] - h[i])

print(result)