s1 = input()
s2 = input()
s3 = input()
L = ["ABC","ARC","AGC","AHC"]
S = [s1,s2,s3]
for i in range(4):
    if L[i] not in S:
        print(L[i])
        exit()