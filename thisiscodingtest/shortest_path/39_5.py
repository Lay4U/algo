import heapq

input = """
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 8 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
""".strip().split('\n')

INF = int(1e3)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

index = 1
while index < len(input):
    n = int(input[index])
    index += 1
    graph = [[int(y) for y in x.split()] for x in input[index:index + n]]
    index += n

    distance = [[INF] * n for _ in range(n)]

    start = 0, 0
    a, b = start
    distance[a][b] = graph[a][b]
    q = [(graph[a][b], a, b)]

    while q:
        dist, x, y = heapq.heappop(q)
        if dist > distance[x][y]:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    print(distance)
