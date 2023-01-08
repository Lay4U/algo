from collections import deque

input = """
4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10
""".strip().split('\n')

n, l, r = map(int, input[0].split())
graph = [list(map(int, row.split())) for row in input[1:]]

total_count = 0


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
