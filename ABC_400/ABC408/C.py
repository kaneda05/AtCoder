N, M = map(int,input().split())
L = []
R = []
for i in range(M):
    l, r = map(int,input().split())
    L.append(l)
    R.append(r)

diff = [0] * (N + 2)
for i in range(M):
    diff[L[i]] += 1
    diff[R[i]+1] -= 1

protected = [0] * (N + 2)
for i in range(1, N + 1):
    protected[i] = protected[i - 1] + diff[i]

ans = min(protected[1:N + 1])
print(ans)