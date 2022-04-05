import sys
input = sys.stdin.readline

sdoku = [list(map(int, input().split())) for _ in range(9)]
empty = []
hor, ver, block = [[[1] * 10 for key in range(9)] for _ in range(3)]

for y in range(9):
    for x in range(9):
        n = sdoku[y][x]
        if n == 0:
            empty.append((y, x))
            continue
        hor[x][n] = ver[y][n] = block[3*(y//3) + x//3][n] = 0

def dfs(idx):
    if idx == len(empty):
        for i in sdoku:
            print(*i)
        exit()

    y, x = empty[idx]
    for i in range(1, 10):
        if hor[x][i] and ver[y][i] and block[3*(y//3) + x//3][i]:
            hor[x][i] = ver[y][i] = block[3 * (y // 3) + x // 3][i] = 0
            sdoku[y][x] = i
            dfs(idx+1)
            hor[x][i] = ver[y][i] = block[3 * (y // 3) + x // 3][i] = 1
            sdoku[y][x] = 0
dfs(0)



