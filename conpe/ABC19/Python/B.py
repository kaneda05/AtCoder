S = input()
cnt_num = 0
cnt_char = S[0]
ans = []
for i in range(len(S)):
    if cnt_char == S[i]:
        cnt_num += 1
    else:
        ans.append(cnt_char)
        ans.append(str(cnt_num))
        cnt_char = S[i]
        cnt_num = 1

ans.append(cnt_char)
ans.append(str(cnt_num))

print("".join(ans))
