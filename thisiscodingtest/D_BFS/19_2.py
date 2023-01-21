input = """
6
1 2 3 4 5 6
2 1 1 1
""".strip().split('\n')

n = int(input[0])
data = list(map(int, input[1].split()))
add, sub, mul, div = map(int, input[2].split())

max_value = -1e9
min_value = 1e9


# print(n, data, add, sub, mul, div)


def dfs(i, now):
    global add, sub, mul, div, min_value, max_value

    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))
            div += 1


dfs(1, data[0])
print(max_value)
print(min_value)