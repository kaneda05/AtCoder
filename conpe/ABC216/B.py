n = int(input())
set_list = set()

for i in range(n):
    set_list.add(input())

m = len(set_list)
if m==n: print("No")
else: print("Yes")