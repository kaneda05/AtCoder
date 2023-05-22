A, B, C, K = map(int,input().split())
S, T = map(int,input().split())
sumc = A*S + B*T
if S+T<K:
    print(sumc)
else:
    print(sumc-C*(S+T))