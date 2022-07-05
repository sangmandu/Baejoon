import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split())) + [0]

mod = [0] * M
for idx in range(N):
    lst[idx] += lst[idx-1]
    mod[lst[idx] % M] += 1

ans = mod[0]
for m in mod:
    ans += m * (m-1) // 2

print(ans)