import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [[-1] * N for _ in range(N)]

for _ in range(int(input())):
    S, E = map(lambda x: int(x)-1, input().split())
    tmp = []

    ans = 0
    for i in range((E-S) // 2 + (E-S) % 2 + int(E == S)):
        if dp[S+i][E-i] != -1:
            ans = dp[S+i][E-i]
            break

        tmp.append((S + i, E - i))
        if nums[S+i] == nums[E-i]:
            continue
        break
    else:
        ans = 1

    for s, e in tmp:
        dp[s][e] = ans

    print(dp[S][E])