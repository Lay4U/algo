import heapq

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

INF = int(1e9)

for _ in range(int(input().strip())):
    n = int(input().strip())
    graph = [list(map(int, input().strip().split())) for _ in range(n)]

    distances = [[INF] * n for _ in range(n)]

    start = (0, 0)
    q = [(graph[start[0]][start[1]], *start)]
    distances[start[0]][start[1]] = graph[start[0]][start[1]]

    while q:
        dist, x, y = heapq.heappop(q)
        if distances[x][y] < dist:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[nx][ny]
                if cost < distances[nx][ny]:
                    distances[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    print(distances[n - 1][n - 1])
