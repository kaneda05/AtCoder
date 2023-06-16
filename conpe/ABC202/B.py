s = list(input())
for i in range(len(s)):
    if s[i] == "6":
        s[i] = "9"
    elif s[i] == "9":
        s[i] = "6"

print("".join(s[::-1]))