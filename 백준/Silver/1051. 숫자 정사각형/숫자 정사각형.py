n, m = map(int, input().split())
edge = min(n, m)-1
board = [input() for _ in range(n)]
while edge > 0:
    for y in range(n-edge):
        for x in range(m-edge):
            if board[y][x] == board[y+edge][x] == board[y][x+edge] == board[y+edge][x+edge]:
                print((edge+1)**2)
                exit()
    edge -= 1
print(1)