import sys
input = sys.stdin.readline

ret = 0
for _ in range(int(input())):
    word = input().strip()
    stack = [word[0]]
    for apbet in word[1:]:
        if apbet == stack[-1]:
            continue
        if apbet not in stack:
            stack.append(apbet)
            continue
        break
    else:
        ret += 1
print(ret)