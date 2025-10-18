from collections import Counter
N, K = map(int,input().split())
S = input().strip()

sub = [S[i:i+K] for i in range(N-K+1)]
c = Counter(sub)

x = max(c.values())

max_sub = sorted([t for t, c in c.items() if c == x])
print(x)
print(*max_sub)
