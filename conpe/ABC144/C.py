n = int(input())
cal = []
for i in range(1,10**6+1):
    if n%i==0:
        cal.append([i,n//i])


ans = 10**12
for i in range(len(cal)):
    if (cal[i][0]-1)+(cal[i][1]-1)<ans:
        ans = (cal[i][0]-1)+(cal[i][1]-1)
print(ans)
