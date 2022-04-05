import sys
input = sys.stdin.readline

n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]
dp = [0] + [sum(stairs[:2])] + [sum(stairs[:3])] + [0] * (n-2)
for i in range(3, n+1):
    a = dp[i-3] + stairs[i-1]
    b = dp[i-2]
    dp[i] = max(a, b) + stairs[i]
print(dp[n])