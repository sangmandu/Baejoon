import sys
input = sys.stdin.readline

T = int(input())
lst = []
pre = int(input())
for _ in range(T-1):
    cur = int(input())
    lst.append(abs(cur-pre))
    pre = cur

from math import gcd
a = lst[0]
for b in lst[1:]:
    a = gcd(a, b)

ret = [i for i in range(2, int(a**0.5)+1) if a % i == 0]
ret += [a // t for t in ret] + [a]

print(*sorted(list(set(ret))))
