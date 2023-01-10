n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

temp = [[0] * m for _ in range(n)]
result = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(data)
print(temp)


def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)


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
