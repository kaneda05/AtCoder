A = int(input())
B = int(input())
C = int(input())
L = []
L.append(A)
L.append(B)
L.append(C)
L.sort(reverse=True)

print(L.index(A)+1)
print(L.index(B)+1)
print(L.index(C)+1)