from collections import deque

n, m = 4, 2
data = [1, 2, 3, 4]

q = deque([(wanted == m, value) for wanted, value in enumerate(data)])
print(q)
count = 0

while True:
    print(q)
    if q[0][1] == max(q, key=lambda x: x[1])[1]:
        count += 1
        if q[0][0]:
            print(count)
            break
        else:
            q.popleft()
    else:
        q.rotate(-1)
