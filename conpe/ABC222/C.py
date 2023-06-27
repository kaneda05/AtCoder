n, m = map(int,input().split())
s = [input() for _ in range(2*n)]
rank = [[0,i] for i in range(2*n)]

def judge(a,b):
    if a==b: return -1
    if a=="G" and b=="P": return 1
    if a=="C" and b=="G": return 1
    if a=="P" and b=="C": return 1
    return 0

for j in range(m):
    for i in range(n):
        player1 = rank[2*i][1]
        player2 = rank[2*i+1][1]
        result = judge(s[player1][j], s[player2][j])
        if result != -1: rank[2*i+result][0] -= 1 # result=0ならばrank[2*i]が−1され、result=1ならばrank[2*i+1]が-1される
    rank.sort()

for i,j in rank: print(j+1)