import heapq
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    maxQueue = []
    minQueue = []
    visited = [False] * 1000001
    for i in range(int(input())):
        op, value = input().split()
        value = int(value)

        if op == 'I':
            heapq.heappush(minQueue, (value, i))
            heapq.heappush(maxQueue, (-value, i))
            visited[i] = True
        else:
            targetQueue = minQueue if value == -1 else maxQueue
            while targetQueue and not visited[targetQueue[0][1]]:
                heapq.heappop(targetQueue)

            if targetQueue:
                visited[targetQueue[0][1]] = False
                heapq.heappop(targetQueue)

    while minQueue and not visited[minQueue[0][1]]:
        heapq.heappop(minQueue)
    while maxQueue and not visited[maxQueue[0][1]]:
        heapq.heappop(maxQueue)

    print(f'{-maxQueue[0][0]} {minQueue[0][0]}' if maxQueue and minQueue else 'EMPTY')
