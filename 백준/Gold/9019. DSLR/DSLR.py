from collections import deque

for _ in range(int(input())):
    start, end = map(int, input().split())
    queue = deque([(start, '')])
    visited = [False] * 10001
    while queue:
        value, op = queue.popleft()
        if value == end:
            print(op)
            break

        d = (value * 2) % 10000
        s = (value - 1) if value != 0 else 9999
        l = (value % 1000) * 10 + (value // 1000)
        r = (value % 10) * 1000 + (value // 10)

        if not visited[d]:
            queue.append((d, op + 'D'))
            visited[d] = True

        if not visited[s]:
            queue.append((s, op + 'S',))
            visited[s] = True

        if not visited[l]:
            queue.append((l, op + 'L',))
            visited[l] = True

        if not visited[r]:
            queue.append((r, op + 'R',))
            visited[r] = True
