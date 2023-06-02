n = int(input())
t_t = 0
x_t = 0
y_t = 0
flag = True
for _ in range(n):
    t,x,y = map(int,input().split())
    d = abs(x-x_t)+abs(y-y_t)
    time = t-t_t

    t_t = t
    x_t = x
    y_t = y

    if time < d:
        flag = False
    elif time %2 != d%2:
        flag = False

print("Yes" if flag==True else "No")
