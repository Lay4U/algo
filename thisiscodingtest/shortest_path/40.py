import heapq
from pprint import pprint

n, m = map(int, input().split())
INF = int(1e4)
start = 1
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

q = []
heapq.heappush(q, (0, start))
distance[start] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for x in graph[now]:
        cost = dist + x[1]
        if cost < distance[x[0]]:
            distance[x[0]] = cost
            heapq.heappush(q, (cost, x[0]))

max_node = 0
max_distance = 0
result = []

for i in range(1, n + 1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    else:
        result.append(i)
print(max_node, max_distance, len(result))
pprint(distance)
