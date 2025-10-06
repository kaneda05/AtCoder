N, M, K = map(int,input().split())

solved = [set() for _ in range(N+1)]
ended = set()
res = []

for _ in range(K):
    A, B = map(int,input().split())
    solved[A].add(B)

    if len(solved[A]) == M and A not in ended:
        res.append(A)
        ended.add(A)

print(*res)