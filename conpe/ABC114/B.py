S = input()

ans = 10**5
for i in range(len(S)-2):
    s = S[i:i+3]
    #print(s)
    if abs(int(s)-753) < ans:
        ans = abs(int(s)-753)
print(ans)
    