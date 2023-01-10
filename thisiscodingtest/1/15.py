"""
1 2
1 3
2 3
2 4
"""
from collections import deque

n, m, k, x = 4, 4, 2, 1

distance = [-1] * (n + 1)

graph = [[] for _ in range(n + 1)]
for x in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance[x] = 0

q = deque([x])

while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] += distance[now] + 1
            q.append(next_node)

    print(x for x in distance if distance[x] == k)
