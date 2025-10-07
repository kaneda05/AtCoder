T = int(input())
for i in range(T):
    a, b, c = map(int,input().split())
    ans = min(a, c, (a+b+c)//3)
    print(ans)