S = input()

for i in reversed(range(len(S))):
    if S[i] == "Z":
        ans_z = i+1
        break

ans_a = S.index("A")

print(ans_z-ans_a)

#print(S[ans_a:ans_z])