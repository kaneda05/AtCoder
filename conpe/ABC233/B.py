l, r = map(int,input().split())
s = input()
ans = s[:l-1] + s[l-1:r][::-1] + s[r:]
print(ans)