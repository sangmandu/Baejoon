import sys
input = sys.stdin.readline

input()
lst = list(map(int, input().split()))
print(max(lst)*min(lst))
