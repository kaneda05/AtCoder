# 入力の受け取り
N,A,B = map(int,input().split())
S = input()

# A文字取り除き、末尾B文字も取り除く
result = S[A:N-B]

# 出力
print(result)
