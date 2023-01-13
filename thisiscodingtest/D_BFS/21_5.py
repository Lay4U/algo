from collections import deque

input = """
4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10
""".strip().split('\n')

n, l, r = map(int, input[0].split())
graph = [list(map(int, raw.split())) for raw in input[1:]]

total_count = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def process(x, y, index):
    united = []
    united.append((x, y))
    queue = deque()
    queue.append((x, y))
    union[x][y] = index

    summary = graph[x][y]
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    united.append((nx, ny))
                    queue.append((nx, ny))
                    summary += graph[nx][ny]
                    count += 1
                    union[nx][ny] = index
    for x, y in united:
        graph[x][y] = summary // count


while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1

    if index == n * n:
        break
    total_count += 1
print(total_count)
