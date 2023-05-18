N = int(input())
X = list(map(int,input().split()))
X.sort()
ans = []
for i in range(N):
    X.pop(0)
    X.pop(-1)

print(sum(X)/len(X))