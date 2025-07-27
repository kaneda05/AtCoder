from itertools import product

N, K, X = map(int, input().split())
S = [input() for _ in range(N)]

S.sort()

candidates = []

for indices in product(range(N), repeat=K):
    word = ''.join(S[i] for i in indices)
    candidates.append(word)

candidates.sort()

print(candidates[X - 1])
