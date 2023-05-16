N = int(input())
S = input()
L = []
cnt = S.index("*")

for i in range(N):
    if S[i] == "|":
        L.append(i)

if int(L[0])<cnt<int(L[1]):
    print("in")
else:
    print("out")
