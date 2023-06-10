n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    if a[i]%2!=0:
        pass
    else:
        if a[i]%3==0 or a[i]%5==0:
            pass
        else:
            print("DENIED")
            exit()

print("APPROVED")