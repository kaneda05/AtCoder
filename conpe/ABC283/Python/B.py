from collections import deque
N = int(input())
A = deque(list(map(int,input().split())))
Q = int(input())
for i in range(Q):
    query = list(map(int,input().split()))
    k = query[1]-1
    if query[0] == 1:
        x = query[2]
        A[k] = x
    
    if query[0] == 2:
        print(A[k])