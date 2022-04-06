import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
rand = []
for _ in range(N):
    rand += list(map(int, input().split()))
rand.sort()

left, right = 0, sum(rand)
rand += [max(rand)+1]
ptr = 0
min_time = 500 * 500 * 256 * 2
for h in range(min(rand), max(rand)):
    while rand[ptr] <= h:
        left += rand[ptr]
        right -= rand[ptr]
        ptr += 1

    push = h * ptr - left
    pop = right - h * (N*M - ptr)

    if B < push - pop:
        break

    time = push + pop * 2
    if time <= min_time:
        min_time = time
        height = h

print(min_time, height)
