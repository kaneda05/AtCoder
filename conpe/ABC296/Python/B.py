S = [list(input()) for _ in range(8)]
alphabet = ["a","b","c","d","e","f","g","h"]

ans = ""
for i in range(8):
    for j in range(8):
        if S[i][j] == "*":
            ans += alphabet[j] + str(8-i)
            print(ans)
            exit()
