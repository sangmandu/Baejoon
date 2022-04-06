import sys
input = sys.stdin.readline

from collections import deque
que = deque()
for _ in range(int(input())):
    cmd, *arg = input().split()
    if cmd == "pop":
        print(que.popleft() if que else -1)
    elif cmd == "size":
        print(len(que))
    elif cmd == "empty":
        print(int(len(que) == 0))
    elif cmd == "front":
        print(que[0] if que else -1)
    elif cmd == "back":
        print(que[-1] if que else -1)
    else:
        que.append(arg[0])
