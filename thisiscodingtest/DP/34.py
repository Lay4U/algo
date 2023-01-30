n = int(input())
array = list(map(int, input().split()))

array.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        print(dp)
        if array[j] < array[i]:
            # print(i, j)
            # print('\t', dp)
            dp[i] = max(dp[i], dp[j] + 1)
            # print()
    print('---')

print(dp)
print(n - max(dp))
