import heapq

input = """
3
10
20
40
""".strip().split('\n')

n = int(input[0])
heap = []
for i in range(n):
    heapq.heappush(heap, int(input[i + 1]))

print(heap)

result = 0
while len(heap) != 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    count = first + second
    result += count
    heapq.heappush(heap, count)

print(heap)
print(result)
