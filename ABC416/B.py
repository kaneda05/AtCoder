S = input()
T = ['.'] * len(S)

i = 0
while i < len(S):
    if S[i] == '#':
        T[i] = '#'
        i += 1
    else:
        T[i] = 'o'
        while i < len(S) and S[i] == '.':
            i += 1

print(''.join(T))
