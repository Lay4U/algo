import heapq
import sys

input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
    data = int(input())
    if data:
        heapq.heappush(heap, data)
    else:
        print(heapq.heappop(heap) if heap else 0)
