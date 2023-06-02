""" 
各桁の合計値を計算
"""
def digitSum(n):
    # 数値を文字列に変換
    s = str(n)
    # １文字ずつ数値化し配列にする。
    array = list(map(int, s))
    # 合計値を返す
    return sum(array)

n,a,b = map(int,input().split())
ans = 0
for i in range(1,n+1):
    if a<=digitSum(i)<=b:
        ans += i
print(ans)