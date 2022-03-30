import sys
input = sys.stdin.readline

n = int(input())
wine = [0] * 3 + [int(input()) for _ in range(n)]
dp = [0] * (n+3)
for i in range(3, n+3):
    dp[i] = max(max(dp[i-4], dp[i-3]) + wine[i-1], dp[i-2]) + wine[i]
print(max(dp))