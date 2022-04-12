import sys
input = sys.stdin.readline

N = int(input())
sizes = [list(map(int, input().split())) for _ in range(N)]
sizes = [a for a, _ in sizes] + [sizes[-1][1]]
dp = [[0] * N for _ in range(N)]

for l in range(1, N):
    for y in range(N-l):
        x = y + l
        m = sizes[y] * sizes[x+1]
        min_yx = min(dp[y][k] + dp[x][k+1] + sizes[k+1] * m for k in range(y, x))
        dp[y][x] = dp[x][y] = min_yx

print(dp[0][-1])
