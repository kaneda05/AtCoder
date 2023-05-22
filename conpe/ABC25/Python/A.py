S = input()
N = int(input())

L = []

for i in S:
    for j in S:
        L.append(i+j)

print(L[N-1])