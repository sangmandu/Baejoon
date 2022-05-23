import sys
input = sys.stdin.readline

from collections import deque
n, h = map(int, input().split())
obt = [int(input()) for idx in range(n)]
bot, top = deque(sorted(obt[::2])), deque(sorted(obt[1::2]))
stair_bot, stair_top = [0]*h, [0]*h

for idx in range(h):
    while bot:
        if idx < bot[0]:
            stair_bot[idx] = len(bot)
            break
        bot.popleft()
    while top:
        if idx < top[0]:
            stair_top[idx] = len(top)
            break
        top.popleft()

lst = [sb+st for sb, st in zip(stair_bot, stair_top[::-1])]
print(min(lst), lst.count(min(lst)))