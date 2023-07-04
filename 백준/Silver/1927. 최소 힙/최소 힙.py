import sys
import heapq
input = sys.stdin.readline

n = int(input())
datas = []
for _ in range(n):
    value = int(input())
    if value == 0:
        print(heapq.heappop(datas) if datas else 0)
    else:
        heapq.heappush(datas, value)
