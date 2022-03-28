n = int(input())
friends = [input() for _ in range(n)]
board = [[0] * n for _ in range(n)]
for y in range(n):
    for x in range(y+1, n):
        if friends[y][x] == "Y":
            board[y][x] = board[x][y] = 1
            continue
        for z in range(n):
            if friends[y][z] == friends[x][z] == "Y":
                board[y][x] = board[x][y] = 1
                break
print(max([sum(b) for b in board]))