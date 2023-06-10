h = int(input())

cnt = 1
ans = 0
while 0<h:
    h //= 2
    ans += cnt
    cnt *= 2
    
print(ans)
