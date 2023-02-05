input = """
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
""".strip().split('\n')

n = int(input[0])
m = int(input[1])

INF = 1e9
graph = [[INF] * (n + 1) for _ in range(n + 1)]
print(graph)

for x in input[2:]:
    a, b, c = map(int, x.split())
    graph[a][b] = min(graph[a][b], c)

for i in range(n + 1):
    graph[i][i] = 0

for k in range(n + 1):
    for i in range(n + 1):
        for j in range(n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

print(graph)
