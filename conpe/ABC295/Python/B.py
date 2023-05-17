from sys import stdin
import copy
R, C = map(int, input().split())
A = [list(stdin.readline()[:-1]) for _ in range(R)]

B = copy.deepcopy(A)

for i in range(R):
    for j in range(C):
        if A[i][j].isnumeric():
            for k in range(R):
                for l in range(C):
                    if abs(i - k) + abs(j - l) <= int(B[i][j]):
                        B[k][l] = "."

for i in range(R):
    print("".join(B[i]))