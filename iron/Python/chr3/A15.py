import bisect
N = int(input())
A = list(map(int,input().split()))

set_A = list(set(A))
set_A.sort()

B = []
for i in range(N):
    B.append(bisect.bisect_left(set_A, A[i])+1)

print(*B)