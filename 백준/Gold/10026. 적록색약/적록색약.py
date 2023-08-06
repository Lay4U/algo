from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
graph1 = [list(input()) for _ in range(n)]
graph2 = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph1[i][j] == 'R' or graph1[i][j] == 'G':
            graph2[i][j] = 'R'
        else:
            graph2[i][j] = 'B'

cnt1 = 0
cnt2 = 0


def bfs(x, y, graph):
    queue = deque([(x, y)])
    color = graph[x][y]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == color:
                queue.append((nx, ny))
                graph[nx][ny] = 0


for i in range(n):
    for j in range(n):
        if graph1[i][j] != 0:
            bfs(i, j, graph1)
            cnt1 += 1
        if graph2[i][j] != 0:
            bfs(i, j, graph2)
            cnt2 += 1

print(cnt1)
print(cnt2)
