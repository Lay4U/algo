from collections import deque


def print_order(test_cases):
    for _ in range(test_cases):
        n, m = map(int, input().split())
        queue = deque(map(int, input().split()))
        queue = deque([(i == m, elem) for i, elem in enumerate(queue)])
        answer = 0
        while True:
            if queue[0][1] == max(queue, key=lambda x: x[1])[1]:
                answer += 1

                if queue[0][0]:
                    print(answer)
                    break
                else:
                    queue.popleft()
            else:
                queue.rotate(-1)


print_order(int(input()))
