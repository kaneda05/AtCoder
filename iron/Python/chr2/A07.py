D = int(input())
N = int(input())
C = [0]*(D+2) # RがD日目の場合を考えて
for i in range(N):
    L,R = map(int,input().split())
    C[L]+=1
    C[R+1]-=1


for i in range(1,D+1):
    C[i]+=C[i-1]

for i in range(1,D+1):
    print(C[i])
