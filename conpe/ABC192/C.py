def g1(n):
    return int(''.join(sorted(str(n)))[::-1])

def g2(n):
    return int(''.join(sorted(str(n))))

def func(n):
    return g1(n) - g2(n)


n, k = map(int,input().split())

for i in range(k):
    n = func(n)

print(n)