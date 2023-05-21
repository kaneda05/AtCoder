N, S ,T = map(int,input().split())
W = int(input())
A = [0]+[int(input()) for _ in range(N-1)]
cnt = 0
for i in range(N):
    W += A[i]
    if S<=W<=T:
        cnt += 1

print(cnt)