N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for b in B:
    for i in range(len(A)):
        if A[i] == b:
            A.pop(i)
            break
print(*A)