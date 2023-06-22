k = int(input())
a,b = input().split()
n = len(a)
m = len(b)
ans1 = 0
for i in range(n):
    ans1 += (k**(n-i-1))*int(a[i])
#print(ans1)

ans2 = 0
for i in range(m):
    ans2 += (k**(m-i-1))*int(b[i])
#print(ans2)

ans = ans1*ans2
print(ans)