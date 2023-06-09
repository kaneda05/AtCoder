n,k,q = map(int,input().split())
ans = [k-q]*(n+1)

for i in range(q):
    a = int(input())
    ans[a] += 1

for i in range(1,n+1):
    if ans[i]<=0:
        print("No")
    else:
        print("Yes")