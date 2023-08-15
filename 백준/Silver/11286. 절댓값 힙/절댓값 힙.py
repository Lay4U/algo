import heapq
import sys
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    value = int(input())
    if value == 0:
        if arr:
            print(heapq.heappop(arr)[1])
        else:
            print(0)
    else:
        heapq.heappush(arr, (abs(value), value))
