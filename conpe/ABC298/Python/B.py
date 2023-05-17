import numpy as np

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
B = [list(map(int,input().split())) for _ in range(N)]

a = np.array(A)
b = np.array(B)

for i in range(4):
    if 0<=np.min(b-a): # bが0,aが1ならb-aをした場合-1が最小値として出てくる
        print("Yes")
        exit()

    a = np.rot90(a)

print("No")