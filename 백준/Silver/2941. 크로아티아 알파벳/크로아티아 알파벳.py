import sys
input = sys.stdin.readline

words = input().strip()
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
ret = 0
for val in lst:
    ret += words.count(val)
    words = words.replace(val, '*')
ret += len(words) - words.count('*')
print(ret)