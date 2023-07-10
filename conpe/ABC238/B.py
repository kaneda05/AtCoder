n = int(input())
A = list(map(int,input().split()))
B = [0]
for a in A:
    B.append((B[-1] + a) % 360)
B.append(360)
B = sorted(B)

ans = float('-inf')
for i in range(len(B)-1):
    res = B[i+1] - B[i]
    ans = max(res, ans)
print(ans)