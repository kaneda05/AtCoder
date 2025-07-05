N = int(input())
A = list(map(int,input().split()))
flag = False
for i in range(N-2):
  if A[i] == A[i+1] == A[i+2]:
    flag = True
print("Yes" if flag else "No")