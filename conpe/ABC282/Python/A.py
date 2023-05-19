l = []
for i in range(ord("A"),ord("Z")+1):
    l.append(chr(i))

K = int(input())
print("".join(l[:K]))