import sys
input = sys.stdin.readline

N = int(input())
c1 = set(map(int, input().split()))
M = int(input())
print(*[int(c in c1) for c in list(map(int, input().split()))])