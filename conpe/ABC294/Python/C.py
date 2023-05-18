import bisect
N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = A + B
C.sort()
ansA = []
for i in range(N):
    ansA.append(bisect.bisect_left(C,A[i])+1)

ansB = []
for i in range(M):
    ansB.append(bisect.bisect_left(C,B[i])+1)

print(*ansA)
print(*ansB)