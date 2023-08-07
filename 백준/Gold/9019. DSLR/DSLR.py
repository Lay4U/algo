import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):

    a, b = map(int, input().split())

    queue = deque([(a, '')])
    visited = [False] * 10001
    while queue:
        value, op = queue.popleft()
        if value == b:
            print(op)
            break

        d = (value * 2) % 10000
        s = value - 1 if value != 0 else 9999
        l = (value % 1000) * 10 + (value // 1000)
        r = (value % 10) * 1000 + (value // 10)

        if not visited[d]:
            visited[d] = True
            queue.append((d, op + 'D'))

        if not visited[s]:
            visited[s] = True
            queue.append((s, op + 'S',))

        if not visited[l]:
            visited[l] = True
            queue.append((l, op + 'L'))

        if not visited[r]:
            visited[r] = True
            queue.append((r, op + 'R'))
