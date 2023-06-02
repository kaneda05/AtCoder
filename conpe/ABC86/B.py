a,b = input().split()
s = a+b
n = int(s)
if any(i**2 == n for i in range(n//2)):
    print("Yes")
else:
    print("No")