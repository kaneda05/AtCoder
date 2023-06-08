n = int(input())
p = list(map(int,input().split()))
cnt = 0
for i in range(n):
    if p[i] != i+1:
        index = p.index(i+1)
        p[i],p[index]= p[index], p[i]
        cnt += 1

if 1<cnt:
    print("NO")
else:
    print("YES")
