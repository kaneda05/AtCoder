S = input()
a, b = S.split("-")
a = int(a)
b = int(b)
if b == 8:
    a += 1
    b = 1
else:
    b += 1
print(str(a)+"-"+str(b))