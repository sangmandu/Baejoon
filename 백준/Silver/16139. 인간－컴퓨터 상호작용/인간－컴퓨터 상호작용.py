import sys
input = sys.stdin.readline

from collections import defaultdict
cnt = defaultdict(list)

for idx, s in enumerate(input().strip()):
    cnt[s].append(idx)

from bisect import bisect_left, bisect_right
for _ in range(int(input())):
    s, *nums = input().split()
    st, ed = map(int, nums)
    print(bisect_right(cnt[s], ed) - bisect_left(cnt[s], st))