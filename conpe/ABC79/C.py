import itertools

S = input()
for X in itertools.product(("+", "-"), repeat=3):
    T = S[0]
    for i in range(3):
        T += X[i]
        T += S[i+1]
    if eval(T) == 7:
        print(T + "=7")
        exit()