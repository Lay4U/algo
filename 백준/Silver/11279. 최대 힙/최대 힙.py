import heapq
import sys
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    value = int(input())
    print(-heapq.heappop(arr) if arr else 0) if value == 0 else heapq.heappush(arr, -value)
