n, x = map(int,input().split())
a = list(map(int,input().split()))
for i in range(n):
    if i%2!=0:
        a[i]-=1
    x -= a[i]
    if x < 0:
        print("No")
        exit()

print("Yes")