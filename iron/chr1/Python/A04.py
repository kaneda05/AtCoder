N = int(input())
ans =""
while 0 < N:
    ans = str(N%2) + ans
    N //= 2

if len(ans)<10:
    for i in range(10-len(ans)):
        ans = "0" + ans

print("".join(ans))