import heapq

input = """
3
10
20
40
""".strip().split("\n")

n = int(input[0])
heap = []
for i in range(1, n + 1):
    data = int(input[i])
    heapq.heappush(heap, data);

result = 0
while len(heap) != 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    count = first + second
    result += count
    heapq.heappush(heap, count)
print(result)
