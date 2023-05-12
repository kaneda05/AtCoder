#　しゃくとり法で２重ループを拒否していいく
#  ２重ループでは計算量が増えてしまうやつをどうにかNの2乗にならないようにするものの一種
# 　
# 　例題
#   いくつか連続した区間を選ぶ時、10メートル以下でできる連続区間で
#   一番多くの区間を含められるのはいくつか

L = list(map(int,input().split()))  # 長さNの連続した区間
X = int(input())                    # 区間

N = len(L)
# 右側の人の位置,答え,メジャーの巻き出している長さを0で定義
right, ans, measure = 0, 0, 0

# 左の人の位置を全探索する形でループ文を記述
for left in range(N):

    print("left詰める","1:r",left,right,"m",measure)

    # 進めるところまでは右側を進めることを定義
    # 条件1:　右側の人の位置がゴールに辿り着いていたら進まない
    # 条件2:　残りメジャーの長さが次の区間の長さに足りなければ左の人を呼ぶ
    while right < N and measure+L[right] <= X:
        measure += L[right]
        right += 1
        print("rightのびる","1:r",left,right,"m",measure)
    ans = max(ans, right-left)

    #右の人が左の人に追いついてしまった時の処理
    if left == right:
        right += 1 # 右の人はメジャーを出さずに区間を越えるので左の人もそのまま何もせず移動
        continue
    measure -= L[left] # 追いつかれずに左の人が積めるときは巻尺を巻く

print(ans)