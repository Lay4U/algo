n, k = map(int, input().split())

data = [i for i in range(1, n + 1)]
result = []
index = 0
while data:
    index = (index + k - 1) % len(data)
    result.append(str(data.pop(index)))

print(f'<{", ".join(result)}>')
