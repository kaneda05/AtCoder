N = int(input())
S = list(input())
flag = True
for i in range(N):
    if flag == True and S[i] == ",":
        S[i] = "."
    
    if S[i] == '"':
        flag = not flag

print("".join(S))