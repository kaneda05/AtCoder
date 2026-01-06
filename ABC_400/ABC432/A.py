a,b,c = map(str,input().split())
ans = []
ans.append(a)
ans.append(b)
ans.append(c)
ans.sort(reverse=True)
res = "".join(ans)
print(res)