import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    answer = 1
    for a in range(M, M-N, -1):
        answer *= a
    for a in range(N, 1, -1):
        answer //= a
    print(answer)