import math
N = int(input())
A = list(map(int,input().split()))
N0 = A.count(0)
N-= N0
print(math.ceil(sum(A)/N))