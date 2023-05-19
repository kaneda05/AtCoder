from collections import deque
Q = int(input())
querys = [input().split() for _ in range(Q)]

D = deque()
for q in querys:
    if q[0] == "1":
        D.append(q[1])

    if q[0] == "2":
        print(D[0])

    if q[0] == "3":
        D.popleft()