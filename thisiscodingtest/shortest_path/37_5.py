from pprint import pprint

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
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    graph[i][i] = 0
for x in input[2:]:
    a, b, c = map(int, x.split())
    graph[a][b] = min(c, graph[a][b])

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
for row in graph[1:]:
    print(*(0 if x == INF else x for x in row[1:]))

print()
pprint(graph)
# print(n, m)
