l = list(map(int,input().split()))
flag1 = False
flag2 = False
for i in range(1,14):
    if l.count(i)==3:
        flag1 = True
    if l.count(i)==2:
        flag2 = True

if flag1 and flag2: print("Yes")
else: print("No")
