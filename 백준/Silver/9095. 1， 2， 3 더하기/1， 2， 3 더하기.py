def count(n, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    if n < 0:
        return 0
    memo[n] = count(n - 1, memo) + count(n - 2, memo) + count(n - 3, memo)
    return memo[n]


for _ in range(int(input())):
    print(count(int(input()), {}))
