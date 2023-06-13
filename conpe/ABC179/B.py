n = int(input())
ans = 0
cnt = 0
for i in range(n):
    d1,d2 = map(int,input().split())
    if d1==d2:
        cnt += 1
        if cnt==3:
            print("Yes")
            exit()
    else:
        cnt = 0

print("No")