n = int(input())
a = list(map(int,input().split()))
left = a[:(2**n)//2]
right = a[(2**n)//2:]

max1 = max(left)
max2 = max(right)

if max1<max2:
    print(a.index(max1)+1)
else:
    print(a.index(max2)+1)
