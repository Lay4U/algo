from collections import deque, defaultdict
import sys

def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for e in sorted(graph[v]):
        if not visited[e]:
            dfs(e)

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if not visited[v]:
            visited[v] = True
            print(v, end=' ')
            for e in sorted(graph[v]):
                if not visited[e]:
                    q.append(e)

N, M, V = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(N+1)
dfs(V)
print()
visited = [False]*(N+1)
bfs(V)
