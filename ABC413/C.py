from collections import deque
import sys

input = sys.stdin.readline

Q = int(input())
A = deque()
ans = []

for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        c = int(query[1])
        x = int(query[2])
        A.append((x, c))
    else:
        k = int(query[1])
        total = 0
        while k > 0:
            x, c = A[0]
            if c <= k:
                total += x * c
                k -= c
                A.popleft()
            else:
                total += x * k
                A[0] = (x, c - k)
                k = 0
        ans.append(str(total))

print('\n'.join(ans))