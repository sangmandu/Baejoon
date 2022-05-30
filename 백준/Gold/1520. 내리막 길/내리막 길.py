import sys
input = sys.stdin.readline

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
sys.setrecursionlimit(2000)


def dfs(y, x):
    if y == m-1 and x == n-1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < m and 0 <= nx < n and board[y][x] > board[ny][nx]:
            dp[y][x] += dfs(ny, nx)
    return dp[y][x]


print(dfs(0, 0))
