N = int(input())
ans1 = 0
max_P = -10**9
L = []
for i in range(N):
    S, P = map(str,input().split())
    P = int(P)
    if max_P < P:
        name = S
        max_P = P
    L.append(P)

if sum(L)//2<max_P:
    print(name)
else:
    print("atcoder")