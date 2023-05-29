from collections import deque

n, m = 4, 2
datas = [1, 2, 3, 4]

queue = deque([(seeking == m, value) for seeking, value in enumerate(datas)])
count = 0
while queue:
    if queue[0][1] == max(queue, key=lambda x: x[1])[1]:
        count += 1
        if queue[0][0]:
            print(count)
            break
        else:
            queue.popleft()
    else:
        queue.rotate(-1)
