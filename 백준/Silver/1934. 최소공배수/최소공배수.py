import sys
input = sys.stdin.readline

from math import gcd
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(int(A * B / gcd(A, B)))
