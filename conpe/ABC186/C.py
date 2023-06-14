n = int(input())
def base_n(num_10,n):
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return str(str_n[::-1])

ans = 0
for i in range(1,n+1):
    if "7" not in str(i) and  "7" not in base_n(i,8):
        ans += 1

print(ans)