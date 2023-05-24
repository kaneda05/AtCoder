S = input()
N = int(input())
for i in range(N):
    l,r = map(int,input().split())
    c = S[l-1:r]
    c = c[::-1]
    S = S[:l-1]+c+S[r:]

print(S)