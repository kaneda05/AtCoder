N, L, R = map(int,input().split())
S = input()
s = S[L-1:R]

for i in range(len(s)):
    if s[i] != "o":
        print("No")
        exit()
print("Yes")