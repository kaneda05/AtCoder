def check(x, N, K, A):
    sum = 0
    for i in range(N):
        sum += x // A[i]
    if K<=sum:
        return True
    else:
        return False

N, K = map(int,input().split())
A = list(map(int,input().split()))

left = 1
right = 10**9
while left<right:
    mid = (left+right)//2
    ans = check(mid, N, K, A)

    if ans == True:
        right = mid # 答えはmid以下

    if ans == False:
        left = mid + 1 # 答えはmid+1以上

print(left)