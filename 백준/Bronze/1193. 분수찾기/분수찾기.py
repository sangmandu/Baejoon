import sys
input = sys.stdin.readline

n = int(input())
cnt, order = 0, 1

while n-cnt > order:
    cnt += order
    order += 1

bot = range(1, order+1)[n-cnt-1] if order & 1 else range(order, 0, -1)[n-cnt-1]
print(f'{order+1-bot}/{bot}')
