n = int(input())
votes = {}
for i in range(n):
    s = input()
    if s in votes:
        votes[s] += 1
    else:
        votes[s] = 1

ans = max(votes, key=votes.get)
print(ans)