N,X = map(int,input().split())
A = list(map(int,input().split()))

def binary_search(A,N,X):
    left = 0
    right = N
    while left!=right:
        mid = (left+right)//2
        if A[mid]<X:
            left = mid
        if X<A[mid]:
            right = mid
        if X==A[mid]:
            return mid


print(binary_search(A,N,X)+1)