import sys
input = sys.stdin.readline
N = int(input().strip())
for _ in range(N):
    a, b = map(lambda x : int(x, 2), input().strip().split())
    print(format(a+b, 'b'))