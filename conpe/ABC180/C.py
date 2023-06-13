import math
n = int(input())
ans = set()
for i in range(1, int(math.sqrt(n)+1)):
    if n%i==0:
        ans.add(i)
        ans.add(n//i)
L = []
for i in ans:
    L.append(i)
    
L.sort()
for i in L:
    print(i)

