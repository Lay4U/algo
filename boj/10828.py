data = []
N = int(input())
for _ in range(N):
    data.append(input())
# data = [line for line in data if line]
# print(data)

result = []
for query in data:
    if 'push' in query:
        split = query.split(' ')
        result.append(split[1])
    elif query == 'pop':
        if result:
            print(result.pop())
        else:
            print(-1)
    elif query == 'size':
        print(len(result))
    elif query == 'empty':
        print(0 if result else 1)
    elif query == 'top':
        print(result[-1] if result else -1)
