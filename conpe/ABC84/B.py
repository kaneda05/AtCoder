a,b = map(int,input().split())
s = input()
num_list = [str(i) for i in range(10)]
s1 = s[:a]
s2 = s[a+1:]

if "-" not in s:
    print("No")
    exit()

if len(s)!=a+b+1:
    print("No")
    exit()

for i in s1:
    if str(i) not in num_list:
        print("No")
        exit()

for i in s2:
    if str(i) not in num_list:
        print("No")
        exit()

print("Yes")