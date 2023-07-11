import heapq
import sys

input = sys.stdin.readline
queue = []
for _ in range(int(input())):
    value = int(input())
    if value == 0:
        print(heapq.heappop(queue) if queue else '0')
    else:
        heapq.heappush(queue, value)
