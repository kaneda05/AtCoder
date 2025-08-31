N = int(input())
S = [input() for _ in range(N)]
X, Y = input().split()
X = int(X) - 1

if S[X] == Y:
    print("Yes")
else:
    print("No")