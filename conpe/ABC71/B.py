s = input()
alphabet = []
for i in range(ord("a"),ord("z")+1):
    alphabet.append(chr(i))

for i in range(len(alphabet)):
    if alphabet[i] not in s:
        print(alphabet[i])
        exit()

print("None")