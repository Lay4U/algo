# n, k = map(int, input().split())


dp = [1] * 100


def factorial(n):
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] * i
    return dp[n]
