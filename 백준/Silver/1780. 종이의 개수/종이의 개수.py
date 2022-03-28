import sys
input = sys.stdin.readline

N = int(input())
board = [input().split() for _ in range(N)]
ret = [0, 0]

step = 3
while step <= N:
    for y in range(0, N, step):
        for x in range(0, N, step):
            elements = [board[y+(dy*step//3)][x+(dx*step//3)] for dy in range(3) for dx in range(3)]
            # print(elements, len(set(elements)), )
            if len(set(elements)) == 1 and elements[0] in ['1', '0', '-1']:
                continue
            board[y][x] = ''.join(elements)
    step *= 3

ret = board[0][0]
for num in ['-1', '0', '1']:
    print(ret.count(num))
    ret = ret.replace(num, '')