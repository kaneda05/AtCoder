N = int(input())
A = [int(input()) for _ in range(N)]
set_A = set(A)
print(N-len(set_A))