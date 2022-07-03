import sys
input = sys.stdin.readline

ret = 0
for _ in range(int(input())):
    s = input().strip()
    ret += list(s) == sorted(s, key=s.find)
print(ret)