S = input().strip()

for c in 'abcdefghijklmnopqrstuvwxyz':
    if c not in S:
        print(c)
        break
