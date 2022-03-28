import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = [cost[0]] + [[0]*3 for _ in range(n-1)]
for y in range(1, n):
    for x in range(3):
        a, b = (x+1) % 3, (x+2) % 3
        dp[y][x] = min(dp[y-1][a], dp[y-1][b]) + cost[y][x]
print(min(dp[n-1]))
