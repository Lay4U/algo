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
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    graph[i][i] = 0
for i in range(1, n + 1):
    a, b = map(int, input[i].split())
    graph[a][b] = 1
pprint(graph)

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = sum(1 for i in range(1, n + 1) if all(graph[i][j] != INF or graph[j][i] != INF for j in range(1, n + 1)))
pprint(graph)
print(result)
