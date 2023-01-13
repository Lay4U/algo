input = """
2 20 50
50 30
20 40
""".strip().split('\n')

n, l, r = map(int, input[0].strip().split())

graph = [list(map(int, row.strip().split())) for row in input[1:]]

total_count = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def process(i, j, index):
    pass


while True:
    for i in range(n):
        for j in range(n):
            process(i, j, index)
