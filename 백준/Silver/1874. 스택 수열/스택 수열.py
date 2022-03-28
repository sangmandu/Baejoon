import sys
input = sys.stdin.readline

N = int(input())
lst = list(range(N, 0, -1))
stack = []
ret = []
for _ in range(N):
    n = int(input())
    while not stack or stack[-1] != n:
        if not lst:
            break
        stack.append(lst.pop())
        ret.append('+')
    else:
        stack.pop()
        ret.append('-')
        continue
    print("NO")
    break
else:
    print(*ret, sep='\n')
