from collections import deque


def bfs(n, k):
    max = 100001
    times = [0] * max
    queue = deque([n])
    while queue:
        v = queue.popleft()
        if v == k:
            return times[v]
        for next_v in (v - 1, v + 1, v * 2):
            if 0 <= next_v < max and not times[next_v]:
                times[next_v] = times[v] + 1
                queue.append(next_v)


n, k = map(int, input().split())
print(bfs(n, k))
