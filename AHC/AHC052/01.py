import sys
from collections import deque

# 標準入力を高速化するためのおまじない
input = sys.stdin.readline

def main():
    # --- 初期入力 ---
    N, ti, tj = map(int, input().split())
    # (ti, tj) はゴール地点
    goal_pos = (ti, tj)
    
    # マップ情報をリストのリストとして保持
    grid = [list(input().strip()) for _ in range(N)]
    
    # 確認済みマスを管理する2次元配列
    revealed = [[False] * N for _ in range(N)]
    
    # 上下左右への移動方向
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] # U, D, L, R

    # --- メインループ ---
    turn = 0
    while True:
        turn += 1
        
        # --- 冒険者の現在位置と新規確認マス情報の入力 ---
        line = input().split()
        if not line: break # 入力がなくなったら終了
        
        pi, pj = int(line[0]), int(line[1])
        current_pos = (pi, pj)
        
        # ゴールに到着したらループを抜ける
        if current_pos == goal_pos:
            break
            
        line = input().split()
        n = int(line[0])
        if n > 0:
            newly_revealed = list(map(int, line[1:]))
            for k in range(n):
                r, c = newly_revealed[2 * k], newly_revealed[2 * k + 1]
                revealed[r][c] = True

        # --- 戦略の実行 ---
        
        # 1. 現状のマップで、現在地からゴールへの最短経路を見つける
        q = deque([(current_pos, [current_pos])])
        visited_path = {current_pos}
        shortest_path = []

        while q:
            (r, c), path = q.popleft()
            if (r, c) == goal_pos:
                shortest_path = path
                break
            
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == '.' and (nr, nc) not in visited_path:
                    visited_path.add((nr, nc))
                    new_path = path + [(nr, nc)]
                    q.append(((nr, nc), new_path))
        
        # 2. 最短経路の周囲にある、木を置ける候補地をリストアップ
        candidates = set()
        if shortest_path:
            for r, c in shortest_path:
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    # 範囲内で、未確認の空きマスが候補
                    if 0 <= nr < N and 0 <= nc < N and not revealed[nr][nc] and grid[nr][nc] == '.':
                        candidates.add((nr, nc))

        # 3. 候補地に木を置いても、スタートからゴールへの道が残るか安全確認
        trees_to_place = []
        for r, c in candidates:
            # 候補地に一時的に木を置いてみる
            grid[r][c] = 'T'
            
            # BFSでスタートからゴールへの到達可能性をチェック
            q_check = deque([(0, N // 2)])
            visited_check = {(0, N // 2)}
            is_connected = False
            while q_check:
                curr_r, curr_c = q_check.popleft()
                if (curr_r, curr_c) == goal_pos:
                    is_connected = True
                    break
                
                for dr, dc in moves:
                    nr, nc = curr_r + dr, curr_c + dc
                    if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == '.' and (nr, nc) not in visited_check:
                        visited_check.add((nr, nc))
                        q_check.append((nr, nc))
            
            if is_connected:
                # 連結性が保たれるなら、この木は配置決定
                trees_to_place.append((r, c))
            else:
                # 連結性が失われるなら、木を置くのを取りやめる（元に戻す）
                grid[r][c] = '.'

        # 4. 配置する木を出力
        output = [str(len(trees_to_place))]
        for r, c in trees_to_place:
            output.append(str(r))
            output.append(str(c))
            
        print(" ".join(output), flush=True)

if __name__ == "__main__":
    main()