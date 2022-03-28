import sys
input = sys.stdin.readline

N, L = map(int, input().split())
leak = sorted(list(map(int, input().split())))
idx = jdx = 0
answer = 1
while idx < len(leak)-1:
    idx += 1
    if leak[idx]-leak[jdx] <= L-1:
        continue
    jdx = idx
    answer += 1
print(answer)