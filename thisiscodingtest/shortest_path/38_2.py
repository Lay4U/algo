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

INF = int(1e9)

n, m = map(int, input[0].split())
graph = [[INF] * n for _ in range(n)]

for x in range(n):
    graph[x][x] = 0

for x in input[1:]:
    a, b = map(int, x.split())
    graph[a - 1][b - 1] = 1
pprint(graph)
for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# result = 0

# for i in range(n):
#     count = 0
#     for j in range(n):
#         if graph[i][j] != INF or graph[j][i] != INF:
#             count += 1
#     if count == n:
#         result += 1
pprint(graph)
result = sum(1 for i in range(n) if all(graph[i][j] != INF or graph[j][i] != INF for j in range(n)))

print(result)

'''
[[0, 1000000000, 1000000000, 1000000000, 1, 1000000000],
 [1000000000, 0, 1000000000, 1000000000, 1000000000, 1000000000],
 [1000000000, 1000000000, 0, 1, 1000000000, 1000000000],
 [1000000000, 1, 1000000000, 0, 1000000000, 1],
 [1000000000, 1, 1000000000, 1, 0, 1000000000],
 [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 0]]
 
 
[[0, 2, 1000000000, 2, 1, 3],
 [1000000000, 0, 1000000000, 1000000000, 1000000000, 1000000000],
 [1000000000, 2, 0, 1, 1000000000, 2],
 [1000000000, 1, 1000000000, 0, 1000000000, 1],
 [1000000000, 1, 1000000000, 1, 0, 2],
 [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 0]]
'''
