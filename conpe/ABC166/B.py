n,k = map(int,input().split())
num_list = [0]*(n+1)
for i in range(k):
    d = int(input())
    a = list(map(int,input().split()))
    for j in range(d):
        num_list[a[j]] += 1

ans = 0
for i in range(1,n+1):
    if num_list[i] == 0:
        ans += 1

print(ans)
    