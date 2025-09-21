import sys
from collections import deque

# --- 定数 ---
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 上, 下, 左, 右

# --- ヘルパー関数群 (ステップ1, 2と同じ) ---
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

# --- 戦略実行関数 ---
def execute_bait_strategy(grid, n, revealed, start_node, goal_node):
    """【攻撃戦略】目的地誘導を実行する"""
    unrevealed_empty = [(r, c) for r in range(n) for c in range(n) if not revealed[r][c] and grid[r][c] == '.']
    
    best_bait, max_dist = None, -1
    if not unrevealed_empty: return None

    for r, c in unrevealed_empty:
        dist = abs(r - goal_node[0]) + abs(c - goal_node[1])
        if dist > max_dist:
            max_dist = dist; best_bait = (r, c)
            
    # 【意思決定】質の高いおとりが存在するか？ (ゴールからN/3マス以上離れているか)
    if best_bait and max_dist > n / 3:
        candidates = {pos for pos in unrevealed_empty if pos != best_bait}
        trees_to_place = []
        for r_c in candidates:
            grid[r_c[0]][r_c[1]] = 'T'
            if is_connected(grid, n, start_node, goal_node):
                trees_to_place.append(r_c)
            else:
                grid[r_c[0]][r_c[1]] = '.'
        return trees_to_place
    return None # 質の高いおとりが見つからなければNoneを返す

def execute_obstruction_strategy(grid, n, revealed, current_pos, start_node, goal_node):
    """【防御戦略】最短経路妨害を実行する"""
    shortest_path = bfs_find_shortest_path(grid, n, current_pos, goal_node)
    candidates = set()
    if shortest_path:
        for r, c in shortest_path:
            for dr, dc in MOVES:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not revealed[nr][nc] and grid[nr][nc] == '.':
                    candidates.add((nr, nc))
    
    trees_to_place = []
    for r_c in candidates:
        grid[r_c[0]][r_c[1]] = 'T'
        if is_connected(grid, n, start_node, goal_node):
            trees_to_place.append(r_c)
        else:
            grid[r_c[0]][r_c[1]] = '.'
    return trees_to_place

def solve():
    """ゲーム全体を管理し、戦略を決定・実行するメイン関数。"""
    N, ti, tj = map(int, input().split())
    start_node, goal_node = (0, N // 2), (ti, tj)
    grid = [list(input().strip()) for _ in range(N)]
    revealed = [[False] * N for _ in range(N)]

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

        # === 【頭脳】戦略決定 ===
        # まず攻撃戦略を試みる
        trees_to_place = execute_bait_strategy(grid, N, revealed, start_node, goal_node)
        
        # 攻撃戦略が有効でなかった場合（Noneが返された場合）、防御戦略に切り替える
        if trees_to_place is None:
            trees_to_place = execute_obstruction_strategy(grid, N, revealed, current_pos, start_node, goal_node)
        
        # 決定した行動を出力
        output_parts = [str(len(trees_to_place))]
        for r, c in trees_to_place:
            output_parts.extend([str(r), str(c)])
        print(" ".join(output_parts), flush=True)

if __name__ == "__main__":
    solve()