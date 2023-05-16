def dfs(x, y):
    if not (0 <= x < n) or not (0 <= y < m) or graph[x][y] == 1:
        return False

    graph[x][y] = 1

    for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        dfs(x + dx, y + dy)

    return True


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

result = sum(dfs(i, j)
             for i in range(n)
             for j in range(m))
print(result)
