import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
print(a // (c-b) + 1 if c-b >= 1 else -1)