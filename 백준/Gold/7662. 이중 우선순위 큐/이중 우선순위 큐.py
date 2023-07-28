import heapq
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    maxq = []
    minq = []
    visited = [False] * 1000001
    for i in range(int(input())):
        op, n = input().split()
        n = int(n)
        if op == 'I':
            heapq.heappush(minq, (n, i))
            heapq.heappush(maxq, (-n, i))
            visited[i] = True
        else:
            targetQ = minq if n == -1 else maxq
            while targetQ and not visited[targetQ[0][1]]:
                heapq.heappop(targetQ)
            if targetQ:
                visited[targetQ[0][1]] = False
                heapq.heappop(targetQ)

    while minq and not visited[minq[0][1]]:
        heapq.heappop(minq)
    while maxq and not visited[maxq[0][1]]:
        heapq.heappop(maxq)

    print(f'{-maxq[0][0]} {minq[0][0]}' if minq and maxq else 'EMPTY')
