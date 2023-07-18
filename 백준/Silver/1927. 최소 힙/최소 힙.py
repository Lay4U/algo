import sys
import heapq
input = sys.stdin.readline

n = int(input())
list = []
for _ in range(n):
    value = int(input())
    if value == 0:
        print(heapq.heappop(list) if list else 0)
    else:
        heapq.heappush(list, value)
