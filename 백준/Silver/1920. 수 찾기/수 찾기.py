import sys
input = sys.stdin.readline

input()
dic={l:1 for l in list(map(int, input().split()))}
input()
for l in list(map(int, input().split())):
    print(dic.get(l, 0))