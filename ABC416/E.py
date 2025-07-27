import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())

    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]

    for i in range(N):
        dist[i][i] = 0

    for _ in range(M):
        A, B, C = map(int, input().split())
        A -= 1
        B -= 1
        dist[A][B] = min(dist[A][B], C)
        dist[B][A] = min(dist[B][A], C)

    K, T = map(int, input().split())
    D = list(map(int, input().split()))
    airports = set()
    for d_node in D:
        airports.add(d_node - 1)

    for k_node in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][k_node] != INF and dist[k_node][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k_node] + dist[k_node][j])
    
    dist_to_airport = [INF] * N
    dist_from_airport = [INF] * N

    for i in range(N):
        for airport_node in airports:
            dist_to_airport[i] = min(dist_to_airport[i], dist[i][airport_node])
            dist_from_airport[i] = min(dist_from_airport[i], dist[airport_node][i])
    
    for i in range(N):
        for j in range(N):
            if dist_to_airport[i] != INF and dist_from_airport[j] != INF:
                dist[i][j] = min(dist[i][j], dist_to_airport[i] + T + dist_from_airport[j])

    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))
        q_type = query[0]

        if q_type == 1:

            x, y, t = query[1], query[2], query[3]
            u, v = x - 1, y - 1

            if t < dist[u][v]:
                dist[u][v] = t
                dist[v][u] = t

                for i in range(N):
                    for j in range(N):

                        if dist[i][u] != INF and dist[v][j] != INF:
                            dist[i][j] = min(dist[i][j], dist[i][u] + dist[u][v] + dist[v][j])

                        if dist[i][v] != INF and dist[u][j] != INF:
                            dist[i][j] = min(dist[i][j], dist[i][v] + dist[v][u] + dist[u][j])

        elif q_type == 2:

            x = query[1]
            u = x - 1
            if u not in airports:
                airports.add(u)

                for i in range(N):
                    for j in range(N):
                        if dist[i][u] != INF and dist[u][j] != INF:
                            dist[i][j] = min(dist[i][j], dist[i][u] + dist[u][j])
                
                dist_to_airport = [INF] * N
                dist_from_airport = [INF] * N

                for i_node in range(N):
                    for airport_node in airports:
                        dist_to_airport[i_node] = min(dist_to_airport[i_node], dist[i_node][airport_node])
                        dist_from_airport[i_node] = min(dist_from_airport[i_node], dist[airport_node][i_node])
                
                for i_node in range(N):
                    for j_node in range(N):
                        if dist_to_airport[i_node] != INF and dist_from_airport[j_node] != INF:
                            dist[i_node][j_node] = min(dist[i_node][j_node], dist_to_airport[i_node] + T + dist_from_airport[j_node])

        elif q_type == 3:
            total_f_sum = 0
            for i in range(N):
                for j in range(N):
                    if dist[i][j] != INF:
                        total_f_sum += dist[i][j]
            print(total_f_sum)

solve()