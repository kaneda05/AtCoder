c1 = list(input())
c2 = list(input())
L1 = []
L1.append(c1)
L1.append(c2)

L2 = []
L2.append(c2[::-1])
L2.append(c1[::-1])


print("YES" if L1==L2 else "NO")