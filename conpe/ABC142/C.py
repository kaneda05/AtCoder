n = int(input())
a = list(map(int,input().split()))

x = [0]*n

for i in range(n):
    x[a[i]-1] = i + 1

print(" ".join(map(str,x)))