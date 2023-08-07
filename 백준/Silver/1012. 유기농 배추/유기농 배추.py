from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global graph, visited, n, m
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    count = 0

    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                count += 1
                bfs(i, j)

    print(count)
