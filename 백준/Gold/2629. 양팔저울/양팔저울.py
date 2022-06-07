import sys
input = sys.stdin.readline

input()
dp = set([0])
for w in list(map(int, input().split())):
    tmp = set()
    for d in dp:
        tmp.update([d, d+w, d-w])
    dp = tmp

input()
print(' '.join(map(lambda x: 'Y' if int(x) in dp else 'N', input().split())))