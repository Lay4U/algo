from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
visited[1] = True
queue = deque([1])
count = 0
while queue:
    v = queue.popleft()
    for v in graph[v]:
        if not visited[v]:
            count += 1
            queue.append(v)
            visited[v] = True

print(count)
