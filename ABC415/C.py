from collections import deque

def is_possible(N, S):
    safe = [S[i] == '0' for i in range(len(S))]
    full_state = (1 << N) - 1
    visited = [False] * (1 << N)
    queue = deque()
    queue.append(0)
    visited[0] = True

    while queue:
        current = queue.popleft()
        for i in range(N):
            if (current >> i) & 1 == 0:
                next_state = current | (1 << i)
                if not visited[next_state]:
                    if safe[next_state - 1]:
                        visited[next_state] = True
                        queue.append(next_state)

    return "Yes" if visited[full_state] else "No"

T = int(input())
results = []
for _ in range(T):
    N = int(input())
    S = input().strip()
    results.append(is_possible(N, S))

print("\n".join(results))
