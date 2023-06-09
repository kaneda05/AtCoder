n = int(input())
a = list(map(int,input().split()))
L = []
if 1 not in a:
    print(-1)
    exit()
    
else:
    num = 1
    for i in range(len(a)):
        if a[i] == num:
            L.append(num)
            num += 1

print(n-len(L))