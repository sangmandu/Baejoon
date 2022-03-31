import sys
input = sys.stdin.readline

while True:
    n, *height = list(map(int, input().split())) + [0]
    if not n:
        break

    area = 0
    stack = [(0, 0)]
    for idx, cur_h in enumerate(height, 1):
        while stack[-1][1] > cur_h:
            i, h = stack.pop()
            area = max(area, h * (idx-stack[-1][0]-1))
        stack.append((idx, cur_h))

    print(area)
    