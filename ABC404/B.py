def check(list_s, list_t):
    res = 0
    for s_i, t_i in zip(list_s, list_t):
        for s_ij, t_ij in zip(s_i, t_i):
            if s_ij != t_ij:
                res += 1
    return res


def rotation(s):
    return list(zip(*s[::-1]))

N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]

ans = check(S, T)
S = rotation(S)
ans = min(ans, check(S, T) + 1)

S = rotation(S)
ans = min(ans, check(S, T) + 2)

S = rotation(S)
ans = min(ans, check(S, T) + 3)

print(ans)