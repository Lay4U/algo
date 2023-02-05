input = """
sunday
saturday
""".strip().split('\n')

str1 = input[0]
str2 = input[1]

n = len(str1)
m = len(str2)

print(n, m)

dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n):
    dp[i][0] = i
for j in range(m):
    dp[0][j] = j

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
print(dp)
