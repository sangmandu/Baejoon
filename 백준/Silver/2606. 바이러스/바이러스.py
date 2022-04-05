from collections import defaultdict
n, m = map(int, [input(), input()])
dic = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

visited = [0, 1] + [0] * (n-1)
stack = [1]
while stack:
    idx = stack.pop()
    for node in dic[idx]:
        if not visited[node]:
            visited[node] = 1
            stack.append(node)
print(visited.count(1)-1)
