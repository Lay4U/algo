from collections import deque

test_cases = int(input())

for _ in range(test_cases):
    n, m = map(int, input().split())
    queue = deque(map(int, input().split()))
    index_queue = deque(range(n))
    count = 0

    while queue:
        print(queue)
        if queue[0] == max(queue):
            count += 1
            queue.popleft()
            if index_queue.popleft() == m:
                print(count)
                break
        else:
            queue.append(queue.popleft())
            index_queue.append(index_queue.popleft())
