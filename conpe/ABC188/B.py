import numpy as np
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

A = np.array(a)
B = np.array(b)
ans = np.dot(A,B)
if ans == 0:
    print("Yes")
else:
    print("No")