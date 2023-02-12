from pprint import pprint

input = """
6 6
1 5
3 4
4 2
4 6
5 2
5 4
""".strip().split('\n')

n, m = map(int, input[0].split())
INF = int(1e4)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for x in range(n + 1):
    graph[x][x] = 0
for x in input[1:]:
    a, b = map(int, x.split())
    graph[a][b] = min(graph[a][b], 1)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = sum(1 for i in range(1, n + 1) if all(graph[i][j] != INF or graph[j][i] != INF for j in range(1, n + 1)))

pprint(graph)
print(result)
