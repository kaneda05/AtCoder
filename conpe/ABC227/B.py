n = int(input())
S = list(map(int,input().split()))

ans = 0
for s in S:
    flag = False
    for a in range(1,1001):
        for b in range(1,1001):
            if 4*a*b+3*a+3*b==s:
                flag = True

    if flag==False:
      ans += 1
print(ans)