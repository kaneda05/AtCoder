n = int(input())
d,x = map(int,input().split())
a = [int(input()) for _ in range(n)]
ans = 0
for i in range(n):
    ans += (d-1)//a[i] + 1
ans += x
print(ans)