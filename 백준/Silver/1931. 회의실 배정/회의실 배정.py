import sys
input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
prior = answer = 0
for st, ed in sorted(meetings, key=lambda x: (x[1], x[0])):
    if prior > st:
        continue
    prior = ed
    answer += 1
print(answer)