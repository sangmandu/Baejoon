import sys
input = sys.stdin.readline

a = b = 0
for _ in range(3):
    c, d = map(int, input().split())
    a = a ^ c
    b = b ^ d
print(a, b)