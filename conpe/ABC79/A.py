n = list(input())
cnt = 0
ans = n[0]
for i in range(1,len(n)):
    if int(n[i-1])==int(n[i]):
        cnt+=1


        if cnt==2:
            print("Yes")
            exit()
    else:
        cnt=0

print("No")
