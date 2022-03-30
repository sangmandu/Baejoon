import sys
input = sys.stdin.readline

from collections import deque
que = deque(list(range(int(input()), 0, -1)))

while que:
    n = que.pop()
    if que:
        que.appendleft(que.pop())
    else:
        print(n)
        break
        