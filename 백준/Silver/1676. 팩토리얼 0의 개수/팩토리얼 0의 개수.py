import sys
input = sys.stdin.readline

N = int(input())
n = 5
ret = 0
while n <= N:
    ret += N // n
    n *= 5
print(ret)
