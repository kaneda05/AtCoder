import sys

N, Q = map(int,input().split())
A = list(map(int,input().split()))
queries = [int(input()) for _ in range(Q)]
A.sort()
prefix_sum = [0] * (N + 1)

for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + A[i]

    total_tea_bags = prefix_sum[N]

for b in queries:
    k = b-1

    left = 0
    right = N - 1
    idx = -1
    while left <= right:
        mid = (left+right) // 2
        if A[mid] <= k:
            idx = mid
            left = mid + 1
        else:
            right = mid - 1

    S = 0
    if idx != -1:
        S = prefix_sum[idx+1]
            
        count_k = N - (idx + 1)
        S += count_k * k
    else:
        S = N * k
        
    x = S + 1

    if x > total_tea_bags:
        print(-1)
    else:
        print(x)