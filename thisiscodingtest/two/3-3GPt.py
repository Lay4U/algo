n, m = 3, 3
datas = [
    [3, 1, 2],
    [4, 1, 4],
    [2, 2, 2]
]

min_values = [min(data) for data in datas]
result = max(min_values)

print(result)
