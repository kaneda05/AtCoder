T = int(input())

for _ in range(T):
    N, M, K = map(int,input().split())
    S = input().strip()
    adj = [[] for _ in range(N)]

    for _ in range(M):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)


    dp = [[False] * (2*K+1) for _ in range(N)]

    for i in range(N):
        dp[i][0] = (S[i] == "A")

    for t in range(1, 2*K+1):
        if t % 2 == 0:
            for u in range(N):
                dp[u][t] = any(dp[v][t-1] for v in adj[u])
        else:
            for u in range(N):
                dp[u][t] = all(dp[v][t-1] for v in adj[u])
        
    if dp[0][2*K]:
        print("Alice")
    else:
        print("Bob")