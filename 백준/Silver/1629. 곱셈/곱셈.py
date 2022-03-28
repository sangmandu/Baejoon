import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
a %= c

rest = []
while b > 1:
    if b % 2:
        rest.append(a)
    a = a * a % c
    b //= 2

ret = a
for r in rest:
    ret *= r
    ret %= c
print(ret)
