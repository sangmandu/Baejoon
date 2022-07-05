import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

acc = 0
mod = [0] * M
for val in lst:
    acc += val
    mod[acc % M] += 1

ans = mod[0]
for m in mod:
    ans += m * (m-1) // 2

print(ans)