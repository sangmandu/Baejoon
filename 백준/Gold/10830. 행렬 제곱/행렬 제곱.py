import sys
input = sys.stdin.readline

N, B = map(int, input().split())
matrix = [list(map(lambda x: int(x) % 1000, input().split())) for _ in range(N)]
rest = []


def matmul(M1, M2):
    M2 = [list(i) for i in zip(*M2)]
    return [[sum([a*b for a, b in zip(M1[y], M2[x])]) % 1000 for x in range(len(M2))] for y in range(len(M1))]


while B > 1:
    if B % 2:
        rest.append(matrix)
    matrix = matmul(matrix, matrix)
    B //= 2

for r in rest:
    matrix = matmul(matrix, r)

for m in matrix:
    print(*m)
