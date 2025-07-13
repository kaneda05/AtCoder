import sys
from collections import deque

def solve():
    N, M = map(int, sys.stdin.readline().split())
    X = list(map(int, sys.stdin.readline().split()))
    X.sort()

    # dp[i][j]: 最初のi個の家をj個の基地局でカバーするときの電波強度の総和の最小値
    # N, M の制約からO(NM)は無理。O(N log X_max)を目指す。

    # cost(k, i) = X[i] - X[k] は、X[k]からX[i]までの範囲をカバーするのに必要な最小電波強度
    # この時、基地局は (X[k] + X[i]) / 2 に配置され、電波強度は X[i] - X[k] となる。
    # 実際は1-indexedのXを0-indexedで扱うため、X[i-1] - X[k] となる。

    # Alien Trick: 各基地局の使用にペナルティ 'C' を課す。
    # dp[i]: 最初の i 個の家をカバーする電波強度の総和の最小値 + (使用した基地局の数) * C
    # count[i]: dp[i] を達成したときの基地局の数

    # check(C) 関数: ペナルティ C のもとでDPを実行し、最小電波強度と使用基地局数を返す
    def check(C):
        dp = [0] * (N + 1)
        count = [0] * (N + 1)
        
        # dequeは(値, インデックス)のペアを格納
        # キューの先頭は最小値を持ち、単調増加を保つ
        from collections import deque
        
        # 0番目の家（仮想的な家）からのスタート
        # dp[0] = 0, count[0] = 0
        # Xを0-indexedにしているので、X[k-1]はk番目の家
        # dp[k-1] + C - X[k] をキューに入れる
        # 初期のキューには、dp[0] + C - X[0] (X[0]は最初の家) を入れる
        # 便宜上、X[0]は考慮しない（最初の家はX[0]とする）
        # X[k] は 0-indexed に変更する
        
        # dp[0] = 0, count[0] = 0 (0個の家をカバーするコストは0, 基地局も0)
        # 実際には dp[i] は i番目までの家をカバーするコスト
        # なので、dp[0] は「どの家もカバーしていない状態」とする
        # count[0] は 0

        # dp[i] = X[i-1] + min(dp[k] - X[k] + C)
        # dp[k] - X[k] + C の最小値をキューで管理する
        
        # dp[i] は i番目の家までをカバーするコスト
        # Xは0-indexedなので、X[i] は (i+1)番目の家の座標
        # 1からNまでの家をカバーするので、dpのサイズはN+1
        # dp[i] は i番目の家 (X[i-1]) までをカバーするコスト
        
        # dp[k] + (X[i-1] - X[k]) + C の最小化
        # = X[i-1] + C + min(dp[k] - X[k])

        q = deque()
        # 最初の仮想的な状態 (0番目の家までカバー済み)
        # dp[0] - X[-1] を考えるが、X[-1]は存在しない
        # 便宜上、dp[0]=0, count[0]=0 とする
        # q には (dp[k] - X[k]の値, k) を入れる

        # X を 0-indexed で扱うため、X[i] は i番目の家の座標
        # dp[i] は i+1 個の家 (X[0]...X[i]) をカバーするコスト
        # count[i] は i+1 個の家をカバーするのに使った基地局の数

        # dp[i] は X[0] から X[i-1] までの家をカバーするコスト
        # count[i] はその時の基地局の数

        for i in range(1, N + 1):
            # i-1番目の家 (X[i-1]) までカバー
            # 新しい基地局でX[j] から X[i-1] までカバーする
            # コストは (X[i-1] - X[j]) + C
            # dp[i] = min_{0 <= j < i} (dp[j] + (X[i-1] - X[j]) + C)
            # dp[j] - X[j] をキューに入れる

            # i-1番目の家を考慮に入れる前のキューの状態を基に、dp[i]を計算
            
            # キューに新しい要素を追加 (dp[i-1] - X[i-1])
            # dp[k-1] は k-1番目の家までカバーしたコスト
            # X[k-1] は k-1番目の家の座標
            # qは (dp[k-1] - X[k-1], k-1) を入れる
            # ここでは X を 0-indexed にしているので
            # dp[k] は X[0] から X[k-1] までの家をカバーするコスト
            # qには (dp[k] - X[k], k) を入れる

            # 新しい要素 (dp[i-1] - X[i-1]) をキューに追加
            # dp[0]を初期値として入れる
            if i == 1:
                q.append((0 - X[0], 0)) # (dp[0] - X[0], 0)
            
            # 単調キューの先頭が現在のiに対して不要な要素を削除
            # この問題では削除の条件は明確ではないが、通常は
            # (dp[k] - X[k]) + X[i-1] + C が最小となる k を探す
            # 探索範囲が i-1 より大きい場合は削除
            
            # キューの先頭が最適解を与える
            while q and q[0][1] < 0: # k < 0 はありえないが、念のため
                q.popleft() # 削除されることはないはず

            # 現在の dp[i] を計算
            # q.popleft() の代わりに q[0] を使う
            val_k, idx_k = q[0]
            dp[i] = val_k + X[i-1] + C
            count[i] = count[idx_k] + 1
            
            # 新しい要素をキューに追加する準備
            new_val = dp[i] - X[i-1] # 次のステップで使われる値 (dp[i] - X[i])

            # キューの末尾から、新しい要素より大きいものを削除 (単調増加を保つため)
            while q and q[-1][0] >= new_val:
                q.pop()
            
            q.append((new_val, i)) # (dp[i] - X[i], i) を追加
            
            # Debugging print
            # print(f"i={i}, dp[{i}]={dp[i]}, count[{i}]={count[i]}, q={q}")
            
        return dp[N], count[N]

    # 二分探索の範囲を設定
    # 最小コストは0 (M=Nで全て同じ位置の場合)
    # 最大コストは N * Max_X (全ての家を個別にカバーし、最も遠いXまで)
    # あるいは、最も端から端までの距離 (X[N-1] - X[0])
    
    # 厳密な上限は (X[N-1] - X[0]) * N だが、通常はX_maxで十分
    low = 0
    high = X[N-1] - X[0] # 最大の電波強度はXの最大差分

    # C の二分探索で使う
    # 最も使う基地局が多いのは M 個なので、M個以上になったらCを増やす
    # 最も使う基地局が少ないのは M 個なので、M個以下になったらCを減らす
    
    ans = -1
    
    # count_M は、最適なCを見つけたときの基地局の数
    # これは M と等しいか、または M に最も近い数になる
    # そのCにおける、電波強度の総和
    
    final_cost = -1
    
    # 二分探索を行う
    # mid はペナルティ C
    
    # 二分探索の回数は log(high - low)
    # 各check(C)は O(N)
    # 合計 O(N log X_max)
    
    # C が実数になる可能性があるので、適切な範囲で十分な回数探索する
    # しかし、問題文に「答えが整数であることが証明できます」とあるので、Cも整数で探索できるはず
    # あるいは、Cが実数でも、整数解が見つかるということ

    # 通常、このタイプの問題では、最適なCが整数とは限らないが、
    # そのCで得られる「コスト - C*基地局数」が最終的な答えになる。
    # しかし、ここでは「電波強度の総和」なので、ペナルティを除去した値が必要。

    # C の探索範囲
    # 最小値は0、最大値は X[N-1] - X[0] (最大の電波強度)
    
    min_C = 0
    max_C = X[N-1] # 実際のXの最大値は10^12なので、これを使うべき
    
    # 適切な初期値と探索範囲
    # 基地局の最小コストは0 (すべて同じ場所)
    # 基地局の最大コストは (X[N-1] - X[0])
    # 適切なCの範囲は [0, X[N-1] - X[0]]
    
    # `low` と `high` はペナルティ `C` の範囲
    low = 0
    high = X[N - 1] # Xの最大値まで考慮
    
    # ans_dp は、M個の基地局を使ったときの最小電波強度
    ans_dp_val = float('inf')
    
    # 二分探索で最適なCを探す
    # 最終的な C が決まったら、そのCで得られる基地局の数が M になるか、Mに近いものを選ぶ
    
    # C の探索は、基地局の数がMになるような C を見つける
    # 基地局の数が多い -> C を増やす (もっと使わせたくない)
    # 基地局の数が少ない -> C を減らす (もっと使わせたい)
    
    while low <= high:
        mid_C = (low + high) // 2
        
        # dp[i]: i番目の家までをカバーする最小コスト
        # prev_dp[k] = dp[k] - X[k]
        
        # (val, idx) -> (dp[idx] - X[idx], idx)
        
        # dp[i] = max(dp[k] + X[i] - X[k+1] + C) # ここは min に修正
        # dp[i] = min(dp[k] + X[i] - X[k+1] + C)
        
        # DPテーブルと使用基地局数テーブル
        # dp[i] = 最初のi個の家をカバーするのに必要な最小電波強度 + cost * num_stations
        # num_stations[i] = その時の基地局の数
        dp_current = [0] * (N + 1)
        num_stations_current = [0] * (N + 1)
        
        # キューには (dp[k] - X[k], k) のペアを格納
        # Xは0-indexedなので、X[k]はk番目の家（0-indexed）の座標
        q = deque()
        q.append((0 - X[0], 0)) # (dp[0] - X[0], 0)
                                 # dp[0]=0 は0個の家をカバーするコスト
        
        for i in range(1, N + 1):
            # qの先頭が現在のiに対して有効な範囲外になったら削除
            # kが i-1 より大きいものは参照できない
            # kが現在の家よりも前にある必要がある
            # ここでは k は q[0][1]
            # X[i-1] は i番目の家の座標 (0-indexed)
            
            # qに入っているのは dp[k] - X[k]
            # 求めたいのは dp[i] = X[i-1] + C + min_{0 <= k < i} (dp[k] - X[k])
            
            while q and q[0][1] >= i: # k >= i はありえない
                q.popleft()

            # ここで q[0][1] は、次に基地局を置くときにカバーを開始する位置 k を示す
            # dp[i] を計算
            # val_k = dp[q[0][1]] - X[q[0][1]]
            val_k, idx_k = q[0] # idx_k は k
            
            # X[i-1] は現在の家の座標
            dp_current[i] = val_k + X[i-1] + mid_C # コスト
            num_stations_current[i] = num_stations_current[idx_k] + 1 # 基地局の数
            
            # 次のステップのためにキューに新しい要素を追加
            # new_val = dp[i] - X[i]
            # X[i] は i+1番目の家の座標
            
            # q に追加する要素は (dp[i] - X[i], i)
            # これは、X[i] までの家をカバーした場合の、次のDP遷移に使う値
            
            if i < N: # 最後の家まで到達するまで追加
                new_val_for_queue = dp_current[i] - X[i]
                while q and q[-1][0] >= new_val_for_queue:
                    q.pop()
                q.append((new_val_for_queue, i))

        stations_used = num_stations_current[N]
        current_total_cost = dp_current[N]

        if stations_used >= M:
            # 基地局をM個以上使った場合、Cを大きくして基地局の使用を抑制する
            low = mid_C + 1
            # ぴったりM個使った場合を記録
            # もし stations_used == M なら、この値が暫定解となる
            # stations_used > M の場合でも、これがM個の場合の最良解かもしれない
            ans_dp_val = min(ans_dp_val, current_total_cost - M * mid_C) # M * mid_C を引いて元の電波強度の総和に戻す
        else:
            # 基地局をM個より少なく使った場合、Cを小さくして基地局の使用を促す
            high = mid_C - 1
            # M個より少ない場合でも、このCで得られる解はM個以上使う場合に比べて効率的ではない
            # しかし、M個に近づけるために記録が必要
            # stations_used <= M の場合、これは有効な候補
            ans_dp_val = min(ans_dp_val, current_total_cost - M * mid_C)
            # これは M 個より少ない場合も含まれるので、
            # 実際には stations_used <= M の場合で ans_dp_val を更新すべき
            # しかし、M個が目標なので、stations_used >= M の場合の方が優先度が高い
            
            # 厳密には、M個以上使った場合の最大コストを記録
            # M個以下使った場合の最小コストを記録、という風に場合分けして
            # 最終的に M 個の候補の中から最適なものを選ぶ
            
            # ここでは `ans_dp_val` を、現在の`mid_C`における「使用基地局数が `M` を超えない範囲での最小コスト」
            # あるいは、「使用基地局数が `M` 以上となる場合の最大コスト（ただし `M` 個の場合も含む）」
            # として更新し続ける。
            # Alien Trick の典型的な実装は、`stations_used >= M` の場合に `ans = current_total_cost - M * mid_C` を更新し、
            # `low = mid_C + 1` とする。
            # `stations_used < M` の場合に `high = mid_C - 1` とする。
            # そうすることで、`low` が最終的に最適な `C` になる。

    # 最終的な answer は、最適な C を用いて求めた dp[N] - M * C
    # 二分探索が終了した時点での low または high が最適 C
    # 通常、low が最適な C を指す
    
    # 最後の check(low-1) または check(high+1) を実行して正しい値を求める
    # ここでは、二分探索中に最適な ans_dp_val を見つけておくのが楽
    
    # 最後の調整
    # low は C の最適な値を指しているはず
    # しかし、ぴったり M 個になる C が存在しない場合もある
    
    # 以下の方法は、二分探索で low, high の範囲を絞り込み、
    # 最終的にその範囲内で M 個の基地局を使用する最適な解を見つける
    # 通常は、lower_bound的な二分探索で、M個以上になる最小のCを求める
    # その後、そのCとC-1での結果を比較する
    
    # ここでは、stations_used >= M の場合に ans_dp_val を更新することで
    # M個以上の場合の最小コストを記録している。
    
    # 最適なCが見つからない場合は、M個に一番近いものを選ぶ
    # 最終的なコストは、check(C)で計算されたdp[N]からM*Cを引いたもの

    # 解決策: Cの範囲で二分探索を行い、M個の基地局が使われるようなCを探す。
    # check(C)の結果が (total_cost, num_stations) となる。
    # num_stations が M より大きい場合: C を大きくする (low = mid_C + 1)
    # num_stations が M より小さい場合: C を小さくする (high = mid_C - 1)
    # num_stations が M と等しい場合: mid_C は候補となる。この時の total_cost - M*mid_C が答えの候補。
    # また、M個ぴったりのCが複数ある可能性や、存在しない可能性もある。
    
    # 最も単純な方法は、stations_used >= M の場合に ans_dp_val を更新する
    # これは、M個以上使う場合に得られる最小コストを記録する
    # M個より少ない場合は、Cを小さくして、M個使う方向に向かう
    
    # `ans_val` は M個の基地局を使う場合に得られる最適なコスト
    
    # `low` が最終的に最適な C の値を保持する (M個以上を使う最小のC)
    # `high` は M個未満を使う最大のC
    
    # `low_c_cost`, `low_c_stations` は `low` での `check` 結果
    # `high_c_cost`, `high_c_stations` は `high` での `check` 結果

    # 再度、check(low) を呼び出し、その結果を最終的な答えとする
    # low は M個以上の基地局を使う最小のC
    
    # dp_final, num_stations_final = check(low)
    # final_answer = dp_final - M * low
    
    # Alien Trick の実装では、二分探索の最終的な `low` (または `high`) で
    # `check` をもう一度呼び出し、その結果が実際の最適な解となる
    
    # `stations_used >= M` の場合に `ans_dp_val` を更新し、`low = mid_C + 1`
    # `stations_used < M` の場合に `high = mid_C - 1`
    
    # この二分探索が終わると、`high` は `M` 個未満を返す最大の `C`、
    # `low` は `M` 個以上を返す最小の `C` となる。
    # 最終的な答えは、`high` と `low` のどちらか、
    # または両方での `check` 結果を使って計算する必要がある。
    
    # `lower_bound` のように、`num_stations >= M` となる最小の `C` を探す
    # `stations_used` が `M` 以上なら `res = current_total_cost - M * mid_C`, `high = mid_C - 1`
    # `stations_used` が `M` 未満なら `low = mid_C + 1`
    
    # これにより `low` は `num_stations >= M` となる最小の `C` になる
    
    ans = -1
    
    # Check with low and low-1 (if low > 0)
    # to find the exact M stations case
    
    # Final step of Alien Trick:
    # Run DP with the 'low' value of C found by binary search
    # This 'low' value of C gives a solution where `num_stations >= M`
    dp_at_low_c, num_stations_at_low_c = check(low)
    
    # The cost with exactly M stations is `dp_at_low_c - (num_stations_at_low_c - M) * low - M * low`
    # = `dp_at_low_c - num_stations_at_low_c * low + M * low - M * low`
    # = `dp_at_low_c - num_stations_at_low_c * low` + (num_stations_at_low_c - M) * low + M * low`
    # This is slightly tricky. The correct way is:
    # `ans = (dp_at_low_c - M * low)`.
    # This represents the cost of using exactly M stations,
    # where the last (num_stations_at_low_c - M) stations
    # are "free" (they don't incur the penalty `low`).
    
    # The actual final cost for M stations:
    # This value has to be calculated based on the fact that we found `low`
    # such that `num_stations_at_low_c` is the smallest number of stations
    # that we get for a penalty `C >= low`.
    # The optimal cost for M stations is `dp_at_low_c - num_stations_at_low_c * low`.
    # Then, we need to add `M * low` to it, but only for the actual M stations.
    # The true sum of strengths is `dp_at_low_c - (num_stations_at_low_c - M) * low_penalty - M * low_penalty` is wrong
    # Correct is `dp_at_low_c - num_stations_at_low_c * low + M * low`.
    # This is `original_sum_of_strengths + num_stations_at_low_c * low - num_stations_at_low_c * low + M * low`
    # = `original_sum_of_strengths + M * low`
    # So `original_sum_of_strengths = dp_at_low_c - M * low`
    
    # If the exact M stations are not achieved,
    # we might need to adjust the cost.
    # But given the problem statement, the answer is always an integer.
    # This suggests that a precise C can be found or the adjustment is simple.
    
    # A common strategy is to select the largest C such that the number of stations used is >= M.
    # And then to make sure the answer is correct for exactly M stations.
    
    # Correct calculation of `ans` based on Alien Trick:
    # Find `dp_val` and `num_stations` for `C = low` (which is `dp_at_low_c`, `num_stations_at_low_c`)
    # Find `dp_val_prev`, `num_stations_prev` for `C = low - 1` (if `low > 0`)
    # The answer is `dp_at_low_c - num_stations_at_low_c * low + M * low`
    # This is the "true" minimum sum of strengths.

    # This logic seems correct for Alien Trick to recover the original cost.
    print(dp_at_low_c - num_stations_at_low_c * low + M * low)

solve()