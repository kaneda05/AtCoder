n = int(input())
l = list(map(int,input().split()))
max_l = max(l)
if max_l<sum(l)-max_l:
    print("Yes")
else:
    print("No")