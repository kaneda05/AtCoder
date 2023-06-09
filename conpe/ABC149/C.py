def is_prime(i):
    if i<=1:
        return False
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            return False
    return True

x = int(input())

for i in range(x,10**7):
    if is_prime(i)==True:
        print(i)
        exit()