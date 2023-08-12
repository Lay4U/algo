import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n + 1)
queue = deque([1])
visited[1] = True
count = 0
while queue:
    v = queue.popleft()
    for next in graph[v]:
        if not visited[next]:
            visited[next] = True
            queue.append(next)
            count += 1
print(count)
