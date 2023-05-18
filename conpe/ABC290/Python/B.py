N, K = map(int,input().split())
S = input()
T = []
cnt = 0
for i in range(N):
    if S[i] == "o" and cnt<K:
        cnt += 1
        T.append("o")
    else:
        T.append("x")

print("".join(T))