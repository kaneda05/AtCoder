N, M = map(int,input().split())
S = [input().strip() for _ in range(N)]

score = [0] * N

for j in range(M):
    votes = [S[i][j] for i in range(N)]
    x = votes.count("0")
    y = votes.count("1")

    if x == 0 or y == 0:
        for i in range(N):
            score[i] += 1
    elif x < y:
        for i in range(N):
            if votes[i] == "0":
                score[i] += 1
    else:
        for i in range(N):
            if votes[i] == "1":
                score[i] += 1

max_score = max(score)
ans = [str(i+1) for i in range(N) if score[i] == max_score]

print(" ".join(ans))