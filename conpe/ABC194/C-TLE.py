n = int(input())
a = list(map(int,input().split()))

c = [0] * 401
for i in a:
    c[i] += 1

ans = 0
for i in range(-200,201):
    for j in range(i+1,201):
        ans += (i-j)**2 * c[i] * c[j]
        
print(ans)