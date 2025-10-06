N, S = map(int,input().split())
T = list(map(int,input().split()))

cnt = 0
for t in T:
    if t-cnt >= S+0.5:
        print("No")
        exit()
    cnt = t

print("Yes")