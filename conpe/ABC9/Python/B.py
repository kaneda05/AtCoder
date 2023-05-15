N = int(input())
A = [int(input()) for _ in range(N)]
set_A = list(set(A))
set_A.sort()
print(set_A[-2])