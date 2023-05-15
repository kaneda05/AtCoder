A = input()
N = len(A)
if 2<=N:
    print("".join(A[0:-1]))
elif A == "a":
    print(-1)
else:
    print(chr(ord(A[0])-1))