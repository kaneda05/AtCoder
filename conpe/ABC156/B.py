n,k = map(int,input().split())

def base_n(num_10,n):
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return str(str_n[::-1])

ans = base_n(n,k)
#print(ans)
print(len(ans))