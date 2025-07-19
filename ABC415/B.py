S = input()
ans = []
for i in range(len(S)):
    if S[i] == "#":
        ans.append(i+1)

m = len(ans)
for i in range(0,m,2):
    print(str(ans[i])+","+str(ans[i+1]))
