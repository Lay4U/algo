from collections import deque

for _ in range(int(input())):
    start, end = map(int, input().split())
    queue = deque([(start, '')])
    visited = [False] * 10001
    while queue:
        v, result = queue.popleft()
        if v == end:
            print(result)
            break
        d = (v * 2) % 10000
        s = v - 1 if v != 0 else 9999
        l = (v % 1000) * 10 + (v // 1000)
        r = (v % 10) * 1000 + (v // 10)

        if not visited[d]:
            visited[d] = True
            queue.append((d, result + 'D'))
        if not visited[s]:
            visited[s] = True
            queue.append((s, result + 'S'))
        if not visited[l]:
            visited[l] = True
            queue.append((l, result + 'L'))
        if not visited[r]:
            visited[r] = True
            queue.append((r, result + 'R'))
