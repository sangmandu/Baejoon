import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
que = list(range(1, N+1))

ret = idx = 0
for item in list(map(int, input().split())):
    move = 0
    while que[idx] != item:
        idx = (idx + 1) % len(que)
        move += 1
    ret += min(move, len(que)-move)
    que.pop(idx)
    if idx == len(que):
        idx = 0

print(ret)
