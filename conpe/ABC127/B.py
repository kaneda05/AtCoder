def func(r,d,x):
    return r*x - d


r, d, x = map(int,input().split())

num = 0
while num!=10:
    if num == 0:
        ans = func(r,d,x)
    else:
        ans = func(r,d,ans)

    print(ans)
    num += 1