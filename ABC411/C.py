import sys

sys.setrecursionlimit(1 << 25)

N, Q = map(int,input().split())
A = list(map(int,input().split()))

colors = [0] * (N + 2)
black_segments = 0
res = []

for a in A:
    if colors[a] == 0:
        colors[a] = 1
        if colors[a - 1] == 0 and colors[a + 1] == 0:
            black_segments += 1
        elif colors[a - 1] == 1 and colors[a + 1] == 1:
            black_segments -= 1
    else:
        colors[a] = 0
        if colors[a - 1] == 0 and colors[a + 1] == 0:
            black_segments -= 1
        elif colors[a - 1] == 1 and colors[a + 1] == 1:
            black_segments += 1

    res.append(black_segments)

print('\n'.join(map(str, res)))
