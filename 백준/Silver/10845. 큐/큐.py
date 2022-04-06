import sys
input = sys.stdin.readline

from collections import deque
que = deque()
for _ in range(int(input())):
    cmd, *arg = input().split()
    if cmd == "pop":
        print(que.popleft() if que else -1)
        continue
    if cmd == "size":
        print(len(que))
        continue
    if cmd == "empty":
        print(int(len(que) == 0))
        continue
    if cmd == "front":
        print(que[0] if que else -1)
        continue
    if cmd == "back":
        print(que[-1] if que else -1)
        continue
    que.append(arg[0])
