N = int(input())
A = list(map(int, input().split()))
K = int(input())

count = sum(1 for a in A if a >= K)

print(count)