import sys
input = sys.stdin.readline
h, w = map(int, input().strip().split())
board = [input().strip() for _ in range(h)]
max_move = 1
q = set([(0, 0, board[0][0])])
while q:
    y, x, visited = q.pop()
    for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < h and 0 <= nx < w and board[ny][nx] not in visited:
            max_move = max(max_move, len(visited)+1)
            q.add((ny, nx, visited+board[ny][nx]))

print(max_move)