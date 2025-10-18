import sys
input = sys.stdin.readline

def good_x(C, D):
    ans = 0
    for k in range(1, 11):  # 桁数1〜10
        mod = 10 ** k
        start = int((C * mod) ** 0.5)
        for n in range(start, start + 3):  # 近傍のみ確認
            val = n * n - C * mod
            x = val - C
            if 1 <= x <= D:
                # 桁数チェック（C+x の桁が k であること）
                if len(str(C + x)) == k:
                    ans += 1
    return ans

T = int(input())
for _ in range(T):
    C, D = map(int, input().split())
    print(good_x(C, D))
