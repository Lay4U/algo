input = """
sunday
saturday
""".strip().split('\n')

str1 = input[0]
str2 = input[1]

n = len(str1)
m = len(str2)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    dp[i][0] = i
for j in range(m):
    dp[0][j] = j

for i in range(n):
    for j in range(m):
        if str1[i] == str2[j]:
            dp[i + 1][j + 1] = dp[i][j]
        else:
            dp[i + 1][j + 1] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i][j])

print(dp)
