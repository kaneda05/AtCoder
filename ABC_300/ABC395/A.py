N = int(input())
A = list(map(int,input().split()))
flag = True
for i in range(N-1):
  if A[i] < A[i+1]:
    continue
  else:
    flag = False
    
print("Yes" if flag else "No")