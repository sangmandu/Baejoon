import sys
input = sys.stdin.readline

st = input().strip()

ret = set([])
for idx in range(len(st)):
    for jdx in range(idx, len(st)):
        ret.add(st[idx:jdx+1])
print(len(ret))
