N, K = 7, 3

data = [i for i in range(1, N + 1)]

index = 0
while data:
    index += K - 1
    if index >= len(data):
        index = index // len(data)
    print(data, index)
    print(data.pop(index))
