from re import X


n = int(input())
sq = int(n**0.5)
s = set()
for a in range(2,sq+1):
    x = a*a
    while x <= n:
        s.add(x)
        x*=a
        
print(n-len(s))