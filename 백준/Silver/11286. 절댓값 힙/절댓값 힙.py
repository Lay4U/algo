import heapq
import sys
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    value = int(input())
    if value == 0:
        print(heapq.heappop(arr)[1] if arr else 0)
    else:
        heapq.heappush(arr, (abs(value), value))
