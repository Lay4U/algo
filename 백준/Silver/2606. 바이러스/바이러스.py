from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = True
count = 0
queue = deque([1])
while queue:
    v = queue.popleft()
    for next in graph[v]:
        if not visited[next]:
            queue.append(next)
            visited[next] = True
            count += 1
print(count)
