a,b = input().split()
ansa = 0
ansb = 0
for i in a:
    ansa += int(i)

for i in b:
    ansb += int(i)

print(max(ansa,ansb))
