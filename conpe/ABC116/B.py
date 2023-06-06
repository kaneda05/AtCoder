def func(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1

s = int(input())
L = [s]
i = 1
while True:
    if L.count(L[-1])==2:
        break
    else:
        L.append(func(L[-1]))
        i += 1

#print(L)
print(i)