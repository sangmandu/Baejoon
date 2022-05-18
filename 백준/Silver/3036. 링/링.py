import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
f = lst[0]

from math import gcd
for i in lst[1:]:
    print(f'{f // gcd(f, i)}/{i // gcd(f, i)}')