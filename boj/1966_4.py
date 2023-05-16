from collections import deque

n, m = 4, 2
datas = [1, 2, 3, 4]

queue = deque([(index, value) for (index, value) in enumerate(datas)])

result = 0
while True:
    if queue[0][1] == max(queue, key=lambda x: x[1])[1]:
        result += 1

        if queue[0][0] == m:
            print(result)
            break
        else:
            queue.popleft()
    else:
        queue.rotate(-1)

for _ in range(int(input())):
    n, m = map(int, input().split())
    queue = deque(map(int, input().split()))
    queue = deque([(index == m, value) for index, value in enumerate(queue)])
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
