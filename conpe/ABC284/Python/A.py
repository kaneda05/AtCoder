N = int(input())
S = [None]*(N)
for i in range(N):
    S[i] = input()

for i in reversed(range(N)):
    print(S[i])