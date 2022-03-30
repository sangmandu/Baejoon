import sys
input = sys.stdin.readline

h, m = map(int, input().split())
c = int(input())

h = (h + (m + c) // 60) % 24
m = (m + c) % 60

print(h, m)