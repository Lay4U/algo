from collections import deque
from sys import stdin


def bfs(start, field, visited):
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(field)) and (0 <= ny < len(field[0])) and field[nx][ny] and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True


T = int(stdin.readline())
for _ in range(T):
    M, N, K = map(int, stdin.readline().split())
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        y, x = map(int, stdin.readline().split())
        field[x][y] = 1

    caterpillar_count = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] and not visited[i][j]:
                bfs((i, j), field, visited)
                caterpillar_count += 1

    print(caterpillar_count)
