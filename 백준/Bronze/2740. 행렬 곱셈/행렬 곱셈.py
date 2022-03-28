import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mat1 = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
mat2 = [list(map(int, input().split())) for _ in range(M)]
mat2 = [list(i) for i in zip(*mat2)]

mat3 = [[0] * K for _ in range(N)]

for y in range(N):
    for x in range(K):
        mat3[y][x] = sum([a*b for a, b in zip(mat1[y], mat2[x])])

for i in mat3:
    print(*i)
