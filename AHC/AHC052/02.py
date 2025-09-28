import sys
from collections import deque

# --- 定数 ---
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 上, 下, 左, 右

# --- ヘルパー関数群 (変更なし) ---
def bfs_find_shortest_path(grid, n, start_pos, goal_pos):
    q = deque([(start_pos, [start_pos])])
    visited = {start_pos}
    while q:
        (r, c), path = q.popleft()
        if (r, c) == goal_pos: return path
        for dr, dc in MOVES:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == '.' and (nr, nc) not in visited:
                visited.add((nr, nc)); q.append(((nr, nc), path + [(nr, nc)]))
    return []

def is_connected(grid, n, start_pos, goal_pos):
    if start_pos == goal_pos: return True
    q = deque([start_pos]); visited = {start_pos}
    while q:
        r, c = q.popleft()
        for dr, dc in MOVES:
            nr, nc = r + dr, c + dc
            if (nr, nc) == goal_pos: return True
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == '.' and (nr, nc) not in visited:
                visited.add((nr, nc)); q.append((nr, nc))
    return False

def solve():
    """
    ゲーム全体を管理し、戦略を実行するメイン関数。
    シンプルな単一ループ構造に戻し、その中に戦略分岐を組み込む。
    """
    # --- 初期入力 ---
    N, ti, tj = map(int, input().split())
    start_node, goal_node = (0, N // 2), (ti, tj)
    grid = [list(input().strip()) for _ in range(N)]
    revealed = [[False] * N for _ in range(N)]

    # --- メインループ ---
    while True:
        parts = input().split();
        if not parts: break
        
        pi, pj = int(parts[0]), int(parts[1]); current_pos = (pi, pj)
        if current_pos == goal_node: break
            
        parts = input().split(); n_revealed = int(parts[0])
        if n_revealed > 0:
            xy = list(map(int, parts[1:]))
            for k in range(n_revealed):
                r, c = xy[2 * k], xy[2 * k + 1]; revealed[r][c] = True

        # === 【頭脳】戦略決定ロジック ===
        trees_to_place = []
        
        # --- 攻撃戦略（目的地誘導）を試行 ---
        unrevealed_empty = [(r, c) for r in range(N) for c in range(N) if not revealed[r][c] and grid[r][c] == '.']
        
        best_bait, max_dist = None, -1
        if unrevealed_empty:
            for r, c in unrevealed_empty:
                dist = abs(r - goal_node[0]) + abs(c - goal_node[1])
                if dist > max_dist:
                    max_dist = dist; best_bait = (r, c)
        
        # 質の高いおとりが見つかった場合、攻撃戦略を実行
        # 条件式 `max_dist > N / 2.5` などは調整の余地あり
        if best_bait and max_dist > N / 3:
            candidates = {pos for pos in unrevealed_empty if pos != best_bait}
            temp_trees = []
            for r_c in candidates:
                grid[r_c[0]][r_c[1]] = 'T'
                if is_connected(grid, N, start_node, goal_node):
                    temp_trees.append(r_c)
                else:
                    grid[r_c[0]][r_c[1]] = '.' # 戻す
            trees_to_place = temp_trees
        
        # --- 防御戦略（最短経路妨害）にフォールバック ---
        else:
            shortest_path = bfs_find_shortest_path(grid, N, current_pos, goal_node)
            candidates = set()
            if shortest_path:
                for r, c in shortest_path:
                    for dr, dc in MOVES:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N and not revealed[nr][nc] and grid[nr][nc] == '.':
                            candidates.add((nr, nc))
            
            temp_trees = []
            for r_c in candidates:
                grid[r_c[0]][r_c[1]] = 'T'
                if is_connected(grid, N, start_node, goal_node):
                    temp_trees.append(r_c)
                else:
                    grid[r_c[0]][r_c[1]] = '.' # 戻す
            trees_to_place = temp_trees
        
        # 決定した行動を出力
        output_parts = [str(len(trees_to_place))]
        for r, c in trees_to_place:
            output_parts.extend([str(r), str(c)])
        print(" ".join(output_parts), flush=True)

if __name__ == "__main__":
    solve()