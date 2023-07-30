def solution(n, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    if n < 0:
        return 0
    memo[n] = solution(n - 1, memo) + solution(n - 2, memo) + solution(n - 3, memo)
    return memo[n]


for _ in range(int(input())):
    print(solution(int(input()), {}))
