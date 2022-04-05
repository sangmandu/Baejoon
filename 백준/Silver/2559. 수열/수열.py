import sys
input = sys.stdin.readline

from itertools import accumulate
n, k = map(int, input().split())
acc = [0]+list(accumulate(list(map(int, input().split()))))
print(max([acc[idx] - acc[idx-k] for idx in range(k, n+1)]))