N, L, R = map(int, input().split())
count = 0

for _ in range(N):
    X, Y = map(int, input().split())
    if X <= L and Y >= R:
        count += 1

print(count)
