input = """
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
""".strip().split('\n')

for x in range(int(input[0])):
    n, m = map(int, input[(x * 2) + 1].split())
    array = list(map(int, input[(x * 2) + 2].split()))
    dp = [[array[(i * m) + j] for j in range(m)] for i in range(n)]
    for j in range(1, m):
        for i in range(n):
            left_up = dp[i - 1][j - 1] if i > 0 else 0
            left_down = dp[i + 1][j - 1] if i < n - 1 else 0
            left = dp[i][j - 1]
            dp[i][j] += max(left, left_up, left_down)
    print(max(dp[i][m - 1] for i in range(n)))
