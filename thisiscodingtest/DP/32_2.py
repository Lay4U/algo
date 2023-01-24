input = """
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
""".strip().split('\n')

n = int(input[0])
dp = [[int(x) for x in index.split()] for index in input[1:]]
for i in range(1, n):
    for j in range(i + 1):
        left = dp[i - 1][j - 1] if j > 0 else 0
        right = dp[i][j - 1] if j < n else 0
        dp[i][j] += max(left, right)

print(max(dp[n - 1]))
