import sys
import bisect

input = sys.stdin.readline

T = int(input())
results = []

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()
    used = [False] * N
    total = 0

    for b in B:
        need = (M - b) % M
        idx = bisect.bisect_left(A, need)

        while idx < N and used[idx]:
            idx += 1

        if idx < N:
            a = A[idx]
            used[idx] = True
        else:
            idx = 0
            while used[idx]:
                idx += 1
            a = A[idx]
            used[idx] = True

        total += (a + b) % M

    results.append(str(total))

print('\n'.join(results))
