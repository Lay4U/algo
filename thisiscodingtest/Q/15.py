from collections import deque

n, m, k, x = 4, 4, 1, 1
edges = [[1, 2], [1, 3], [2, 3], [2, 4]]

distance = [-1] * (n + 1)
distance[x] = 0

graph = [[] for _ in range(n + 1)]
for a, b in edges:
    graph[a].append(b)

queue = deque([x])
while queue:
    now = queue.popleft()

    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            queue.append(next_node)

    distance_node = [i for i in distance if distance[i] == k]
    if not distance_node:
        print(-1)
    else:
        print(distance_node)
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if not check:
    print(-1)
