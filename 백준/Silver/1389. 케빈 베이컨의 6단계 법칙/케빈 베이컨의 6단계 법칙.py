n, m = map(int, input().split())
inf = 1e9
graph = [[inf] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = [0] * (n + 1)

for i in range(1, n + 1):
    result[i] = (sum(graph[i][1:]))

print(result.index(min(result[1:])))
