import heapq

input = """
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
""".strip().split('\n')

n, m = map(int, input[0].split())
INF = int(1e4)

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for x in input[1:]:
    a, b = map(int, x.split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))
start = 1
distance[start] = 0
q = []
heapq.heappush(q, (0, start))
while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for v, w in graph[now]:
        cost = dist + w
        if cost < distance[v]:
            distance[v] = cost
            heapq.heappush(q, (cost, v))

print(graph)
print(distance)

max_value = max(distance[1:])
max_index = distance.index(max_value)
result = [i for i, dist in enumerate(distance) if i == max_value]

print(max_index, max_value, len(result))
