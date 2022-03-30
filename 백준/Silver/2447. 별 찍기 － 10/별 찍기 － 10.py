import sys
input = sys.stdin.readline

N = int(input())

stars = [list(' ' * N) for _ in range(N)]

def pattern(N, ny=0, nx=0):
    if N == 1:
        stars[ny][nx] = '*'
    else:
        for y in range(3):
            for x in range(3):
                if y == x == 1:
                    continue
                pattern(N//3, N//3*y+ny, N//3*x+nx)

pattern(N)

print('\n'.join([''.join(line) for line in stars]))
