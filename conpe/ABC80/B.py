n = input()
h = 0
for i in n:
    h += int(i)

if int(n)%h==0:
    print("Yes")
else:
    print("No")