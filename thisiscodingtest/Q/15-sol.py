# 341, 532
# 1 2
# 1 3
# 1 4
from collections import deque

input = [[1, 2], [1, 3], [2, 3], [2, 4]]

n, m, k, x = 4, 4, 2, 1
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input[_])
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

print(distance)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if not check:
    print(-1)
