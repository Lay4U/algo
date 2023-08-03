n = int(input())
graph = [[int(value) for value in input()] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    global graph, visited, count
    visited[x][y] = True
    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                count += 1
                dfs(nx, ny)


visited = [[False] * n for _ in range(n)]
result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            count = 1
            dfs(i, j)
            result.append(count)

print(len(result))
for value in sorted(result):
    print(value)
