import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    employee = [tuple(map(int, input().split())) for _ in range(int(input()))]
    heapify(employee)

    answer, cut = 0, len(employee)
    while employee:
        _, view = heappop(employee)
        if cut < view:
            continue
        answer += 1
        cut = view
    print(answer)