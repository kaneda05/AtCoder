N = int(input())
D = list(map(int, input().split()))

pos = [0] * N
for i in range(1, N):
    pos[i] = pos[i-1] + D[i-1]

for i in range(N - 1):
    row = []
    for j in range(i + 1, N):
        row.append(str(pos[j] - pos[i]))
    print(" ".join(row))
