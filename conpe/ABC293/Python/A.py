S = list(input())

ans = ""
for i in range(len(S)//2):
    S1 = S[2*i]
    S2 = S[2*i+1]
    ans += S2+S1
print(ans)