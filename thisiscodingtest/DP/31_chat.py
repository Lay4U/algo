def max_path_sum(tc, testcases):
    for n, m, array in testcases:

        dp = [[array[i * m + j] for j in range(m)] for i in range(n)]

        for j in range(1, m):
            for i in range(n):
                left_up = dp[i - 1][j - 1] if i > 0 else 0
                left_down = dp[i + 1][j - 1] if i < n - 1 else 0
                left = dp[i][j - 1]
                dp[i][j] += max(left_up, left_down, left)
                for row in dp:
                    print(row)
                print()

        result = max(dp[i][m - 1] for i in range(n))
        print(result)


tc = 2
testcases = [(3, 4, [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7]),
             (4, 4, [1, 3, 1, 5, 2, 2, 4, 1, 5, 0, 2, 3, 0, 6, 1, 2])]

max_path_sum(tc, testcases)
