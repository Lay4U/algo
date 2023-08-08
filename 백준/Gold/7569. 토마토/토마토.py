from collections import deque

m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                queue.append((i, j, k))

while queue:
    x, y, z = queue.popleft()
    for i in range(6):
        nx, ny, nz = dx[i] + x, dy[i] + y, dz[i] + z
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and tomato[nx][ny][nz] == 0:
            tomato[nx][ny][nz] = tomato[x][y][z] + 1
            queue.append((nx, ny, nz))

result = - 1
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                print(-1)
                exit()
            result = max(result, tomato[i][j][k])

print(result - 1)
