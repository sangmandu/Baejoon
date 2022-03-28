import sys
from itertools import combinations
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    point = [list(map(int, input().split())) for _ in range(N)]
    sum_x, sum_y = map(sum, zip(*point))

    min_dist = 4e+5
    cases = list(combinations(list(range(N)), N // 2))
    for c in cases[:len(cases)//2]:
        part_x, part_y = map(sum, zip(*[point[idx] for idx in c]))
        x, y = sum_x - 2*part_x, sum_y - 2*part_y
        min_dist = min(min_dist, (x**2 + y**2) ** 0.5)

    print(min_dist)

