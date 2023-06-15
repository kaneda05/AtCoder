n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
maxa = max(a)
minb = min(b)
if minb-maxa+1 < 0:
    print(0)
else:
    print(minb-maxa+1)