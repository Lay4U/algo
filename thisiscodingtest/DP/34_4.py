input = """
7
15 11 4 8 5 2 4
""".strip().split('\n')

n = int(input[0])
array = list(map(int, input[1].split()))
array.reverse()
print(array)

dp = [1] * n
for i in range(1, n):
    for j in range(i):
        print(i, j)
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)
