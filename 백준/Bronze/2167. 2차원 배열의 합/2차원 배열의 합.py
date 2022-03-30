import sys
input = sys.stdin.readline

from itertools import accumulate
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cum = [list(accumulate(b)) for b in board]

k = int(input())
for _ in range(k):
    y1, x1, y2, x2 = map(lambda x: int(x)-1, input().split())
    print(sum([cum[y][x2]-cum[y][x1]+board[y][x1] for y in range(y1, y2+1)]))
