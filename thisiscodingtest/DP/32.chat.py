n = int(input())
dp = [[int(x) for x in input().split()] for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        print(i, j)
        up_left = dp[i - 1][j - 1] if j > 0 else 0
        up = dp[i - 1][j] if j < i else 0
        dp[i][j] += max(up, up_left)

print(max(dp[n - 1]))
