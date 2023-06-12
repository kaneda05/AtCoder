n,m = map(int,input().split())
A = list(map(int,input().split()))
cnt = 0
for a in A:
    if 4*m*a >= sum(A):
        cnt += 1

if cnt >= m:
    print("Yes")
else:
    print("No")
