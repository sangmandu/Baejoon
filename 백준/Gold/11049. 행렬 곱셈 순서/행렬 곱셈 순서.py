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
        min_yx = min(yk + xk + sz * m for yk, xk, sz in zip(dp[y][y:x], dp[x][y+1:x+1], sizes[y+1:x+1]))
        dp[y][x] = dp[x][y] = min_yx

print(dp[0][-1])
