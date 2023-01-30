input = """
7
15 11 4 8 5 2 4
""".strip().split('\n')

n = int(input[0])
array = list(map(int, input[1].split()))
array.reverse()
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
