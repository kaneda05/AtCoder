N, M = map(int,input().split())
A = list(map(int,input().split()))

ans = []
stack = []
for i in range(1,N+1):
    if i in A:
        stack.append(i)
    else:
        ans.append(i)
        if 0<len(stack):
            while len(stack)!=0:
                ans.append(stack.pop())
        stack = []
    
print(*ans)