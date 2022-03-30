import sys
input = sys.stdin.readline
N = int(input())
perm = ''.join(input().split())
max_up = max_down = 1
up = down = 1
for idx in range(1, N):
    if perm[idx-1] == perm[idx]:
        up, down = up+1, down+1
    elif perm[idx-1] < perm[idx]:
        up, down = up+1, 1
    else:
        up, down = 1, down+1
    max_up = max(max_up, up)
    max_down = max(max_down, down)
print(max(max_up, max_down))