n = int(input())
d = list(map(int,input().split()))
ans = 0
d.sort()
a = d[n//2-1]
b = d[n//2]
print(b-a)