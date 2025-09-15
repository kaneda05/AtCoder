import sys
import heapq
from collections import deque

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A, B, C = [], [], []
    for _ in range(N):
        a, b, c = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)

    ans = [-1] * N

    leave_heap = []
    queue = deque()
    inside = 0

    for i in range(N):
        now = A[i]

        while leave_heap and leave_heap[0][0] <= now:
            t, ppl = heapq.heappop(leave_heap)
            inside -= ppl

            while queue and inside + C[queue[0]] <= K:
                j = queue.popleft()
                ans[j] = t
                inside += C[j]
                heapq.heappush(leave_heap, (t + B[j], C[j]))

        queue.append(i)

        while queue and inside + C[queue[0]] <= K:
            j = queue.popleft()
            ans[j] = now
            inside += C[j]
            heapq.heappush(leave_heap, (now + B[j], C[j]))

    while queue:
        if not leave_heap:
            break
        t, ppl = heapq.heappop(leave_heap)
        inside -= ppl
        while queue and inside + C[queue[0]] <= K:
            j = queue.popleft()
            ans[j] = t
            inside += C[j]
            heapq.heappush(leave_heap, (t + B[j], C[j]))

    print("\n".join(map(str, ans)))

if __name__ == "__main__":
    main()
