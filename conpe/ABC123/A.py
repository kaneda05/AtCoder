A = [int(input()) for i in range(5)]
k = int(input())

if A[4] - A[0] > k:
    print(":(")
else:
    print("Yay!")