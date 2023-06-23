import sys

sys.setrecursionlimit(10 ** 7)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        elif field[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx, ny)


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        field[x][y] = 1

    answer = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1 and not visited[i][j]:
                answer += 1
                dfs(i, j)

    print(answer)
