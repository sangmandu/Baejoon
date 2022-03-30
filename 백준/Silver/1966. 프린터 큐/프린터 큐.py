import sys
input = sys.stdin.readline

from collections import deque

for _ in range(int(input())):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    que = deque([(idx, val) for idx, val in enumerate(lst)])
    lst.sort()
    ret = []

    while que:
        idx, val = que.popleft()
        if val == lst[-1]:
            ret.append(idx)
            lst.pop()
        else:
            que.append((idx, val))

        if ret and ret[-1] == M:
            print(len(ret))
            break
