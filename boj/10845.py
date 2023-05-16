N = int(input())
data = []
for _ in range(N):
    data.append(input())

# data = [r for r in data if r]
# print(data)

queue = []
for query in data:
    if 'push' in query:
        queue.append(query.split()[1])
    elif 'pop' == query:
        print(queue.pop(0) if queue else -1)
    elif 'size' == query:
        print(len(queue))
    elif 'empty' == query:
        print(0 if queue else 1)
    elif 'front' == query:
        print(queue[0] if queue else -1)
    elif 'back' == query:
        print(queue[-1] if queue else -1)
