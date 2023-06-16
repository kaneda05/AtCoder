n = int(input())
ans = 0
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    for i in range(1,n):
        ans += i
        if n<=ans:
            print(i)
            exit()