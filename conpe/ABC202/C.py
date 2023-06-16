n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))


cnti = [0]*(n+1)
for i in a:
    cnti[i] += 1

cntj = [0]*(n+1)
for j in c:
    cntj[b[j-1]]+=1

ans = 0
for i in range(n+1):
    ans += cnti[i]*cntj[i]

#print(cnti)
#print(cntj)

print(ans)