s1 = input()
s2 = input()
s3 = input()
t = list(map(int,input()))
n = len(t)
S = [s1,s2,s3]

ans = []
for i in range(n):
    ans.append(S[t[i]-1])
print("".join(ans))