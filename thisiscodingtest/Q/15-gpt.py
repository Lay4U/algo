from collections import deque


def find_k_distance_nodes(n, m, k, x, edges):
    graph = [[] for _ in range(n + 1)]
    for a, b in edges:
        graph[a].append(b)

    distance = [-1] * (n + 1)
    distance[x] = 0

    q = deque([x])
    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if distance[next_node] == -1:
                distance[next_node] = distance[now] + 1
                q.append(next_node)

    k_distance_node = [i for i in range(1, n + 1) if distance[i] == k]
    if not k_distance_node:
        return [-1]
    return k_distance_node


n, m, k, x = 4, 4, 2, 1
edges = [[1, 2], [1, 3], [2, 3], [2, 4]]
