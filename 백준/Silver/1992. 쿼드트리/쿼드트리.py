import sys
input = sys.stdin.readline

N = int(input())
board = [list(str(input().strip())) for _ in range(N)]
ret = [0, 0]

step = 2
while step <= N:
    for y in range(0, N, step):
        for x in range(0, N, step):
            elements = [board[y][x], board[y][x+step//2], board[y+step//2][x], board[y+step//2][x+step//2]]
            if len(set(elements)) == 1 and len(elements[0]) == 1:
                continue
            board[y][x] = '('+''.join(elements)+')'
    step *= 2

print(board[0][0])
