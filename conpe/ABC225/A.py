# 順列全探索
import itertools
s = input()
set_s = set()
permutations = itertools.permutations(s)
for permutation in permutations:
    set_s.add("".join(permutation))

print(len(set_s))