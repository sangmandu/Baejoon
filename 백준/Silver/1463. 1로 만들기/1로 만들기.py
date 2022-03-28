import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
for m in range(n-1, -1, -1):
    a = b = n
    if m*2 <= n:
        a = dp[m*2]
    if m*3 <= n:
        b = dp[m*3]
    dp[m] = min(a, b, dp[m+1]) + 1
print(dp[1])
