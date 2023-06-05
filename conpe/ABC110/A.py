l = list(map(int,input().split()))

l.sort()

a = str(l[2])
b = str(l[1])
c = l[0]
ab = a+b
print(int(ab)+c)

