import sys
input = sys.stdin.readline

N = int(input())
nums = sorted([int(input()) for _ in range(N)])
print(round(sum(nums)/N))
print(nums[N//2])

from collections import Counter
order = Counter(nums).most_common()
if len(order) == 1:
    print(order[0][0])
else:
    print(order[1][0] if order[0][1] == order[1][1] else order[0][0])
print(nums[-1] - nums[0])
