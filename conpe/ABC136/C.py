n = int(input())
h = list(map(int,input().split()))
for i in reversed(range(1,n)):
    #print(h[i])
    if h[i-1]<= h[i]:
        continue

    elif h[i-1]==h[i]+1:
        h[i-1] -= 1
    else:
        print("No")
        exit()

print("Yes")