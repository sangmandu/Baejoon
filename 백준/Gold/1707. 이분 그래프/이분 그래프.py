import sys
input = sys.stdin.readline

from collections import defaultdict
for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    left, right = set([]), set([])
    visited = [1] + [0] * V
    for node in range(1, V+1):
        if visited[node]:
            continue
        stack = [node]
        visited[node] = 1
        while stack:
            idx = stack.pop()
            for neigh in graph[idx]:
                if not visited[neigh]:
                    visited[neigh] = 1
                    stack.append(neigh)

            if not left.intersection(graph[idx]):
                left.add(idx)
                continue
            if not right.intersection(graph[idx]):
                right.add(idx)
                continue
            print("NO")
            break
        else:
            continue
        break
    else:
        print("YES")
