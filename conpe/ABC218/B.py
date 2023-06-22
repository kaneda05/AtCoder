p = list(map(int,input().split()))
ans = []
alhpbet = [chr(i) for i in range(ord("a"),ord("z")+1)]


for i in range(len(p)):
    ans.append(alhpbet[p[i]-1])
print("".join(ans))