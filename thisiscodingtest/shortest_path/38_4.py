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

for x in range(1, n + 1):
    graph[x][x] = 0

for x in input[1:]:
    a, b = map(int, x.split())
    graph[a][b] = 1
pprint(graph)
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

pprint(graph)

result = 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result += 1

print(result)
result = sum(1 for i in range(1, n + 1) if all(graph[i][j] != INF or graph[j][i] != INF for j in range(1, n + 1)))
print(result)
