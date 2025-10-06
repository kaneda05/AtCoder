import sys
input = sys.stdin.readline

# 入力受け取り
N,Q = map(int,input().split())

A = [i + 1 for i in range(N)]
offset = 0

for _ in range(Q):
    query = input().split()
    t = int(query[0])
    
    if t == 1:
        p = int(query[1])
        x = int(query[2])
        idx = (p - 1 + offset) % N
        A[idx] = x
    elif t == 2:
        p = int(query[1])
        idx = (p - 1 + offset) % N
        print(A[idx])
    elif t == 3:
        k = int(query[1])
        offset = (offset + k) % N
