import sys
input = sys.stdin.readline

que = []
for _ in range(int(input())):
    cmd, *arg = input().split()
    if "po" in cmd:
        print(que.pop(0) if que else -1)
        continue
    if "z" in cmd:
        print(len(que))
        continue
    if "e" in cmd:
        print(int(len(que) == 0))
        continue
    if "f" in cmd:
        print(que[0] if que else -1)
        continue
    if "b" in cmd:
        print(que[-1] if que else -1)
        continue
    que.append(arg[0])
