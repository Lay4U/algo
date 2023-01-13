input = """
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
"""

lines = input.strip().split("\n")
n, m = map(int, lines[0].split())

data = [list(map(int, line.split())) for line in lines[1:]]

result = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

temp = [[0] * m for _ in range(n)]

print(data)
print(temp)


def virus(a, b):
    for i in range(4):
        x = dx[i] + a
        y = dy[i] + b
        if 0 <= x < n and 0 <= y < m:
            if temp[x][y] == 0:
                temp[x][y] = 2
                virus(x, y)


def get_score():
    score = 0
    for x in range(n):
        for y in range(m):
            if temp[x][y] == 0:
                score += 1
    return score


def dfs(count):
    global result
    if count == 3:
        for x in range(n):
            for y in range(m):
                temp[x][y] = data[x][y]

        for x in range(n):
            for y in range(m):
                if temp[x][y] == 2:
                    virus(x, y)

        result = max(result, get_score())
        return
    for x in range(n):
        for y in range(m):
            if data[x][y] == 0:
                data[x][y] = 1
                count += 1
                dfs(count)
                count -= 1
                data[x][y] = 0


dfs(0)
print(result)
