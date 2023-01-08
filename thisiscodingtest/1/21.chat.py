from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]


def find_alliance(x, y, index):
    united = []
    united.append((x, y))
    queue = deque()
    queue.append((x, y))
    union[x][y] = index
    summary = graph[x][y]
    count = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    queue.append((nx, ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    for x, y in united:
        graph[x][y] = summary // count
    return count


total_count = 0
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                find_alliance(i, j, index)
                index += 1
    if index == n * n:
        break
    total_count += 1
print(total_count)
