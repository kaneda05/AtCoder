def bin_2(n):
    p=""
    while n!=0:
        pi = n%2
        p=str(pi*2)+p
        n=n//2
    return p

k = int(input())
print(bin_2(k))