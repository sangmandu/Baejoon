import sys
input = sys.stdin.readline

N = int(input())
ret = min(N, 99)
for n in range(100, N+1):
    num = str(n)
    length = len(set([int(num[idx])-int(num[idx+1]) for idx in range(len(num)-1)]))
    if length == 1:
        ret += 1

print(ret)