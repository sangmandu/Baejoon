n = int(input())
lst = [int(input())-1 for _ in range(n)]
cost = [0] * n
for idx in range(n):
    stack = [idx]
    visited = [0] * n
    visited[idx] = 1
    while stack:
        src = stack.pop()
        dst = lst[src]
        if not visited[dst]:
            visited[dst] = 1
            stack.append(dst)
            cost[idx] += 1
print(cost.index(max(cost))+1)