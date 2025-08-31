N = int(input())
S = input().strip()

pos = [i for i, ch in enumerate(S) if ch == "A"]

target1 = [2*i for i in range(N)]
ans1 = sum(abs(p - t) for p, t in zip(pos, target1))

target2 = [2*i+1 for i in range(N)]
ans2 = sum(abs(p - t) for p, t in zip(pos, target2))

print(min(ans1, ans2))