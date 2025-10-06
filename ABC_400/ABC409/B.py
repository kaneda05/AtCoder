def max_x(A):
    N = len(A)
    
    def check(x):
        # x 以上の要素の個数を数える
        cnt = sum(1 for a in A if a >= x)
        return cnt >= x

    left, right = 0, N + 1
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid):
            left = mid
        else:
            right = mid
    return left

N = int(input())
A = list(map(int,input().split()))
print(max_x(A))
