n,s,d = map(int,input().split())
ans = 0
for i in range(n):
    x,y = map(int,input().split())
    if x<s and d<y:
        print("Yes")
        exit()

print("No")