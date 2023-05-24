S = input()
T = input()
li = ["a","t","c","o","d","e","r"]
for i in range(len(S)):
    if S[i]!=T[i]:

        if S[i] == "@" and T[i] == "@":
            continue

        elif S[i] == "@":
            if T[i] in li:
                continue
            else:
                print("You will lose")
                exit()

        elif T[i] == "@":
            if S[i] in li:
                continue
            else:
                print("You will lose")
                exit()

        else:
            print("You will lose")
            exit()


print("You can win")