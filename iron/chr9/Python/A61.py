N,M=map(int,input().split())
G=[[] for _ in range(N+1)]
 
for _ in range(M):
    A,B=map(int,input().split())
    G[A].append(B)
    G[B].append(A)
 
for i in range(1,N+1):
    print(str(i)+': {'+','.join(map(str,G[i]))+'}')