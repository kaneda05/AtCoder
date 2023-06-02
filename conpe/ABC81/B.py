n = int(input())
a = list(map(int,input().split()))
cnt = 0

while True:
    for i in range(n):
        if a[i]%2!=0:
            print(cnt)
            exit()
            break
        else:
            a[i]//=2

    cnt += 1