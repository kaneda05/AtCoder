N = int(input())
S = "0"+input()

for i in range(1,N):
    l = 0
    for j in range(1,N+1):
        if i+j<=N and S[j]!=S[j+i]:
            l = j
        else:
            print(l)
            break