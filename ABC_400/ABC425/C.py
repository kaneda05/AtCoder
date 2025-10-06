N, Q = map(int,input().split())
A = list(map(int, input().split()))

pre = [0] * (N+1)
for i in range(N):
    pre[i+1] = pre[i] + A[i]

shift = 0
ans = []

for _ in range(Q):
    query = list(input().split())
    if query[0] == "1":
        c = int(query[1])
        shift = (shift + c) % N
    else:
        l, r = int(query[1]), int(query[2])
        start = (shift + l - 1) % N 
        end = (shift + r - 1) % N
        if start <= end:
            res = pre[end+1] - pre[start]
        else:
            res = (pre[N] - pre[start]) + (pre[end+1]-pre[0])
        ans.append(res)

for i in range(len(ans)):
    print(ans[i])