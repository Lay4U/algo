input = """
4
5 1 7 9
""".strip().split('\n')

n = int(input[0])
data = list(map(int, input[1].split()))
data.sort()
print(data[(n - 1) // 2])
print(data)
