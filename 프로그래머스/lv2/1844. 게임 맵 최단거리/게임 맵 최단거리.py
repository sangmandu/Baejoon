from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    que = deque([[0, 0, 1]]) # y, x, dist
    while que:
        y, x, dist = que.popleft()
        if y == n-1 and x == m-1:
            return dist
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y+dy, x+dx
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 0:
                if maps[ny][nx] == 1 or maps[ny][nx] > dist+1:
                    maps[ny][nx] = dist+1
                    que.append([ny, nx, dist+1])
    else:
        return -1