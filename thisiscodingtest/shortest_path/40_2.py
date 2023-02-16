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
INF = 1e3
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for x in input[1:]:
    a, b = map(int, x.split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

print(graph)

start = 1
q = []
distance[start] = 0
heapq.heappush(q, (0, start))
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for v, w in graph[now]:
        cost = dist + w
        if cost < distance[v]:
            distance[v] = cost
            heapq.heappush(q, (cost, v))

max_distance = max(distance[1:])
max_node = distance.index(max_distance)
result = [i for i, dist in enumerate(distance) if dist == max_distance]

print(distance)
print(max_node, max_distance, len(result))
