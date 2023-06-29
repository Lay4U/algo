from collections import deque


def bfs(n, k):
    MAX = 100001
    times = [0] * MAX
    queue = deque([n])

    while queue:
        v = queue.popleft()
        if v == k:
            print(times[v])
            break
        for next_v in (v + 1, v - 1, v * 2):
            if 0 <= next_v < MAX and not times[next_v]:
                times[next_v] = times[v] + 1
                queue.append(next_v)


n, k = map(int, input().split())
bfs(n, k)
