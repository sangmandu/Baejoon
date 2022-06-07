import sys
input = sys.stdin.readline

N = int(input())
weight = list(map(int, input().split()))
max_weight = 40001

dp = [[0] * max_weight for _ in range(N+1)]
for idx, w in enumerate(weight, 1):
    for jdx in range(idx, N+1):
        dp[jdx][w] = 1
    for x in range(max_weight):
        if dp[idx-1][x]:
            for jdx in range(idx, N+1):
                dp[jdx][abs(w-x)] = dp[jdx][w+x] = 1

input()
YorN = ['N', 'Y']
print(' '.join(list(map(lambda x: YorN[dp[-1][int(x)]], input().split()))))