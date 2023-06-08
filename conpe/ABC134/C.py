n = int(input())
a = [int(input()) for _ in range(n)]

left = [0]*(n+1)
right = [0]*(n+1)

for i in range(n):
    left[i+1] = max(left[i],a[i])
    right[i+1] = max(right[i],a[n-i-1])

#print(left)
#print(right)

for i in range(n):
    print(max(left[i],right[n-i-1]))