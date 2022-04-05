move = [(0, -1), (0, 1), (-1, 0), (1, 0)]
def check_air(board, y, x):
    flag = 0
    for dy, dx in move:
        ny, nx = dy+y, dx+x
        if ny < 0 or ny >= h or nx < 0 or nx >= w:
            flag += 1
            continue
        if board[ny][nx] == -1:
            flag += 1
            continue
        if board[ny][nx] == 0 and (ny, nx) not in outer_air:
            outer_air.add((ny, nx))
            flag += check_air(board, ny, nx)
    return flag

def check_melt(y, x):
    for dy, dx in move:
        ny, nx = dy + y, dx + x
        if board[ny][nx] == -1:
            return True
    return False

import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline
h, w = map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for _ in range(h)]
time = 0
prev_cheese = 0
while True:
    total_cheese = 0
    for y in range(h):
        for x in range(w):
            outer_air = set()
            if board[y][x] == 0 and (y, x) not in outer_air:
                outer_air.add((y, x))
                flag = check_air(board, y, x)
                if flag > 0:
                    for ny, nx in list(outer_air):
                        board[ny][nx] = -1
            elif board[y][x] == 1:
                total_cheese += 1

    if total_cheese == 0:
        print(time)
        print(prev_cheese)
        break

    melt = set()
    for y in range(h):
        for x in range(w):
            if board[y][x] == 1:
                if check_melt(y, x):
                    melt.add((y, x))
    for ny, nx in list(melt):
        board[ny][nx] = -1

    time += 1
    prev_cheese = total_cheese
