S = input()
N = len(S)
ans = S[0].upper() + S[1:N].lower()
print("".join(ans))

# capitalize()を使えばこの問題は一瞬だった
# print(S.capitalize())