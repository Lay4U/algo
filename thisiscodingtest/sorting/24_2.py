input = """
4
5 1 7 9
""".strip().split('\n')

data = list(map(int, input[1].split()))
data.sort()
size = len(data)
print(data[(size // 2) - 1])
