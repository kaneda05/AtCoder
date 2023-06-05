n = input()
s = int(n)
N = 0
for i in n:
    N += int(i)
if s%N==0:
    print("Yes")
else:
    print("No")