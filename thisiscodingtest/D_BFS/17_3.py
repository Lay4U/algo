from collections import deque

input = """
3 3
1 0 2
0 0 0
3 0 0
2 3 2 """.strip().split('\n')

n, k = map(int, input[0].split())

data = []
graph = [list(map(int, line.split())) for line in input[1:-1]]

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)
print(graph)
print(data)
target_s, target_x, target_y = map(int, input[-1].split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])